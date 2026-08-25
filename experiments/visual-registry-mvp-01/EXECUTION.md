# Execution Record

## UNIT_02_STATIC_COMPILER

### Basis

- `idaibin/ai-handbook@dc8925bd7b5760a1a591c77e8e9e69abcbacb722`
- existing experiment rules in `experiments/README.md`

### Result

```text
status: passed_static_validation
contracts: 3
consumer_cases: 3
adapters: 3
compilations: 9
compiler_output_sha256: 46b3be7e6600c8e7284324e1a85cd1ee6cf6093fce365a7fc187efe346b01edb
```

The static compiler remained in `ai-handbook/experiments`; it was not promoted to `skills`, and no public website was authorized.

## UNIT_03_QUERY_AND_IMAGE_CASES

### Entry basis

- `idaibin/ai-handbook@44cb4312a34e4082a79e67829a3047a822477794`
- user requirement: support querying and different-Prompt image examples
- scope decision: implement query and fixed Prompt/image case contracts before running a Provider trial

### Scope

- add direct file-backed Registry query without a database;
- expose list, search, show, compile, examples, and prompt-set commands;
- support exact ID, Unicode, category, consumer, status, and target filters;
- define two original A/B/C Prompt-to-image comparison cases;
- generate six deterministic Prompt variants and hashes;
- preserve the distinction between Prompt readiness and real image generation.

### Validation history

1. Added `image-generation-case.schema.json` and two fixed comparison definitions.
2. Added a deterministic catalog and query CLI over contracts and image cases.
3. Added A subject-only, B manual reference, and C contract-compiled Prompt rendering.
4. Added Schema, query, CLI, image-case, determinism, and negative tests.
5. Full suite passed in the working copy.
6. Generated compiler output, query index, and image Prompt sets were byte-identical across two independent processes.
7. Query by Chinese text `班超` returned the intended image case.
8. No image result or Provider receipt was created or claimed.

### Result

```text
status: passed_query_and_prompt_case_validation
validation_level: static_unit_and_clean_copy_tests
catalog_records: 5
contracts: 3
image_comparison_cases: 2
prompt_variants: 6
planned_images: 6
compiler_output_sha256: 46b3be7e6600c8e7284324e1a85cd1ee6cf6093fce365a7fc187efe346b01edb
query_index_sha256: 763a4d6c55f1acc4eabe128624d7151a1da5e39929261da5315388fe303a9115
image_case_prompts_sha256: ef17045bbf8de44c860e00edf3591a75d191d15d1abc53e807524156f40591d3
```

### Gate decision

The query and Prompt comparison layer may remain in `ai-handbook/experiments`. It is still not authorized for promotion into `skills`, a standalone repository, or a public website.

### Not verified

- real Provider image generation;
- different-Prompt image output examples;
- blind Review scores;
- visual consistency or quality gains;
- Story Studio/UI Spec runtime integration.

### Next action

`VISUAL_REGISTRY_MVP_01 / UNIT_04_IMAGE_GENERATION_TRIAL`

Generate six controlled images for the two A/B/C cases using the same Provider/model and aspect ratio, fixed seed where supported, no post-processing, exact Prompt hashes, Provider receipts, image SHA-256 values, and blind Review records. Add query support for real result records only after the first valid result exists.
