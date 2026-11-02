---
name: cofa-explain
description: "Use during COFA task work before submission confirmation to produce a Korean explanation artifact grounded in the actual implementation, design choices, validation and limitations. Not for answering the later written/oral questions."
---

# Explain the actual implementation before confirmation

The participant requests an explanation file as a submission artifact. During permitted task work, write `IMPLEMENTATION.ko.md` in the actual project by default. If the task mandates a different documentation name, merge the explanation into the permitted file instead; do not violate an output whitelist. This toolkit cannot submit it automatically. After platform confirmation or during the written/oral stage, stop AI assistance under `cofa-prelim`.

Read the implemented code, entrypoints, requirements and actual evidence. Use `.cofa-kit/assets/IMPLEMENTATION.template.ko.md` as an outline, replace every writing prompt with actual facts and omit irrelevant sections. Do not deliver the untouched template. Explain in clear Korean for a participant who must understand their own work; introduce technical terms with their concrete role.

Include the problem and exact scope, input-to-output data flow, implementation entrypoints and important files, algorithm/model and why chosen, required constraints/objective and where enforced, one small accurately calculated example where useful, commands/observations actually checked, and unresolved assumptions/limitations. For optimization, distinguish feasibility from optimality, model status, objective units, heuristic/solver stopping conditions and unsupported real-world constraints. Include baseline comparisons only if actually performed on comparable valid results.

Explain important choices and tradeoffs from the final code, not an abandoned plan or a generic architecture. Give the participant a traceable flow: what enters, what decides, what is stored, what comes out, and what happens on invalid input or failure. Cite real local project-relative paths in the document, preserving required filenames and identifiers. Do not invent benchmarks, run outcomes, exact optimality, external API use or features.

Keep the artifact concise enough to read before submission, with detail proportional to the code. Review it after final edits so it agrees with the submitted implementation. A documentation edit can stale the kit's conservative fingerprint; record new final checks as needed. Add the actual permitted explanation path to `handoff --required-file`, and have the participant confirm it appears in the platform submission list.

This is implementation documentation prepared during authorized task work. Do not generate anticipated exam questions, model answers or a written/oral script; the participant answers those independently in the later stage.
