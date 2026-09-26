"""Minimal executable VAL-01 boundary/semantic tests.

Uses only Python standard library so the reference validation package has
no third-party runtime dependency.
"""

from __future__ import annotations

import json
import pathlib
import unittest

from validator.validate_registry import validate_registry

ROOT = pathlib.Path(__file__).parents[1]
FIXTURES = ROOT / "fixtures"


class ValidatorTests(unittest.TestCase):
    def test_minimum_and_maximum_ids_are_in_range(self) -> None:
        entries = json.loads((FIXTURES / "valid.json").read_text())
        result = validate_registry(
            entries=entries,
            approved_control_ids={"UCSF-CTRL-001"},
            mandatory_control_ids={"UCSF-CTRL-001"},
        )
        self.assertEqual(result["status"], "PASS")

    def test_invalid_fixture_is_rejected_by_boundary_check(self) -> None:
        entries = json.loads((FIXTURES / "invalid.json").read_text())
        result = validate_registry(
            entries=entries,
            approved_control_ids={"UCSF-CTRL-001"},
            mandatory_control_ids={"UCSF-CTRL-001"},
        )
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("outside canonical capacity" in e for e in result["errors"]))

    def test_duplicate_ids_are_rejected(self) -> None:
        entries = json.loads((FIXTURES / "valid.json").read_text())
        entries.append(entries[0].copy())
        result = validate_registry(
            entries=entries,
            approved_control_ids={"UCSF-CTRL-001"},
            mandatory_control_ids={"UCSF-CTRL-001"},
        )
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any("duplicate classification ID" in e for e in result["errors"]))


if __name__ == "__main__":
    unittest.main()
