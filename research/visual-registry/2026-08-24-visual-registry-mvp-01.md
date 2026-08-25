# Visual Language Registry + Prompt Compiler MVP 01

Status: `passed_static_validation`

## Decision

The durable asset is a provider-neutral Visual Contract. Gemini, Flux, Midjourney, and future video prompts are derived Adapter outputs.

The current work remains an experiment in `ai-handbook`; it is not a standalone product repository, a prompt collection, or a public website.

## Durable contract boundary

Included:

- visual intent and domain;
- style, palette, materials, textures, and atmosphere;
- camera, lighting, and composition;
- positive requirements and forbidden properties;
- provider-neutral output medium and aspect ratio.

Excluded:

- provider prompt text;
- model-version parameters;
- Midjourney flags;
- community prompt and image ingestion;
- artist-name emulation;
- website, user, marketplace, and social features.

## Implemented experiment

Path:

```text
experiments/visual-registry-mvp-01/
```

Fixed trial:

```text
3 original Golden Candidate contracts
× 3 consumer cases
× 3 adapters
= 9 deterministic compilation outputs
```

Contracts:

- `historical_han_realism` — narrative visual domain; Story Studio consumer;
- `saas_bento_dashboard` — interface visual domain; UI Spec and `dev-frontend` consumers;
- `minimal_tech_cover` — editorial visual domain; Createway consumer.

Adapters:

- Gemini prose instruction;
- Flux positive and negative prompt fields;
- Midjourney compact instruction with adapter-owned flags.

## Source policy

Six named repositories were read at fixed commits. They were used only to assess taxonomy, metadata, Adapter, and interaction patterns. No third-party prompt, image, artist list, or implementation was imported.

The original “all are high-star repositories” premise was rejected: `CaylaLuo/awesome-midjourney-prompts` had one star at the recorded snapshot and no declared license, so it was excluded from the MVP.

See:

```text
experiments/visual-registry-mvp-01/SOURCES.md
experiments/visual-registry-mvp-01/sources/source-audit.json
```

## Verified result

```text
status: passed_static_validation
validation_level: static_and_unit_tests
compiler_output_sha256: 46b3be7e6600c8e7284324e1a85cd1ee6cf6093fce365a7fc187efe346b01edb
```

Verified:

- Draft 2020-12 Schema validation;
- rejection of provider fields and consumer identity as a visual category;
- strict TypeScript compilation;
- deterministic objects and byte-identical output across separate processes;
- one semantic trace/signature preserved across all three adapters;
- positive and negative constraints retained in generated text;
- invalid target and empty subject rejected.

## Not verified

- real model image generation;
- cross-provider visual similarity;
- quality relative to manually authored prompts;
- Story Studio/UI Spec runtime integration;
- readiness for promotion into `skills`;
- need for `prompt.idaibin.dev`.

## Next gate

A provider-backed comparison must preserve exact inputs, Adapter outputs, provider receipts, image identities, and review criteria. Only evidence from that trial can justify contract changes, Skill promotion, or a separate product repository.
