# UCSF — Baseline Status

**Baseline branch:** `main`  
**Integration branch:** `ucsf/val-01-bootstrap`  
**Specification status:** Working Draft v0.2  
**Baseline lock:** NOT LOCKED  
**Production approval:** NOT APPROVED

## Purpose

This document records the repository baseline, evidence boundaries, and active validation gaps for UCSF.

## Current validation state

- VAL-01 — Ontology Validation: **PARTIAL / BOOTSTRAPPED**
- VAL-02 — State Machine Conformance: **NOT STARTED**
- VAL-02A — Transactional State Consistency: **NOT STARTED**
- VAL-02B — Durable Recovery / Fault Injection: **NOT STARTED**

## Evidence boundary

Repository bootstrap artifacts establish source-of-truth structure and validation contracts. They do not prove runtime security effectiveness, production readiness, or independent audit conformance.

A validation item may be marked CLOSED only when its acceptance criteria are satisfied with reproducible evidence and the applicable review gate has passed.

## Foundational invariants

1. 717,000,000 is a logical classification capacity, not a requirement to instantiate 717 million physical defense layers.
2. Canonical classification identifiers span `UCSF-C-000000000` through `UCSF-C-716999999`.
3. Classification, control, and security-layer identities remain distinct concepts.
4. Mandatory security controls cannot be weakened or removed through project classification.
5. Defender, authorized active defense, and isolated Hunter/deception operate only within explicit authorization, scope, isolation, resource, and evidence boundaries.
6. Deception loops must have bounded resource consumption and termination conditions.
7. Recovery requires evidence preservation and security validation before re-entry.
8. PASS, release, and production-readiness claims require applicable evidence.

## Known gaps

- Full ontology vocabulary and semantic constraints are still under review.
- VAL-01 executable tests are not yet evidenced in this branch.
- Independent review has not yet occurred.
- No implementation or production environment has been validated by this repository state.
