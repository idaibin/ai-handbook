# Agent Skills Deep Analysis — Batch 028

- Batch ID: `2026-08-08-batch-028`
- Stage: repository deep analysis
- Queue source: `sources/catalog/batches/agentskills-created-2026-03-30-deterministic.json`
- Repositories completed: **10**
- Direct `SKILL.md` bodies reviewed: **27**
- Runtime/build/eval execution: **not_executed**

## Completion gate

A repository is counted in this batch only after repository identity and observed stars were verified, an exact revision was pinned, and actual repository contents were read. Metadata-only entries are not accepted as complete. Large candidates whose individual skills could not be fully reviewed in this run were left in the queue rather than being marked complete.

## Repository results

| Repository | ID | Stars observed | Reviewed revision | Indexed class | Content-proven class | Skill reports | Result |
|---|---:|---:|---|---|---|---:|---|
| `RisorseArtificiali/agent-ready-skill` | `1196375122` | 8 | `364fba90748b69379bb27b6fd05cff3dbda0ae2b` | single/domain package | skill collection | 6 | v2 agent-readiness suite with router, scan/fix/report/diff/init, canonical scoring/remediation references and seven read-only helper scripts |
| `dglijin-oss/xuanji-five-skills` | `1195918665` | 7 | `3f685a97b6ec634171394ec4823f70924983cb90` | skill collection | skill collection | 5 | five bundled metaphysics skills; documentation and implementation contain material drift and several source-level defects |
| `pinkpixel-dev/agentskills-mcp` | `1195679864` | 2 | `808be83bf4344e4db532e1bb36da9811e7300194` | skill tooling | skill tooling + local skill collection | 5 | FastMCP/Pydantic GitHub skill discovery/install server plus five local Codex skills, helper scripts and an MCP evaluation guide |
| `dglijin-oss/fengshui-skill` | `1195920040` | 4 | `7c84ed48ed4d97319d077f0678d494afa4e3646e` | single/domain package | single/domain package | 1 | SKILL claims v5 capability while source header/exports remain v1.x/v2.x-era; later helpers are not exported |
| `dglijin-oss/liuren-skill` | `1195920133` | 2 | `a3bbd3890bc9fc4c2fc97ab1d2e7a19a570c26db` | single/domain package | single/domain package | 1 | v5 SKILL claims substantially exceed the explicitly simplified v1.1 implementation surface |
| `Willmo103/AgentSkillsBuilder` | `1196541772` | 0 | `b43c9195880b287a646f23227ff6659c94e6ff9a` | skill tooling | single skill package | 1 | repository has no root README/SKILL at the reviewed revision; contains a focused `python-uv-scripting` skill |
| `dglijin-oss/ze-ri-skill` | `1195919542` | 0 | `411081b9713ce541c081e81c71d4114705d95014` | single/domain package | single/domain package | 1 | static contract bug between `{yi, ji}` return values and callers expecting Chinese-key properties; v5 claims not present in source |
| `dglijin-oss/taiyi-skill` | `1195919940` | 1 | `2aafc24a4c10397a3dc7c12e0acd7e918e4e04dd` | single/domain package | single/domain package | 1 | v5 SKILL substantially outpaces the simplified v1.1 implementation; additional source-level argument/type concerns identified |
| `dglijin-oss/ziwei-skill` | `1195919803` | 0 | `2972be97eed709dc2487f1944e9d1b34ae59648b` | single/domain package | single/domain package | 1 | README says pure Python but usage/source are JavaScript; v5 feature claims are not represented by the reviewed implementation |
| `maeste/agent-ready-skill` | `1196376579` | 1 | `71c2049ffeb0052719ffa6e6263909d714d0319a` | single/domain package | skill collection | 5 | older five-skill, eight-dimension v1 model; distinct from the later Risorse v2 branch and therefore not deduplicated |

## 1. `RisorseArtificiali/agent-ready-skill`

### Structure and design

The repository is a six-skill suite: `agent-ready` routes to `agent-ready-scan`, `agent-ready-fix`, `agent-ready-report`, `agent-ready-diff`, and `agent-ready-init`. The current model defines seven weighted dimensions (18/18/16/14/12/12/10) and separates portable signals from target-agent-specific signals. `.agent-ready/` is the vendor-neutral persistence directory.

The suite has two canonical references under `skills/agent-ready/references/`: `scoring.md` is the scoring/schema source of truth and `remediation.md` is keyed by the same subcriterion IDs with `why`, `consequence`, `fixable_by`, `fix_ref`, and `effort`. This is a useful explicit sync contract, but it also creates a maintenance obligation: duplicated quick-reference tables in README/router/scan must remain aligned with the canonical reference.

