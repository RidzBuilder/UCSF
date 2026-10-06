# UCSF Integration Manifest — VAL-01A through VAL-02B

Status: staged integration manifest; Path A internal validation is active; source payload integration beyond VAL-01A is not complete.

## Provenance and workstream inventory

| Workstream | Recovered local package | Recorded local tests | Integration status |
|---|---|---:|---|
| VAL-01A | UCSF_VAL_01A_package.zip | 12/12 | Pending source file commit and clean-checkout rerun |
| VAL-02 | UCSF_VAL_02_package.zip | 17/17 | Pending source file commit and clean-checkout rerun |
| VAL-02A | UCSF_VAL_02A_package.zip | 15/15 | Pending source file commit and clean-checkout rerun |
| VAL-02B | UCSF_VAL_02B_package.zip | 14/14 | Pending source file commit and clean-checkout rerun |

## Artifact policy
- Include source, tests, schemas, fixtures, test plans, manifests, and human-readable evidence.
- Exclude Python bytecode/cache files (`__pycache__`, `*.pyc`).
- Preserve original package evidence manifests as historical evidence; generate a separate repository integration manifest after calculating repository-file hashes.
- Do not silently modify source while claiming it is byte-for-byte the original package. Any remediation must be recorded as a distinct change with rationale and tests.
- The local package ZIP checksums and prior test records are provenance claims, not a substitute for reproducing tests from the repository.

## Required repository-native completion
1. Commit all source and test files to this integration branch.
2. Add dependency and supported-runtime declarations.
3. Run each workstream test suite from a clean checkout and record exact command, interpreter, commit SHA, output, and exit code.
4. Review cross-workstream interface consistency and security assumptions.
5. Add CI and verify successful repository-native runs on the relevant branch HEADs.
6. Conduct internal engineering review, reconcile evidence, and update gates only when evidence is sufficient.
7. Treat independent external review as a separate assurance track, not a Path A R&D blocker.

## Gate
Overall integration gate: **BLOCKED/PARTIAL**. VAL-01A exact-HEAD tests and schema validation have been reproduced and passed after remediation. Source payloads for VAL-02/VAL-02A/VAL-02B remain absent from this repository branch, so broader integration is not closed. This manifest alone does not close VAL-01 or VAL-02B.
