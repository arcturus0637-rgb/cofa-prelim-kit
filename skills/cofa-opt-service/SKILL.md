---
name: cofa-opt-service
description: "Use when building a service or application whose real inputs must produce optimized decisions, using a task-specific model and solver with honest result status and verified end-to-end behavior."
---

# Build the service around the actual optimization

Use `cofa-optimize` to formulate the actual task and select relevant public skill references. Codex must implement and solve that model in the supplied project, then connect it to the requested service. A skill, solver tutorial, canned workflow or precomputed sample result cannot replace the assignment. Reusing a permitted solver/algorithm is appropriate; it does not remove the need for task-specific modeling, integration and checking.

Implement the smallest complete path demanded by the prompt:
actual input -> input validation -> task-specific model -> bounded solve -> independent result checks -> meaningful result/error UI or API -> required persistence/export.

Preserve the provided stack and architecture. Separate input/model, solve and result-check responsibilities enough to test them; do not introduce a platform, queue, cache, database or new framework without an actual need. The source `optimization-project-structure` offers optional organization, not a required scaffold. Never install packages or call external optimization/model services to make an example work.

## Decisions and status must reach the user

- Parse and validate real inputs, units, bounds, eligibility and policies. Recompute for changed inputs and settings. Demonstrate at least two relevant input cases through the actual execution path; equal optima can be legitimate, so check the underlying constraints/objective rather than demanding every edit change the answer.
- Return decisions with traceable IDs, objective components/units, checked hard constraints and termination status. Report valid bound/gap and proof method when available. Distinguish invalid input, running, feasible without proof, proven optimum within stated tolerance, proven model infeasible, unbounded, no solution found by limit, execution failure and canceled. Expose only relevant states supported by the actual implementation; do not fabricate a solver guarantee.
- Bound computation and handle limits/failures predictably. Preserve a validated incumbent when available. For asynchronous work prevent older responses overwriting newer input results. Mark displayed results stale on input changes. If caching is needed, key on all model/input/settings versions; do not leak data or reuse stale global state across requests.
- Connect the real solver path to requested actions and display/export/persistence. A disconnected solver script, static graph, success toast or hardcoded JSON is not the complete service. Persist enough input/settings to reproduce results if the task needs saved scenarios; avoid unsolicited infrastructure.

## Verify and explain the built artifact

Check tiny known optima or a bounded exhaustive oracle; infeasible and limit/error cases relevant to the implementation; constraint/objective recomputation; and changed-input behavior at the service boundary. Do not compare only mocked solver totals. Use the existing test runner, local requests or stdlib as appropriate. The participant manually checks platform preview; do not use browser automation. Never label an unexecuted UI path verified.

Document actual entry points, data flow, model, algorithm and why it fits, status/proof, observed tests and remaining limits using `cofa-explain`. Include the requested implementation explanation file in the allowed submission format before confirmation. If exact global optimality cannot be established, say that clearly, investigate the gap and keep working on a defensible method; a polished UI does not establish optimality. Stop AI work after platform submission confirmation.
