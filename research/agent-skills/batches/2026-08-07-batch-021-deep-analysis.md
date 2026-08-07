# GitHub Skills Catalog deep analysis — Batch 021

Observed: 2026-08-07

Status: `structure-reviewed`

Runtime validation: `not_executed`

## Scope and method

This batch continued from the existing indexed repository queue in `sources/catalog/batches/agentskills-pages-2-3.json`. Ten queued repositories were selected and analyzed at content level. Repository identity was verified through the GitHub repository API, Stars were checked from the latest public GitHub UI snapshot accessible during the run, and actual repository files were read before a repository was counted as structure-reviewed.

The review surface included, as applicable: repository structure, README, `SKILL.md` or equivalent specification/definition, supporting references, implementation scripts/code, and test/eval surfaces. Source/test presence is not treated as runtime success: no third-party CLI, installer, build, test suite, eval runner, browser, media renderer, service, database, or external API was executed.

Star counts are point-in-time UI observations. For sources whose public crawl was older than the run date, freshness is explicitly noted rather than presenting the value as a live API count.

## Batch result

| Repository | Star observation | Repository-scoped Skill reports | Content-level classification |
| --- | ---: | ---: | --- |
| `ersinkoc/project-architect` | 248 (GitHub UI, crawled today) | 1 | `single_skill_methodology_planning` |
| `zht043/AgentSkills` | 10 (GitHub UI snapshot, crawl ~2 months old) | 5 | `deprecated_skill_collection_legacy_workspace` |
| `armelhbobdad/bmad-module-skill-forge` | 91 (GitHub UI, crawled today) | 16 | `skill_collection_and_skill_tooling` |
| `tiangolo/agentskills` | 9 (latest accessible GitHub UI snapshot in this run, recent) | 0 | `specification_reference_sdk_fork` |
| `onmax/npm-agentskills` | 31 (GitHub UI, crawled today) | 0 | `skill_tooling_distribution_cli` |
| `netresearch/claude-code-marketplace` | 51 (GitHub UI, crawled today) | 0 | `marketplace_source_reference_catalog` |
| `agentsdance/agentskills` | 3 (GitHub UI snapshot, crawl ~2 months old) | 0 | `community_scaffold_template` |
| `yammaku/typewriter-video` | 39 (GitHub UI snapshot, crawl ~1 week old) | 1 | `single_skill_domain_package_video` |
| `sno-ai/mda` | 613 (GitHub UI snapshot, crawl ~3 days old) | 0 | `specification_compiler_tooling` |
| `opencrust-org/opencrust` | 142 (GitHub UI, crawled today) | 0 | `agent_runtime_skill_platform` |
| **Total** |  | **23** | **10 repositories** |

## Repository reports

### 1. `ersinkoc/project-architect`

**Identity / state verified**

- Public repository, default branch `main`; GitHub repository identity was read directly.
- GitHub page shows the repository root contains `SKILL.md`, `README.md`, `plugin.json`, and `references/`.
- Star observation: 248.

**Actual content read**

- README and repository root structure.
- Full `SKILL.md` body.
- `references/elicitation-guide.md`.

**Analysis**

This is a genuine single Skill, not a repository that merely contains the word "skills". Its principal artifact is a documentation-first project-planning workflow. The Skill deliberately stages discovery and produces interconnected planning artifacts rather than a single prose answer. The README and Skill agree on the main pipeline: specification → implementation plan → task breakdown → optional branding → synthesized execution prompt. Supporting references split elicitation, technology selection, design patterns, and output templates into on-demand context.

The useful engineering pattern is the separation of **question elicitation**, **decision support**, **artifact production**, and **human review gates**. `references/elicitation-guide.md` further prioritizes extracting what is already known before asking more questions and varies discovery depth by project complexity.

**Scripts / references / evals**

- References: present and directly sampled.
- Scripts: none observed in the reviewed root structure.
- Eval/test suite: none observed in reviewed paths.
- Runtime execution: not performed.

