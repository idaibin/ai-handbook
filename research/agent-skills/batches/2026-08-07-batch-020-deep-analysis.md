# GitHub Skills Catalog Deep Analysis — Batch 020

## Scope

- Batch ID: `2026-08-07-batch-020`
- Queue basis: existing indexed repository queue under `sources/catalog/batches/agentskills-pages-2-3.json`
- Repositories completed in this batch: **10**
- Repository-scoped individual skill reports: **42**
- Completion level: **`structure-reviewed`**
- Runtime validation: **`not_executed`**
- Star snapshot observed from GitHub repository pages during the 2026-08-07 run. Stars are point-in-time observations and can drift after the run.

A repository is counted complete here only after content-level reading. Repository metadata alone was not sufficient. For every repository below, identity/stars were checked and actual repository files were read. `SKILL.md`, equivalent definitions, scripts, references, tests/eval surfaces, and implementation files were read when present and relevant.

## Batch results

| Repository | Stars observed | Repository-scoped skill reports | Content-level classification | Main evidence read |
| --- | ---: | ---: | --- | --- |
| `chigwell/skilldock.io` | 85 | 0 | `skill_tooling_registry_sdk` | README, package/install source, dependency-resolution source, package tests |
| `akshayaggarwal99/agentskills` | 7 | 0 | `skill_tooling_registry_cli` | README, provider implementation, registry implementation |
| `phronetic-ai/agentskills` | 7 | 16 | `skill_collection_sdk` | README, all 16 `SKILL.md`, discovery/parser code, validator and token-loading validation script |
| `trancong12102/agentskills` | 3 | 5 | `skill_collection_plugin` | README, all 5 current plugin `SKILL.md`, llms probe script, ast-grep rule reference |
| `jason-allen-oneal/openclaw-skill-scanner` | 11 | 1 | `single_skill_security_tooling` | README, root `SKILL.md`, scan/install script, systemd reference |
| `AnsonLai/AgentSkills.legal-Multi-Contract-Analyzer` | 2 | 0 | `adjacent_legal_ai_application` | README, repository search for `SKILL.md`, Gemini/skill-selection application code |
| `civitai/civitai-gen-skill` | 16 | 1 | `single_skill_domain_package` | README, `civitai-gen/SKILL.md`, CLI implementation, smoke-test definition |
| `SherifEldeeb/agentskills` | 5 | 11 | `skill_collection` | README, all 11 `SKILL.md`, development/testing guidance |
| `editframe/skills` | 14 | 7 | `skill_collection_domain_sdk_docs` | all 7 `SKILL.md`, render reference, webhook security reference |
| `tiann/execplan-skill` | 66 | 1 | `single_skill_methodology` | repository identity, `SKILL.md`, full ExecPlan methodology reference |

## Repository analysis

### 1. chigwell/skilldock.io

**Verified facts**

This repository is a Python SDK/CLI and package-management client for a skill registry rather than a collection of locally bundled skills. Actual source reading shows a packaging layer that requires a `SKILL.md` in the input skill directory, produces deterministic sorted ZIP contents, excludes common repository/cache/build directories and symlinks, and records SHA-256/size/file counts. The local-skill layer defines manifests/lock metadata, version requirements, dependency graph resolution, conflict handling, release lookup, and reconciliation. Package tests cover top-level archive naming behavior.

A repository search for `SKILL.md` surfaced README/source/tests that reference skill files, not a local skill package to count. Therefore this batch records **0 repository-scoped skills**.

**Inference**

The reusable value is its package-manager architecture: provenance/lock state, deterministic packaging, release constraints, and dependency resolution are separate from skill content itself.

**Not verified**

No unit test suite, publishing flow, registry API, authentication, purchase flow, or installation was executed.

### 2. akshayaggarwal99/agentskills

**Verified facts**

The README describes a CLI for browsing, searching, installing, zipping, and removing skills sourced from `anthropics/skills`. Source reading confirms a `SkillProvider` abstraction, an `AnthropicSkillProvider` that clones/updates the upstream repository and parses its `SKILL.md` files, a `LocalSkillProvider`, and a `SkillRegistry` that aggregates providers with browse/search/pagination/get/install behavior.

The repository does not bundle the upstream Anthropic skill corpus as its own repository-scoped skill definitions. The search surface contains references to `SKILL.md`, but no local skill package to count. Therefore this batch records **0 repository-scoped skills**.

**Inference**

This is best indexed as skill discovery/install tooling, not as a skill collection. Counting upstream Anthropic skills here would double-count externally sourced content.

**Not verified**

The CLI, git cache update path, provider installation, PyPI package, and any implicit tests were not executed.

### 3. phronetic-ai/agentskills

**Verified facts**

