# Execution Record

## UNIT_02_STATIC_COMPILER

Basis: `idaibin/ai-handbook@dc8925bd7b5760a1a591c77e8e9e69abcbacb722`

```text
status: passed_static_validation
contracts: 3
adapters: 3
compilations: 9
```

## UNIT_03_QUERY_AND_IMAGE_CASES

Basis: `idaibin/ai-handbook@44cb4312a34e4082a79e67829a3047a822477794`

```text
status: passed_query_and_prompt_case_validation
catalog_records: 5
image_comparison_cases: 2
prompt_variants: 6
planned_images: 6
```

No image or Provider receipt was claimed.

## UNIT_04_GENERATION_BATCH_QUERY_CONTRACT

Basis: `idaibin/ai-handbook@ee0969c45407380a3d8a343b655dae22c8b5cfdb`

Implemented:

- Draft 2020-12 `prompt-case.schema.json`;
- PromptCase → GenerationBatch → independent ImageResult identities;
- exact and related query separation;
- provider-native evidence requirements;
- exclusion of combined reports, dashboards, collages, and contact sheets.

Result:

```text
status: passed_contract_and_query_validation_generation_blocked
catalog_records: 11
prompt_cases: 1
generation_batches: 1
independent_result_identities: 4
provider_native_images: 0
saved_result_files: 0
```

Image generation remained blocked because ChatGPT Image returned combined report images and Adobe Firefly returned HTTP 403 twice. Invalid attempts were preserved under Drive folder `1LvfPHztXKDUhZ-Kpu0NTPKPi_Veu8y3D` and were not counted.

## UNIT_05_NEXTJS_WEB_MVP

Entry basis:

- user correction: use React and Next.js, not handwritten static HTML;
- truthful image state remained `0/4`.

A Next.js prototype was implemented under `experiments/visual-registry-mvp-01/web/`. It demonstrated the intended routes and React query interaction, but storing a runnable product inside `ai-handbook` violated the repository boundary.

## UNIT_06_EXTRACT_PROMPTS_HUB

### Entry basis

- user correction: real product projects must not live inside `ai-handbook`;
- requested target project: `prompts-hub`;
- source baseline: `idaibin/ai-handbook@68220929832a0aa898262566b30aab8310b0a61b`.

### Execution

1. Rebuilt a clean standalone Next.js + React + TypeScript project at `/mnt/data/prompts-hub`.
2. Retained Style browsing, PromptCase search/filter, Style and Prompt detail routes, and four independent pending ImageResult slots.
3. Kept Prompt text, image files, and result evidence as separate assets.
4. Ran project structure checks, TypeScript/TSX syntax transpilation, Prompt SHA-256 verification, and fake-image URL guards.
5. Created a local Git repository with initial commit `b58624698cc2bcc4ef7bf3ea90e3b6e14127d1df`.
6. Created and cloned back a Git bundle to verify commit recoverability.
7. Uploaded the source ZIP, Git bundle, and Manifest to the independent Drive folder `Prompts Hub` (`1a3gAeZIYih6UQS0GRvANTf-ji78srtOa`).
8. Removed the runnable `web/` project and its two dedicated workflows from `ai-handbook`.
9. Added `PROJECT.md` as the migration and authority pointer.

### Validation result

```text
status: application_extracted_repository_creation_blocked
validation_level: source_structure_and_typescript_syntax
framework: Next.js + React + TypeScript
typed_files: 13
prompt_sha256: 7b9028e383835b574e0a25bcfb97f7e4ab9f34b9047918cdd86c1afe8fbec66f
independent_result_identities: 4
valid_images: 0
local_initial_commit: b58624698cc2bcc4ef7bf3ea90e3b6e14127d1df
bundle_readback: passed
```

Not executed in that environment:

```text
npm install
Next.js production build
browser/E2E validation
Vercel deployment
```

### Blocker at completion of UNIT_06

The connected GitHub tool exposed writes to existing repositories but did not expose repository creation. `idaibin/prompts-hub` did not exist at that time.

## UNIT_07_REMOTE_REPOSITORY_ACTIVATION

### Evidence basis

User reported:

```text
repository: idaibin/prompts-hub
visibility: private
branch: main
commit: 2d9b9640228023e2e0c775a349a34124b4d8573a
commit message: chore: complete project initialization
local and remote SHA: matched
working tree: clean
npm run verify: passed
production build: passed
static pages generated: 16
deployment: not verified
```

GitHub connector readback verified:

```text
repository exists: true
visibility: private
default branch: main
remote main SHA: 2d9b9640228023e2e0c775a349a34124b4d8573a
commit message: chore: complete project initialization
parent: b58624698cc2bcc4ef7bf3ea90e3b6e14127d1df
repository description: Browse visual styles, Prompt cases, and independent image results.
```

The commit tree contains the standalone Next.js application, `package-lock.json`, validation script, MIT license, project guidance, and Prompt/Style routes.

### Validation classification

```text
repository_creation: verified
remote_push_and_readback: verified
private_visibility: verified
local_npm_verify: user_reported
remote_commit_status_checks: none
production_deployment: not_verified
live_browser_runtime: not_verified
custom_domain: not_verified
valid_independent_images: 0/4
```

The absence of GitHub commit-status checks means the user-reported local build must not be represented as GitHub Actions validation.

### Gate decision

```text
status: repository_ready_deployment_not_verified
code_authority: idaibin/prompts-hub@2d9b9640228023e2e0c775a349a34124b4d8573a
experiment_authority: idaibin/ai-handbook
large_image_asset_authority: Google Drive
```

### Next valid action

Deploy the exact remote commit and verify:

```text
deployment receipt and provider project identity
production URL and commit SHA
HTTP reachability
browser rendering at desktop and mobile sizes
search/filter behavior
Style detail route
PromptCase detail route
truthful 0/4 image state
custom domain prompt.idaibin.dev, if configured
```

Only after those checks pass may online operation move from `not_verified` to `verified`.