### 2. `zht043/AgentSkills`

**Identity / state verified**

- Public repository, default branch `main`.
- README explicitly labels the repository **Deprecated** and says major suites have been split into independent repositories.
- Star observation: 10 from the latest public GitHub snapshot accessible in this run; the page crawl is older (~2 months), so this is not claimed as a live API value.

**Actual content read**

- README.
- Root `SKILL.md` (`agent-skills`).
- `skill-creator/SKILL.md`.
- `skills/markdown-mermaid-illustrator/SKILL.md`.
- `skills/doc-illustrator/SKILL.md`.
- `skills/export-history/SKILL.md`.
- `skills/export-history/scripts/export-claude-history.mjs`.

**Analysis**

The repository is important mainly as a **migration/architecture case study**. Its README explains why the original monorepo was split: it mixed author workspace, index, and distribution responsibilities; contained a naming collision; assumed co-location between Skills; lacked independent installation; and lacked an eval/plugin distribution layer. The new intended direction is independent repositories with a portable core.

Five formal Skill definitions still physically exist and were reported, but they are not equivalent in current authority:

- root `agent-skills`: a legacy repository-level routing/read-depth instruction;
- `skill-creator`: legacy copy that README says moved to `agent-skill-architect`;
- `markdown-mermaid-illustrator`: current canonical residual, pending migration;
- `doc-illustrator`: legacy predecessor, pending archival;
- `export-history`: residual capability pending migration.

This prevents a common catalog error: treating every physically present definition as equally current. Authority/status is part of the analysis.

**Scripts / references / evals**

- `export-history` implementation script was directly read. It parses local JSONL session records and emits a self-contained HTML viewer.
- README explicitly says the old monorepo lacked an eval structure; no runtime eval was executed.

### 3. `armelhbobdad/bmad-module-skill-forge`

**Identity / state verified**

- Public repository, default branch `main`.
- Star observation: 91.

**Actual content read**

- Repository README and `src/README.md`.
- `src/skf-forger/SKILL.md`.
- `src/skf-create-skill/SKILL.md`.
- `src/skf-campaign/SKILL.md`.
- `src/skf-test-skill/SKILL.md`.
- Live search/path inventory for remaining `src/skf-*/SKILL.md` definitions and shared scripts.

**Content-level correction**

`src/README.md` states there are 14 workflow Skills plus the Ferris agent. The live source also contains `src/skf-campaign/SKILL.md`, which is a full formal workflow. Therefore the live repository contains **16 formal repository-scoped `SKILL.md` definitions** in the reviewed inventory: Ferris + 14 README-listed workflow Skills + Campaign.

This correction could not be obtained from the indexed queue or repository name.

**Analysis**

The strongest pattern is treating Skill authoring as a **provenance-backed production pipeline** rather than prompt writing. `skf-create-skill` requires source extraction, evidence, staged compilation, validation, and artifact generation. `skf-test-skill` defines stable result envelopes and exit codes so a scheduler can distinguish pass/fail/inconclusive/drift without scraping prose. `skf-campaign` adds file-backed resumable orchestration, dependency ordering, decision logging, and deterministic state validation for multi-session production.

The repository also contains deterministic shared helpers for package resolution, frontmatter validation, name rewriting, and trace checks. These were identified from actual paths; they were not executed.

**Scripts / references / evals**

- References/stage files: extensive and directly evidenced by the reviewed Skills.
- Scripts: deterministic shared scripts observed.
- Eval/test surface: `skf-test-skill` defines a concrete quality-gate workflow and external-validator stage.
- Execution: no SKF workflow, validator, or external test was run.

### 4. `tiangolo/agentskills`

**Identity / state verified**

- Public repository, default branch `main`; current repository metadata was read directly.
- The repository is a fork of the Agent Skills specification repository.
- Star observation: 9 from the latest accessible GitHub UI snapshot available in the run.

