# GitHub Skills Deep Analysis — Batch 006

- Observed date: `2026-08-07`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Index snapshot: `1731` unique repositories; `1325` provisionally deep-analysis eligible; `406` held for review
- Repositories completed: `10`
- Individual skills reviewed: `88`
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`

A repository is counted complete only after its GitHub identity and displayed star count were checked and actual repository content was read. This batch read the README/equivalent and every identified primary `SKILL.md` entrypoint for each skill-bearing repository, plus representative scripts, references, tests, or eval assets where available. Metadata-only inspection is not sufficient for completion.

Star counts are GitHub UI observations from 2026-08-07 and can change. Values abbreviated with `k` are retained as displayed.

## Batch summary

| Repository | GitHub ID | Stars observed | Skills | Result |
|---|---:|---:|---:|---|
| `apify/agent-skills` | `1129716674` | `2.3k` | 5 | structure-reviewed |
| `callstackincubator/agent-skills` | `1134388286` | `1.6k` | 7 | structure-reviewed |
| `kepano/obsidian-skills` | `1126947080` | `44.3k` | 5 | structure-reviewed |
| `palkan/skills` | `1150861761` | `410` | 1 | structure-reviewed |
| `vuejs-ai/skills` | `1138832642` | `2.8k` | 8 | structure-reviewed |
| `remotion-dev/skills` | `1137388347` | `4.2k` | 12 | structure-reviewed |
| `google-labs-code/stitch-skills` | `1135847870` | `7.9k` | 15 | structure-reviewed |
| `antfu/skills` | `1143952193` | `5.7k` | 18 | structure-reviewed |
| `tiangolo/library-skills` | `1221742654` | `758` | 0 | structure-reviewed |
| `hashicorp/agent-skills` | `1092101865` | `785` | 17 | structure-reviewed |

## 1. `apify/agent-skills`

- GitHub repository ID: `1129716674`
- Stars observed: `2.3k`
- Primary skills reviewed: `5`

**Structure and evidence.** Root `skills/` contains five installable skills; `.claude-plugin/`, `agents/`, `commands/`, and `scripts/` provide packaging and cross-agent surfaces. `README.md` and all five `skills/*/SKILL.md` entrypoints were read. `scripts/generate_agents.py` was also read: it enumerates `skills/*/SKILL.md`, parses frontmatter, generates a deterministic `agents/AGENTS.md`, and checks that marketplace plugin sources cover every discovered skill.

**Analysis.** The repository separates user-facing task routers from Apify implementation details and reference material. The strongest reusable pattern is a single skill authority feeding generated agent documentation plus a marketplace consistency check. Actor-development/actorization guidance also treats scraped content as untrusted and keeps credentials/security boundaries explicit.

**Validation boundary.** Generator/marketplace validation code was inspected but not executed; no Actor was run or deployed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `apify-ultimate-scraper` | Selects Apify Actors/scrapers, defines input schema, runs jobs, and retrieves normalized results. |
| `apify-actor-development` | Guides Actor project structure, schemas, local testing, deployment, and security boundaries. |
| `apify-actorization` | Converts existing JavaScript/TypeScript/Python scraping or automation code into an Apify Actor. |
| `apify-generate-output-schema` | Builds Actor output-schema metadata so datasets and outputs are discoverable and typed. |
| `apify-sdk-integration` | Integrates Apify SDK/client use into applications with task-specific API patterns. |

## 2. `callstackincubator/agent-skills`

- GitHub repository ID: `1134388286`
- Stars observed: `1.6k`
- Primary skills reviewed: `7`

**Structure and evidence.** `skills/` contains seven React Native/GitHub skills. `README.md` and every primary `SKILL.md` were read, including the migration assessment and library-scaffolding skills. The collection relies mainly on focused `references/` documents rather than a shared executable validation harness.

**Analysis.** This collection is unusually strong at separating decision work from implementation. `assess-react-native-migration` is explicitly read-only, inventories every supported client, labels claims as observed/measured/reported/assumed/unknown, and gates recommendations on evidence coverage. Only after a path is accepted does it hand off to the brownfield implementation skill. This is a reusable authority-boundary pattern for catalog skills.

**Validation boundary.** No migration, scaffold, GitHub mutation, CI workflow, or device validation was executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `react-native-best-practices` | Performance/correctness guidance for React Native, organized as a router to focused references. |
| `github` | Repository/PR/issue workflows with GitHub CLI and explicit verification-oriented operating rules. |
| `github-actions` | GitHub Actions workflow authoring and debugging patterns for CI/CD. |
| `upgrading-react-native` | Evidence-driven React Native upgrade workflow with native diffing and staged validation. |
| `react-native-brownfield-migration` | Implementation guidance for embedding React Native into existing native applications. |
| `assess-react-native-migration` | Read-only migration assessment with platform inventory, evidence labels, decision gates, checkpoint and ROI contract. |
| `create-react-native-library` | Routes standalone vs local React Native library scaffolding and implementation references. |

## 3. `kepano/obsidian-skills`

- GitHub repository ID: `1126947080`
- Stars observed: `44.3k`
- Primary skills reviewed: `5`

**Structure and evidence.** Five compact skills cover Obsidian Markdown, Bases, JSON Canvas, Obsidian CLI, and Defuddle. `README.md` and all five `SKILL.md` files were read. The primary knowledge is embedded in the skill files; the inspected repository surface does not depend on a large script/eval framework.

**Analysis.** The collection maps directly to stable artifact formats or CLI domains instead of creating a generic “Obsidian” mega-skill. That keeps activation narrow and makes each skill independently useful. The format-oriented skills are especially reusable because they specify concrete syntax/shape rules rather than visual prose alone.

**Validation boundary.** No Obsidian vault, CLI command, Defuddle extraction, or rendered Canvas was run.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `obsidian-markdown` | Obsidian-flavored Markdown authoring: links, embeds, callouts, properties and vault conventions. |
| `obsidian-bases` | Creates and edits Obsidian Bases definitions with filters, formulas, views and properties. |
| `json-canvas` | Creates/edits JSON Canvas documents with nodes, edges, groups and coordinate conventions. |
| `obsidian-cli` | Uses Obsidian CLI for vault operations and command-oriented workflows. |
| `defuddle` | Extracts clean article content using Defuddle for downstream Markdown/Obsidian workflows. |

## 4. `palkan/skills`

- GitHub repository ID: `1150861761`
- Stars observed: `410`
- Primary skills reviewed: `1`

**Structure and evidence.** The source is a Claude plugin repository whose installable core is `layered-rails/skills/layered-rails/SKILL.md`, surrounded by `workflows/`, `references/`, `examples/`, plugin `commands/`, and planner/reviewer agent wrappers. The README, primary skill, command/workflow index, and supporting architecture surface were inspected.

**Analysis.** One router skill owns a large but coherent Rails architecture domain. It exposes seven repeatable workflows (analysis, review, specification test, service/callback/god-object audits, and gradual layerification) while detailed patterns live in references. The “specification test” and unidirectional layer rules give the skill a falsifiable review model rather than only style advice.

**Validation boundary.** No Rails repository was analyzed and none of the workflows were executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `layered-rails` | Rails layered-architecture router covering analysis, review, specification tests, refactoring patterns, and gradual adoption workflows. |

## 5. `vuejs-ai/skills`

- GitHub repository ID: `1138832642`
- Stars observed: `2.8k`
- Primary skills reviewed: `8`

**Structure and evidence.** Eight Vue-domain skills were found and all eight `SKILL.md` files were read. They are predominantly reference routers with topic files under each skill. The repository README explicitly describes the project as an early/community experiment and warns that content may be incomplete or hallucinated.

**Analysis.** Splitting Vue core, Options API, Router, Pinia, testing, JSX, debugging, and adaptable composable design creates useful activation boundaries. The cost is duplicated guidance and a large reference surface whose freshness must be maintained. The repository's own warning materially lowers confidence: these are useful structured references, not authoritative framework specifications.

**Validation boundary.** No example project, test suite, browser run, or framework build was executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `vue-best-practices` | Vue 3 Composition API and SFC best-practice router. |
| `vue-options-api-best-practices` | Options API-specific Vue guidance for projects that intentionally use that style. |
| `vue-router-best-practices` | Vue Router routing, guards, data flow and navigation patterns. |
| `vue-pinia-best-practices` | Pinia store design, state/actions/getters and integration patterns. |
| `vue-testing-best-practices` | Vue testing strategy and component-test guidance. |
| `vue-jsx-best-practices` | Vue JSX/TSX authoring conventions and framework-specific caveats. |
| `vue-debug-guides` | Diagnostic router for common Vue runtime, reactivity, component and tooling failures. |
| `create-adaptable-composable` | Designs reusable Vue composables that accept reactive/plain inputs and preserve predictable behavior. |

## 6. `remotion-dev/skills`

- GitHub repository ID: `1137388347`
- Stars observed: `4.2k`
- Primary skills reviewed: `12`

**Structure and evidence.** `skills/` contains twelve task-oriented Remotion skills. The README and all twelve `SKILL.md` files were read, including the small `remotion-studio` operational skill. The root also contains `scripts/` and TypeScript tooling used to maintain/package the collection.

**Analysis.** The collection deliberately separates “knowledge” (`remotion-best-practices`) from concrete operations such as create, preview, render, captions, upgrade, docs, and multimedia. This lowers prompt ambiguity and allows operational skills to be very small. Version metadata in entrypoints is useful for freshness, but it makes synchronization with Remotion releases a maintenance requirement.

**Validation boundary.** Studio, rendering, export, media processing, and network/documentation calls were not executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `remotion-best-practices` | Primary Remotion authoring guidance and reference router. |
| `remotion-create` | Creates a new Remotion project with the supported bootstrap workflow. |
| `remotion-markup` | Edits/constructs compositions and markup following Remotion composition conventions. |
| `remotion-studio` | Starts Remotion Studio and opens the preview URL. |
| `remotion-render` | Renders compositions through the Remotion CLI with output/codec options. |
| `remotion-maps` | Integrates maps into Remotion video compositions. |
| `remotion-captions` | Handles caption/transcript workflows for timed video text. |
| `remotion-saas` | Guides server/SaaS rendering architecture for Remotion workloads. |
| `remotion-interactivity` | Adds interactive/player behaviors around Remotion content. |
| `remotion-docs` | Routes questions to Remotion documentation and relevant concepts. |
| `remotion-upgrade` | Guides version upgrades and dependency alignment for Remotion projects. |
| `remotion-multimedia` | Works with media assets, timing, audio/video/image loading and composition. |

## 7. `google-labs-code/stitch-skills`

- GitHub repository ID: `1135847870`
- Stars observed: `7.9k`
- Primary skills reviewed: `15`

**Structure and evidence.** Three plugin groups (`stitch-design`, `stitch-build`, `stitch-utilities`) expose fifteen skills. The README and every primary `SKILL.md` were read. Skills use supporting `scripts/`, `references/`, `examples/`, and Stitch MCP operations; `code-to-design` explicitly composes `extract-static-html`, `extract-design-md`, `manage-design-system`, and `upload-to-stitch`.

**Analysis.** This is a strong example of compositional skills with explicit artifact boundaries: standalone HTML, `.stitch/DESIGN.md`, design-system assets, screen instances, and generated app code. `manage-design-system` includes a user-confirmation gate before uploading a generated design system. The major risk is coupling to Stitch-specific MCP/API schemas and the need to keep multi-skill handoffs synchronized.

**Validation boundary.** No Stitch project was mutated, no uploader script was executed, and no generated screen/app was built.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `stitch::code-to-design` | Orchestrates static-HTML extraction, DESIGN.md extraction/design-system creation, and upload into Stitch. |
| `stitch::generate-design` | Generates/edits/variants screens through Stitch MCP with mandatory prompt-enhancement and project design-system handling. |
| `stitch::manage-design-system` | Creates/retrieves/applies Stitch design systems and requires confirmation before uploading a generated DESIGN.md. |
| `stitch::extract-design-md` | Analyzes frontend source and emits a structured DESIGN.md representation. |
| `stitch::extract-static-html` | Delegates to deterministic extraction tooling to materialize a standalone HTML artifact. |
| `stitch::upload-to-stitch` | Uploads HTML/images/design markdown through a Python uploader/API path. |
| `react-components` | Converts Stitch output into React components with componentization and fidelity constraints. |
| `react-native` | Routes Stitch designs into React Native implementation guidance. |
| `remotion` | Routes Stitch design output into Remotion implementation. |
| `shadcn-ui` | Builds Stitch-derived UIs with shadcn/ui conventions. |
| `react-vite-dashboard` | Builds dashboard implementations using React/Vite from Stitch design artifacts. |
| `design-md` | Defines DESIGN.md design-system extraction/authoring conventions. |
| `enhance-prompt` | Refines vague UI requests into structured design-generation prompts. |
| `stitch-loop` | Iterative generate/review/refine loop for Stitch screens with persisted local artifacts. |
| `taste-design` | Visual quality/anti-generic design guidance used to critique and improve generated interfaces. |

## 8. `antfu/skills`

- GitHub repository ID: `1143952193`
- Stars observed: `5.7k`
- Primary skills reviewed: `18`

**Structure and evidence.** The repo contains hand-maintained skills, generated skills sourced from upstream docs, and vendored skills synchronized from other repositories. All eighteen current `skills/*/SKILL.md` entrypoints were read. `scripts/`, `sources/`, `vendor/`, git submodules, and generation metadata make provenance part of the repository design. The README explicitly calls the project a proof of concept and says generated skills are not fully tested.

**Analysis.** The most reusable design is provenance-aware generation: generated skills record source repository/version/date, while vendored skills remain distinguishable from Anthony Fu's own opinionated skills. This makes maintenance and attribution clearer than flattening everything into one hand-written catalog. The weakness is the stated test gap plus time-sensitive version claims in generated content.

**Validation boundary.** Generation/sync tooling and upstream source trees were inspected as repository structure, but generation and test commands were not executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `antfu` | Anthony Fu's JS/TS project conventions: explicit code, tooling choices, tests and project organization. |
| `antfu-design` | UnoCSS-first semantic tokens, dual-theme design rules, anti-slop checks and micro-interaction guidance. |
| `vue` | Generated Vue 3.5 Composition API/router skill with focused references. |
| `nuxt` | Generated Nuxt 4 reference router for routing, data, modules, rendering and server features. |
| `pinia` | Generated Pinia reference router for stores, plugins, SSR, testing and composability. |
| `vite` | Generated Vite 8/Rolldown-oriented configuration/plugin/SSR guidance. |
| `vitepress` | Generated VitePress reference router for docs sites, themes, Markdown and deployment. |
| `vitest` | Generated Vitest reference router for testing, mocking, coverage and fixtures. |
| `unocss` | Generated UnoCSS usage and configuration reference. |
| `pnpm` | Generated pnpm workspace/package-management reference. |
| `slidev` | Vendored Slidev skill covering Markdown slides, code, export, diagrams and presenter features. |
| `tsdown` | Vendored tsdown skill covering library builds, declaration generation, bundling and validation. |
| `turborepo` | Vendored Turborepo skill with package-task-first rules, caching, filtering, CI and boundaries. |
| `vueuse-functions` | Vendored VueUse function-selection/reference skill. |
| `vue-best-practices` | Vendored Vue best-practice skill. |
| `vue-router-best-practices` | Vendored Vue Router best-practice skill. |
| `vue-testing-best-practices` | Vendored Vue testing best-practice skill. |
| `web-design-guidelines` | Vendored web UI review/guideline skill. |

## 9. `tiangolo/library-skills`

- GitHub repository ID: `1221742654`
- Stars observed: `758`
- Primary skills reviewed: `0`

**Structure and evidence.** Current content is a Python + TypeScript installer/scanner, not an installable skill collection. `README.md`, `src/library_skills/scanner.py`, and scanner tests were read. Repository search did not expose a repository-owned `.agents/skills/<name>/SKILL.md`; mentions of `SKILL.md` belong to docs, test fixtures, and scanning logic.

**Analysis.** The scanner discovers skills embedded inside installed Python distributions and Node packages, validates YAML frontmatter, enforces the skill-name grammar and parent-directory match, deduplicates resolved skill directories, and handles editable Python installs. The tests cover valid, invalid, duplicate, missing-metadata, editable-install, and Node-package cases. This repository should therefore be classified as `skill_tooling`, not `skill_collection`.

**Validation boundary.** Tests were read but not run; no environment was scanned and no symlink/install operation was performed. Individual skill reports: **0**, because this repo supplies tooling rather than its own installable skill.

### Individual skill reports

No repository-owned installable skill was found; count = `0`.

## 10. `hashicorp/agent-skills`

- GitHub repository ID: `1092101865`
- Stars observed: `785`
- Primary skills reviewed: `17`

**Structure and evidence.** Product/plugin hierarchy (`packer/`, `terraform/`) contains seventeen current primary `SKILL.md` entrypoints found in the inspected tree/search surface. All seventeen were read. `scripts/validate-structure.sh` was read; it verifies marketplace JSON, plugin metadata, skill directories/frontmatter, orphan plugins, and product structure. Terraform Policy also ships `evals/eval.yaml` with positive/negative trigger tasks and focused references.

**Analysis.** This repository combines narrow operational Packer skills with deeper Terraform development skills and is the strongest validation-oriented collection in this batch. Skill ownership mirrors product/plugin boundaries, while the root validator enforces catalog invariants. The `terraform-policy` skill is itself a router into author/test references, and several provider skills explicitly require build/tests or acceptance-test workflows. Some Packer instructions can create paid cloud resources; that makes runtime execution materially higher risk than static review.

**Validation boundary.** The structure validator, evals, Packer builds, Terraform tests, provider acceptance tests, and cloud operations were not executed.

### Individual skill reports

| Skill | Assessment |
|---|---|
| `push-to-registry` | Configures Packer builds to publish metadata to HCP Packer registry. |
| `aws-ami-builder` | Packer amazon-ebs AMI build templates, authentication and validation guidance. |
| `terraform-policy` | Router for Terraform Policy authoring/conversion and `.policytest.hcl` testing references. |
| `new-terraform-provider` | Scaffolds a Plugin Framework provider and explicitly finishes with build/test commands. |
| `windows-builder` | Packer Windows image patterns using WinRM/PowerShell and cleanup guidance. |
| `azure-image-builder` | Packer Azure managed-image/Compute Gallery patterns and authentication. |
| `provider-docs` | Provider Registry docs workflow driven from schema descriptions/templates and tfplugindocs generation. |
| `provider-resources` | Plugin Framework resource/data-source CRUD, schema, state and acceptance-test guidance. |
| `terraform-style-guide` | Terraform HCL style/structure conventions. |
| `refactor-module` | Refactors Terraform modules while preserving behavior and module contracts. |
| `terraform-search-import` | Finds/imports existing infrastructure into Terraform configuration/state workflows. |
| `terraform-stacks` | Guidance for Terraform Stacks organization and configuration. |
| `provider-actions` | Implements provider actions using Terraform Plugin Framework patterns. |
| `azure-verified-modules` | Guidance for authoring/using Azure Verified Modules conventions. |
| `run-acceptance-tests` | Runs targeted provider acceptance tests with required environment setup and guardrails. |
| `terraform-test` | Authors and runs Terraform module tests (`.tftest.hcl`) and CI-oriented test workflows. |
| `provider-test-patterns` | Provider test architecture, acceptance tests, sweepers and reusable testing patterns. |

## Cross-repository findings

1. **Router + references is the dominant scalable shape.** Callstack, Palkan, Vue, Antfu, and HashiCorp keep activation/decision logic in `SKILL.md` and move deep domain material into references/workflows.
2. **Generated catalogs need provenance and validation.** Antfu records generated/vendored provenance; Apify generates an `AGENTS.md` view from skill frontmatter and checks marketplace coverage; HashiCorp validates plugin/skill structure. These are stronger than manually duplicating catalog metadata.
3. **Decision skills should not silently become execution skills.** Callstack's migration assessment keeps diagnosis read-only and hands implementation to a separate skill after an evidence gate.
4. **Machine-readable intermediate artifacts improve handoffs.** Stitch's HTML → DESIGN.md → design system → screen/app chain is an explicit example. Tiangolo similarly treats package metadata and `.agents/skills/*/SKILL.md` as discoverable contracts.
5. **Freshness remains a major risk.** Remotion and Antfu carry explicit version/date assumptions; Vue's repository warns that experimental content may be incomplete; cloud/API-centric skills can drift as providers change.

## Classification correction

`tiangolo/library-skills` was indexed as a skill collection but current content is tooling that discovers and installs skills embedded in dependency packages. Deep analysis therefore recommends reclassification to `skill_tooling`. It is still counted as a completed repository analysis because identity, stars, README, implementation, and tests were actually inspected; it contributes `0` individual skill reports.

## Verification boundary

No third-party command, test suite, browser workflow, cloud build, deployment, package installation, Stitch mutation, or other external side-effect workflow was executed in this batch. `structure-reviewed` means the repository and skill definitions were read deeply enough to characterize architecture, workflow, supporting assets, validation mechanisms, and limitations; it does not mean runtime correctness was proven.
