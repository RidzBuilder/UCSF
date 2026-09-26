# UCSF — Universal Cybersecurity Framework

**Repository status:** Bootstrap baseline  
**Specification status:** Working Draft (v0.2; not locked)  
**Security/release status:** Not production-approved

UCSF is a universal, evidence-driven cybersecurity framework intended to support security assessment, classification, architecture, implementation, verification, audit, and recovery across AI agents, applications, infrastructure, data, platforms, and projects.

## Foundational invariants

1. The classification capacity of 717,000,000 is a logical classification space, not a requirement to instantiate 717 million physical layers or controls.
2. Canonical classification identifiers range from `UCSF-C-000000000` through `UCSF-C-716999999`.
3. Project controls and security layers are derived from the applicable Project Security Specification (PSS), architecture, threat model, risk, and requirements. Universal mandatory controls may not be weakened because a project uses fewer classifications or layers.
4. Defender, authorized Active Defense, and isolated Hunter/deception capabilities operate under explicit scope, authorization, safety limits, evidence preservation, and recovery controls.
5. No external retaliation, unauthorized access, unbounded loops, or uncontrolled deception is permitted.
6. No PASS, release, or production-readiness claim without applicable acceptance criteria and reproducible evidence. Local reference tests are not production evidence.

## Initial integration workstreams

- VAL-01A — Ontology validation reference
- VAL-02 — State machine conformance reference
- VAL-02A — Transactional state consistency reference
- VAL-02B — Durable recovery, backup/restore, and fault-injection reference

The above workstreams are reference validation packages. Their integration does not itself close the overall UCSF audit gates.

## Repository bootstrap note

This initial commit establishes a traceable repository baseline only. It does not claim that the specification, threat model, architecture, implementation, or independent audit is complete. Subsequent integration is to occur on a dedicated branch and be reviewed through a pull request.

See `docs/BASELINE_STATUS.md` for current status, evidence boundaries, and known gaps.
