---
name: cofa-test-design
description: "Use when choosing meaningful COFA acceptance checks, boundary cases or property tests, or when passing tests may not exercise the required behavior."
license: CC-BY-SA-4.0
---

# Tests that can catch the wrong implementation

Start with the actual required outcome and the code path that enforces it. Pick the smallest check whose assertion would fail for a plausible defect. Test production functions or actual application entrypoints, not a copied implementation or mocked success alone. Scale effort to consequence and remaining time.

For each important behavior, choose relevant cases from normal input, boundary values, invalid input and state transitions. These are prompts, not a mandatory test matrix for every change. Derive expected results independently from the requirement, a hand-computed fixture or a trusted oracle. Preserve distinctions such as zero versus missing, numeric precision, record multiplicity and unavailable versus empty.

For suitable transformations, read `.cofa-kit/upstream/trailofbits/plugins/property-based-testing/skills/property-based-testing/SKILL.md`, then only the reference matching the current work. Use properties the contract actually supports: preservation, a valid encode/decode roundtrip, idempotence, an independent oracle, or a transformation with a known effect. Pair a broad property with a concrete example: an identity function satisfies idempotence but does not trim or lowercase. A normalizer is lossy, so do not demand its inverse recovers the input.

Apply these corrections when consulting that reference: a specification-derived oracle such as Python integer addition is valid even if its expression resembles the implementation. Reject copied erroneous assumptions, not resemblance alone. Algebraic properties do not have a universal strength ordering; use complementary checks tied to the contract. Commutativity and associativity also hold for XOR and cannot alone establish addition. Inspect the actual generator's output and exit status rather than assuming how an exhausted filter is reported.

Example: for a required descending score sort with ascending ID ties and no lost records, check the exact result of a fixture with ties and duplicate rows, then check adjacent order and full-row multiplicities. Comparing sets would hide duplicate loss; sorted scores alone would miss the tie rule. Do not impose uniqueness if duplicates are allowed.

If a generator library is already usable, reuse it. Otherwise use explicit fixtures, bounded exhaustive cases or fixed-seed standard-library generation with case/time limits. This fallback does not supply automatic shrinking or prove correctness for all inputs. Save a failing input and minimize it where useful. No package acquisition, long fuzz campaign or new runtime is required.

For required persistence, exercise write and an independent read from actual storage. A mocked HTTP 201 proves only the mocked path. Ask the participant to check refresh in the allowed platform preview; test server restart durability only if required. Failure handling should preserve valid state and communicate failure rather than manufacture a successful result.

Read test collection/execution counts, skips, assertions, output and exit status. Import errors, zero executed cases, over-filtered generators, blanket exception catches and missing assertions cannot establish the behavior. A failed property may expose a wrong property or an invalid input rather than an implementation bug; check the contract before changing code. Record ambiguous rules as unresolved instead of silently accepting, rejecting or converting values.

Use `cofa-verify` for evidence recording. Preserve known failures and rerun the original repro after fixes. UI observations remain participant-reported; do not automate the browser.

Attribution: adapted from Trail of Bits Property-Based Testing (pinned in `config/sources.lock.json`), with COFA-specific acquisition, timing, contract and evidence guidance. This adapter and the upstream material retain CC BY-SA 4.0; see `.cofa-kit/upstream/trailofbits/LICENSE`. Other toolkit files retain their stated licenses.
