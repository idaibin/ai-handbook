# Visual Language Registry + Prompt Compiler MVP 01

Status: `passed_contract_and_query_validation_generation_blocked`

## Decision

The durable asset remains a provider-neutral Visual Contract. Provider prompts, query indexes, PromptCase executions, generated images, receipts, and Web galleries are derived artifacts.

The current work remains an experiment in `ai-handbook`; it is not a standalone product repository, database, public website, or imported Prompt collection.

## Implemented layers

```text
Visual Contract
    ↓
Prompt Compiler / Adapter
    ↓
PromptCase
    ↓
GenerationBatch
    ↓
ImageResult 1:N
```

### Static compiler

```text
3 contracts × 3 adapters = 9 deterministic outputs
```

### Query catalog

```text
3 Visual Contracts
2 A/B/C image comparison cases
1 PromptCase
1 GenerationBatch
4 ImageResult identities
= 11 queryable records
```

The query layer reads source JSON directly and supports:

```text
ID / Unicode / free text
kind / category / consumer / status / target
style / provider / model
has:image / has:receipt / count:>=N
exact_results / related_results
```

Related results are returned separately and may miss exactly one free-text term. Structured filters remain strict.

## Prompt 1:N contract

The first PromptCase is:

```text
anthropomorphic_watercolor_cat_librarian_v01
```

It freezes one Prompt SHA-256 and four independent result identities:

```text
r01 / r02 / r03 / r04
```

A collage, contact sheet, report, infographic, Dashboard, or grid cannot be a canonical result. Every counted image requires an independent provider-native file, Provider receipt, Drive file ID, SHA-256, width, and height.

## Image execution result

Current state:

```text
PromptCase: generation_blocked
GenerationBatch: blocked
provider_native_images: 0/4
saved_result_files: 0/4
```

Verified execution evidence:

- ChatGPT Image repeatedly returned one combined report/contact-sheet image instead of independent files;
- Adobe Firefly `image_generate` returned HTTP 403 twice, including the required retry;
- no combined output was assigned a result ID, uploaded to the canonical `results/` directory, or counted as an image;
- the three combined outputs were archived only as invalid-attempt evidence in Drive folder `1LvfPHztXKDUhZ-Kpu0NTPKPi_Veu8y3D`.

## Verified result

Verified:

- three Draft 2020-12 Schemas;
- Visual Contract / Adapter separation;
- deterministic Prompt compilation;
- Prompt SHA-256 identity;
- PromptCase → GenerationBatch → ImageResult relationship;
- one Prompt to four contiguous independent result identities;
- provider-native evidence requirements;
- deterministic file-backed query;
- exact and related result separation;
- truthful blocked execution state;
- invalid combined images excluded from canonical counts.

## Not verified

- four independent provider-native image files;
- Provider receipts, image hashes, and dimensions;
- different-Prompt image quality comparison;
- visual consistency or quality gains;
- Story Studio/UI Spec runtime integration;
- readiness for `skills` promotion;
- need for `prompt.idaibin.dev`.

## Next gate

Use a Provider route that returns four independent files from the exact frozen Prompt. Only after each image has a receipt, Drive identity, hash, dimensions, and Review status may the PromptCase advance beyond `generation_blocked`.