This repository combines an Agent Skills SDK with **16 actual local skill packages**. All 16 `SKILL.md` files were read: `pdf`, `xlsx`, `pptx`, `docx`, `canvas-design`, `algorithmic-art`, `theme-factory`, `frontend-design`, `webapp-testing`, `web-artifacts-builder`, `slack-gif-creator`, `internal-comms`, `doc-coauthoring`, `skill-creator`, `mcp-builder`, and `brand-guidelines`.

The SDK implementation was also read. Discovery recursively locates directories containing `SKILL.md`, avoids recursing further once a skill directory is found, deduplicates by skill name with first occurrence winning, and supports metadata-only discovery. The parser validates frontmatter through Pydantic and discovers scripts/references/assets. A `quick_validate.py` helper checks the skill file/frontmatter and common name/description constraints.

The repository includes `examples/validate.py`, which compares loading all skill instructions against metadata plus selective skill loading. Its token estimate is implemented using character-count heuristics rather than a tokenizer, so it is evidence of the intended progressive-disclosure mechanism, not a rigorous token benchmark.

**Inference**

The strongest reusable pattern is the explicit split between metadata discovery and on-demand instruction/resource loading. The code makes the progressive-disclosure concept concrete rather than leaving it only as README guidance.

**Not verified**

No pytest suite, framework adapter, external model invocation, document/media tool, browser workflow, or validation script was executed.

### 4. trancong12102/agentskills

**Verified facts**

The current `ora` plugin contains **5 actual skills**: `code-search`, `ast-grep`, `lib-docs`, `repo-research`, and `pkg-versions`. All five `SKILL.md` files were read.

The skills are narrow routing contracts rather than broad tutorials. `code-search` distinguishes exact/semantic/symbol/AST/history questions and explicitly requires verification of load-bearing conclusions against cited source. `ast-grep` delegates detailed rule syntax to a reference; that reference was read and covers atomic, relational, and composite rules and the importance of `stopBy`. `lib-docs` prefers author-published `llms.txt` before a Context7 fallback; its `llms-probe.sh` implementation probes multiple paths, follows redirects, rejects HTML soft-404s, handles unknown sizes, and deduplicates final URLs. `repo-research` selects different mechanisms for conceptual repo search, exact identifiers, deep source dives, and issue/PR/release/history work. `pkg-versions` exposes a narrow package-version/deprecation contract.

**Inference**

The reusable design is capability routing: a small `SKILL.md` can encode when *not* to use a tool and how to verify uncertain tool output, reducing context and search noise.

**Not verified**

None of the MCP servers, Sourcegraph, Morph, Context7, `gh`, git-clone helper, ast-grep, deps.dev, or shell scripts were executed.

### 5. jason-allen-oneal/openclaw-skill-scanner

**Verified facts**

This repository contains **1 formal skill**, `openclaw-skill-scanner`. The root `SKILL.md` defines a defensive supply-chain gate around an external skill scanner. The actual `scan_and_add_skill.sh` implementation was read: it validates candidate paths/names, invokes the scanner, parses severity counts from the generated report, blocks High/Critical findings unless explicitly forced, allows lower severities with warnings, and copies accepted skill directories to the OpenClaw skill location. A systemd user service reference points to the automatic scanner script.

**Inference**

The useful pattern is policy separation: scanning produces evidence, while installation policy maps findings to block/warn behavior. This is clearer than treating “scanner ran” as equivalent to “skill is safe.”

**Not verified**

The Cisco scanner dependency, `uv`, systemd path activation, quarantine behavior, report parsing against live scanner output, or install workflow was not executed.

### 6. AnsonLai/AgentSkills.legal-Multi-Contract-Analyzer

**Verified facts**

The README describes a browser-based contract review/redlining application using Gemini and internal “legal skills”/rules. Repository search returned **no formal `SKILL.md`**. Actual `skills-ai.js` application code was read and contains Gemini response parsing/debugging, normalized findings, internal skill-summary construction, and analysis payload handling.

This is therefore a **classification correction** from name-based AgentSkills adjacency to `adjacent_legal_ai_application`. It receives **0 formal repository-scoped skill reports**.

**Inference**

The term “skill” here is an application-level rule/checklist abstraction, not evidence of an Agent Skills package. Indexing must distinguish domain terminology from actual Agent Skills format.

**Not verified**

No browser application, Gemini API call, DOCX mutation, legal analysis quality, redline correctness, or export was executed.

### 7. civitai/civitai-gen-skill

**Verified facts**

This repository contains **1 formal skill**, `civitai-gen`. Its `SKILL.md` defines one unified workflow surface for multiple media-generation job types, cost estimation, asynchronous lifecycle operations, batching, and experiments. `generate.mjs` was read and implements a zero-npm-dependency Node CLI with domain logic separated into API/image/video/audio modules and a common submit/poll/download lifecycle.

The smoke-test definition was read. It contains a read-only mode for help/engine/cost/error-path checks and a separate write section that can consume service credits. The existence of that test file is recorded as a test surface, not as evidence the tests passed.

**Inference**