**Actual content read**

- README.
- `docs/specification.mdx`.

**Analysis**

This is not a local Skill collection. The README describes a **specification, documentation, and reference SDK**. Example Skill trees in the documentation demonstrate the format; they are not repository-scoped Skills to count.

The specification defines a required `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`; frontmatter requirements; progressive disclosure; relative file references; and validation with the reference tooling. Consequently this repository should be classified as a specification/reference implementation fork, not as a Skill collection.

**Scripts / references / evals**

- Specification/docs were directly read.
- No repository-scoped Skill report was created.
- Reference tooling was not executed.

### 5. `onmax/npm-agentskills`

**Identity / state verified**

- Public repository, default branch `main`.
- Star observation: 31.

**Actual content read**

- README.
- `package.json`.
- `test/scan.test.ts`.

**Analysis**

This repository is **distribution/discovery tooling**, not a local Skill collection. It lets npm packages declare agent capabilities/Skills and provides scanning/export behavior for target agent directories. The README documents package discovery, deduplication, target export, and manifest generation.

The repository has a real automated test surface: `test/scan.test.ts` uses Vitest fixtures to verify reading `agents.skills`, ignoring packages without the field, and supporting skills-only declarations. This test source was read, but not executed.

**Scripts / references / evals**

- CLI/build/test scripts are defined in `package.json`.
- Unit-test source directly reviewed.
- Runtime test command not executed.
- Local repository-scoped formal Skill count: 0.

### 6. `netresearch/claude-code-marketplace`

**Identity / state verified**

- Public repository, default branch `main`.
- Star observation: 51.

**Actual content read**

- README.
- `.claude-plugin/marketplace.json`.

**Analysis**

The critical finding is architectural: README explicitly says this marketplace uses **source references**. The repository's catalog points to separate Skill repositories and fetches them from those source repositories when installed. The `marketplace.json` entries confirm this with GitHub repository references and categories.

Therefore the roughly 40 cataloged Skills must **not** be duplicated as repository-scoped local Skill reports here. Counting them locally would double-count the same Skill when its source repository is later analyzed.

**Scripts / references / evals**

- Marketplace manifest directly read.
- Site/catalog architecture described in README.
- External Skill bodies were intentionally not treated as local content in this repository.
- Runtime installation not executed.

### 7. `agentsdance/agentskills`

**Identity / state verified**

- Public repository, default branch `master`.
- Star observation: 3 from an older (~2 month) public GitHub snapshot; identity/content were read from the current repository through GitHub access.

**Actual content read**

- README.
- `template/SKILL.md`.

**Analysis**

This is a **community contribution scaffold**, not a populated Skill collection in the verified content. README instructs contributors to create `skills/<name>/SKILL.md` and provides `template/SKILL.md`. The template uses placeholder name/description/instructions/examples and therefore is not counted as an actual repository-scoped Skill.

This is another important metadata correction: a repository named `agentskills` can still have zero real local Skills.

**Scripts / references / evals**

- No implementation/eval surface was identified in the reviewed files.
- Template intentionally excluded from Skill report count.

### 8. `yammaku/typewriter-video`

**Identity / state verified**

- Public repository, default branch `main`.
- Star observation: 39 from a GitHub UI snapshot crawled about one week ago.

**Actual content read**

- README.
- Full root `SKILL.md`.

**Analysis**

A genuine single domain Skill. It packages Remotion-based typewriter/video production knowledge, but deliberately distinguishes its own domain knowledge from the upstream general Remotion Skill. The Skill covers requirements, template setup, reading engine/reference files, content/timing authoring, aspect-ratio configuration, optional narration synchronization, preview, and render.

The repository demonstrates good progressive disclosure: API fields, content/storytelling guidance, audio behavior, and narration timing are split into dedicated reference files while the main Skill remains the operational entry point.

**Scripts / references / evals**

