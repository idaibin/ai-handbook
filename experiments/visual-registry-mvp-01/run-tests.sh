#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
rm -rf dist
mkdir -p evidence

tsc -p tsconfig.json
python3 tests/validate_schema.py > evidence/schema-validation.json
node tests/compiler.test.mjs > evidence/compiler-test.json
node prototype/demo.mjs > evidence/compiler-output.json
node prototype/demo.mjs > evidence/compiler-output.rerun.json
cmp --silent evidence/compiler-output.json evidence/compiler-output.rerun.json
OUTPUT_SHA="$(sha256sum evidence/compiler-output.json | awk '{print $1}')"
python3 - "$OUTPUT_SHA" <<'PY' > evidence/determinism-rerun.json
import json
import sys
print(json.dumps({
    "status": "passed",
    "process_runs": 2,
    "byte_identical": True,
    "compiler_output_sha256": sys.argv[1],
}, indent=2))
PY
rm evidence/compiler-output.rerun.json

for file in \
  schema/visual-contract.schema.json \
  contracts/*.json \
  cases/*.json \
  sources/source-audit.json \
  evidence/schema-validation.json \
  evidence/compiler-test.json \
  evidence/compiler-output.json \
  evidence/determinism-rerun.json; do
  python3 -m json.tool "$file" >/dev/null
done

python3 tests/generate_manifest.py > evidence/manifest.json
python3 -m json.tool evidence/manifest.json >/dev/null

printf 'visual-registry-mvp-01: all static checks passed\n'
