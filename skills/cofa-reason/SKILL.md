---
name: cofa-reason
description: "Use when translating a COFA assignment into implementation decisions, comparing feasible approaches, or resolving an uncertain requirement or technical assumption before coding."
---

# From assignment to a testable solution

Use the assignment, supplied project and current phase/time as evidence. Keep analysis proportional: a clear local correction needs a local check, not a design ceremony. Follow `cofa-prelim` for event constraints.

For a new or ambiguous feature, keep a short working record:

| Field | What belongs here |
|---|---|
| Required outcome | The actual problem statement and observable acceptance condition |
| Constraints | Supplied interfaces, data, runtime, acquisition rules and remaining time |
| Known / uncertain | What was observed, what is inferred, and which unknown changes the next action |
| Chosen approach | Why this is the smallest feasible complete path; its decisive check |

Read existing callers, data formats and run scripts before choosing a design. Trace the path from input through computation/storage to output. Separate a feature that exists in code from a path that was exercised. Preserve existing architecture, exact units, precision and required records.

If multiple interpretations change required results, consult the supplied practitioner agent through the permitted channel. Investigate checkable facts yourself. For reversible implementation choices, select a reasonable default and state it; do not ask the participant to approve each routine step. Do not invent missing business rules or add features to make a demonstration look complete.

For a consequential technical uncertainty, compare plausible approaches by correctness, existing support, implementation cost and ease of verification. Run the cheapest local probe that could change the choice. Where the cause is unclear, consider rival explanations and name an observation that separates them. If evidence already identifies a straightforward cause, fix it directly. No fixed hypothesis count or hidden chain-of-thought transcript is required: report the decision, key evidence and next check.

Build one complete required path early, then extend it. Track actual requirements with `require`; use `note --kind decision|limitation|blocker` for consequential choices or unknowns. Keep investigation records inside the task; no external tracker, personal model or MCP is needed. Route failure diagnosis to `cofa-debug`, test selection to `cofa-test-design`, and final evidence to `cofa-verify`.

Example: if fees may be zero and some quotes are unavailable, inspect the schema and eligibility contract. A numeric zero is not evidence of unavailability. Preserve valid zero values; resolve the missing-value policy before asserting it as a requirement.
