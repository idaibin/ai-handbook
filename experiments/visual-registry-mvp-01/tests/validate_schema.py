#!/usr/bin/env python3
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    return json.loads((ROOT / name).read_text())


def validate_directory(schema_path: str, directory: str):
    schema = load(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    paths = sorted((ROOT / directory).glob("*.json"))
    validated = []
    for path in paths:
        instance = json.loads(path.read_text())
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        if errors:
            rendered = "\n".join(f"{list(error.path)}: {error.message}" for error in errors)
            raise SystemExit(f"{path.name} failed schema validation:\n{rendered}")
        validated.append(path.name)
    return validator, paths, validated


contract_validator, contract_paths, validated_contracts = validate_directory(
    "schema/visual-contract.schema.json", "contracts"
)
image_case_validator, image_case_paths, validated_image_cases = validate_directory(
    "schema/image-generation-case.schema.json", "image-cases"
)

contract_ids = {
    json.loads(path.read_text())["id"]
    for path in contract_paths
}
for path in image_case_paths:
    instance = json.loads(path.read_text())
    if instance["contract_id"] not in contract_ids:
        raise SystemExit(f"{path.name} references unknown contract: {instance['contract_id']}")
    kinds = [variant["kind"] for variant in instance["variants"]]
    expected = {"subject_only", "manual_reference", "contract_compiled"}
    if set(kinds) != expected or len(kinds) != len(expected):
        raise SystemExit(f"{path.name} must contain exactly one A/B/C prompt variant")

base = json.loads(contract_paths[0].read_text())
contract_negative_cases = []
for forbidden_key, value in (
    ("prompt", "provider prompt"),
    ("template", "{subject}"),
    ("models", {"gemini": "x"}),
):
    candidate = copy.deepcopy(base)
    candidate[forbidden_key] = value
    errors = list(contract_validator.iter_errors(candidate))
    if not errors:
        raise SystemExit(f"schema incorrectly accepted provider-specific field: {forbidden_key}")
    contract_negative_cases.append(forbidden_key)

bad_id = copy.deepcopy(base)
bad_id["id"] = "Bad ID"
if not list(contract_validator.iter_errors(bad_id)):
    raise SystemExit("schema incorrectly accepted invalid id")
contract_negative_cases.append("invalid_id")

consumer_category = copy.deepcopy(base)
consumer_category["category"] = "story_studio"
if not list(contract_validator.iter_errors(consumer_category)):
    raise SystemExit("schema incorrectly accepted a consumer identity as visual category")
contract_negative_cases.append("consumer_identity_as_category")

image_base = json.loads(image_case_paths[0].read_text())
image_negative_cases = []

missing_manual_prompt = copy.deepcopy(image_base)
manual = next(variant for variant in missing_manual_prompt["variants"] if variant["kind"] == "manual_reference")
del manual["prompt"]
if not list(image_case_validator.iter_errors(missing_manual_prompt)):
    raise SystemExit("image case schema accepted manual_reference without prompt")
image_negative_cases.append("manual_reference_without_prompt")

subject_with_prompt = copy.deepcopy(image_base)
subject_variant = next(variant for variant in subject_with_prompt["variants"] if variant["kind"] == "subject_only")
subject_variant["prompt"] = "should not be stored"
if not list(image_case_validator.iter_errors(subject_with_prompt)):
    raise SystemExit("image case schema accepted prompt on subject_only variant")
image_negative_cases.append("subject_only_with_prompt")

bad_target = copy.deepcopy(image_base)
bad_target["target"] = "unknown_provider"
if not list(image_case_validator.iter_errors(bad_target)):
    raise SystemExit("image case schema accepted unsupported target")
image_negative_cases.append("unsupported_target")

print(json.dumps({
    "status": "passed",
    "schemas": [
        {
            "schema": "visual-contract.schema.json",
            "validated": validated_contracts,
            "rejected_negative_cases": contract_negative_cases,
        },
        {
            "schema": "image-generation-case.schema.json",
            "validated": validated_image_cases,
            "rejected_negative_cases": image_negative_cases,
        },
    ],
}, indent=2))