- Concrete TypeScript/Remotion source/template and reference paths are documented.
- No render/build/test was executed in this batch.
- Repository-scoped Skill count: 1.

### 9. `sno-ai/mda`

**Identity / state verified**

- Public repository, default branch `main`.
- Star observation: 613 from a GitHub UI snapshot crawled about three days ago.

**Actual content read**

- README.
- `scripts/validate-conformance.mjs`.

**Analysis**

MDA is a **document specification + compiler/tooling project**, not a local Skill collection. Its premise is one `.mda` source compiled into targets such as `SKILL.md`, `AGENTS.md`, `MCP-SERVER.md`, and `CLAUDE.md`, with structured metadata, relationships, integrity information, and signatures.

The README clearly separates shipped capabilities from future ecosystem work: schema/conformance/compiler exist; a bundled signature verifier, dependency resolver, central registry, graph indexer, and runtime routing ecosystem are not all shipped. This self-declared boundary was preserved instead of upgrading planned components to verified facts.

`validate-conformance.mjs` is real deterministic test infrastructure. The code loads JSON Schemas, validates manifest fixtures, performs strict frontmatter parsing, checks cross-field digest/signature consistency, and includes trusted-runtime policy checks.

**Scripts / references / evals**

- Conformance runner source directly read.
- Schemas/conformance architecture verified from README/source.
- Runner was not executed.
- Generated target examples are not counted as repository-scoped Skills.

### 10. `opencrust-org/opencrust`

**Identity / state verified**

- Public repository, default branch `main`.
- Star observation: 142.

**Actual content read**

- Repository README/root structure from GitHub.
- Search/path inventory under `crates/opencrust-skills`.
- `crates/opencrust-skills/src/parser.rs`.

**Analysis**

OpenCrust is an **agent runtime/platform with a Skill subsystem**, not a local Skill collection. Its README describes `SKILL.md` discovery, lifecycle/install/remove behavior, hot reload, and agentskills.io compatibility. The Rust implementation verifies this is not merely a README claim: the parser defines Skill frontmatter and validation behavior, and the skill crate also contains scanner/installer/runtime components.

`parser.rs` includes unit tests for valid and invalid parsing/validation cases. Test code was read, not run.

The correct catalog treatment is therefore runtime/tooling evidence with zero repository-scoped local Skill reports, avoiding the error of counting a runtime's support for Skills as if the runtime itself shipped a Skill catalog.

## Cross-repository findings

1. **Repository naming remains a weak signal.** `agentskills` may mean a specification fork, npm distribution tool, contribution scaffold, deprecated workspace, runtime subsystem, or real Skill collection.
2. **Authority and provenance matter.** The deprecated zht043 monorepo physically retains legacy definitions, but its README points users to split repositories. Physical presence alone is not enough to call an artifact current.
3. **Catalog references must not be double-counted.** Netresearch's marketplace explicitly references external repositories; its 40 entries are not 40 local Skill reports.
4. **README counts can drift.** BMAD's current source contains `skf-campaign` in addition to the 14 workflow Skills named by `src/README.md`, producing 16 formal definitions including Ferris.
5. **Deterministic validation surfaces are increasingly common.** BMAD, npm-agentskills, MDA, and OpenCrust all expose machine-checkable validation/test surfaces, but source inspection is distinct from executing those checks.

## Verification boundary

Verified in this batch:

- live GitHub repository identity/public state;
- latest accessible public GitHub star snapshot with freshness caveats where needed;
- actual README/specification/Skill/source/test files listed above;
- repository-level classifications and local-vs-external Skill counting decisions;
- 23 repository-scoped individual Skill reports.

Not verified by execution:

- dependency installation;
- builds;
- test suites / eval runners;
- external validators;
- browsers or rendered media;
- network services, databases, or APIs;
- installer/export behavior.

Accordingly all ten repositories are recorded as **`structure-reviewed`**, not runtime-validated.
