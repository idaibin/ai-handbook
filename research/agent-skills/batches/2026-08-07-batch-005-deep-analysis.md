# GitHub Skills Catalog — Deep Analysis Batch 005

- Observed: `2026-08-07`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Queue snapshot blob: `0cf88664b98a2d75773bd793291060ccc55ff3b9`
- Snapshot: `1637` unique repositories, `1255` provisionally eligible, `382` held for review.
- Completion rule used: a repository is counted only after GitHub identity and displayed star count are checked and actual repository content is read. Metadata-only candidates are not complete.
- Validation level: `structure-reviewed`.
- Runtime validation: `not_executed`. Third-party CLIs, APIs, installs, deploys, and test suites were not executed in this batch.

## Batch result

10 repositories were completed. The repository reports below cover current structure, README/equivalent documentation, skill definitions, representative scripts/references, and tests/evals when discoverable. The individual-skill section contains 22 skill/equivalent reports: 21 Agent Skills packages plus one legacy Azure Cognitive Search WebApiSkill equivalent. `agentskills/agentskills` is a specification/reference-implementation repository and contains no installable skill package, so no synthetic skill was invented for it.

| Repository | GitHub ID | Stars observed | Current-content classification | Skill / equivalent reports |
|---|---:|---:|---|---:|
| `alibaba-flyai/flyai-skill` | `1186572375` | `905` | single Agent Skill + external CLI runtime | 1 |
| `Young140430/voxcpm2-openai-skill` | `1211580579` | `0` | single Agent Skill + Python client | 1 |
| `matdac12/openai-skill` | `1078864377` | `1` | single generated API-reference skill | 1 |
| `Kinopoint/piapi-video-toolkit-skill` | `1195616593` | `0` | single Agent Skill + TypeScript CLI | 1 |
| `ignaciofls/openaiskill` | `566711877` | `2` | legacy Azure Cognitive Search WebApiSkill | 1 equivalent |
| `supabase/agent-skills` | `1135501937` | `2.5k` displayed | two-skill official collection | 2 |
| `firebase/agent-skills` | `1154880547` | `397` | multi-skill official collection | 12 |
| `railwayapp/railway-skills` | `1127614661` | `304` | one installable skill + plugin/MCP packaging | 1 |
| `laravel/agent-skills` | `1131154155` | `686` | three-skill official collection + separate agent | 3 |
| `agentskills/agentskills` | `1117639997` | `23.9k` displayed | Agent Skills specification + reference validator | 0 |

Star values are the values displayed by GitHub repository pages during this review. Large values are preserved in GitHub's displayed abbreviated form instead of being converted into invented exact integers.

## Repository reports

### 1. `alibaba-flyai/flyai-skill`

**Identity and structure.** Public repository, default branch `main`. Current root exposes `.claude-plugin/`, `assets/`, `skills/`, `README.md`, and license material. The installable skill is `skills/flyai/`.

**Read evidence.** `skills/flyai/SKILL.md` blob `951165b0d06c4b4c3e5801107556a313cf4b12ea`; `skills/flyai/references/search-flight.md` blob `e5097dc4acdd88f13fdcdc0d78ad9058945fe201`; README was inspected as part of the repository review.

**Design.** The repository separates agent routing from execution. `SKILL.md` maps travel intents to a fixed command surface and requires the relevant command reference to be read before invocation. Actual searches are delegated to `@fly-ai/flyai-cli`; command results are structured JSON and the references define command parameters and result contracts.

**Useful patterns.** Strong intent-to-command routing, progressive reference loading, explicit machine-readable output expectations, and keeping network implementation outside the prompt package. This is a good example of a skill acting as a thin, deterministic orchestration layer over a separately versioned tool.

**Limits.** Repository-local behavior does not prove the external CLI or upstream service. No repository-local eval/test harness was found in the inspected skill surface. Network freshness, authentication, and upstream result quality therefore remain outside this review.

### 2. `Young140430/voxcpm2-openai-skill`

**Identity and structure.** Public repository, default branch `main`; root contains `README.md`, `SKILL.md`, setup scripts, and `voxcpm2_speech.py`.

**Read evidence.** `SKILL.md` blob `1f7bc00471ebfda1a4f8a04608a51cfb7fc1314f`; `voxcpm2_speech.py` blob `61e4985a64e1c6e5cc3efffc2147f541c35d2dc3`; README blob `5bd02b56e5d1cfe754673ebce40a827b193fb17b`.