### Scripts inspected

Seven helper scripts are described by the suite. Source was inspected for the principal signal generators, including:

- `repo_map.py`: read-only symbol/import map; Python uses `ast.parse` without importing/executing target code, while other languages use explicitly lower-confidence regex heuristics; capped and token-budgeted.
- `file_metrics.py`: read-only LOC/language histogram and oversized-file detection, with file caps.
- `coverage_signals.py`: AST-based Python type/docstring signals and lower-confidence JS/TS regex signals.
- `secret_hygiene.py`: `.gitignore`/env-template checks plus deliberately limited high-confidence regex secret signals; source explicitly warns it is not a real secret scanner.
- `lockfile_check.py`: ecosystem lockfile detection plus best-effort `.gitignore` checks.
- `test_commands.py`: extracts, but explicitly never executes, test/build/lint commands.
- `instruction_audit.py`: instruction length, boilerplate, duplication and simple contradiction signals.

### Assessment

Strengths: clear separation between scoring, remediation, execution roles and rendering; portable-vs-target layering avoids penalizing projects for undeclared vendor artifacts; helper scripts are designed to be read-only and bounded; the `fix` and `init` skills include a confirmation gate before writes.

Risks/limitations: several signals are intentionally heuristic; `secret_hygiene.py` cannot replace a real secret scanner; non-Python semantic mapping and JS/TS coverage are explicitly lower confidence; scoring/reference duplication can drift. No dedicated executed eval/test result was verified in this run. Source presence is not treated as execution success.

## 2. `dglijin-oss/xuanji-five-skills`

The root README describes five OpenClaw AgentSkills: `ze-ri-skill`, `ziwei-skill`, `taiyi-skill`, `fengshui-skill`, and `liuren-skill`. Each reviewed package consists principally of `SKILL.md` plus `index.js`. All five SKILL bodies and all five implementation files were read.

The collection has material contract drift. The SKILL files describe ongoing or future validation and reference richer helper/module structures, but at least one referenced helper (`ze-ri-skill/jiechu.js`) is absent at the pinned revision. Three bundled implementations contain obvious source-level syntax defects involving full-width punctuation or malformed JavaScript tokens. The other implementations are explicitly simplified.

This repository is therefore retained as a real skill collection, but its skill metadata should not be interpreted as verified capability coverage.

## 3. `pinkpixel-dev/agentskills-mcp`

### MCP server

The project is a Python 3.11+ package using `mcp[cli]` and Pydantic v2. Its stdio server exposes five tools:

- `github_skills_list_repositories`
- `github_skills_search_skills`
- `github_skills_get_skill`
- `github_skills_install_skill`
- `github_skills_suggest_skill_scaffold`

The server has built-in curated repositories, strict Pydantic input models, a cached recursive GitHub tree, `SKILL.md` discovery, simple path/name token scoring, file retrieval and local installation. Tool annotations distinguish read-only/idempotent discovery from the writing install operation. Search ranking is intentionally simple and does not use semantic embeddings.

### Local skill layer

Five local `.codex/skills/*/SKILL.md` packages were identified and read: `code-documentation-doc-generate`, `project-setup`, `skill-creator`, `mcp-builder`, and `web-design-review`.

The `skill-creator` package contains `init_skill.py`, `quick_validate.py`, and `package_skill.py`. Static review found a small contract mismatch: initialization help advertises a maximum skill-name length, but `quick_validate.py` does not enforce that length. The packager docstring also uses an older `utils/package_skill.py` path while the file is stored under `scripts/`.

`mcp-builder` contains progressive-disclosure reference documents including an evaluation guide that specifies ten independent, read-only, stable, multi-step questions with verifiable answers. This is an eval **design guide**, not evidence that this repository's MCP server has passed such an evaluation.

`project-setup` depends on Copilot-specific tool names despite being stored under `.codex/skills`, reducing portability. `web-design-review` requires browser navigation/screenshots and a source-edit/reverify loop; those capabilities were not executed in this batch.

## 4. `dglijin-oss/fengshui-skill`

`SKILL.md` declares v5.0.0 and a broad feature set including 八宅, 玄空飞星, 二十四山向, 三元九运, 流年飞星, scoring and feedback. The implementation header remains v1.1 and contains later v2.1/v2.2 helper additions. Those later helpers are defined after the export block and are not exported through `module.exports` at the reviewed revision. This is a verified source-level version/contract drift; runtime behavior was not executed.

