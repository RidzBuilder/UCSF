# Recovered Source Checksum Inventory

Generated from the recovered local source directories on 2026-09-26. SHA-256 is computed over each file's exact bytes. Python bytecode and __pycache__ files are intentionally excluded.

This inventory records source material for reconciliation; it does not assert that these files are already committed to GitHub or that tests have been reproduced from the repository.

| Workstream | Relative path | Bytes | SHA-256 |
|---|---|---:|---|
| VAL-01A | UCSF_VAL_01A/README.md | 1034 | c3eb6873ff87c43fb2dc8e38974417b51a946c233fc9b26a34d52ab3ab0c3bc9 |
| VAL-01A | UCSF_VAL_01A/evidence/VAL-01A-test-plan.json | 465 | c62fd9d1a17243de360cd1f3713d0ea6bb06c71f052094c3b6e8722c8842ad61 |
| VAL-01A | UCSF_VAL_01A/evidence/evidence-manifest.json | 1791 | 15b26a11f6f0d665bcf25b0557f298959b311a1b3730713c6a54bc9119358c7d |
| VAL-01A | UCSF_VAL_01A/fixtures/valid-entry.json | 825 | a55de7ddf546ac57a7aa74edfa53d52a2eed1af102e9eaf438e6b808454fcd28 |
| VAL-01A | UCSF_VAL_01A/schemas/ontology-entry-v0.1.schema.json | 5307 | a83aee0e79d16d9c167204ba83c92a15c2f51c19813a4b0e5b42bd9ae1ce1334 |
| VAL-01A | UCSF_VAL_01A/src/ucsf_ontology_validator.py | 4459 | edec1c28b60ecac68f81902a1203b377235f828d603d797014c835a00c426aab |
| VAL-01A | UCSF_VAL_01A/tests/test_ontology_validator.py | 3530 | d66f3cc182aad5a36de9155f87592d11ec5f95ce81885d1233edbfa6707355dd |
| VAL-02 | UCSF_VAL_02/README.md | 1046 | 23ca5d55ea8c36b9177d214cb57dec8dc412cf342fa2c15680e494b08395c845 |
| VAL-02 | UCSF_VAL_02/evidence/VAL-02-test-plan.json | 480 | 04f51843969d171151d8318cfd29d5c6e0d69c8cb47b80694e800cf9362e9309 |
| VAL-02 | UCSF_VAL_02/evidence/evidence-manifest.json | 1829 | fa5f672c50c80f1cfd0b5bd10207c49616c580c704ad6465592f1ee5dcd08504 |
| VAL-02 | UCSF_VAL_02/schemas/state-transition-v0.1.schema.json | 3197 | bbc0ebaa1cfdb920923687931cb9cbe33056609708266d6da5f4ec16b8ed2c25 |
| VAL-02 | UCSF_VAL_02/src/ucsf_state_machine.py | 5636 | ac07cccd6b5173d6c6393aaac1aaae053c5fde60a9430b4dff377f655c0ae12f |
| VAL-02 | UCSF_VAL_02/tests/test_state_machine.py | 5384 | 2c5f8f7b45785324db5aebb6c3901a04b04dbaa64430c5f66a36e9840807f551 |
| VAL-02A | UCSF_VAL_02A/README.md | 937 | 5fb6c04c051ec17838784421f4a826c18019a8ade24986d9e1a05ef592258147 |
| VAL-02A | UCSF_VAL_02A/evidence/evidence-manifest.json | 1537 | c37a232f5520c20073889a3b77d852c35e2ddc6fe6ff75507e70ec7faa4917cf |
| VAL-02A | UCSF_VAL_02A/src/ucsf_transactional_store.py | 9554 | aa3fd9c8f577cde258a290a67789d43896a3e78b9b54a312fa9946761237185b |
| VAL-02A | UCSF_VAL_02A/tests/test_transactional_store.py | 5154 | b4b4891c00210637ccfd4ec47c35339aa9dc816dc72487f929bfb8dc83fddf8a |
| VAL-02B | UCSF_VAL_02B/README.md | 1435 | e44afb1a0b31c5cb0d7bf2108bd6a03c5ecf426121220695be567ec5067e074b |
| VAL-02B | UCSF_VAL_02B/evidence/manifest.json | 630 | f7daad4970d42a46f38414f87338c2d32441a9993fa1e12ed0ffc3ce8bfcc42f |
| VAL-02B | UCSF_VAL_02B/src/__init__.py | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| VAL-02B | UCSF_VAL_02B/src/recovery.py | 3811 | 92e5e515188c52f20c192397a946b5ba1f16026d66fe9ea0cdcb46f4a7f26e53 |
| VAL-02B | UCSF_VAL_02B/tests/test_recovery.py | 4295 | 3ae567b621ae3a11dc198fb4631b8d9da4358e43f63d8abc11559b0c1654cf94 |

## Reconciliation status
- 22 non-cache source, schema, fixture, test, and evidence files enumerated.
- Original ZIP archives are retained outside the repository and are not uploaded in this source inventory.
- The inventory is a recovery snapshot. Recompute hashes after copying files into the repository and compare exact byte-level equality.
- Historical package-level ZIP checksums are separate from per-file checksums.
