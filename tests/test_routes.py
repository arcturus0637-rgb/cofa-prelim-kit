"""Independent, hand-computed fixtures for the limited route verifier."""
import copy
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/cofa-routing/scripts/check_routes.py'


def fixture():
    instance = {
        'schema': 'cofa-fixed-pickup-v1',
        'nodes': [{'id': 'depot', 'demand': 0},
                  {'id': 'a', 'demand': 2, 'window': [8, 12], 'service_time': 2},
                  {'id': 'b', 'demand': 1, 'window': [11, 20]},
                  {'id': 'company', 'demand': 0, 'window': [0, 25]}],
        'distance': [[0, 4, 9, 7], [8, 0, 3, 8], [3, 6, 0, 5], [7, 8, 5, 0]],
        'travel_time': [[0, 4, 9, 7], [8, 0, 3, 8], [3, 6, 0, 5], [7, 8, 5, 0]],
        'required': ['a', 'b'],
        'vehicles': [{'id': 'bus', 'start': 'depot', 'end': 'company',
                      'capacity': 3, 'available': [0, 30], 'max_duration': 20}],
    }
    candidate = {'schema': 'cofa-fixed-pickup-v1',
                 'routes': [{'vehicle': 'bus', 'stops': ['a', 'b'], 'departure': 0}]}
    return instance, candidate


class RouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('cofa_route_checker', SCRIPT)
        cls.checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.checker)

    def check(self, instance=None, candidate=None):
        original, proposed = fixture()
        return self.checker.validate(instance or original, candidate or proposed)

    def test_open_route_waiting_service_and_independent_metrics(self):
        result = self.check()
        self.assertTrue(result['valid'], result)
        self.assertFalse(result['optimality_proven'])
        route = result['routes'][0]
        self.assertEqual(route['distance'], 12)
        self.assertEqual(route['travel_time'], 12)
        self.assertEqual(route['duration'], 18)
        self.assertEqual(route['waiting_time'], 4)
        self.assertEqual(route['load'], 3)
        self.assertEqual(route['finish'], 18)
        self.assertEqual(route['visits'][0]['service_start'], 8)

    def test_directed_cost_and_reversed_order_recomputed(self):
        instance, candidate = fixture()
        for node in instance['nodes']:
            node.pop('window', None)
        instance['vehicles'][0]['max_duration'] = 40
        candidate['routes'][0]['stops'] = ['b', 'a']
        r = self.check(instance, candidate)
        self.assertTrue(r['valid'], r)
        self.assertEqual(r['routes'][0]['distance'], 23)
        self.assertEqual(r['routes'][0]['duration'], 25)

    def test_omission_is_not_free_improvement(self):
        _, candidate = fixture()
        candidate['routes'][0]['stops'] = ['a']
        self.assertFalse(self.check(candidate=candidate)['valid'])

    def test_duplicate_visit_and_vehicle_reuse_rejected(self):
        _, candidate = fixture()
        candidate['routes'][0]['stops'] = ['a', 'a', 'b']
        self.assertFalse(self.check(candidate=candidate)['valid'])
        _, candidate = fixture()
        candidate['routes'].append(copy.deepcopy(candidate['routes'][0]))
        self.assertFalse(self.check(candidate=candidate)['valid'])

    def test_capacity_and_vehicle_limit(self):
        instance, _ = fixture()
        instance['vehicles'][0]['capacity'] = 2
        self.assertFalse(self.check(instance=instance)['valid'])

    def test_service_duration_and_waiting_count_for_deadline(self):
        instance, _ = fixture()
        instance['vehicles'][0]['max_duration'] = 17
        self.assertFalse(self.check(instance=instance)['valid'])
        instance, _ = fixture()
        instance['nodes'][3]['window'] = [0, 17]
        self.assertFalse(self.check(instance=instance)['valid'])

    def test_endpoint_waiting_and_availability(self):
        instance, _ = fixture()
        instance['nodes'][3]['window'] = [20, 25]
        r = self.check(instance=instance)
        self.assertTrue(r['valid'], r)
        self.assertEqual(r['routes'][0]['finish'], 20)
        self.assertEqual(r['routes'][0]['waiting_time'], 6)
        instance['vehicles'][0]['available'] = [0, 19]
        self.assertFalse(self.check(instance=instance)['valid'])

    def test_shift_start_and_stop_window(self):
        instance, candidate = fixture()
        instance['vehicles'][0]['available'] = [1, 30]
        self.assertFalse(self.check(instance, candidate)['valid'])
        instance, candidate = fixture()
        candidate['routes'][0]['departure'] = 10
        self.assertFalse(self.check(instance, candidate)['valid'])

    def test_unreachable_arc_is_not_zero(self):
        instance, _ = fixture()
        instance['distance'][1][2] = None
        self.assertFalse(self.check(instance=instance)['valid'])

    def test_unknown_field_or_node_fails_closed(self):
        instance, candidate = fixture()
        instance['max_ride_time'] = 3
        with self.assertRaises(ValueError):
            self.check(instance, candidate)
        instance, candidate = fixture()
        candidate['routes'][0]['stops'] = ['unknown', 'b']
        with self.assertRaises(ValueError):
            self.check(instance, candidate)

    def test_invalid_numeric_schema_and_duplicate_ids(self):
        for change in ['negative', 'nan', 'float', 'bool', 'shape', 'duplicate', 'endpoint']:
            with self.subTest(change=change):
                instance, _ = fixture()
                if change == 'shape':
                    instance['distance'][0].pop()
                elif change == 'duplicate':
                    instance['nodes'][2]['id'] = 'a'
                elif change == 'endpoint':
                    instance['vehicles'][0]['start'] = 'a'
                else:
                    instance['distance'][0][1] = {'negative': -1, 'nan': float('nan'),
                                                 'float': 1.5, 'bool': True}[change]
                with self.assertRaises(ValueError):
                    self.check(instance=instance)

    def test_empty_demand_empty_routes_and_zero_distance(self):
        instance, candidate = fixture()
        instance['required'] = []
        candidate['routes'] = []
        r = self.check(instance, candidate)
        self.assertTrue(r['valid'])
        self.assertEqual(r['metrics']['used_vehicles'], 0)
        instance, candidate = fixture()
        instance['distance'][0][1] = 0
        self.assertTrue(self.check(instance, candidate)['valid'])

    def test_empty_route_does_not_claim_unused_bus_travel(self):
        instance, candidate = fixture()
        instance['required'] = []
        candidate['routes'][0]['stops'] = []
        with self.assertRaises(ValueError):
            self.check(instance, candidate)

    def test_inputs_not_mutated_and_vehicle_id_not_inferred_from_order(self):
        instance, candidate = fixture()
        instance['vehicles'].insert(0, {'id': 'spare', 'start': 'company', 'end': 'company',
                                        'capacity': 0, 'available': [0, 30]})
        before = copy.deepcopy((instance, candidate))
        self.assertTrue(self.check(instance, candidate)['valid'])
        self.assertEqual((instance, candidate), before)

    def test_cli_rejects_invalid_candidate_and_never_trusts_claimed_metric(self):
        with tempfile.TemporaryDirectory() as directory:
            instance, candidate = fixture()
            a, b = Path(directory) / 'instance.json', Path(directory) / 'candidate.json'
            a.write_text(json.dumps(instance), encoding='utf-8')
            b.write_text(json.dumps(candidate), encoding='utf-8')
            proc = subprocess.run([sys.executable, str(SCRIPT), str(a), str(b)],
                                  capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertTrue(json.loads(proc.stdout)['valid'])
            candidate['routes'][0]['distance'] = 0
            b.write_text(json.dumps(candidate), encoding='utf-8')
            proc = subprocess.run([sys.executable, str(SCRIPT), str(a), str(b)],
                                  capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(proc.returncode, 2)
            self.assertFalse(json.loads(proc.stdout)['valid'])

    def test_cli_supports_unicode_ids_with_restrictive_stdout_encoding(self):
        instance, candidate = fixture()
        instance['nodes'][1]['id'] = '\U0001f68c'
        instance['required'][0] = '\U0001f68c'
        candidate['routes'][0]['stops'][0] = '\U0001f68c'
        with tempfile.TemporaryDirectory() as directory:
            paths = [Path(directory) / name for name in ['instance.json', 'candidate.json']]
            for path, data in zip(paths, [instance, candidate]):
                path.write_text(json.dumps(data), encoding='utf-8')
            proc = subprocess.run([sys.executable, str(SCRIPT), *map(str, paths)],
                                  env={**os.environ, 'PYTHONIOENCODING': 'cp949'},
                                  capture_output=True)
            self.assertEqual(proc.returncode, 0, proc.stderr.decode('ascii', errors='replace'))
            self.assertTrue(json.loads(proc.stdout)['valid'])


if __name__ == '__main__':
    unittest.main()
