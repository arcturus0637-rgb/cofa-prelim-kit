---
name: cofa-verify
description: "Use before claiming a COFA implementation is fixed, complete, tested or ready for submission, or after a source change invalidates previous evidence."
---

# Evidence before completion claims

Read `.cofa-kit/upstream/superpowers/skills/verification-before-completion/SKILL.md` as technical guidance, under current task permissions and remaining time.

Map each actual must-have requirement to a relevant check. Use `cofa-test-design` when selecting checks or when passing tests may miss the behavior. Run the real command and inspect full output/exit status, test collection, executed count and skips. Failed collection or zero executed cases cannot establish passing behavior. Use `python .cofa-kit/kit.py check --name <name> -- <command>` to retain raw local logs and source freshness markers. A test of the wrong behavior, linter pass, build pass or agent report is not evidence of the requested user flow.

Report separately what was implemented, executed and observed, and what remains unverified or blocked. Source inspection supports a source-level claim; a mocked helper supports only that seam. Neither establishes real persistence or UI behavior. Correct earlier success claims if new evidence contradicts them. List partial or unchecked mandatory outcomes and the next feasible check rather than calling the whole task complete. Do not hide a failing path, substitute sample output for real results, or silently lower the requirement to fit the implementation.

Link passing evidence with `require --id <R> --status verified --evidence <E>`. Do not fabricate evidence. For web tasks, participant manually exercises the main flow, invalid input, navigation and persistence in the allowed platform preview. Only after the participant reports observations, use `manual --name manual-ui --result pass|fail --note <actual-observation>`. This is explicitly human-reported, not an automated browser check. No Playwright, screenshots, CDP, browser-use or other computer automation.

Source changes stale previous evidence; rerun only affected meaningful checks, and the necessary final build/regression checks. The conservative fingerprint may stale more than necessary; it never proves behavior by itself. Don't hide failures in truncated output. Use `handoff` with actual required filenames; inspect saved state/conflicts and the platform preview. Handoff report is not final platform submission. Confirmed submission ends AI task work and oral assistance remains prohibited.
