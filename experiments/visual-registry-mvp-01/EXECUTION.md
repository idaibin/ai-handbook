# Execution Record

## UNIT_02_STATIC_COMPILER

Basis: `idaibin/ai-handbook@dc8925bd7b5760a1a591c77e8e9e69abcbacb722`

Result:

```text
status: passed_static_validation
contracts: 3
adapters: 3
compilations: 9
```

## UNIT_03_QUERY_AND_IMAGE_CASES

Basis: `idaibin/ai-handbook@44cb4312a34e4082a79e67829a3047a822477794`

Result:

```text
status: passed_query_and_prompt_case_validation
catalog_records: 5
image_comparison_cases: 2
prompt_variants: 6
planned_images: 6
```

No image or Provider receipt was claimed.

## UNIT_04_GENERATION_BATCH_QUERY_CONTRACT

### Entry basis

- `idaibin/ai-handbook@ee0969c45407380a3d8a343b655dae22c8b5cfdb`;
- user requirement: every image must be an independent file;
- user requirement: one Prompt must query to N image effects;
- research decision: introduce `GenerationBatch` and separate `exact_results` from `related_results`.

### Scope

- add a Draft 2020-12 `prompt-case.schema.json`;
- add one original `PromptCase` with one blocked `GenerationBatch` and four independent pending `ImageResult` identities;
- make PromptCase, Batch, and Result queryable;
- add style, Provider, model, image/receipt presence, and count filters;
- add query-expression syntax and exact/related result separation;
- attempt real image generation without accepting a combined image as valid output;
- preserve accurate failure evidence.

### Image execution evidence

ChatGPT Image attempts:

```text
8b28cb60-74e9-48ba-ac62-85bd854fee1d -> combined report/contact sheet
11167813-592a-4f04-99ff-9ce0517f1e86 -> combined Visual Registry report
714bfc22-3602-43f4-81a0-83572c8a364d -> combined Dashboard-style result
```

Adobe Firefly:

```text
image_generate -> HTTP 403
required retry -> HTTP 403
```

All generated combined images are `invalid_attempt`. They are not stored under the PromptCase `results/` directory and are not counted as provider-native images. They were isolated as failure evidence under Drive folder `1LvfPHztXKDUhZ-Kpu0NTPKPi_Veu8y3D`:

```text
8b28cb60 -> Drive 1vJSnmYh6zOPqGbkRPQl1Alo8s0niPRyy
             SHA-256 6b750bc2a9fa4b2e13262b0039c43f59f975e794a3aef4bd3c1cc038c49399b4
11167813 -> Drive 1kAvjhtRkjyM3XbgsR6hSw_MYjZGog_Wc
             SHA-256 e5bc05366ee78107913d0e218f8512d563eb6db9e0260a4d76cb80442bfe9566
714bfc22 -> Drive 1M904qhgguiU5v06vXZVEjHtUJEawlUBX
             SHA-256 601dfcc4f198dc9f9b4d4b935b01005e830feacbd2c5cd21a55bbdaba25c29c4
```

### Validation result

```text
status: passed_contract_and_query_validation_generation_blocked
validation_level: static_unit_and_clean_copy_tests
catalog_records: 11
prompt_cases: 1
generation_batches: 1
independent_result_identities: 4
provider_native_images: 0
saved_result_files: 0
```

Verified:

- PromptCase Schema and negative tests;
- Prompt SHA-256 identity;
- Batch-to-Prompt identity consistency;
- contiguous `r01-r04` result identities;
- Provider-native evidence requirements;
- combined outputs cannot be counted;
- exact and related query results remain separate;
- structured query expressions work;
- current blocked state matches real execution evidence.

### Gate decision

The contract and query changes may remain in `ai-handbook/experiments`.

The task is not promoted to `skills`, a standalone repository, or a public website. Image completion remains blocked because no available route returned four independent provider-native files.

### Next valid action

Execute the exact frozen Prompt through a Provider route that returns four independent files. For each result, preserve:

```text
result_id
provider / model
provider receipt
Drive file ID
image SHA-256
width / height
Review status
```

Only then may the PromptCase move from `generation_blocked` to `generated_unverified`.

## UNIT_05_NEXTJS_WEB_MVP

### Entry basis

- `idaibin/ai-handbook@27ae1d2045da94a6391ea97099cbbe2cca2f276c`;
- user correction: use React and Next.js, not a standalone native HTML/JavaScript page;
- current image execution remains blocked at 0/4 and must not be hidden by the Web UI.

### Scope

- supersede the handwritten static HTML prototype;
- add a Next.js App Router application under `web/`;
- implement typed Registry records and React search/filter state;
- add Style and PromptCase list/detail routes;
- keep Prompt text and independent ImageResult presentation separate;
- configure static export and a GitHub Actions build gate;
- preserve the truthful 0/4 image state.

### Local validation

```text
TypeScript/TSX syntax transpilation: passed
plain source .html/.js guard: passed
package/config JSON parsing: passed
Next.js dependency installation: blocked locally by registry.npmjs.org DNS EAI_AGAIN
```

### Remote gate

The first commit containing `web/` must run `.github/workflows/visual-registry-web.yml`. Completion requires:

```text
npm install
npm run typecheck
next build
static export route assertion
GitHub Actions artifact readback
```

Until that workflow succeeds, status remains `nextjs_web_source_ready_build_pending_generation_blocked`.
