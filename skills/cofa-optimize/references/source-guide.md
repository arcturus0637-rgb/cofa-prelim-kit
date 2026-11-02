# Select a public skill and apply it critically

Read only the row needed now. Paths below are relative to the kit root: in the source checkout use its root; after registration use `.cofa-kit/`. Original skills live outside active discovery paths. Source commits/licenses are in `config/sources.lock.json`. No upstream agents, global AGENTS, hooks or examples run automatically. Missing upstream cross-links are optional background, not instructions to fetch/install more material.

| Need | Included original under `upstream/combinatorial/skills/` |
|---|---|
| LP, dual bounds, formulation | `linear-programming-fundamentals/SKILL.md` |
| Binary/integer choices | `integer-programming-techniques/SKILL.md` |
| Products, implications, piecewise formulations | `linearization-techniques/SKILL.md` |
| Bounds and exact discrete search | `branch-and-bound/SKILL.md` |
| Scheduling/logical constraints | `constraint-programming/SKILL.md` |
| State recurrences and exact substructure | `dynamic-programming/SKILL.md` |
| Capacities and conservation | `network-flow-optimization/SKILL.md` |
| Pairing and allocation | `assignment-problems/SKILL.md` |
| Feasibility/objective cross-checking | `solution-validation-testing/SKILL.md` |
| Solver options already available | `open-source-solvers/SKILL.md` |
| Priorities/tradeoffs | `multi-objective-optimization/SKILL.md` |
| Separating model/solve/check in the existing app | `optimization-project-structure/SKILL.md` |

For continuous convex/nonconvex optimization, scaling, derivatives and KKT, read `upstream/optimization-scientist/scientific-agents/optimization-scientist/skills/optimization-scientist/SKILL.md`. Use its methods as reference; do not invoke a separate scientist agent or copy an environment/workflow wholesale.

## Local corrections and scope (apply before upstream suggestions)

- Continuous is not synonymous with linear. Require the actual affine structure for LP. Convexity does not itself imply feasibility, boundedness, attainment or convergence of a chosen run.
- KKT is not a global-optimality certificate for general nonconvex NLP. For example, zero is stationary for minimizing `-x^2` on `[-1,1]`, but the endpoints have lower objective. Necessity needs suitable constraint qualifications; sufficiency needs appropriate convex conditions and valid multipliers, including variable-bound terms.
- The scientist source writes complementarity with primal `x_i`; for inequalities `g_i(x) <= 0` the standard condition is `lambda_i >= 0` and `lambda_i * g_i(x) = 0`, using the inequality multiplier, not the decision variable. Keep the chosen constraint/Lagrangian sign convention consistent.
- Binary product truth tables have four corners, despite a source's wording about five feasible points. Continuous-continuous McCormick constraints generally give a relaxation, not exact equivalence. An epigraph for absolute value/max becomes tight only when the surrounding objective/constraints justify it; it is not arbitrary graph equality.
- Derive a valid tight big-M from bounds and verify which binary branch activates each inequality. Do not use a universal large constant. A binding LP constraint can have zero multiplier; reduced costs depend on variable bounds. Do not invent solver sensitivity ranges or treat empirical perturbations as exact sensitivity certificates.
- Branch-and-bound proof requires valid bounds, pruning and complete remaining-space coverage. Binary-variable counts and advertised speed are not runtime guarantees. A tolerance-based OPTIMAL status may allow a nonzero gap.
- Weighted sums can miss unsupported nondominated points; a sampled Pareto set is not a proven complete frontier. Positive correlation of sample objectives does not justify replacing the actual multiobjective requirement.
- Independently recompute relevant constraints and objective; there is no obligation to duplicate every parser, test every helper exhaustively or run every suggested validation layer. Tests must address the actual model and service. Do not import a reference's finished example output or fixed instance as the submission.
- Metamorphic properties need model-specific premises. Adding a worse-cost/resource option can still change feasibility or the optimum when it adds capacity or interacts with eligibility/count constraints; do not assume every allegedly dominated machine is irrelevant. Relaxing a constraint cannot worsen the true optimum in its optimization direction, but a time-limited heuristic's returned incumbent may get worse. Such a change alone does not prove a solver bug.
- Relabeling IDs preserves the mathematical feasible set/objective only when IDs carry no business meaning. An order-dependent heuristic may return another valid solution or objective even with a fixed seed; do not require invariant incumbent quality without a justified algorithm guarantee. Optimal decisions may also differ under ties.
- Positive scaling of the entire scalar objective preserves its mathematical optimizers, but finite-precision tolerances, limits and heuristic decisions may change a returned incumbent. Test the exact claim justified by the method rather than demanding every returned heuristic objective scale perfectly.
- Public popularity, solver recommendations and example code are not quality/performance evidence for the task. Check actual installed APIs. Original pip/uv/npm instructions, commercial runtimes/accounts, external services, mandatory review/benchmark/manuscript workflows and new frameworks are outside this adaptation. Use only permitted tools. Do not download dependencies.

The public originals remain byte-for-byte intact for attribution. These corrections and `cofa-opt-service` are local adaptations, not claims that all original examples are correct or runnable.
