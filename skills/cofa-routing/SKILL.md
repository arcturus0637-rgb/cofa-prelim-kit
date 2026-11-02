---
name: cofa-routing
description: "Use for employee shuttle buses, vehicle routing, capacity/time-window routes or coupled stop selection and passenger assignment in a COFA optimization task."
---

# Shuttle and vehicle routing

Start with `cofa-optimize` and read [shuttle-model.md](references/shuttle-model.md). Identify whether the assignment selects stops, assigns employees, sequences buses, schedules trips, or combines these. Do not assume every home is a required stop or that every route returns to the depot. The previous exam topic is context, not a specification for the retest.

Model actual coverage and load: each employee's identity and demand, allowed stops, walking limits if required, vehicle capacity, pickup/dropoff precedence and occupancy along the route. Count mandatory employees even at shared coordinates. Enforce actual endpoints, company arrival, shifts and ride limits; do not silently omit hard-to-serve demand or make all visits optional.

Use provided directed travel/time matrices and their units. Include boarding/service and allowed waiting in the schedule. Distinguish maximum total route duration from each passenger's in-vehicle time. Straight-line drawing is not evidence of road travel time. No external geocoding/map API or employee-data upload is part of this skill.

First verify a feasible baseline, then improve the specified objective with bounded search. Recheck modified route cost/time/load and global coverage after accepted changes. Do not rely on symmetric local-search deltas for asymmetric matrices or on clustering as a feasibility certificate. If OR-Tools is already usable, add the actual dimensions/endpoints/eligibility constraints and a time limit using that version's API. Source Clone does not install OR-Tools.

For the deliberately limited fixed-stop, all-pickup, one-trip-per-vehicle model, read [fixed-pickup-schema.md](references/fixed-pickup-schema.md) and run the stdlib checker through the kit's guarded check runner:

```bash
python .cofa-kit/kit.py check --name routes -- python .cofa-kit/skills/cofa-routing/scripts/check_routes.py INSTANCE.json CANDIDATE.json
```

This independently recomputes coverage, capacity, directed cost, windows, waiting/service and vehicle duration for its explicit schema. It rejects unknown fields rather than silently claiming to validate unsupported constraints. It neither solves routes nor certifies optimality. Do not project a richer problem into this schema and claim the omitted requirements were checked; build corresponding independent checks.

Present the solution's actual assignment table and metrics as well as any required map. Separate feasibility, objective improvement and proof status. Record unserved demand and unresolved assumptions honestly. Before confirmation use `cofa-explain` to write the actual algorithm, data flow, guarantees, tests and limitations into the permitted submission explanation file.
