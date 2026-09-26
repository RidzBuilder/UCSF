# UCSF Repository Baseline Status

## Baseline
- Bootstrap commit on `main`: `aed796e94b1556fc7a8864cfb70b0403b7d5f779`
- Integration branch: `ucsf/val-01-val-02b-integration`
- Specification: UCSF Fundamental Specification v0.2, Working Draft (not locked).
- This document records integration status, not a security certification.

## Local reference packages recovered
The following package directories were present in the execution environment:
- `UCSF_VAL_01A`
- `UCSF_VAL_02`
- `UCSF_VAL_02A`
- `UCSF_VAL_02B`

Their test outcomes were previously recorded as:
| Workstream | Local tests | Current gate | Key limitations |
|---|---:|---|---|
| VAL-01A | 12 passed, 0 failed | PARTIAL | Incomplete taxonomy; no independent review; sparse fixtures; no full 717M enumeration |
| VAL-02 | 17 passed, 0 failed | PARTIAL | In-memory, single process; no durable/distributed concurrency |
| VAL-02A | 15 passed, 0 failed | PARTIAL | Local SQLite; no distributed consensus, production HA, signed provenance, or independent review |
| VAL-02B | 14 passed, 0 failed | PARTIAL overall | Local SQLite backup/restore and deterministic failpoints; no production storage fault, distributed consensus, signed provenance, or independent review |

These are inherited local execution records and are not yet independently reproduced from this repository. They must not be represented as repository CI results.

## Current integration status
- Repository bootstrap is complete.
- Integration branch is created.
- PR #1 is open and non-draft against `main`; head is `dae0f99c8687d7e33bc951a9adb356561c94c959`.
- VAL-01A source, test, schema, fixture, and evidence files are present in the integration branch; repository-native CI evidence exists for the VAL-01A reference suite.
- No merge to `main` has been authorized or performed.

## Blocking conditions
1. Reconcile repository-file byte hashes against the recovered-source inventory; current inspection has not independently recomputed those SHA-256 values from a local checkout.
2. Inspect code and tests for security-sensitive behavior, dependency assumptions, and cross-package interfaces.
3. Integrate on the integration branch, preserving package provenance and licensing.
4. Run the complete VAL-01 acceptance suite from a clean checkout and capture exact command, runtime, output, and commit SHA; current CI evidence covers the VAL-01A unittest suite only.
5. Reconcile schema-vs-validator enforcement and execute schema validation if required by the governing acceptance criteria.
6. Obtain genuinely independent review; the current GitHub review is authored by `RidzBuilder` and is not an external reviewer.
7. Update audit gates only from evidence. Overall UCSF readiness remains BLOCKED/PARTIAL as applicable.

## Security and governance invariants
- No unauthorized external access, retaliation, or active defense outside owned/authorized scope.
- Deception/hunter functions must be isolated, bounded, observable, and kill-switchable.
- Exceptions require scope, owner, rationale, expiration, residual risk, compensating controls, and remediation.
- No gate may be promoted to PASS by documentation alone.
