# VAL-01 Independent Review Request Packet

Status: **OPEN — reviewer not yet appointed**  
Prepared: 2026-09-27  
Repository: `RidzBuilder/UCSF`  
PR: [#1](https://github.com/RidzBuilder/UCSF/pull/1)

## Purpose
Obtain a genuinely independent review of VAL-01 ontology validation and its evidence. This packet is a request specification, not proof that a reviewer has accepted or completed the review.

## Independence and qualification requirements
The reviewer must:
- Be a person or qualified review organization other than the repository owner/author (`RidzBuilder`) and not act under the same authoring account.
- Disclose relevant employment, financial, personal, or project conflicts.
- Demonstrate relevant experience in software assurance, ontology/data validation, secure software engineering, or equivalent review practice.
- Access the exact commit under review and the complete source, tests, schema, CI logs, checksum inventory, and governing VAL-01 acceptance criteria.
- Submit findings under their own verifiable identity, identifying exact commit SHA and evidence reviewed.

A self-review, assistant-generated review, automated code scan, or review posted by the repository owner does not by itself satisfy this criterion. Automated analysis may be supplementary.

## Required review coverage
1. Canonical classification ID format and capacity boundaries, including 0, 716999999, and rejection of 717000000.
2. Ontology schema validity and parity/intentional differences between JSON Schema and runtime validator.
3. Semantic field requirements, relationship references/types, duplicate IDs, and graph constraints claimed by acceptance criteria.
4. Control mapping validation, mandatory-control registry semantics, and whether registry inputs are governed and trustworthy.
5. Provenance fields, timestamp parsing, source traceability, and byte-level checksum handling.
6. Test adequacy, negative cases, error handling, dependency/runtime assumptions, and CI reproducibility.
7. Security limitations, misuse cases, and explicit non-claims (no 717M population completeness, production effectiveness, cryptographic signing, or distributed guarantees unless separately evidenced).

## Required reviewer output
- Reviewer name/organization and verifiable GitHub identity or signed report reference.
- Qualifications and conflict-of-interest declaration.
- Exact commit SHA reviewed and date.
- Scope, exclusions, methods, and evidence artifacts examined.
- Findings with severity, affected file/line or requirement, reproducible evidence, and recommended disposition.
- Explicit conclusion against each acceptance criterion, including unresolved limitations.
- Reviewer signature or attributable submission in a channel controlled by the reviewer.

## Disposition and gate
The repository owner must record each finding as accepted, remediated, or formally deferred with rationale, risk owner, compensating controls, and due date. Remediated findings require a retest and reviewer confirmation where material.

VAL-01 remains **BLOCKED** until the independent review is completed, findings are dispositioned, source/checksum provenance is reconciled, and a clean-checkout acceptance run is evidenced against the exact final reviewed commit. This request packet does not promote any gate to PASS.

## Action needed
A qualified reviewer must be identified and invited by the repository owner. No reviewer identity is inferred or fabricated in this packet.
