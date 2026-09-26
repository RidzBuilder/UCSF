"""UCSF VAL-01A reference registry validator. Python standard library only."""
import re
from datetime import datetime
from collections import defaultdict

CAPACITY = 717_000_000
ID_RE = re.compile(r"^UCSF-C-([0-9]{9})$")
CONTROL_RE = re.compile(r"^UCSF-CTRL-[0-9]{3}$")
REL_TYPES = {"is_a", "part_of", "depends_on", "related_to", "supersedes"}
MAP_TYPES = {"mandatory", "conditional_mandatory", "supplementary"}

def validate_registry(entries, approved_control_ids, mandatory_control_ids):
    errors = []
    by_id = {}
    for i, entry in enumerate(entries):
        cid = entry.get("classification_id", "") if isinstance(entry, dict) else ""
        m = ID_RE.fullmatch(cid) if isinstance(cid, str) else None
        if not m:
            errors.append(f"ENTRY[{i}]: invalid classification ID")
            continue
        n = int(m.group(1))
        if n >= CAPACITY:
            errors.append(f"{cid}: ID exceeds capacity")
            continue
        if cid in by_id:
            errors.append(f"{cid}: duplicate classification ID")
            continue
        by_id[cid] = entry

    for cid, entry in by_id.items():
        # Basic required semantic and provenance checks.
        sem = entry.get("semantic_definition", {})
        for field in ("canonical_name", "definition", "security_domain"):
            if not isinstance(sem.get(field), str) or not sem[field].strip():
                errors.append(f"{cid}: missing semantic_definition.{field}")
        prov = entry.get("provenance", {})
        for field in ("created_by", "created_at", "source_reference", "change_reason"):
            if field not in prov or prov[field] in ("", None, []):
                errors.append(f"{cid}: missing provenance.{field}")
        if prov.get("created_at"):
            try:
                datetime.fromisoformat(prov["created_at"].replace("Z","+00:00"))
            except (ValueError, AttributeError):
                errors.append(f"{cid}: invalid provenance.created_at")

        for rel in entry.get("relationships", []):
            target = rel.get("target_id")
            rtype = rel.get("relation_type")
            if rtype not in REL_TYPES:
                errors.append(f"{cid}: invalid relationship type {rtype}")
            if target not in by_id:
                errors.append(f"{cid}: unresolved relationship {target}")
            if target == cid and rtype in {"is_a","part_of","supersedes"}:
                errors.append(f"{cid}: prohibited self-reference for {rtype}")

        seen_maps = set()
        for mapping in entry.get("control_mappings", []):
            control_id = mapping.get("control_id")
            mapping_type = mapping.get("mapping_type")
            if not isinstance(control_id, str) or not CONTROL_RE.fullmatch(control_id):
                errors.append(f"{cid}: malformed control ID {control_id}")
            elif control_id not in approved_control_ids:
                errors.append(f"{cid}: unknown control {control_id}")
            if mapping_type not in MAP_TYPES:
                errors.append(f"{cid}: invalid mapping type {mapping_type}")
            if not isinstance(mapping.get("applicability"), str) or not mapping["applicability"].strip():
                errors.append(f"{cid}: empty control applicability")
            key = (control_id, mapping_type)
            if key in seen_maps:
                errors.append(f"{cid}: duplicate control mapping {key}")
            seen_maps.add(key)

    for control_id in mandatory_control_ids:
        if control_id not in approved_control_ids:
            errors.append(f"Baseline registry missing mandatory control {control_id}")

    # A record's mappings cannot waive the baseline mandatory set.
    return {
        "status": "PASS" if not errors else "FAIL",
        "entry_count": len(by_id),
        "capacity": CAPACITY,
        "errors": errors
    }

def validate_schema(entry, schema):
    """Optional JSON Schema validation; requires jsonschema package."""
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        return {"status":"BLOCKED", "errors":["Install jsonschema to run schema validation"]}
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(entry), key=lambda e: list(e.path))
    return {"status":"PASS" if not errors else "FAIL",
            "errors":[f"{list(e.path)}: {e.message}" for e in errors ]}