# Visual Registry MVP 01

Status: `passed_static_validation`

## Goal

Test one minimal claim:

> A provider-neutral Visual Contract can compile deterministically into target-specific prompt forms without leaking provider syntax into the durable contract.

This is not a prompt library and not a website.

## Basis

- Design baseline: `research/visual-registry/2026-08-24-visual-registry-mvp-01.md`
- GitHub basis before implementation: `idaibin/ai-handbook@dc8925bd7b5760a1a591c77e8e9e69abcbacb722`
- External source decisions: [`SOURCES.md`](./SOURCES.md) and [`sources/source-audit.json`](./sources/source-audit.json)

## Contents

```text
schema/visual-contract.schema.json
contracts/
  historical-han-realism.json
  saas-bento-dashboard.json
  minimal-tech-cover.json
cases/
  story-studio-ban-chao.json
  ui-spec-asset-dashboard.json
  createway-rust-async-cover.json
requirements.txt
prototype/
  types.ts
  adapters.ts
  compiler.ts
  demo.mjs
tests/
  validate_schema.py
  compiler.test.mjs
evidence/
```

`run-tests.sh` generates `evidence/compiler-output.json`. The full generated output is archived in the Drive execution package rather than committed to GitHub; `evidence/manifest.json` records its immutable SHA-256 and size.

## Contract boundary

Durable:

- visual intent
- camera, lighting, composition
- palette, material, texture, atmosphere
- required and forbidden properties
- default output medium and aspect ratio

Derived:

- provider prompt wording
- negative prompt syntax
- Midjourney flags
- future provider/model-version parameters

The JSON Schema uses `additionalProperties: false`, so fields such as `prompt`, `template`, and `models` are rejected.

`category` describes a provider-neutral visual domain (`narrative`, `interface`, or `editorial`). Story Studio, UI Spec, Createway, and `dev-frontend` are recorded only as consumers in metadata, so consumer identity does not leak into the durable visual taxonomy.

## Fixed trial

Three original Golden Candidate contracts are compiled against three fixed consumer cases and three targets:

```text
3 contracts × 3 adapters = 9 deterministic compilation outputs
```

Adapters:

- Gemini: prose-oriented visual instruction
- Flux: positive prompt plus explicit negative prompt
- Midjourney: compact prompt plus adapter-owned `--ar`, `--style raw`, and `--no`

The Midjourney adapter intentionally does not pin `--v`; model versions are ephemeral.

## Validation

Requirements in the executed environment:

```text
Node.js 22.16.0
TypeScript 5.8.3
Python 3.13.5
jsonschema 4.26.0
```

Pinned development dependencies:

```bash
npm install
python3 -m pip install -r requirements.txt
```

Run:

```bash
./run-tests.sh
```

Checks:

1. all three contracts validate against Draft 2020-12 Schema;
2. provider-specific fields are rejected by the Schema;
3. contract JSON contains no provider syntax;
4. every case compiles twice to byte-equivalent objects;
5. two separate compiler processes produce byte-identical evidence;
6. every positive and negative semantic trace entry appears in target output;
7. all three adapters retain one identical semantic signature per case;
8. target-specific syntax remains inside the adapter layer;
9. invalid targets and empty subjects are rejected at runtime.

## Result boundary

Verified by this trial:

- Schema structure;
- provider/contract separation;
- deterministic compilation;
- semantic trace preservation in generated text;
- nine generated adapter outputs.

Not verified:

- real Gemini, Flux, or Midjourney image generation;
- visual similarity across provider outputs;
- prompt quality relative to a manually authored baseline;
- production integration with Story Studio or UI Spec;
- suitability for promotion into `skills`.

A real provider trial is required before any cross-model visual consistency claim.
