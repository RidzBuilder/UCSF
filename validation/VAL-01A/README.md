# UCSF VAL-01A — Ontology Validation Package

Status: reference implementation / draft. Not a production security certification.

## Run
From this directory:
`python -m unittest discover -s tests -v`

The core registry validator uses Python standard library only. JSON Schema validation is optional and requires `jsonschema`.

## Scope
- Canonical ID format and 717,000,000 capacity boundaries
- Duplicate IDs and unresolved relationships
- Semantic/provenance presence
- Control mapping shape and approved-control references
- Mandatory control registry presence
- Sparse registry validation

## Explicit limitations
- Does not populate 717 million classifications.
- Does not establish ontology semantic completeness or real-world control effectiveness.
- Approved control IDs and mandatory controls must come from a separately governed baseline registry.
- Does not implement cryptographic signing, distributed registry transactions, or full ontology cycle detection.
- No production deployment or independent review is implied.
