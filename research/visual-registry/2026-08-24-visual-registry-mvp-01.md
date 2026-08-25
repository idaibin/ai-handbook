# Visual Language Registry + Prompt Compiler MVP 01

Status: `passed_query_and_prompt_case_validation`

## Decision

The durable asset is a provider-neutral Visual Contract. Gemini, Flux, Midjourney, future video prompts, query projections, comparison prompts, generated images, and Provider receipts are derived artifacts.

The current work remains an experiment in `ai-handbook`; it is not a standalone product repository, a prompt collection, database, or public website.

## Durable contract boundary

Included:

- visual intent and domain;
- style, palette, materials, textures, and atmosphere;
- camera, lighting, and composition;
- positive requirements and forbidden properties;
- provider-neutral output medium and aspect ratio.

Excluded:

- Provider prompt text and model-version parameters;
- Midjourney flags;
- A/B/C experiment prompts and image outputs;
- query indexes and gallery projections;
- community prompt and image ingestion;
- artist-name emulation;
- website, user, marketplace, and social features.

## Implemented experiment

Path:

```text
experiments/visual-registry-mvp-01/
```

Compiler trial:

```text
3 original Golden Candidate contracts
× 3 consumer cases
× 3 adapters
= 9 deterministic compilation outputs
```

Query and image-case extension:

```text
3 Visual Contracts
+ 2 A/B/C image comparison cases
= 5 queryable records

2 cases
× 3 Prompt variants
= 6 planned controlled images
```

The query layer scans source JSON directly and supports exact ID, free text, Unicode, category, consumer, status, target, and machine-readable JSON. It introduces no database and does not become a second authority.

Each image comparison case fixes:

- A: subject-only Prompt;
- B: original manual reference Prompt;
- C: Visual Contract compiled Prompt;
- same Provider/model and aspect ratio;
- fixed seed when supported;
- no post-processing;
- blind Review criteria before generation.

## Source policy

Six named repositories were read at fixed commits. They were used only to assess taxonomy, metadata, Adapter, and interaction patterns. No third-party Prompt, image, artist list, or implementation was imported.

The original “all are high-star repositories” premise was rejected: `CaylaLuo/awesome-midjourney-prompts` had one star at the recorded snapshot and no declared license, so it was excluded from the MVP.

## Verified result

```text
status: passed_query_and_prompt_case_validation
validation_level: static_unit_and_clean_copy_tests
compiler_output_sha256: 46b3be7e6600c8e7284324e1a85cd1ee6cf6093fce365a7fc187efe346b01edb
query_index_sha256: 763a4d6c55f1acc4eabe128624d7151a1da5e39929261da5315388fe303a9115
image_case_prompts_sha256: ef17045bbf8de44c860e00edf3591a75d191d15d1abc53e807524156f40591d3
```

Verified:

- two Draft 2020-12 Schemas;
- Provider fields rejected from durable Visual Contracts;
- strict TypeScript compilation and deterministic Adapter output;
- deterministic file-backed query and Unicode lookup;
- exact A/B/C Prompt case structure;
- six distinct Prompt identities;
- byte-identical compiler output, query index, and Prompt sets across clean reruns;
- planned cases remain explicitly marked as image-generation pending.

## Not verified

- real model image generation;
- different-Prompt image output examples;
- blind Review scores and quality gain;
- cross-Provider visual similarity;
- Story Studio/UI Spec runtime integration;
- readiness for promotion into `skills`;
- need for `prompt.idaibin.dev`.

## Next gate

`VISUAL_REGISTRY_MVP_01 / UNIT_04_IMAGE_GENERATION_TRIAL`

Generate the six fixed images and preserve exact Prompt hashes, Provider/model identity, parameters, Provider receipts, image SHA-256 values, and blind Review records. Only after the first valid result exists should result records be added to the query catalog.
