---
name: cofa-review
description: "Use when reviewing changed COFA task code for concrete bugs, regression risk, requirement omissions or a concise Caveman/Matt/Ponytail code review."
---

# Review the actual diff

Read requirements, touched callers and the diff. Prioritize wrong outcomes, omitted must-have flows, destructive data handling, broken persistence, invalid input and runtime errors. Use `.cofa-kit/upstream/matt-pocock/skills/engineering/code-review/SKILL.md` for focused review and `.cofa-kit/upstream/ponytail/skills/ponytail-review/SKILL.md` for scoped simplification checks. Caveman concise review reference: `.cofa-kit/upstream/caveman/skills/caveman-review/SKILL.md`.

Trace important changed paths across input validation, computation, storage and failure handling. For protected operations, check authorization at the actual enforcement point. Match depth to the feature; do not apply a full security audit to every file. Use `cofa-test-design` if tests miss a plausible wrong result. For React/Next.js-specific issues read `.cofa-kit/docs/REACT.ko.md` selectively.

Report only actionable findings with file/location, trigger, impact and a small fix. State uncertainty when no reproduction exists. Findings are not proof of test execution. No invented bugs, bulk formatting, PR creation, repository uploads or mandatory multi-agent review. Near the deadline, fix correctness/submission blockers first; record optional cleanup instead of expanding scope. Run a focused relevant check after a fix; don't claim UI success from a build.
