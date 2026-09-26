# VAL-01 Test Matrix

| Test ID | Scenario | Expected |
|---|---|---|
| ONTO-T01 | Minimum ID `UCSF-C-000000000` | ACCEPT |
| ONTO-T02 | Maximum ID `UCSF-C-716999999` | ACCEPT |
| ONTO-T03 | First ID above capacity `UCSF-C-717000000` | REJECT |
| ONTO-T04 | Malformed/non-numeric ID | REJECT |
| ONTO-T05 | Duplicate active classification ID | REJECT |
| ONTO-T06 | Unresolved relationship target | REJECT |
| ONTO-T07 | Unknown control mapping | REJECT |
| ONTO-T08 | Missing required semantic/provenance fields | REJECT |
| ONTO-T09 | Semantic change without version/change record | REJECT |
| ONTO-T10 | Attempt to weaken mandatory controls | REJECT |
| ONTO-T11 | Duplicate aliases within an entry | REJECT |
| ONTO-T12 | Sparse registry with valid entries | ACCEPT |

## Evidence rule

The table defines expected outcomes only. It does not constitute execution evidence.

Actual validation evidence must capture:

- executed command or workflow;
- repository revision;
- test runner and version;
- input fixture revision;
- actual output;
- timestamp;
- result;
- artifact integrity information where applicable.

A local or reference test result is not production evidence.
