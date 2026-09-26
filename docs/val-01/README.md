# VAL-01 — Ontology Validation Package

## Objective

VAL-01 defines the machine-readable ontology contract and validation boundary for UCSF classification.

## Scope

- Canonical classification identifiers
- 717,000,000 logical identifier capacity
- Structural schema validation
- Semantic registry validation
- Relationship integrity
- Control mapping integrity
- Lifecycle and provenance
- Negative validation cases

## Non-goals

VAL-01 does not claim:

- that 717,000,000 semantic classifications already exist;
- that each classification represents a unique physical security layer;
- that runtime security controls are effective;
- that UCSF has passed an independent audit;
- that the overall UCSF baseline is locked.

## Package contents

- `schema/ontology-entry.schema.json`
- `validator/validate_registry.py`
- `fixtures/valid.json`
- `fixtures/invalid.json`
- `tests/TEST_MATRIX.md`
- `EVIDENCE.md`

## Acceptance

VAL-01 remains PARTIAL until the validator and test matrix are executed in an authorized environment and reproducible evidence is captured.