## 5. `dglijin-oss/liuren-skill`

`SKILL.md` declares v5-level capabilities such as 金口诀, a 天将 relationship network, a large 毕法赋 ruleset, case library and feedback. `index.js` identifies itself as v1.1 and repeatedly labels core calculations as simplified. Exported functionality is far narrower than the SKILL description, and the file terminates after a v2.1 evolution comment rather than implementing the v5 scope. Capability claims are therefore unverified beyond the source actually present.

## 6. `Willmo103/AgentSkillsBuilder`

The pinned revision has no root README or root SKILL. Repository search and direct reads identify `python-uv-scripting/SKILL.md`, a focused v2.0 skill for creating single-file Python scripts with `uv`, Typer and Rich. It mandates `uv init --script`, dependency management via `uv add --script`, editing rather than overwriting the generated metadata block, and only running/testing when explicitly requested. No separate eval/reference package was verified in this run.

## 7. `dglijin-oss/ze-ri-skill`

The v5 SKILL describes 通胜, annual auspicious-day tables, Bazi linkage, conflict handling and feedback. The reviewed implementation remains a simplified v1.1-era file. A concrete static contract defect exists: `getYiJi()` returns `{ yi, ji }`, while `zeRi()` reads properties named `宜` and `忌`; downstream `tuiJianJiRi()` calls `.includes` on `result.宜`. This is a source-level mismatch likely to break that path, but no runtime claim is made because execution was not performed.

## 8. `dglijin-oss/taiyi-skill`

The SKILL declares v5 features including fine-grained time calculation, historical-event library, 三式合参 and feedback. The source header is v1.1 and describes simplified algorithms. Static review also found suspicious call/type contracts, including a call that supplies a numeric second argument to a function whose second parameter is treated as a yin/yang-dun selector. These are source-level concerns, not executed test failures.

## 9. `dglijin-oss/ziwei-skill`

The v5 SKILL claims flow-month/day calculations, compatibility analysis, 108 auxiliary stars and feedback. The README simultaneously describes the implementation as pure Python while its own commands and API examples use `node index.js` and CommonJS `require`. The actual `index.js` header is v1.1 and labels the core arrangement algorithm simplified; the reviewed file does not implement the advertised v5 surface.

## 10. `maeste/agent-ready-skill`

This repository contains five skills: router, scan, fix, report and diff. It uses an older eight-dimension model and a fixed 76-point agnostic / 24-point Claude-specific split, with artifacts under `claudedocs/`. Its current README installation example points at the RisorseArtificiali repository rather than its own repository.

This is not an exact duplicate of the current Risorse content: the Risorse revision contains a later six-skill v2 architecture, seven dimensions, dynamic portable/target layers, helper scripts, remediation registry, `.agent-ready/`, and `init`. Both repositories therefore receive repository-scoped skill reports rather than being collapsed as mirrors.

## Cross-batch findings

1. **Index classification corrections are justified by content.** `RisorseArtificiali/agent-ready-skill` and `maeste/agent-ready-skill` were indexed as single/domain packages but are actual multi-skill collections. `Willmo103/AgentSkillsBuilder` is indexed as tooling but the pinned repository content is essentially one skill package. These are content-level corrections, not metadata guesses.
2. **Version claims need stronger catalog treatment.** Several dglijin SKILL files claim v5 while implementations remain v1.1/simplified or contain source defects. Catalog consumers should distinguish `declared_skill_version` from `implementation_evidence`.
3. **Eval/reference presence is not execution evidence.** Both agent-ready and MCP-builder repositories contain sophisticated validation/evaluation guidance, but this batch did not run those tools or observe passing test/eval outputs.
4. **Large collections remain gated.** High-volume repositories encountered in the queue were deliberately not counted when full individual-skill review could not be completed in this run.

## Validation status

- Repository identity: verified for all 10 selected repositories.
- Stars: point-in-time exact values verified for all 10 selected repositories.
- Exact revision: pinned for all 10.
- README/root docs: read where present; root absence recorded where verified.
- `SKILL.md`/equivalent definitions: 27 bodies directly reviewed.
- Scripts/references/eval material: read when materially present, including agent-ready helper scripts, scoring/remediation references, MCP server implementation, skill-creator scripts and MCP evaluation guidance.
- Runtime/build/tests/evals: **not_executed**. No source-only observation is promoted to runtime success.
