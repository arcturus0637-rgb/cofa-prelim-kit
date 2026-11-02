# Model the decision and original requirements

| Decision structure | Candidate method | Check before choosing |
|---|---|---|
| Linear objective/constraints, divisible variables | LP | Affineness, domains, feasibility/boundedness |
| Binary/integer choices or logical conditions | MIP, CP/CP-SAT, exact combinatorial algorithm | Integrality, valid bounds, correct implications |
| Pair eligible entities with costs | Matching, assignment, min-cost flow | Capacities, eligibility, full coverage, side constraints |
| Network capacities/conservation | Flow/shortest path as appropriate | Direction, negative costs/cycles, conservation |
| Select a subset under resources/coverage | DP, MIP, CP, branch-and-bound | State size, coverage vs partition, interaction costs |
| Start times, precedence, shared resources | CP, interval/flow methods, MIP | Availability, overlap, durations and deadlines |
| Repeated discrete substructure | DP or bounded search | Complete state captures future consequences |
| Smooth convex/nonconvex continuous objective | Convex solver or nonlinear method | Actual convexity, derivatives, domain and guarantee |
| Several competing objectives | Lexicographic, epsilon-constraint, justified scalarization | Required priorities vs sampled tradeoffs |

Continuous variables alone do not make a problem linear. A combined problem can couple decisions; optimizing parts separately need not optimize the whole. Avoid arbitrary size thresholds and do not choose a solver from the visual presentation alone.

Record decisions/domains, fixed inputs, eligibility, mandatory coverage, reuse/splitting policies, hard constraints, soft preferences, objective direction, units and numerical tolerances. Identify the actual enforcement/check for every hard requirement. Do not silently convert a requirement into a penalty. For lexicographic objectives preserve earlier optimum values in later stages; an arbitrary huge coefficient can change priorities or overflow.

Audit IDs and explicit index maps, missing/duplicate values, NaN/infinity, invalid signs, matrix shapes, directionality, units and unavailable choices. Preserve distinct records even when their attributes coincide. Zero is not missing unless specified. Check cheap necessary conditions such as aggregate capacity and per-item eligibility, but passing them is not a feasibility proof. A greedy failure is not an infeasibility proof.

Use valid bounds for linearization. For integer-only APIs choose an explicit scale, check coefficient bounds, and validate in original units: rounding can fabricate feasibility. Keep input/model assumptions visible and task data local. Use permitted clarification for decision-changing ambiguity; otherwise state a narrow assumption. Preserve the supplied stack and data sources.
