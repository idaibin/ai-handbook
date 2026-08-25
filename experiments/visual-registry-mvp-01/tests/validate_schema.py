#!/usr/bin/env python3
import copy
import hashlib
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
prompt_case_validator, prompt_case_paths, validated_prompt_cases = validate_directory(
    "schema/prompt-case.schema.json", "prompt-cases"
)

contract_ids = {json.loads(path.read_text())["id"] for path in contract_paths}
for path in image_case_paths:
    instance = json.loads(path.read_text())
    if instance["contract_id"] not in contract_ids:
        raise SystemExit(f"{path.name} references unknown contract: {instance['contract_id']}")
    kinds = [variant["kind"] for variant in instance["variants"]]
    expected = {"subject_only", "manual_reference", "contract_compiled"}
    if set(kinds) != expected or len(kinds) != len(expected):
        raise SystemExit(f"{path.name} must contain exactly one A/B/C prompt variant")

for path in prompt_case_paths:
    instance = json.loads(path.read_text())
    actual_prompt_sha = hashlib.sha256(instance["prompt_text"].encode("utf-8")).hexdigest()
    if actual_prompt_sha != instance["prompt_sha256"]:
        raise SystemExit(
            f"{path.name} prompt_sha256 mismatch: {instance['prompt_sha256']} != {actual_prompt_sha}"
        )

    for batch in instance["generation_batches"]:
        if batch["prompt_sha256"] != instance["prompt_sha256"]:
            raise SystemExit(f"{path.name} batch prompt_sha256 differs from PromptCase")
        if len(batch["results"]) != batch["requested_count"]:
            raise SystemExit(
                f"{path.name} batch {batch['batch_id']} result identity count does not equal requested_count"
            )
        sequences = [result["sequence"] for result in batch["results"]]
        if sequences != list(range(1, batch["requested_count"] + 1)):
            raise SystemExit(f"{path.name} batch result sequence must be contiguous and ordered")
        for result in batch["results"]:
            expected_id = f"{instance['prompt_id']}__r{result['sequence']:02d}"
            if result["result_id"] != expected_id:
                raise SystemExit(
                    f"{path.name} result identity mismatch: {result['result_id']} != {expected_id}"
                )
            if result["status"] in {"generated_unverified", "verified", "rejected"}:
                if result["source_kind"] != "provider_native":
                    raise SystemExit(f"{path.name} counted result is not provider_native")
            if result["source_kind"] == "derived_from_composite" and result["status"] != "invalid_attempt":
                raise SystemExit(f"{path.name} derived composite result cannot be counted")

    if instance["metadata"]["status"] == "generation_blocked":
        if not any(batch["status"] == "blocked" for batch in instance["generation_batches"]):
            raise SystemExit(f"{path.name} generation_blocked without a blocked batch")

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

prompt_base = json.loads(prompt_case_paths[0].read_text())
prompt_negative_cases = []

fake_generated = copy.deepcopy(prompt_base)
fake_result = fake_generated["generation_batches"][0]["results"][0]
fake_result["status"] = "verified"
if not list(prompt_case_validator.iter_errors(fake_generated)):
    raise SystemExit("prompt case schema accepted verified result without evidence")
prompt_negative_cases.append("verified_without_evidence")

blocked_without_failure = copy.deepcopy(prompt_base)
del blocked_without_failure["generation_batches"][0]["failure"]
if not list(prompt_case_validator.iter_errors(blocked_without_failure)):
    raise SystemExit("prompt case schema accepted blocked batch without failure")
prompt_negative_cases.append("blocked_without_failure")

bad_result_id = copy.deepcopy(prompt_base)
bad_result_id["generation_batches"][0]["results"][0]["result_id"] = "bad_result"
if not list(prompt_case_validator.iter_errors(bad_result_id)):
    raise SystemExit("prompt case schema accepted invalid result id")
prompt_negative_cases.append("invalid_result_id")

print(
    json.dumps(
        {
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
                {
                    "schema": "prompt-case.schema.json",
                    "validated": validated_prompt_cases,
                    "rejected_negative_cases": prompt_negative_cases,
                    "cross_checks": [
                        "prompt_sha256_matches_prompt_text",
                        "batch_prompt_sha_matches_prompt_case",
                        "requested_count_matches_result_identities",
                        "contiguous_result_sequence",
                        "provider_native_required_for_counted_results",
                        "derived_composite_never_counted",
                        "blocked_status_has_failure_evidence",
                    ],
                },
            ],
        },
        indent=2,
    )
)
