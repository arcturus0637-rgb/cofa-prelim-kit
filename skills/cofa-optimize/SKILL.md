---
name: cofa-optimize
description: "Use when a COFA task optimizes assignments, schedules, routes, resource allocation, costs or service levels subject to constraints; also when diagnosing an infeasible model or evaluating a claimed optimum."
---

# Model, find a feasible baseline, then improve

Read the actual assignment and data before choosing an algorithm. Use `cofa-prelim` for current event rules. Do not assume the retest repeats the previous bus problem.

Write a compact model contract: decision variables and domains; required coverage; hard constraints; objective direction, units and priorities; what counts as a feasible output; uncertain policies. Separate hard feasibility from soft preferences. A changed penalty or dropped requirement defines a different problem, not a fix. Use the permitted practitioner channel for unresolved business meaning.

Read [modeling.md](references/modeling.md) to classify the problem and audit its data. Use [methods.md](references/methods.md) for bounded exact/heuristic search, solver statuses and verification. For bus/shuttle or vehicle routing use `cofa-routing` as well. The presence of OR-Tools in the catalogue does not mean it is installed: inspect provided tools and run a tiny real operation if available. No package downloads, external routing service or extra model is required by this skill.

First construct a complete feasible baseline for the actual constraints. Recompute its coverage, resource use and objective independently. If this fails, diagnose data, units, indices, time semantics and model restrictions before tuning performance. A greedy failure or timeout does not prove infeasibility. Keep an incumbent only after validation; preserve its inputs, parameters and metrics locally.

Choose an approach based on structure and size. Use existing exact solvers where appropriate, or bounded enumeration/dynamic programming for genuinely small instances. For larger routing problems, a constructive heuristic followed by feasible local improvements can be practical. Keep a wall-clock budget, seeds where supported and a reproducible stopping rule. Leave time for checks, explanation and submission; do not consume all memory/cores or run factorial search on large inputs.

Compare candidates under the same full model, data, units and objective. Recheck every changed route/assignment plus global coverage. Report feasible heuristic, best-found, bounded or solver result accurately; record solver status, objective, bound/gap when available, time and settings. A successful routing run or independent feasibility check is not a global optimality certificate. Even an OPTIMAL label applies to the modeled problem and configured tolerances, not omitted real-world constraints.

Use `cofa-test-design` for tiny counterexamples and independent checks, `cofa-debug` for failures and `cofa-explain` to produce an implementation-grounded explanation before submission confirmation. Separate verified results, assumptions and remaining gaps.
