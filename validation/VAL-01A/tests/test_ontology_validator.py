import unittest
from ucsf_ontology_validator import validate_registry, CAPACITY

CONTROLS = {"UCSF-CTRL-001", "UCSF-CTRL-010"}
MANDATORY = {"UCSF-CTRL-001"}

def entry(cid="UCSF-C-000000001", rels=None, mappings=None):
    return {
      "ontology_version":"0.1.0",
      "classification_id":cid,
      "semantic_definition":{"canonical_name":"Test classification","definition":"Test definition","security_domain":"identity"},
      "dimensions":{"asset":[],"data":[],"trust":[],"threat":[],"risk":[],"security_objective":[]},
      "relationships": rels or [],
      "control_mappings": mappings or [{"control_id":"UCSF-CTRL-001","mapping_type":"mandatory","applicability":"Always applicable"}],
      "lifecycle":{"status":"draft","effective_version":"0.1.0","supersed_by":None},
      "provenance":{"created_by":"test","created_at":"2026-09-26T00:00:00Z","source_reference":["test-fixture"],"change_reason":"initial test"}
    }

class TestOntologyValidator(unittest.TestCase):
    def test_min_boundary(self):
        self.assertEqual(validate_registry([entry("UCSF-C-000000000")],CONTROLS,MANDATORY)["status"],"PASS")
    def test_max_boundary(self):
        self.assertEqual(validate_registry([entry("UCSF-C-716999999")],CONTROLS,MANDATORY)["status"],"PASS")
    def test_over_capacity(self):
        self.assertEqual(validate_registry([entry("UCSF-C-717000000")],CONTROLS,MANDATORY)["status"],"FAIL")
    def test_bad_format(self):
        self.assertEqual(validate_registry([entry("UCSF-C-ABC")],CONTROLS,MANDATORY)["status"],"FAIL")
    def test_duplicate_id(self):
        result=validate_registry([entry(),entry()],CONTROLS,MANDATORY)
        self.assertTrue(any("duplicate classification ID" in e for e in result["errors"]))
    def test_unresolved_relationship(self):
        result=validate_registry([entry(rels=[{"relation_type":"is_a","target_id":"UCSF-C-000000099"}])],CONTROLS,MANDATORY)
        self.assertTrue(any("unresolved relationship" in e for e in result["errors"]))
    def test_unknown_control(self):
        result=validate_registry([entry(mappings=[{"control_id":"UCSF-CTRL-099","mapping_type":"mandatory","applicability":"Always"}])],CONTROLS,MANDATORY)
        self.assertTrue(any("unknown control" in e for e in result["errors"]))
    def test_missing_semantics(self):
        e=entry(); e["semantic_definition"]["definition"]=""
        result=validate_registry([e],CONTROLS,MANDATORY)
        self.assertTrue(any("semantic_definition.definition" in x for x in result["errors"]))
    def test_missing_provenance(self):
        e=entry(); e["provenance"]["source_reference"]=[]
        result=validate_registry([e],CONTROLS,MANDATORY)
        self.assertTrue(any("provenance.source_reference" in x for x in result["errors"]))
    def test_mandatory_control_registry_missing(self):
        result=validate_registry([entry()],CONTROLS,set(CONTROLS)|{"UCSF-CTRL-999"})
        self.assertTrue(any("Baseline registry missing mandatory" in x for x in result["errors"]))
    def test_self_hierarchy_reference(self):
        result=validate_registry([entry(rels=[{"relation_type":"part_of","target_id":"UCSF-C-000000001"}])],CONTROLS,MANDATORY)
        self.assertTrue(any("prohibited self-reference" in x for x in result["errors"]))
    def test_sparse_registry_valid(self):
        result=validate_registry([entry()],CONTROLS,MANDATORY)
        self.assertEqual(result["status"],"PASS")
        self.assertEqual(result["capacity"],CAPACITY)

if __name__ == "__main__":
    unittest.main(verbosity=2)