**Design.** A compact instruction layer wraps an OpenAI-compatible speech endpoint. The Python client supports ordinary TTS plus reference-audio input, transforms local reference audio into a data URI, sends the request, and saves the returned audio bytes.

**Verified drift.** Documentation and `SKILL.md` describe the default model as `voxcpm2`, while the Python implementation currently defaults to `/home/ubuntu/OpenBMB/VoxCPM2`. That is a concrete documentation/runtime mismatch that can make a supposedly portable skill environment-specific. The script also installs `httpx` automatically when missing, which is convenient but reduces dependency determinism and should preferably be replaced by an explicit install/lock step.

**Specification note.** The root `SKILL.md` declares `name: voxcpm2-openai-speech` while the repository directory name is `voxcpm2-openai-skill`. A strict Agent Skills validator that treats the repository root as the skill directory would reject a name/directory mismatch; packaging tools may avoid this by installing under the declared skill name, so this is recorded as a compatibility risk rather than a universal failure.

**Safety/privacy boundary.** The repository includes reference-voice functionality. Any real use should require authorization for the referenced voice and should avoid impersonation. No generation was executed here.

### 3. `matdac12/openai-skill`

**Identity and structure.** Public repository, default branch `main`; the main package is `openai-api/` and is described as documentation generated from an OpenAPI specification.

**Read evidence.** README blob `1c4ad83363ce8717bd7111f7080b577c87dc3e3f`; `openai-api/SKILL.md` blob `5ee4b4c1c7e53b8da870aa4353b3056bd23dd34c`; `openai-api/references/responses.md` blob `c5c45bd8a4892a70d201195c3db8ee28ec58978e`.

**Design.** A shallow top-level skill routes questions into many endpoint-specific Markdown references. This keeps the activation document smaller than the full API reference and makes the repository a useful example of generated reference partitioning.

**Limits.** The generated material mixes newer Responses API reference material with older examples such as legacy chat/completions model usage. Static generated API documentation can become stale quickly, so the package should record the source spec revision and generation timestamp and treat current provider documentation as authoritative. No meaningful repository-local eval harness was discovered in the inspected surface.

### 4. `Kinopoint/piapi-video-toolkit-skill`

**Identity and structure.** Public repository, default branch `main`; root includes `docs/`, `piapi-video-toolkit/`, `src/`, `tests/`, package metadata, and environment example files.

**Read evidence.** README blob `29ff845b7104b915991c658091ed564a07ffea40`; skill blob `7100167986e434a439499fde7076e34dcf7fdba0`; pricing reference blob `2e3119386291424a924d9ffa77eb1d90ad52df8d`; `package.json` blob `ba1ce911cc026d65062b9d116c1dbd1b0bc95db8`.

**Design.** The repository deliberately separates a decision/advisory skill from a runnable Node.js/TypeScript toolkit. The skill chooses models, compares price/duration tradeoffs, and describes workflow boundaries; the CLI handles actual API calls, polling, history, and downloads. `package.json` declares Node 22+, TypeScript build, and a `vitest run` test command.

**Useful patterns.** Clear distinction between knowledge layer and execution layer; explicit treatment of unknown pricing instead of fabricating totals; references split by models, pricing, and workflows.

**Limits.** The `tests/` directory and Vitest command are present, but the connector's code-search snapshot did not expose an individual test file during this run, so test definitions were not represented as executed evidence. Pricing is time-sensitive and needs a source/update process; the skill currently stores values as static reference data.

### 5. `ignaciofls/openaiskill`

**Identity and structure.** Public repository, default branch `main`. This is not an Agent Skills-format package; it is a legacy Azure Cognitive Search custom WebApiSkill implemented as an Azure Function.

**Read evidence.** README blob `47803e0e68d85ec3df1cfcb18e0035a06ef615fc`; Azure Function implementation `aoaicustomskill/__init__.py` blob `7af431a4957048c4dc8d820920acabd1bb81d9d0`.

**Design.** The README defines the equivalent skill contract as an Azure Cognitive Search `WebApiSkill` with input/output fields. The Python function receives Cognitive Search enrichment records, splits text into chunks, invokes Azure OpenAI completions, and returns summarized enrichment records.