A useful design pattern is a single skill contract over a modular runtime: the `SKILL.md` presents stable workflow semantics while implementation details are split into domain modules.

**Not verified**

No API key was used; no media generation, cost request, live engine lookup, smoke test, download, or external service operation was executed.

### 8. SherifEldeeb/agentskills

**Verified facts**

This repository contains **11 actual skills**: 6 baseline (`docx`, `xlsx`, `pptx`, `pdf`, `research`, `image-generation`) and 5 defensive cybersecurity-domain skills (`soc-operations`, `incident-response`, `threat-intelligence`, `vulnerability-management`, `grc`). All 11 `SKILL.md` files were read.

`DEVELOPMENT.md` was also read. It defines repository skill structure, frontmatter/body conventions, coding standards, dependency guidance, and manual validation/testing expectations. The cybersecurity skills are primarily operational/documentation/assessment workflows rather than offensive exploit instructions.

**Inference**

The repository demonstrates a simple two-tier taxonomy: reusable baseline artifact/research capabilities plus domain-specific workflow skills. The taxonomy is explicit in both paths and metadata.

**Not verified**

No Python utility module, dependency installation, manual validation command, test case, feed access, document generation, or security workflow was executed.

### 9. editframe/skills

**Verified facts**

The repository exposes **7 direct skill packages**: `composition`, `editframe-api`, `editframe-cli`, `editframe-create`, `editor-gui`, `vite-plugin`, and `webhooks`. All seven `SKILL.md` files were read.

The skills form a product-family documentation surface rather than unrelated tasks. `composition` covers HTML/React video composition and points to fine-grained references; the render-to-video reference was read and describes browser/WebCodecs and React rendering. `webhooks` includes operational event guidance; its security reference was read and specifies HMAC-SHA256 over raw request bodies, timing-safe comparison, and replay/timestamp considerations. `vite-plugin` explicitly identifies its package/version metadata and proprietary license marker, while the other reviewed skills carry their own license metadata.

**Inference**

A reusable pattern is “reference-index skill”: keep the entry `SKILL.md` navigational and route agents into narrow, task-specific references instead of embedding the entire SDK manual in one context payload.

**Not verified**

No npm package installation, local/browser render, WebCodecs check, cloud API call, file upload, transcription, webhook delivery, HMAC test, Vite plugin test, or visual regression test was executed.

### 10. tiann/execplan-skill

**Verified facts**

This repository contains **1 formal skill**, `execplan`. Its `SKILL.md` is intentionally very small and delegates the methodology to `references/PLANS.md`, which was read. The reference defines an ExecPlan as a self-contained living implementation document that should guide a novice from context to observable working behavior. It requires exact repository paths/commands, validation and acceptance, idempotence/recovery, milestones, captured evidence, and maintained `Progress`, `Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective` sections.

**Inference**

This is a strong example of keeping the trigger/entry contract minimal while placing durable methodology in one authoritative reference. A skill can be useful without scripts when its core value is an execution discipline rather than a tool wrapper.

**Not verified**

No real project was planned or implemented using the methodology in this batch, so effectiveness is not experimentally validated here.

## Individual skill artifacts

The 42 repository-scoped skill reports are stored in:

`research/agent-skills/batches/2026-08-07-batch-020-skill-reports.md`

Zero-skill repositories are intentionally absent from that file's skill-section count. They remain fully represented by the repository analysis above.

## Cross-repository findings

1. **Do not double-count registry/tooling repositories as skill collections.** A CLI that downloads `anthropics/skills` or a registry that packages arbitrary `SKILL.md` directories contributes tooling patterns but not repository-scoped skills.
2. **Repository names are not sufficient classification evidence.** `AnsonLai/AgentSkills.legal-Multi-Contract-Analyzer` uses “skills” internally but does not contain Agent Skills definitions.
3. **Progressive disclosure is strongest when implemented in code.** `phronetic-ai/agentskills` separates metadata discovery, full instruction loading, scripts, references, and assets in the SDK instead of relying only on prose conventions.
4. **Reference-first skills can reduce prompt bulk.** The `ora`, Editframe, and ExecPlan repositories keep some entry skills small and route detailed material to narrow references.
5. **Test/eval files are evidence of intended validation, not evidence of successful execution.** The Civitai smoke tests, SkillDock unit tests, and phronetic validation scripts were read but not run.
6. **Generated/copied/upstream skill surfaces must be separated from canonical local skill sources.** This avoids inflated counts and makes provenance review possible.

## Validation boundary

This batch is a **content/source deep analysis**. It read real repository files rather than relying on index metadata. It did **not** execute third-party installers, package managers, unit test suites, eval runners, API requests, model calls, browsers, media rendering, systemd services, security scanners, document-generation pipelines, or other external runtimes.

Accordingly, every repository completed in this batch is marked:

- `status: structure-reviewed`
- `runtime_validation: not_executed`

No repository is represented as runtime-validated merely because scripts, tests, or eval definitions exist.
