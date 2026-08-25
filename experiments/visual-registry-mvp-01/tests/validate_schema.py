#!/usr/bin/env python3
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema" / "visual-contract.schema.json").read_text())
validator = Draft202012Validator(SCHEMA)
contract_paths = sorted((ROOT / "contracts").glob("*.json"))
validated = []

for path in contract_paths:
    instance = json.loads(path.read_text())
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        rendered = "\n".join(f"{list(error.path)}: {error.message}" for error in errors)
        raise SystemExit(f"{path.name} failed schema validation:\n{rendered}")
    validated.append(path.name)

base = json.loads(contract_paths[0].read_text())
negative_cases = []
for forbidden_key, value in (
    ("prompt", "provider prompt"),
    ("template", "{subject}"),
    ("models", {"gemini": "x"}),
):
    candidate = copy.deepcopy(base)
    candidate[forbidden_key] = value
    errors = list(validator.iter_errors(candidate))
    if not errors:
        raise SystemExit(f"schema incorrectly accepted provider-specific field: {forbidden_key}")
    negative_cases.append(forbidden_key)

bad_id = copy.deepcopy(base)
bad_id["id"] = "Bad ID"
if not list(validator.iter_errors(bad_id)):
    raise SystemExit("schema incorrectly accepted invalid id")
negative_cases.append("invalid_id")

consumer_category = copy.deepcopy(base)
consumer_category["category"] = "story_studio"
if not list(validator.iter_errors(consumer_category)):
    raise SystemExit("schema incorrectly accepted a consumer identity as visual category")
negative_cases.append("consumer_identity_as_category")

print(json.dumps({
    "status": "passed",
    "schema": "visual-contract.schema.json",
    "validated_contracts": validated,
    "rejected_negative_cases": negative_cases,
}, indent=2))
