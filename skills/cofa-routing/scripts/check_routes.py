"""Recompute limited fixed-pickup route feasibility; never certify optimality."""
import argparse
import json
from collections import Counter
from pathlib import Path

SCHEMA = 'cofa-fixed-pickup-v1'


def object_fields(value, required, optional, label):
    if not isinstance(value, dict):
        raise ValueError(label + ' must be an object')
    missing, extra = set(required) - value.keys(), value.keys() - set(required) - set(optional)
    if missing or extra:
        raise ValueError(f'{label}: missing={sorted(missing)}, unsupported={sorted(extra)}')
    return value


def integer(value, label):
    if type(value) is not int or value < 0:
        raise ValueError(label + ' must be a nonnegative integer in declared units')
    return value


def identifier(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(label + ' must be a nonblank string')
    return value


def array(value, label):
    if not isinstance(value, list):
        raise ValueError(label + ' must be an array')
    return value


def window(value, label):
    array(value, label)
    if len(value) != 2:
        raise ValueError(label + ' needs [earliest, latest]')
    low, high = [integer(v, label) for v in value]
    if low > high:
        raise ValueError(label + ' has reversed bounds')
    return low, high


def validate(instance, candidate):
    """Validate the documented schema; raise ValueError for malformed/unsupported data."""
    object_fields(instance, ['schema', 'nodes', 'distance', 'travel_time', 'required', 'vehicles'], [], 'instance')
    object_fields(candidate, ['schema', 'routes'], [], 'candidate')
    if instance['schema'] != SCHEMA or candidate['schema'] != SCHEMA:
        raise ValueError('Both files must explicitly declare schema ' + SCHEMA)
    nodes, indices = {}, {}
    for index, node in enumerate(array(instance['nodes'], 'nodes')):
        object_fields(node, ['id', 'demand'], ['window', 'service_time'], 'node')
        nid = identifier(node['id'], 'node id')
        if nid in nodes:
            raise ValueError('Duplicate node id: ' + nid)
        integer(node['demand'], 'demand')
        integer(node.get('service_time', 0), 'service_time')
        if 'window' in node:
            window(node['window'], 'node window')
        nodes[nid], indices[nid] = node, index
    if not nodes:
        raise ValueError('At least one node is required')
    for name in ['distance', 'travel_time']:
        matrix = array(instance[name], name)
        if len(matrix) != len(nodes):
            raise ValueError(name + ' must match node order and count')
        for row in matrix:
            if len(array(row, name + ' row')) != len(nodes):
                raise ValueError(name + ' must be square')
            for value in row:
                if value is not None:
                    integer(value, name)
    required = array(instance['required'], 'required')
    for nid in required:
        identifier(nid, 'required node')
        if nid not in nodes:
            raise ValueError('Unknown required node: ' + nid)
    if len(set(required)) != len(required):
        raise ValueError('Required node ids must be unique; demand counts passengers')
    vehicles = {}
    for vehicle in array(instance['vehicles'], 'vehicles'):
        object_fields(vehicle, ['id', 'start', 'end', 'capacity', 'available'], ['max_duration'], 'vehicle')
        vid = identifier(vehicle['id'], 'vehicle id')
        if vid in vehicles:
            raise ValueError('Duplicate vehicle id: ' + vid)
        integer(vehicle['capacity'], 'capacity')
        window(vehicle['available'], 'vehicle available')
        if 'max_duration' in vehicle:
            integer(vehicle['max_duration'], 'max_duration')
        for key in ['start', 'end']:
            nid = identifier(vehicle[key], key)
            if nid not in nodes or nid in required:
                raise ValueError('Vehicle terminals must be known non-required nodes')
            if nodes[nid]['demand'] or nodes[nid].get('service_time', 0):
                raise ValueError('Terminals must have zero demand and zero service time')
        vehicles[vid] = vehicle

    violations, reports, used = [], [], set()
    counts = Counter()
    for route in array(candidate['routes'], 'routes'):
        object_fields(route, ['vehicle', 'stops', 'departure'], [], 'route')
        vid = identifier(route['vehicle'], 'route vehicle')
        if vid not in vehicles:
            raise ValueError('Unknown vehicle: ' + vid)
        stops = array(route['stops'], 'route stops')
        if not stops:
            raise ValueError('Omit unused vehicles; empty routes are not supported')
        for nid in stops:
            identifier(nid, 'stop')
            if nid not in nodes or nid not in required:
                raise ValueError('Route stops must be required nodes: ' + nid)
        if vid in used:
            violations.append('vehicle reused: ' + vid)
        used.add(vid)
        vehicle = vehicles[vid]
        departed = integer(route['departure'], 'departure')
        low, high = vehicle['available']
        if not low <= departed <= high:
            violations.append('departure outside availability: ' + vid)
        start = nodes[vehicle['start']]
        if 'window' in start and not start['window'][0] <= departed <= start['window'][1]:
            violations.append('departure outside terminal window: ' + vid)
        current, stamp = vehicle['start'], departed
        distance = travel = waiting = load = 0
        visits = []
        reachable = True
        for nid in [*stops, vehicle['end']]:
            a, b = indices[current], indices[nid]
            dist, duration = instance['distance'][a][b], instance['travel_time'][a][b]
            if dist is None or duration is None:
                violations.append(f'unreachable arc: {current}->{nid} ({vid})')
                reachable = False
                break
            distance += dist
            travel += duration
            arrival = stamp + duration
            node = nodes[nid]
            service_start = max(arrival, node['window'][0]) if 'window' in node else arrival
            if 'window' in node and service_start > node['window'][1]:
                violations.append(f'late service/arrival: {nid} ({vid})')
            waiting += service_start - arrival
            stamp = service_start + node.get('service_time', 0)
            if nid != vehicle['end']:
                counts[nid] += 1
                load += node['demand']
                visits.append({'node': nid, 'arrival': arrival, 'service_start': service_start,
                               'departure': stamp, 'load': load})
            current = nid
        if load > vehicle['capacity']:
            violations.append('capacity exceeded: ' + vid)
        if reachable and stamp > high:
            violations.append('finish outside availability: ' + vid)
        if reachable and 'max_duration' in vehicle and stamp - departed > vehicle['max_duration']:
            violations.append('maximum duration exceeded: ' + vid)
        reports.append({'vehicle': vid, 'distance': distance, 'travel_time': travel,
                        'waiting_time': waiting, 'duration': stamp - departed,
                        'finish': stamp, 'load': load, 'visits': visits, 'reachable': reachable})
    for nid in required:
        if counts[nid] != 1:
            violations.append(f'coverage {nid}: expected 1, observed {counts[nid]}')
    return {'valid': not violations, 'scope': SCHEMA, 'optimality_proven': False,
            'violations': violations, 'routes': reports,
            'metrics': {'distance': sum(r['distance'] for r in reports),
                        'used_vehicles': len(used),
                        'max_duration': max((r['duration'] for r in reports), default=0)},
            'notice': 'Metrics are recomputed. Validity covers this fixed-pickup schema only; no optimality proof.'}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON field: ' + key)
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('instance', type=Path)
    parser.add_argument('candidate', type=Path)
    args = parser.parse_args()
    try:
        data = [json.loads(p.read_text(encoding='utf-8-sig'), object_pairs_hook=unique_object)
                for p in [args.instance, args.candidate]]
        result = validate(*data)
    except (OSError, ValueError) as exc:
        result = {'valid': False, 'optimality_proven': False, 'error': str(exc)}
    print(json.dumps(result, ensure_ascii=True, indent=2, allow_nan=False))
    return 0 if result['valid'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
