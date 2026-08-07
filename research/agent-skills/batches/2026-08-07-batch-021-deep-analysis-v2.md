# GitHub Skills Catalog deep analysis — Batch 021 (v2)

Observed: 2026-08-07

Status: `structure-reviewed`

Runtime validation: `not_executed`

This v2 report supersedes the first Batch 021 report after completing direct body review of every repository-scoped `SKILL.md` reported in the batch. The batch used the existing indexed repository queue and completed content-level review for **10 repositories**. Repository identity was verified through GitHub access; Stars were checked against the latest public GitHub UI snapshot accessible during the run, with freshness caveats where the UI snapshot was older than the run date.

## Result

| Repository | Star observation | Local Skill reports | Content-level classification |
| --- | ---: | ---: | --- |
| `ersinkoc/project-architect` | 248, GitHub UI crawled today | 1 | `single_skill_methodology_planning` |
| `zht043/AgentSkills` | 10, latest accessible UI snapshot ~2 months old | 5 | `deprecated_skill_collection_legacy_workspace` |
| `armelhbobdad/bmad-module-skill-forge` | 91, GitHub UI crawled today | 16 | `skill_collection_and_skill_tooling` |
| `tiangolo/agentskills` | 9, latest accessible recent UI snapshot | 0 | `specification_reference_sdk_fork` |
| `onmax/npm-agentskills` | 31, GitHub UI crawled today | 0 | `skill_tooling_distribution_cli` |
| `netresearch/claude-code-marketplace` | 51, GitHub UI crawled today | 0 | `marketplace_source_reference_catalog` |
| `agentsdance/agentskills` | 3, latest accessible UI snapshot ~2 months old | 0 | `community_scaffold_template` |
| `yammaku/typewriter-video` | 39, latest accessible UI snapshot ~1 week old | 1 | `single_skill_domain_package_video` |
| `sno-ai/mda` | 613, latest accessible UI snapshot ~3 days old | 0 | `specification_compiler_tooling` |
| `opencrust-org/opencrust` | 142, GitHub UI crawled today | 0 | `agent_runtime_skill_platform` |
| **Total** |  | **23** | **10 repositories** |

## 1. `ersinkoc/project-architect`

Actual content read: README/root structure, full root `SKILL.md`, and `references/elicitation-guide.md`.

This is a real single Skill. It converts structured discovery into interlinked specification, implementation, task, optional branding, and final prompt artifacts. References split elicitation, technical choice, design patterns, and output guidance into on-demand context. The strongest reusable pattern is separation of fact extraction/question elicitation from artifact production, with explicit review gates between major documents.

No repository-local runtime/eval execution was performed.

## 2. `zht043/AgentSkills`

Actual content read: README; root `SKILL.md`; `skill-creator/SKILL.md`; `skills/markdown-mermaid-illustrator/SKILL.md`; `skills/doc-illustrator/SKILL.md`; `skills/export-history/SKILL.md`; and `skills/export-history/scripts/export-claude-history.mjs`.

The repository is explicitly deprecated. Its README says the original monorepo mixed author workspace, index, and distribution responsibilities and that major suites were split into independent repositories. Five formal definitions remain physically present, but they have different authority: the root router and `skill-creator` are legacy; `markdown-mermaid-illustrator` is the canonical residual pending migration; `doc-illustrator` is a legacy predecessor; `export-history` remains pending migration.

The key catalog lesson is that physical presence does not imply current authority. The export-history implementation script was read but not executed.

## 3. `armelhbobdad/bmad-module-skill-forge`

Actual content read: repository README, `src/README.md`, and **all 16 observed formal Skill bodies**:

`skf-forger`, `skf-setup`, `skf-analyze-source`, `skf-brief-skill`, `skf-create-skill`, `skf-quick-skill`, `skf-create-stack-skill`, `skf-verify-stack`, `skf-refine-architecture`, `skf-update-skill`, `skf-audit-skill`, `skf-test-skill`, `skf-export-skill`, `skf-rename-skill`, `skf-drop-skill`, `skf-campaign`.

Content-level correction: `src/README.md` still describes Ferris plus 14 workflow Skills, but live source includes the additional formal `skf-campaign/SKILL.md`; therefore the observed formal corpus is **16**, not 15.

The repository treats Skill production as an evidence/provenance pipeline rather than prompt authoring. Direct body review verified patterns including tier-aware source analysis, narrow Skill scoping, provenance-backed creation, source-change surgical update, drift auditing, completeness gates, publishing as a separate gate, transactional rename, guarded drop, stack feasibility/refinement, and resumable multi-Skill campaign orchestration. The Skills repeatedly use stable result envelopes, exit codes, file-backed state, deterministic helpers, and explicit degraded/headless paths.

Shared helper/script paths for package resolution, frontmatter validation, naming, result envelopes, state/schema checks, and trace verification were observed. Neither those helpers nor SKF's test/eval workflows were executed.

## 4. `tiangolo/agentskills`

Actual content read: README and `docs/specification.mdx`.