**Verified classification drift.** This repository should not be treated as a portable Agent Skills package. It is adjacent historical material with a different meaning of “skill.” The implementation hardcodes `text-davinci-002` and uses the legacy `openai.Completion.create` surface, while the README still describes 2022-era gated-preview setup. It is valuable mainly as a historical integration pattern, not as a current Agent Skills implementation.

**Limits.** No `SKILL.md`; no Agent Skills frontmatter; no current eval harness observed; current Azure/OpenAI compatibility was not executed.

### 6. `supabase/agent-skills`

**Identity and structure.** Public repository, default branch `main`; root contains `skills/`, `scripts/`, `test/`, `.github/`, package metadata, and release/discovery tooling.

**Read evidence.** README blob `528beca0861b4a42368c87f8190d6fa96df44900`; `skills/supabase/SKILL.md` blob `0b29abc8d947e31d858c9d5a8a230cb302f99745`; `skills/supabase-postgres-best-practices/SKILL.md` blob `6400792389dfcc82c81953054e546bd72ebcd259`; `scripts/build-release.ts` blob `3f89f294c225ed6c7bd8932a2bddda99841059a6`; `test/sanity.test.ts` blob `2a85c0d52871d5195e41aa2c4c7f4140576620f5`.

**Design.** Two public skills are intentionally separated: broad Supabase product guidance and PostgreSQL best practices. The release builder discovers skill directories, validates `name` and `description`, creates deterministic tarballs, computes SHA-256 digests, and emits a discovery index using the Agent Skills discovery schema. The sanity test checks that exactly the two intended public skills are discoverable/installable and that installation produces `SKILL.md` files.

**Useful patterns.** This is one of the stronger packaging examples in the batch: deterministic archives, digest-based integrity, generated discovery metadata, explicit public-skill allowlist, and install-path sanity tests. The main Supabase skill also emphasizes current docs and post-change verification, while the Postgres skill decomposes advice into focused rules/references.

**Runtime boundary.** Tests were read, not executed.

### 7. `firebase/agent-skills`

**Identity and structure.** Public repository, default branch `main`; README describes a cross-agent skill collection with installation paths for multiple clients. Current `skills/` surface contains 12 primary `SKILL.md` packages reviewed here, plus references and a Swift project-modification script.

**Read evidence.** README blob `5047fd111769a1efd29aef22207dcf7563f7d533`; primary skill blobs: Crashlytics `2c162fda7ad62f60210edf51d755870211f8355b`, Hosting `174dab84cee92c2889ce230b89b2f2d5c076df01`, App Hosting `d772ef8259de8e8bd5d9bd8783fd0b2f1970dfbb`, Firestore `87b5bc5e9a5e5daa45fb275e952a7b77d75730f8`, Auth `c86b59234f1dab8d92321e9e4ccdb1acdf002555`, Basics `22b6ef1632955bc515633f59fbd2f1d7102ac6e0`, Xcode project setup `54cccad77a1905306f975ea9e800288e955a8324`, Security Rules Auditor `a235dee39dbbacd4af686990fa3d26ba744e1a9e`, Extension migration `0581d43bf7f8e4739d5834c439e19e3e3b327b7c`, Remote Config `772b1e1416f966adb49ee5580e62b5e0399b90bd`, AI Logic `065c677708319e37a84db14c659bdac35cf5647b`, SQL/Data Connect `346c1c8e59098aee89bc7e1cd46d1cc4aff733b8`. Representative implementation/reference evidence: `xcode_spm_setup/Sources/main.swift` blob `d4ca68c465ff15f579040e5e1493e33092741b06`; SQL Connect operations reference blob `5b2e5741ce884dd930b1433e339e1873032b59f8`.

**Design.** The collection uses narrowly routed product skills rather than one monolithic Firebase prompt. Most skills explicitly state what not to use them for, then push detail into platform/product references. `firebase-basics` centralizes CLI/project setup; product skills cross-reference it. The Xcode skill includes native Swift automation using `XcodeProj` and `PathKit` instead of raw `.pbxproj` text editing. SQL Connect requires schema inspection and compile validation rather than guessing generated operations.

