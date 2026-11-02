# Search, diagnose and substantiate

## A feasible incumbent first

Construct a valid baseline with explicit input-to-output coverage. Pick constraints likely to block later choices (restricted eligibility, tight windows, large indivisible demands) early when useful. A heuristic may fail even though another assignment exists: try a different order, repair/reassignment or a bounded exact subproblem before declaring no solution.

Preserve the best validated incumbent during improvement. Reject an improving numeric score if feasibility deteriorates. Revalidate after each accepted move. Compute objective values in a checker independent of the solver's own reported total. Do not compare an invalid baseline with a feasible candidate as a percentage improvement; report feasibility separately. If the baseline objective is zero, a percentage division is undefined.

For a minimization model, a feasible incumbent is an upper bound, and a valid relaxation or exact method may provide a lower bound. Bounds must concern the same full objective/model. Report absolute gap or solver-defined relative gap with its convention; distinguish proof from an empirical best-known value. Do not relabel a heuristic cost as a lower bound.

## Method selection and budgets

- Exploit assignment/flow/linear structure when it actually fits. Do not reach for vehicle routing for every optimization task.
- Reuse provided OR-Tools/other solvers when usable. Check actual installed APIs, time limits and status enums. Repository source alone does not include native binaries or dependencies.
- For tiny inputs, bounded enumeration or dynamic programming can supply an independent oracle. Estimate state/permutation count first and stop predictably. A result is exact only if the entire relevant space was searched with valid pruning.
- For larger routes, feasible insertion followed by relocate/swap/2-opt-style local improvement can be useful. Asymmetric costs and time windows require full affected-route recalculation; the symmetric four-edge 2-opt delta is not generally correct for a reversed directed segment.
- Clustering can seed a solution but may make later capacity/time assignments impossible. Keep repair/reassignment available and test global coverage.
- Set a wall-clock/search budget from actual time remaining. Use bounded restarts only if they can improve the incumbent without losing it. Seeds do not guarantee identical output across solver versions, thread counts or machines; record those too.

## Solver outcomes

CP-SAT: FEASIBLE means a feasible model solution without an exact-optimum claim. UNKNOWN after a limit does not prove infeasibility. MODEL_INVALID means fix the model. INFEASIBLE is a proof about the submitted model; investigate accidental restrictions and data before asserting the original task impossible. OPTIMAL may reflect configured gap tolerances or a pure feasibility task, so record the objective/bound/settings and describe the guarantee precisely.

Routing: read the routing solver's own status enum. A returned route or ROUTING_SUCCESS does not on its own establish global optimality. Display dropped/unserved locations explicitly and allow dropping only when the actual task permits it. Adding a visit penalty to a mandatory all-served model changes that model.

On infeasibility or missing solutions: inspect a tiny instance, a known feasible construction, each added constraint family, unit/index transformations and unreachable pairs. Diagnostic relaxations may isolate a conflict, but their solutions are not valid final answers to the original hard constraints. If using unsat-core assumptions, a sufficient conflicting subset need not be a minimum conflict.

## Meaningful verification

Use small hand-computable cases, infeasible cases, uneven capacities, equal coordinates with distinct IDs, asymmetric/unreachable travel, tight windows, service/waiting times and no-demand cases relevant to the assignment. Relabeling IDs should preserve the problem if IDs have no business meaning. Exact permutation/sum assertions over arbitrary floating point may be invalid; use declared numeric tolerances and original-unit checks.

For fixed all-pickup routes only, `cofa-routing` includes a limited independent verifier. It does not check stop placement, individual employee walking/ride limits, transfers, multiple trips per bus, stochastic traffic, or optimality. Extend a task-specific checker when those are actual requirements.

## Official references checked during preparation

These links record provenance; reading local guidance does not require downloading pages in the exam.

- [OR-Tools CVRP](https://developers.google.com/optimization/routing/cvrp)
- [OR-Tools time windows](https://developers.google.com/optimization/routing/vrptw)
- [Routing search limits/status](https://developers.google.com/optimization/routing/routing_options)
- [Penalties change visit requirements](https://developers.google.com/optimization/routing/penalties)
- [CP-SAT model and statuses](https://developers.google.com/optimization/cp/cp_solver)
- [CP-SAT troubleshooting, gap tolerance and infeasibility](https://github.com/google/or-tools/blob/stable/ortools/sat/docs/troubleshooting.md)

These are independently written working notes, not copied OR-Tools code or a bundled solver. APIs and guarantees must be checked against the provided version.
