"""Reference validator for UCSF VAL-01.

This module performs registry-level semantic checks in addition to JSON Schema.
It is a validation reference, not a production security control.
"""

from __future__ import annotations

import re
from typing import Any

CAPACITY = 717_000_000
ID_PATTERN = re.compile(r"^UCSF-C-(\\d{9})$")


def validate_registry(
    entries: list[dict[str, Any]],
    approved_control_ids: set[str],
    mandatory_control_ids: set[str],
) -> dict[str, Any]:
    errors: list[str] = []
    by_id: dict[str, dict[str, Any]] = {}

    for index, entry in enumerate(entries):
        cid = str(entry.get("classification_id", ""))
        match = ID_PATTERN.fullmatch(cid)

        if not match:
            errors.append(f"ENTRY[{index}]: invalid classification ID")
            continue

        numeric_id = int(match.group(1))
        if numeric_id < 0 or numeric_id >= CAPACITY:
            errors.append(f"{cid}: ID outside canonical capacity")
            continue

        if cid in by_id:
            errors.append(f"{cid}: duplicate classification ID")
            continue

        by_id[cid] = entry

    for cid, entry in by_id.items():
        for relation in entry.get("relationships", []):
            target = relation.get("target_id")
            if target not in by_id:
                errors.append(f"{cid}: unresolved relationship {target}")

        for mapping in entry.get("control_mappings", []):
            control_id = mapping.get("control_id")
            if control_id not in approved_control_ids:
                errors.append(f"{cid}: unknown control {control_id}")

    missing_mandatory_controls = mandatory_control_ids - approved_control_ids
    for control_id in sorted(missing_mandatory_controls):
        errors.append(f"baseline control registry missing mandatory control {control_id}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "entry_count": len(by_id),
        "errors": errors,
    }