**Two concrete spec-conformance findings.** First, `skills/firebase-data-connect-basics/SKILL.md` declares `name: firebase-data-connect`; the current Agent Skills specification and reference validator require the skill directory name to match `name`, so strict validation would report a mismatch. Second, `skills/firebase-ai-logic-basics/SKILL.md` has a top-level `version: 1.0.1`; the current reference validator allows only `name`, `description`, `license`, `allowed-tools`, `metadata`, and `compatibility`, so strict validation would report `version` as an unexpected field. These are format-level findings from static inspection; the validator was not executed against this repository in this run.

**Useful patterns.** Strong trigger exclusion boundaries, mandatory reference reading for risky/complex operations, current-doc lookup instructions for fast-changing AI models, explicit user review before Remote Config deployment, and implementation helpers for error-prone Xcode project edits.

**Limits.** No repository-wide eval/test harness was identified by the inspected code-search surface. Several skills depend on fast-changing Firebase CLI/product behavior, so their accuracy relies on active maintenance and current-doc checks.

### 8. `railwayapp/railway-skills`

**Identity and structure.** Public repository, default branch `main`. The repository packages one installable `use-railway` skill together with plugin manifests, hosted MCP configuration, hooks, scripts, references, and CI assets for several agent clients.

**Read evidence.** README blob `3a48455dd67b563ba1f000a91103f758ce42d132`; `plugins/railway/skills/use-railway/SKILL.md` inspected; GraphQL helper `scripts/railway-api.sh` blob `39a4665375dccdf2eeb3718fd10a43b558e18dc0`; sandbox reference blob `34bcf5bd02adbc3460570e71f8940a61bf01eb53`; hook regression test `plugins/railway/hooks/auto-approve-api.test.sh` blob `5c9f8c389ec0f7e328e4f9e0d7c4be3466a56790`.

**Design.** `use-railway` is route-first: it chooses among CLI, remote MCP, and GraphQL based on the operation and local-context needs. It parses dashboard IDs, distinguishes deploy/signup flows from diagnostic preflight, checks agent-tooling freshness, and moves operation-specific detail into references. The GraphQL helper deliberately keeps bearer tokens and request bodies out of process arguments. The hook regression test checks that auto-approval remains restricted to intended single-command forms rather than broad shell input.

**Useful patterns.** Clear authority/path routing, explicit context resolution, freshness checks, security-conscious helper implementation, and regression tests around approval boundaries. This is a strong example of a skill that coordinates multiple execution mechanisms rather than pretending one tool is universal.

**Runtime boundary.** CI/test definitions were inspected but not run.

### 9. `laravel/agent-skills`

**Identity and structure.** Public repository, default branch `main`. README identifies three installable skills: `starter-kit-upgrade`, `deploying-laravel-cloud`, and `configure-nightwatch`. A separate `laravel-simplifier` agent exists but is not counted as a skill.

**Read evidence.** README blob `46cf27a9b6e51267e980829436383bcc607fc006`; `starter-kit-upgrade/SKILL.md` inspected; Cloud skill blob `4f59a99c573a0ba45d7f19ae552d132a18d61751`; Nightwatch skill blob `000a031b1304b6412ef25b4560984e4e487ab414`; preflight script blob `51764a696942d7e4a687878a963a3536226fa86c`; test runner blob `168913e2f3945bfc146f1fd12dfb34482071a009`.

**Design.** The collection is organized by domain/product. The starter-kit upgrade skill has a strong change-safety workflow: clean-tree preflight, dedicated branch, baseline verification, constrained feature commits, and comparison of post-change failures against baseline. `run_tests.sh` discovers PHP tests, JS typechecks, and JS builds, records structured JSON, and can report regressions relative to a baseline. The Cloud skill requires runtime CLI help discovery instead of hardcoding unstable signatures and requires deploy monitoring. Nightwatch decomposes observability configuration into sampling, filtering, redaction, and references.

**Useful patterns.** Explicit preconditions before side effects, baseline-vs-post validation, deterministic error boundaries, and separating strict rules from judgment calls. The starter-kit upgrade package is particularly useful as an example of encoding repository mutation discipline into a skill.

**Runtime boundary.** Scripts and validation logic were read but not executed.

### 10. `agentskills/agentskills`

**Identity and structure.** Public repository, default branch `main`. This is the Agent Skills specification and reference tooling repository, not a distributable skill collection.

