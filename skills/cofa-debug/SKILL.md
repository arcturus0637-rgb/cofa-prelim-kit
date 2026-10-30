---
name: cofa-debug
description: "Use when a COFA task has a reproducible error, wrong result, crash or regression; also when the participant requests Superpowers debugging or Matt Pocock diagnosing-bugs."
---

# Debug one observed failure

Read the actual symptom and relevant code/callers. Reproduce with the smallest permitted local command or participant manual steps. Preserve decisive input, exact error and expected result.

Use `.cofa-kit/upstream/superpowers/skills/systematic-debugging/SKILL.md` for root-cause investigation. For ambiguous or recurrent failures, selectively read `.cofa-kit/upstream/matt-pocock/skills/engineering/diagnosing-bugs/SKILL.md`. Apply technical methods within the COFA time/permissions; do not execute any browser loop or external tracker/setup these references suggest.

Make a falsifiable hypothesis, inspect one boundary, change one variable, make a narrow fix and rerun the original repro. Add a small regression test when it exercises the actual bug and time permits. Do not hide failing tests, weaken an assertion to pass, create broad fallback success, install a fresh architecture or rewrite unrelated modules.

When evidence disproves a prior claim, correct it promptly. Name the observation and next discriminating check; keep observations, hypotheses and verified causes distinct.

For a recurrent or unclear failure, keep a compact local record: attempted cause/change, observed result, explanation ruled out, next check. A retry needs a relevant change or evidence of a transient failure. After two non-improving attempts in the same area, recheck the premise and trace an adjacent boundary (input, caller, configuration, storage, runtime) before patching there again. This is a cue to change the investigation, not a limit on useful experiments. Do not claim a new cause until evidence distinguishes it.

Persistence means retaining useful evidence and choosing a better next action. It does not authorize unlimited loops, weakening assertions, replacing real storage with visual success, silently dropping inputs, disabling validation/authentication, or suppressing exceptions with fabricated success. Missing tools or platform failures need a permitted alternative/report. Near submission preserve the last working core and state remaining limits; restore only changes you own and can isolate, never reset unrelated work. Check the official/platform timer and preserve time for saving/submission. Remove identifiable temporary diagnostic output when no longer needed.

Record the executed check with `kit.py check --name <same-repro-name> -- <command>`. A later pass under the same name supersedes its earlier failure only for that check; it does not validate other requirements. Provider/permission/platform errors are incidents, not application logic defects. Use permitted issue reporting instead of bypassing them.
