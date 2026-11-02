# Build the model from the assignment

## Classify the decision, not the picture

| Actual decision | Candidate model | Frequent wrong shortcut |
|---|---|---|
| One path between two fixed vertices | Shortest path | Treating many-bus assignment as one shortest path |
| Assign workers/jobs to limited resources | Assignment, matching, min-cost flow, MIP/CP-SAT | Greedy nearest assignment despite capacities |
| Select sites/stops to cover demand | Set cover, facility location, p-median/p-center as appropriate | Clustering employees and declaring coverage satisfied |
| Order visits for one/multiple vehicles | TSP/VRP; add actual capacity/time/endpoint restrictions | Optimizing each route without global demand coverage |
| Choose start times with dependencies and limited resources | Scheduling, CP-SAT, interval/flow methods | Sorting by duration while ignoring availability |
| Allocate divisible quantities under linear constraints | LP; MIP if integrality is required | Rounding a continuous solution and assuming feasibility |
| Small discrete state/sequence with reusable substructure | Dynamic programming or bounded exact search | Enumerating permutations regardless of size |

Do not use an exact-sounding model name as evidence the implementation matches the task. A combined stop-selection, employee-assignment and routing problem contains several coupled decisions. Decomposition is a method with possible tradeoffs, not a proof that the parts optimize the whole.

## Model contract

For each hard requirement identify its actual enforcement and independent check. Record:

- What each entity and ID represents: employee, stop, vehicle, company, job or time slot. Preserve distinct records even at identical coordinates. Map IDs to matrix indices explicitly.
- What decisions may change, which inputs are fixed and which assignments are eligible.
- Whether every demand is mandatory, whether splitting/reassignment is permitted and whether a resource can be reused over time.
- Capacity units, time zone, travel/service/waiting time, money, precision and objective direction.
- Whether fairness, walking distance, maximum ride time, lateness or vehicle count is a hard limit, a soft cost or absent from the task.
- Objective order: scalar weighted sum, lexicographic priorities or several reported metrics. Do not invent weights. A lexicographic objective can be implemented in stages that preserve earlier optimum values; using a huge arbitrary coefficient can overflow or distort the objective.
- What output must contain, what happens to infeasible/unserved demand and what evidence supports completion.

## Input checks and cheap necessary conditions

Check missing/duplicate IDs, NaN/infinity, invalid negative values, coordinate order/projection, matrix dimensions, directionality and unreachable pairs. Zero is not a missing-data marker unless specified. A disconnected arc is not a free connection. Never invent live road times or silently replace provided travel data with Euclidean distance.

Compare total demand with available capacity when each vehicle is used once, verify each indivisible group fits at least one eligible resource, and test time reachability. Necessary checks can establish particular contradictions; passing them does not establish feasibility. Fleet reuse, employee splitting and pickup/dropoff loads change those tests and must come from the contract.

CP-SAT uses integer model data. Choose an explicit exact scale where possible, check coefficient bounds and units, and document rounding/tolerance where unavoidable. Rounding resource use down or deadline travel down can fabricate feasibility. Rounding a continuous solution does not preserve general constraints. Validate the returned solution against the original units and business rules.

## Scope and clarification

Preserve provided architecture and data sources. During the event, use permitted local/provided data and Git Clone acquisition only. Employee locations and generated routes stay inside the task. An external mapping/geocoding/optimization API is not an implicit option. Missing information should become a narrow permitted clarification or a labeled assumption, not a hidden policy.