**Read evidence.** README blob `247e4a18e908d3bf27092f886f25c2515d84ecbc`; specification blob `d9a2db099d905da8b879a5c6f996728073985279`; validator implementation blob `22cf6f8ae5f905d780cb097c0938711cc37016a9`; validator tests blob `3b5e89da7af4b5db2eb8aa74d35a5f7e2e3893c7`.

**Design.** The specification formalizes progressive disclosure: metadata for discovery, full `SKILL.md` on activation, and referenced resources on demand. Required frontmatter is minimal (`name`, `description`), with optional license, compatibility, metadata, and experimental allowed-tools. The reference validator checks required files, name syntax and directory matching, description/compatibility lengths, and unexpected frontmatter fields. Tests cover valid/invalid names, directory mismatches, optional fields, internationalized names, normalization, and length limits.

**Useful patterns.** This repository provides the strongest normative basis for evaluating other packages in the catalog. A practical catalog should store a distinction between `specification-conformant`, `host-compatible but non-conformant`, and `not-validated`, rather than assuming that any repository containing `SKILL.md` is valid.

**No individual skill.** No installable `SKILL.md` package is represented as a product of this repository; the repository is counted as a completed specification/reference implementation review only.

## Individual skill / equivalent reports

### `flyai` — `alibaba-flyai/flyai-skill`

Travel-search orchestration skill. The key reusable idea is intent routing into a small fixed CLI surface with one reference document per command. Execution and freshness belong to an external CLI/service, not the skill body. Status: structure-reviewed; runtime not executed.

### `voxcpm2-openai-speech` — `Young140430/voxcpm2-openai-skill`

OpenAI-compatible speech client skill. Includes a real Python execution script and reference-audio support. Main finding: documented default model and script default differ; dependency installation is performed dynamically. Root-directory/name conformance may depend on installer behavior. Status: structure-reviewed; no audio generation performed.

### `openai-api` — `matdac12/openai-skill`

Generated API-reference skill with endpoint-specific references. Useful for reference partitioning, but generated API content needs explicit source-version/freshness metadata. Status: structure-reviewed; no API request executed.

### `piapi-video-toolkit` — `Kinopoint/piapi-video-toolkit-skill`

Decision layer for model selection, published pricing, and workflow planning, paired with a separate TypeScript execution CLI. Strong separation of advisory vs execution responsibilities. Static prices require maintenance. Status: structure-reviewed; no external API call or test run.

### `azureopenai_skill` (legacy equivalent) — `ignaciofls/openaiskill`

Azure Cognitive Search `WebApiSkill`, not an Agent Skills package. It summarizes enrichment records through a legacy Azure OpenAI completions integration. Counted only as an equivalent historical skill definition so catalog classification can be corrected. Status: legacy structure-reviewed; current runtime compatibility not verified.

### `supabase` — `supabase/agent-skills`

General Supabase guidance skill. It centralizes product workflow, security/RLS concerns, current-doc lookup, and post-change verification. Status: structure-reviewed.

### `supabase-postgres-best-practices` — `supabase/agent-skills`

Focused Postgres rules/reference package. Complements rather than duplicates the broader Supabase skill. Repository packaging and installer sanity tests explicitly include this skill. Status: structure-reviewed; tests not executed.

### `firebase-crashlytics` — `firebase/agent-skills`

Crashlytics setup and SDK-usage router for Android/iOS, with platform references and Firebase CLI/MCP dependency. Status: structure-reviewed.

### `firebase-hosting-basics` — `firebase/agent-skills`

Classic static/SPAs Firebase Hosting skill with explicit negative routing against App Hosting and unrelated Firebase products. Splits configuration/deployment detail into references. Status: structure-reviewed.

### `firebase-app-hosting-basics` — `firebase/agent-skills`

Full-stack SSR App Hosting workflow. Encodes billing prerequisite, source deployment, secrets, CI/CD, and emulation references. Status: structure-reviewed.

### `firebase-firestore` — `firebase/agent-skills`

Firestore workflow that first resolves database edition, then routes to Standard/Enterprise references. Strong point: it requires generated-schema/reference inspection before application code. Status: structure-reviewed.

### `firebase-auth-basics` — `firebase/agent-skills`

Authentication setup and SDK/security-rules guidance. Defines provisioning and deployment steps and delegates platform-specific implementation to references. Status: structure-reviewed.

