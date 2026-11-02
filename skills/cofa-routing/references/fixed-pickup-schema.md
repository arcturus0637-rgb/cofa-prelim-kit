# Independent verifier schema: cofa-fixed-pickup-v1

The script checks a limited fixed-stop all-pickup model, not an entire employee transport problem. Both JSON files must set `schema` to `cofa-fixed-pickup-v1`. Unknown fields and duplicate JSON keys are errors. This avoids silently ignoring a `max_ride_time` or similar unsupported requirement. Use an explicit task-specific adapter/checker for richer constraints.

## Instance

- `nodes`: ordered array of objects with unique string `id` and nonnegative integer `demand`; optional `window: [earliest, latest]` and `service_time` (default 0). Windows constrain service start, allow waiting, and include their endpoints.
- `distance`, `travel_time`: separate square directed matrices in that exact node order. Entries are nonnegative integers or `null` for an unreachable arc. Zero remains valid. Choose and record the scale/units before adapting; fractions, booleans and nonfinite values are rejected. This checker does not infer travel time from distance.
- `required`: unique node IDs, each to be visited exactly once globally. Passenger count is represented by demand, not repeated IDs. Non-required nodes cannot be intermediate stops in this schema.
- `vehicles`: objects with unique `id`, node IDs `start`/`end`, integer `capacity`, `available: [earliest, latest]`; optional nonnegative integer `max_duration`. Terminals must be known, non-required, zero-demand, zero-service nodes. Different starts/ends and capacities are supported. A terminal window constrains departure at start and arrival-after-allowed-wait at end.

Every route starts empty, picks up nonnegative demand and unloads only at its terminal. Each vehicle can have at most one route. Unused vehicles are omitted. All time quantities use one shared origin/scale; this script does not parse clock strings or time zones.

## Candidate

`routes` is an array of objects with `vehicle`, nonempty `stops` and nonnegative integer `departure`. The first/last terminal are inferred only from that vehicle's declared start/end; do not include them in `stops`. Claimed objective/schedule fields are unsupported: the checker recomputes them from the instance.

Travel advances the clock; arrival before a window waits; service starts within the window; service time then advances departure. Final travel, waiting and service count toward the vehicle's availability and duration. Windows constrain service start rather than service completion. A departure is fixed by the candidate. The checker does not search for a better departure time.

## Result and limits

Exit 0 means `valid: true` for this schema; exit 2 means malformed data or violated constraints. `optimality_proven` is always false. Violation reports include coverage, capacity, windows, availability, duration, vehicle reuse and unreachable arcs. Metrics on invalid or partially traversed routes are diagnostics, not a feasible objective for comparison.

This does not check home-to-stop coverage, walking distance, individual passenger ride time, mixed pickups/dropoffs, transfers, driver breaks, repeated trips, optional visits, actual road validity, costs/penalties, or any global optimality claim. Preserve original requirements in a richer checker instead of discarding those fields to make this one pass. No package, network access, solver or full application is supplied.
