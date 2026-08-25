# Visual Registry MVP 01

Status: `passed_query_and_prompt_case_validation`

## Goal

Test two minimal claims:

1. a provider-neutral Visual Contract can compile deterministically into target-specific prompt forms without leaking Provider syntax into the durable contract;
2. the same files can be queried deterministically and can define controlled A/B/C Prompt-to-image comparison cases without pretending that planned images already exist.

This is not a prompt library, database, or public website.

## Basis

- Design baseline: `research/visual-registry/2026-08-24-visual-registry-mvp-01.md`
- Compiler baseline: `idaibin/ai-handbook@44cb4312a34e4082a79e67829a3047a822477794`
- External source decisions: [`SOURCES.md`](./SOURCES.md) and [`sources/source-audit.json`](./sources/source-audit.json)

## Contents

```text
schema/
  visual-contract.schema.json
  image-generation-case.schema.json
contracts/
  historical-han-realism.json
  saas-bento-dashboard.json
  minimal-tech-cover.json
cases/
  story-studio-ban-chao.json
  ui-spec-asset-dashboard.json
  createway-rust-async-cover.json
image-cases/
  han-writing-room-prompt-comparison.json
  saas-dashboard-prompt-comparison.json
prototype/
  compiler.ts
  adapters.ts
  catalog.mjs
  query-cli.mjs
  image-case-demo.mjs
  image-case-output.mjs
tests/
evidence/
```

## Contract boundary

Durable:

- visual intent;
- camera, lighting, composition;
- palette, material, texture, atmosphere;
- required and forbidden properties;
- default output medium and aspect ratio.

Derived:

- Provider prompt wording;
- negative prompt syntax;
- Midjourney flags;
- A/B/C experiment prompts;
- future Provider/model-version parameters;
- generated images and Provider receipts.

The Visual Contract Schema uses `additionalProperties: false`, so fields such as `prompt`, `template`, and `models` are rejected. Prompt comparison definitions live under `image-cases/`, not inside durable contracts.

## Query support

The MVP scans JSON files directly. It does not introduce a database or duplicate Registry authority.

Build once:

```bash
npm run build
```

Examples:

```bash
node prototype/query-cli.mjs list --json
node prototype/query-cli.mjs search "班超" --json
node prototype/query-cli.mjs search dashboard --consumer ui_spec --json
node prototype/query-cli.mjs show historical_han_realism --json
node prototype/query-cli.mjs examples prompt --target gemini --json
node prototype/query-cli.mjs prompt-set han_writing_room_prompt_comparison --json
node prototype/query-cli.mjs compile historical_han_realism \
  --subject "Ban Chao copying documents in Luoyang" \
  --target gemini \
  --json
```

Supported query dimensions:

- exact ID and free text;
- Unicode text;
- record kind;
- visual category;
- consumer;
- status;
- target Provider;
- stable machine-readable JSON output.

The current catalog contains three Visual Contracts and two image comparison cases.

## Prompt-to-image comparison cases

Two controlled cases are ready:

| Case | Consumer | Variants | Planned images | Current status |
| --- | --- | ---: | ---: | --- |
| `han_writing_room_prompt_comparison` | Story Studio | A subject-only / B manual / C compiled | 3 | `prompt_set_ready` |
| `saas_dashboard_prompt_comparison` | UI Spec | A subject-only / B manual / C compiled | 3 | `prompt_set_ready` |

Controls require the same Provider/model, aspect ratio, no post-processing, and fixed seed when supported. Review criteria are fixed before generation.

`prototype/image-case-output.mjs` deterministically renders all six Prompt variants and their SHA-256 identities. No generated image or Provider receipt exists yet, so the cases remain `image_generation_pending`.

## Validation

Requirements in the executed environment:

```text
Node.js 22.16.0
TypeScript 5.8.3
Python 3.13.5
jsonschema 4.26.0
```

Run:

```bash
./run-tests.sh
```

Checks include:

1. both Draft 2020-12 Schemas validate;
2. durable contracts reject Provider fields;
3. image cases contain exactly one subject-only, manual, and compiled variant;
4. all compiler outputs preserve one semantic trace;
5. compiler output is byte-identical across processes;
6. query catalog and image Prompt sets are byte-identical across processes;
7. queries work by exact ID, Unicode text, and filters;
8. CLI emits deterministic JSON;
9. all six Prompt hashes are distinct;
10. image case status does not overstate real generation.

## Result boundary

Verified:

- Schema structure and Provider/contract separation;
- deterministic compilation;
- deterministic file-backed query;
- two controlled Prompt comparison definitions;
- six deterministic Prompt variants;
- query and comparison CLI behavior.

Not verified:

- real Gemini, Flux, or Midjourney image generation;
- different-Prompt image output examples;
- cross-Provider visual similarity;
- quality against the manual reference baseline;
- production integration with Story Studio or UI Spec;
- suitability for promotion into `skills`;
- public Web query interface.

The next unit must generate and preserve real image outputs and Provider receipts before any image-quality conclusion.