### `firebase-basics` — `firebase/agent-skills`

Foundation/routing skill for CLI, authentication, project selection/creation, and config retrieval. It intentionally excludes product-specific work and is reused by the rest of the collection. Status: structure-reviewed.

### `xcode-project-setup` — `firebase/agent-skills`

Xcode dependency/project automation skill backed by a Swift helper. The helper edits project objects through `XcodeProj`, links Swift Package products, adds Firebase linker configuration, and handles Crashlytics build settings. Status: structure-reviewed; Swift helper not executed.

### `firebase-security-rules-auditor` — `firebase/agent-skills`

Defensive review skill for Firestore/Storage rules with a fixed audit checklist and structured JSON findings. It focuses on authorization and validation weaknesses. Status: structure-reviewed; no live ruleset tested.

### `extension-to-functions-codebase` — `firebase/agent-skills`

Migration workflow for turning Firebase Extensions into modern Cloud Functions code or reusable packages. It defines V1→V2 migration rules, lifecycle mapping, IAM/API declarations, and packaging constraints. Status: structure-reviewed.

### `firebase-remote-config-basics` — `firebase/agent-skills`

Remote Config template/SDK skill. Notable safety property: it requires user review before deploying prepared template changes and verifies version history afterward. Status: structure-reviewed.

### `firebase-ai-logic-basics` — `firebase/agent-skills`

Firebase AI Logic integration guidance with current-model lookup instructions, App Check requirements, and platform references. Spec finding: top-level `version` is outside the current reference validator's allowed frontmatter fields. Status: structure-reviewed.

### `firebase-data-connect` — `firebase/agent-skills`

SQL Connect/Data Connect schema, authorized-operations, SDK generation, and deployment workflow. Strong validation pattern: inspect generated schema and compile operations rather than guessing. Spec finding: declared name differs from parent directory `firebase-data-connect-basics`. Status: structure-reviewed.

### `use-railway` — `railwayapp/railway-skills`

Infrastructure-operation router across CLI, hosted MCP, and GraphQL fallback. Includes references, analysis scripts, a token-conscious GraphQL helper, hooks, and regression tests around approval boundaries. Status: structure-reviewed; CI/tests not executed.

### `starter-kit-upgrade` — `laravel/agent-skills`

Repository-upgrade skill with clean-tree preflight, branching discipline, baseline tests, constrained edits, and regression comparison. Strong example of encoding mutation safety and verification into the skill contract. Status: structure-reviewed; scripts not executed.

### `deploying-laravel-cloud` — `laravel/agent-skills`

Laravel Cloud CLI operations skill. Uses runtime help discovery, explicit non-interactive flag policy, deployment monitoring, and destructive-operation confirmation. Status: structure-reviewed.

### `configure-nightwatch` — `laravel/agent-skills`

Observability configuration skill covering sampling, event filtering, and redaction, with official documentation as primary authority and a quick reference layer. Status: structure-reviewed.

## Cross-batch findings worth preserving

1. **“Skill” is not one repository type.** `ignaciofls/openaiskill` uses the older Azure Cognitive Search WebApiSkill meaning, while `agentskills/agentskills` defines the current Agent Skills format. Catalog classification must preserve that distinction.
2. **Spec validation is materially useful.** The current Agent Skills reference validator exposes concrete format drift in otherwise high-quality collections, including Firebase's directory/name mismatch and unexpected top-level `version` field.
3. **Strong repositories separate instructions from execution.** Supabase, Railway, Laravel, Alibaba, and Kinopoint each keep core routing/constraints in `SKILL.md` while moving tools, scripts, or references into separate assets.
4. **Read tests without claiming they ran.** Supabase installer sanity tests, Railway hook regression tests, and Agent Skills validator tests are substantive evidence of intended invariants, but this batch remains static/structural review only.
5. **Fast-changing domains need freshness contracts.** Generated API references, cloud CLIs, model names, and price tables should carry source/version/update metadata and preferably automated freshness checks.

## Verification boundary

This batch did **not** install dependencies, execute third-party scripts, invoke external services, deploy infrastructure, synthesize audio/video, or run test suites. `structure-reviewed` means the repository identity, displayed stars, and actual source/reference/test material were inspected and analyzed. It does not mean behavior was runtime-verified.
