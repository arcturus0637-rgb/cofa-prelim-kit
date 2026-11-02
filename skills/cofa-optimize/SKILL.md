---
name: cofa-optimize
description: "Use when a task requires optimal decisions under constraints: assignment, scheduling, selection, allocation, flows, integer or continuous optimization; also use for infeasibility diagnosis and optimality claims."
---

# Formulate the actual problem, solve it, substantiate the result

Read the assignment, supplied data and existing project. Use `cofa-prelim` for current rules. This skill supplies methods, not an answer or a finished application. Codex must derive and implement the task-specific model, obtain a result for actual inputs and connect it to the required service using `cofa-opt-service`.

1. Write a short model contract: decisions/domains, hard constraints, objective direction/units/priorities, input meaning and output acceptance criteria. Link each requirement to its enforcement and check. Separate facts, assumptions and unresolved policy. Do not drop constraints or invent weights to make a problem easier.
2. Read [modeling.md](references/modeling.md), then [source-guide.md](references/source-guide.md). Select only the relevant upstream skill(s); read the local corrections in that guide before applying them. These are real pinned public SKILL.md references, not activated agents. Do not load the whole collection.
3. Check actual available tools and run a tiny operation when using a solver. Clone-only acquisition does not authorize pip/npm/uv/npx downloads, external APIs, commercial accounts or extra models. Missing solver: exploit mathematical structure or a bounded stdlib method; report limitations rather than pretending a solver ran.
4. Choose the method from structure, scale and the required guarantee. Prefer an exact structural algorithm, LP/MIP/CP, DP or exhaustive search with valid pruning when tractable. Obtain a validated feasible incumbent where useful without making construction a prerequisite for invoking an exact solver. Keep computation within the real remaining time and memory. Use [methods.md](references/methods.md) for bounds, statuses and diagnosis.
5. Check the returned decisions against the original constraints and units, and independently recompute the objective. Test tiny hand-solvable cases and relevant failure/boundary cases. Solver success alone does not verify a complete model. A timeout with no incumbent is not proof of infeasibility.
6. If global optimality is required, seek a proof appropriate to this model: an exact structural result, exhausted search, or valid matching objective/bound within stated tolerances. A local stationary point, local optimum or heuristic best-found is not that proof. If the requirement cannot be met with available time/tools, say so and continue with a justified alternative; never silently redefine success.
7. Use `cofa-opt-service` to implement the actual input-to-result service. Use `cofa-explain` to document the implemented model, algorithm, proof/status, checks and limitations before submission confirmation. Preserve actual results and their settings locally. Correct unsupported claims promptly and use `cofa-debug` to investigate failed assumptions.

These methods cover many optimization families; no skill guarantees a tractable globally optimal answer for every possible problem.
