# Visual Registry MVP 01

Status: `nextjs_web_source_ready_build_pending_generation_blocked`

## Goal

Test three minimal claims:

1. a provider-neutral Visual Contract can compile deterministically into target-specific Prompt forms without leaking Provider syntax into the durable contract;
2. Registry files can be queried deterministically without introducing a database or second authority;
3. one immutable Prompt can own multiple GenerationBatch executions and multiple independent ImageResult identities without treating a collage or contact sheet as valid results.

This is not a prompt marketplace, public website, or large third-party Prompt collection.

## Basis

- design baseline: `research/visual-registry/2026-08-24-visual-registry-mvp-01.md`;
- query/compiler baseline: `idaibin/ai-handbook@ee0969c45407380a3d8a343b655dae22c8b5cfdb`;
- Drive contract: `visual-registry-prompt-1vn-contract-v0.1.json`;
- external source decisions: [`SOURCES.md`](./SOURCES.md).

## Contents

```text
schema/
  visual-contract.schema.json
  image-generation-case.schema.json
  prompt-case.schema.json
contracts/
cases/
image-cases/
prompt-cases/
  anthropomorphic-watercolor-cat-librarian-v01.json
prototype/
  compiler.ts
  adapters.ts
  catalog.mjs
  query-cli.mjs
  image-case-demo.mjs
  image-case-output.mjs
tests/
evidence/
web/
  src/app/
  src/components/
  src/data/
  package.json
  next.config.mjs
```

## Asset boundaries

### Durable Visual Contract

Stores visual intent, palette, material, texture, atmosphere, camera, lighting, composition, positive requirements, and forbidden properties.

It does not store Provider Prompt text, model versions, Midjourney flags, generated images, or receipts.

### PromptCase

```text
PromptCase
├── prompt_id
├── style_id
├── subject
├── prompt_text
├── prompt_sha256
├── tags
└── generation_batches[]
```

### GenerationBatch

```text
GenerationBatch
├── batch_id
├── prompt_sha256
├── requested_count
├── provider / model / parameters
├── status / failure evidence
└── results[]
```

### ImageResult

Each result has its own `result_id`, sequence, file identity, receipt, Drive file ID, SHA-256, dimensions, status, and Review status.

A contact sheet, report page, collage, grid, Dashboard, or infographic is never a canonical result. It may exist only as `derived_review_only` after independent provider-native files exist.

## Current 1:N PromptCase

```text
prompt_id:
anthropomorphic_watercolor_cat_librarian_v01

prompt_sha256:
7b9028e383835b574e0a25bcfb97f7e4ab9f34b9047918cdd86c1afe8fbec66f

requested_count:
4

result identities:
r01 / r02 / r03 / r04
```

Current state:

```text
PromptCase: generation_blocked
GenerationBatch: blocked
provider_native_images: 0/4
saved_result_files: 0/4
```

Verified failure evidence:

- ChatGPT Image repeatedly returned one combined report/contact-sheet image instead of independent files;
- Adobe Firefly `image_generate` returned HTTP 403 twice, including the required retry;
- no combined output was entered into `results[]` or counted as an image;
- the three combined outputs were isolated under Drive folder `invalid-attempts` (`1LvfPHztXKDUhZ-Kpu0NTPKPi_Veu8y3D`) with independent Drive IDs and SHA-256 evidence.

## Query support

The catalog scans the JSON files directly. It contains:

```text
3 Visual Contracts
2 A/B/C image comparison cases
1 PromptCase
1 GenerationBatch
4 ImageResult identities
= 11 queryable records
```

Build:

```bash
npm run build
```

Examples:

```bash
node prototype/query-cli.mjs list --json
node prototype/query-cli.mjs search "班超" --json
node prototype/query-cli.mjs search "橘猫 图书管理员" --kind prompt_case --json
node prototype/query-cli.mjs search \
  "watercolor style:anthropomorphic_watercolor status:generation_blocked has:no-image" \
  --json
node prototype/query-cli.mjs search \
  "anthropomorphic watercolor fox kind:prompt_case" \
  --related --json
node prototype/query-cli.mjs show anthropomorphic_watercolor_cat_librarian_v01 --json
node prototype/query-cli.mjs results anthropomorphic_watercolor_cat_librarian_v01 --json
```

Supported fields:

```text
kind category consumer status target style provider model
has:image has:receipt has:no-image has:no-receipt count:>=N
```

`--related` returns two separate arrays:

```json
{
  "exact_results": [],
  "related_results": []
}
```

A related result may miss exactly one free-text term. Structured filters remain strict. Related results are never silently merged into exact results.

## Next.js Web query MVP

The previous standalone static HTML prototype is superseded. The maintained Web source now lives at:

```text
experiments/visual-registry-mvp-01/web/
```

Implementation constraints:

- Next.js App Router;
- React Client Component for search and filters;
- TypeScript source;
- static export with `output: "export"`;
- routes for `/`, `/styles/`, `/styles/[id]/`, `/prompts/`, and `/prompts/[id]/`;
- Prompt text and ImageResult presentation remain separate UI regions;
- no standalone source `index.html` or handwritten browser JavaScript;
- no image is rendered until an ImageResult has a valid image URL and evidence identity.

The Web app is a read-only projection. GitHub contracts and Drive images remain authoritative.

Build gate:

```bash
cd web
npm install
npm run verify
```

The GitHub Actions workflow `.github/workflows/visual-registry-web.yml` performs the remote build and uploads `out/` as an artifact.

## Validation

Run:

```bash
./run-tests.sh
```

The suite verifies:

1. all three Draft 2020-12 Schemas;
2. Prompt SHA-256 and Batch identity consistency;
3. one Prompt to four contiguous independent result identities;
4. Provider-native evidence requirements for counted images;
5. rejection of verified images without receipts, Drive identity, hash, and dimensions;
6. exclusion of combined/derived images from canonical counts;
7. deterministic compiler, query snapshot, and Prompt sets;
8. exact/related query separation;
9. query by ID, Unicode, style, status, Provider, model, image/receipt presence, and result count;
10. CLI error handling and clean-copy reproducibility.

## Result boundary

Verified:

- Visual Contract / Adapter separation;
- deterministic Prompt compilation;
- file-backed query;
- PromptCase → GenerationBatch → ImageResult data relationship;
- exact and related result separation;
- truthful blocked execution state;
- no invalid image counted as provider-native output.

Not verified:

- four independent provider-native images;
- Provider receipts, image SHA-256 values, and dimensions;
- different-Prompt visual comparison;
- visual consistency or quality gains;
- Story Studio/UI Spec runtime integration;
- readiness for `skills` promotion;
- public deployment and live browser validation of the Next.js Web interface.

The next valid image execution must return four independent original files from one exact Prompt. Until then, the current PromptCase remains `generation_blocked`.