This is a fork of the Agent Skills specification/documentation/reference SDK, not a repository-local Skill collection. The specification defines required `SKILL.md`, optional `scripts/`, `references/`, `assets/`, frontmatter requirements, progressive disclosure, relative references, and validation tooling. Documentation examples are examples, not local Skill reports.

Local Skill reports: 0. Reference tooling was not executed.

## 5. `onmax/npm-agentskills`

Actual content read: README, `package.json`, and `test/scan.test.ts`.

This is npm discovery/distribution tooling rather than a local Skill collection. It discovers declared `agents.skills` capabilities and exports/registers them for agent environments. A real Vitest test surface exists: the reviewed tests check packages with/without `agents` fields and skills-only declarations.

Local Skill reports: 0. Tests were read, not run.

## 6. `netresearch/claude-code-marketplace`

Actual content read: README and `.claude-plugin/marketplace.json`.

The repository explicitly uses **source references**. Its catalog entries point to independent GitHub Skill repositories and installation fetches from those sources. Therefore the roughly 40 catalog entries are not repository-local Skills and must not be duplicated here; each source repository should be analyzed independently.

Local Skill reports: 0. Marketplace installation was not executed.

## 7. `agentsdance/agentskills`

Actual content read: README and `template/SKILL.md`.

This is a community submission scaffold. The README describes the desired `skills/<name>/SKILL.md` layout, but the verified template is placeholder content (`my-skill-name`, generic instructions/examples), so it is not counted as a real local Skill.

Local Skill reports: 0.

## 8. `yammaku/typewriter-video`

Actual content read: README and complete root `SKILL.md`.

This is a genuine single domain Skill for Remotion-based typewriter/video B-roll. The workflow covers requirement gathering, template setup, engine/reference reading, content/timing authoring, aspect/layout configuration, optional narration synchronization, preview, and render. The repository uses progressive disclosure through dedicated API/content/audio/A-roll reference documents and intentionally distinguishes its domain knowledge from the upstream general Remotion Skill.

Local Skill reports: 1. npm install, preview, render, and media execution were not run.

## 9. `sno-ai/mda`

Actual content read: README and `scripts/validate-conformance.mjs`.

MDA is a document specification/compiler/tooling project. It defines one `.mda` source that can compile into targets including `SKILL.md`, `AGENTS.md`, `MCP-SERVER.md`, and `CLAUDE.md`, with schemas, relationships, integrity/signature metadata, and conformance rules. The README explicitly distinguishes shipped components from planned ecosystem work; those planned components were not promoted to verified facts.

The conformance runner is concrete code: it loads JSON Schemas, performs strict frontmatter parsing, validates manifest fixtures, checks digest/signature consistency, and applies trusted-runtime policy rules.

Local Skill reports: 0. The conformance runner was read, not executed.

## 10. `opencrust-org/opencrust`

Actual content read: repository README/root material, Skill subsystem paths, and `crates/opencrust-skills/src/parser.rs`.

OpenCrust is an agent runtime/platform with a Skill subsystem, not a local Skill catalog. The Rust parser implements `SKILL.md` frontmatter parsing/validation and includes unit tests for valid/invalid cases. Other observed Skill-subsystem paths include scanner and installer components.

Local Skill reports: 0. Rust tests/runtime were not executed.

## Cross-repository corrections and reusable findings

1. **Repository names are weak evidence.** An `agentskills` repository may be a specification fork, package manager/distribution tool, empty contribution scaffold, deprecated workspace, runtime subsystem, or actual Skill collection.
2. **Authority must be recorded separately from existence.** zht043's legacy definitions still exist but its README declares a split/migration; a catalog should preserve this status rather than treating every physical file as current.
3. **External catalogs must not inflate local counts.** Netresearch's marketplace references external source repositories; counting those entries locally would double-count them later.
4. **README inventories can drift from live source.** BMAD's source currently contains 16 formal definitions even though `src/README.md` describes Ferris plus 14 workflows.
5. **Templates/examples are not Skills.** `agentsdance`'s placeholder template and specification/generated examples in tooling/spec repos were deliberately excluded.
6. **Source-level test/eval evidence is not runtime validation.** BMAD, npm-agentskills, MDA, and OpenCrust all expose deterministic validation/test surfaces, but none was marked passed without execution.

## Verification boundary

Verified:
- 10 repository identities through GitHub access;
- Stars from the latest accessible GitHub UI snapshot, with freshness caveats;
- actual repository README/structure and relevant Skill/spec/tooling files;
- all **23 / 23** reported local `SKILL.md` bodies directly read;
- repository-level classification and local-vs-external counting decisions;
- scripts/references/tests/eval definitions where available and relevant.

Not runtime-verified:
- dependency installation;
- builds;
- test/eval runners;
- third-party validators;
- browsers/media rendering;
- services/databases/APIs;
- package/install/export behavior.

Accordingly Batch 021 completion means **content-level `structure-reviewed`**, not runtime-validated.
