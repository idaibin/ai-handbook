#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
rm -rf dist
mkdir -p evidence

tsc -p tsconfig.json
python3 tests/validate_schema.py > evidence/schema-validation.json
node tests/compiler.test.mjs > evidence/compiler-test.json
node tests/query.test.mjs > evidence/query-test.json
node tests/image-case.test.mjs > evidence/image-case-test.json
node tests/prompt-case.test.mjs > evidence/prompt-case-test.json

node prototype/demo.mjs > evidence/compiler-output.json
node prototype/demo.mjs > evidence/compiler-output.rerun.json
cmp --silent evidence/compiler-output.json evidence/compiler-output.rerun.json
COMPILER_SHA="$(sha256sum evidence/compiler-output.json | awk '{print $1}')"
rm evidence/compiler-output.rerun.json

node prototype/query-cli.mjs snapshot --json > evidence/query-index.json
node prototype/query-cli.mjs snapshot --json > evidence/query-index.rerun.json
cmp --silent evidence/query-index.json evidence/query-index.rerun.json
QUERY_SHA="$(sha256sum evidence/query-index.json | awk '{print $1}')"
rm evidence/query-index.rerun.json

node prototype/image-case-output.mjs > evidence/image-case-prompts.json
node prototype/image-case-output.mjs > evidence/image-case-prompts.rerun.json
cmp --silent evidence/image-case-prompts.json evidence/image-case-prompts.rerun.json
IMAGE_CASE_SHA="$(sha256sum evidence/image-case-prompts.json | awk '{print $1}')"
rm evidence/image-case-prompts.rerun.json

PROMPT_CASE_SHA="$(sha256sum prompt-cases/anthropomorphic-watercolor-cat-librarian-v01.json | awk '{print $1}')"

python3 - "$COMPILER_SHA" "$QUERY_SHA" "$IMAGE_CASE_SHA" "$PROMPT_CASE_SHA" <<'PY' > evidence/determinism-rerun.json
import json
import sys
print(json.dumps({
    "status": "passed",
    "process_runs_per_generated_artifact": 2,
    "byte_identical": True,
    "compiler_output_sha256": sys.argv[1],
    "query_index_sha256": sys.argv[2],
    "image_case_prompts_sha256": sys.argv[3],
    "prompt_case_source_sha256": sys.argv[4],
}, indent=2))
PY

for file in \
  schema/*.json \
  contracts/*.json \
  cases/*.json \
  image-cases/*.json \
  prompt-cases/*.json \
  sources/source-audit.json \
  evidence/schema-validation.json \
  evidence/compiler-test.json \
  evidence/query-test.json \
  evidence/image-case-test.json \
  evidence/prompt-case-test.json \
  evidence/compiler-output.json \
  evidence/query-index.json \
  evidence/image-case-prompts.json \
  evidence/determinism-rerun.json; do
  python3 -m json.tool "$file" >/dev/null
done

python3 tests/generate_manifest.py > evidence/manifest.json
python3 -m json.tool evidence/manifest.json >/dev/null

printf 'visual-registry-mvp-01: all batch, query, and prompt-case checks passed\n'
