# GitHub Agent Skills Deep Analysis — Batch 010

## Run result

- Batch: `2026-08-07-batch-010`
- Repository completions: **10**
- Individual skill reports: **300**
- Completion basis: repository identity + displayed GitHub stars + actual repository content inspection; no repository was completed from metadata alone.
- Runtime validation: **not_executed**. Third-party scripts, installers, external services, browser flows, validators, and test commands were inspected where available but were not executed in this run.
- Queue snapshot used for reconciliation: `sources/catalog/github-agent-skills-index-latest.json`, observed `2026-08-07T11:21:21+08:00`, `2502` unique, `2088` deep-analysis eligible, `414` held.

This batch follows the schema-1.3 evidence rule used by the preceding runs: the immutable batch report is authoritative for repository-specific skill identities and evidence depth. Large collections use the repository's current maintained inventory to ensure every current skill receives an individual report, while body-level conclusions are limited to definitions or support files directly read in this batch. Inventory-only rows are labeled as such and are not represented as direct body reads.

## Repository summary

| Repository | GitHub repository ID | Default branch | Stars observed | Current skill reports | Direct content evidence |
| --- | ---: | --- | ---: | ---: | --- |
| `mar-antaya/my-claude-skills` | `1182785677` | `main` | 149 | 6 | README/current inventory; `pr-review-expert/SKILL.md`; `skill-security-auditor/SKILL.md`; scanner implementation/reference |
| `mrgoonie/claudekit-skills` | `1081645030` | `main` | 2.2k | 42 | Root README/current catalog; `context-engineering/SKILL.md`; `skill-creator/SKILL.md`; quick validator; marketplace/reference search |
| `msrv-tech/skills` | `1252004951` | `main` | 41 | 82 | `SKILLS_TABLE.md`; `codex-test-bridge/SKILL.md`; compiler/validator/reference search |
| `muratcankoylan/Agent-Skills-for-Context-Engineering` | `1120349776` | `main` | 17.6k | 17 | README/current 17-skill map; `context-fundamentals/SKILL.md`; researcher/evaluation surface |
| `nimrodfisher/data-analytics-skills` | `1131964042` | `main` | 346 | 31 | README/current 31-skill taxonomy; `programmatic-eda/SKILL.md`; repository `validate_skills.py`; structure/reference search |
| `NTCoding/claude-skillz` | `1096667452` | `main` | 331 | 16 | Current README `Available Skills`; `independent-research/SKILL.md`; repository search over skill/persona/plugin layers |
| `ognjengt/founder-skills` | `1148320602` | `main` | 258 | 15 | README/current Available Skills table; `strategic-planning/SKILL.md`; documented `FOUNDER_CONTEXT.md` and references-oriented package convention |
| `grp06/useful-codex-skills` | `1148255206` | `main` | 73 | 9 | README/current 9-skill inventory; `grillcraft/SKILL.md`; `publish.sh` symlink/publishing implementation |
| `aiskilloftheweek/claude-ai-skill-of-the-week` | `1182002141` | `main` | 96 | 14 | Current `skills/001`–`014` directory inventory; repository README; `014-mock-interview-simulator/SKILL.md` |
| `phuryn/pm-skills` | `1170266927` | `main` | 24.9k | 68 | README/current 68-skill, 42-workflow, 9-plugin inventory; `pm-execution/skills/create-prd/SKILL.md`; root `validate_plugins.py`; root test/CI surface |

Stars are observations from public GitHub repository pages during this run, not immutable repository properties.

---

## 1. `mar-antaya/my-claude-skills`

### Repository analysis

**Identity and structure.** Public, non-archived repository on `main`, organized as six top-level self-contained skill directories. The README is the current inventory authority.

**Direct content evidence.** `pr-review-expert` encodes a structured review pass around change impact, tests, security, compatibility, and performance. `skill-security-auditor` is backed by a real static Python scanner and references rather than prose alone.

**Quality / risk.** The strongest pattern is deterministic support code for repeated checks. The scanner is heuristic/pattern-based, so its PASS/WARN/FAIL result should be treated as triage rather than proof of safety; this run inspected the implementation but did not execute it.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `pr-review-expert` | direct body | Structured pull-request review workflow covering blast radius, tests, compatibility, security, and performance. |
| `skill-security-auditor` | direct body + script/reference | Static pre-install skill audit with a concrete scanner; useful as triage, not a substitute for sandboxed execution or human review. |
| `ci-cd-pipeline-builder` | README/current inventory | CI/CD pipeline construction workflow; body not directly read in this batch. |
| `dependency-auditor` | README/current inventory | Dependency-review workflow focused on package risk, freshness, and maintenance signals; body not directly read in this batch. |
| `performance-profiler` | README/current inventory | Performance investigation workflow for profiling and bottleneck identification; body not directly read in this batch. |
| `tech-debt-tracker` | README/current inventory | Technical-debt inventory and prioritization workflow; body not directly read in this batch. |

---

## 2. `mrgoonie/claudekit-skills`

### Repository analysis

**Identity and structure.** Public, non-archived repository on `main`. Skills live under `.claude/skills/` and are additionally packaged through plugin/marketplace metadata. The root README currently exposes 42 unique catalog entries; `context-engineering` is listed in two categories but counted once.

**Direct content evidence.** `context-engineering` uses a thin main body plus references/scripts for progressive disclosure. `skill-creator` explicitly prescribes `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`, with validation/testing expectations. Its `quick_validate.py` implements basic packaging/frontmatter/name checks.

**Quality / risk.** The repository has useful packaging and progressive-disclosure patterns, but some quantitative claims inside `context-engineering` are presented as fixed rules without evidence in the directly read body. The embedded `.claude/skills/README.md` also mirrors Anthropic example material and is not the repository's authoritative inventory, so this report uses the root catalog.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `better-auth` | README/current catalog | Current catalog entry for better auth; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `context-engineering` | direct body + referenced scripts | Context-engineering playbook using progressive disclosure, references, and analysis/compression helpers; several numeric heuristics should be independently validated. |
| `google-adk-python` | README/current catalog | Current catalog entry for google adk python; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `backend-development` | README/current catalog | Current catalog entry for backend development; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `ai-multimodal` | README/current catalog | Current catalog entry for ai multimodal; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `aesthetic` | README/current catalog | Current catalog entry for aesthetic; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `web-frameworks` | README/current catalog | Current catalog entry for web frameworks; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `ui-styling` | README/current catalog | Current catalog entry for ui styling; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `frontend-design` | README/current catalog | Current catalog entry for frontend design; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `frontend-development` | README/current catalog | Current catalog entry for frontend development; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `threejs` | README/current catalog | Current catalog entry for threejs; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `chrome-devtools` | README/current catalog | Current catalog entry for chrome devtools; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `web-testing` | README/current catalog | Current catalog entry for web testing; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `bunny` | README/current catalog | Current catalog entry for bunny; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `devops` | README/current catalog | Current catalog entry for devops; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `databases` | README/current catalog | Current catalog entry for databases; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `claude-code` | README/current catalog | Current catalog entry for claude code; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `mcp-builder` | README/current catalog | Current catalog entry for mcp builder; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `mcp-management` | README/current catalog | Current catalog entry for mcp management; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `repomix` | README/current catalog | Current catalog entry for repomix; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `media-processing` | README/current catalog | Current catalog entry for media processing; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `docs-seeker` | README/current catalog | Current catalog entry for docs seeker; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `code-review` | README/current catalog | Current catalog entry for code review; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `debugging/defense-in-depth` | README/current catalog | Current catalog entry for debugging/defense in depth; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `debugging/root-cause-tracing` | README/current catalog | Current catalog entry for debugging/root cause tracing; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `debugging/systematic-debugging` | README/current catalog | Current catalog entry for debugging/systematic debugging; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `debugging/verification-before-completion` | README/current catalog | Current catalog entry for debugging/verification before completion; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `document-skills/docx` | README/current catalog | Current catalog entry for document skills/docx; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `document-skills/pdf` | README/current catalog | Current catalog entry for document skills/pdf; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `document-skills/pptx` | README/current catalog | Current catalog entry for document skills/pptx; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `document-skills/xlsx` | README/current catalog | Current catalog entry for document skills/xlsx; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `shopify` | README/current catalog | Current catalog entry for shopify; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `payment-integration` | README/current catalog | Current catalog entry for payment integration; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `problem-solving/collision-zone-thinking` | README/current catalog | Current catalog entry for problem solving/collision zone thinking; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `problem-solving/inversion-exercise` | README/current catalog | Current catalog entry for problem solving/inversion exercise; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `problem-solving/meta-pattern-recognition` | README/current catalog | Current catalog entry for problem solving/meta pattern recognition; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `problem-solving/scale-game` | README/current catalog | Current catalog entry for problem solving/scale game; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `problem-solving/simplification-cascades` | README/current catalog | Current catalog entry for problem solving/simplification cascades; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `problem-solving/when-stuck` | README/current catalog | Current catalog entry for problem solving/when stuck; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `sequential-thinking` | README/current catalog | Current catalog entry for sequential thinking; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `mermaidjs-v11` | README/current catalog | Current catalog entry for mermaidjs v11; inventory-level role recorded from repository-maintained README/table. Body not directly read in this batch. |
| `skill-creator` | direct body + quick validator | Skill-authoring guidance centered on compact `SKILL.md`, progressive disclosure, bundled resources, deterministic scripts, and validation/testing expectations. |

---

## 3. `msrv-tech/skills`

### Repository analysis

**Identity and structure.** Public, non-archived repository on `main`. The repository-maintained `SKILLS_TABLE.md` is unusually useful: it declares a curated 82-skill set, provenance (`curated` vs `local`), file counts, and concise activation descriptions. Skills are top-level packages with `SKILL.md`, optional scripts and references.

**Direct content evidence.** `codex-test-bridge/SKILL.md` is not a prose-only wrapper: it documents a dedicated test-only extension, client, build helpers, and an explicit production-safety boundary. Search also confirms deterministic compiler/validator helpers and detailed references in several packages.

**Quality / risk.** The collection is cohesive around 1C development and favors XML/source-oriented deterministic tooling plus explicit validation. Some skills can modify local databases, web publication state, or generated configuration artifacts, so their safety depends on environment isolation and correct target selection. No external 1C/Apache/Playwright workflow was executed here.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `cf-add-object` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cf-edit` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cf-info` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cf-init` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cf-new-project` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cf-validate` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cfe-borrow` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cfe-diff` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cfe-full-cycle` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cfe-init` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cfe-patch-method` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `cfe-validate` | SKILLS_TABLE/current inventory | 1C configuration source workflow covering creation/edit/inspection/validation or extension lifecycle, per the curated repository table. |
| `db-create` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-dump-cf` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-dump-xml` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-list` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-load-cf` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-load-git` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-load-xml` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-run` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `db-update` | SKILLS_TABLE/current inventory | Database lifecycle wrapper for the local 1C environment; body not directly read in this batch. |
| `epf` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-bsp-add-command` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-bsp-init` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-build` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-dump` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-full-cycle` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-init` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `epf-validate` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `erf` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `erf-build` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `erf-dump` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `erf-init` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `erf-validate` | SKILLS_TABLE/current inventory | External processing/report artifact workflow covering source, build/dump, and validation tasks. |
| `form-add` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `form-compile` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `form-edit` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `form-info` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `form-patterns` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `form-remove` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `form-validate` | SKILLS_TABLE/current inventory | Managed-form source/compiler/inspection/validation workflow from the curated inventory. |
| `help-add` | SKILLS_TABLE/current inventory | Adds integrated help assets to supported 1C objects; body not directly read in this batch. |
| `ibcmd-1c-builds` | SKILLS_TABLE/current inventory | Local build/update workflow around ibcmd for configuration and extension artifacts. |
| `inspect` | SKILLS_TABLE/current inventory | Unified read-oriented inspection/router skill over several 1C source artifact types. |
| `interface-edit` | SKILLS_TABLE/current inventory | Command-interface editing workflow; body not directly read in this batch. |
| `interface-validate` | SKILLS_TABLE/current inventory | Command-interface validation workflow; body not directly read in this batch. |
| `meta-compile` | SKILLS_TABLE/current inventory | Metadata object source/compiler/inspection/validation workflow from the curated inventory. |
| `meta-edit` | SKILLS_TABLE/current inventory | Metadata object source/compiler/inspection/validation workflow from the curated inventory. |
| `meta-info` | SKILLS_TABLE/current inventory | Metadata object source/compiler/inspection/validation workflow from the curated inventory. |
| `meta-remove` | SKILLS_TABLE/current inventory | Metadata object source/compiler/inspection/validation workflow from the curated inventory. |
| `meta-validate` | SKILLS_TABLE/current inventory | Metadata object source/compiler/inspection/validation workflow from the curated inventory. |
| `mxl` | SKILLS_TABLE/current inventory | Tabular-document/template workflow covering compile/decompile/inspection/validation. |
| `mxl-compile` | SKILLS_TABLE/current inventory | Tabular-document/template workflow covering compile/decompile/inspection/validation. |
| `mxl-decompile` | SKILLS_TABLE/current inventory | Tabular-document/template workflow covering compile/decompile/inspection/validation. |
| `mxl-info` | SKILLS_TABLE/current inventory | Tabular-document/template workflow covering compile/decompile/inspection/validation. |
| `mxl-validate` | SKILLS_TABLE/current inventory | Tabular-document/template workflow covering compile/decompile/inspection/validation. |
| `playwright-test` | SKILLS_TABLE/current inventory | Browser-test scaffolding workflow for 1C web-client features; runtime not executed here. |
| `query-optimization` | SKILLS_TABLE/current inventory | Query-language composition and optimization guidance backed by repository references. |
| `role` | SKILLS_TABLE/current inventory | Role/permission source workflow covering creation, inspection, and validation. |
| `role-compile` | SKILLS_TABLE/current inventory | Role/permission source workflow covering creation, inspection, and validation. |
| `role-info` | SKILLS_TABLE/current inventory | Role/permission source workflow covering creation, inspection, and validation. |
| `role-validate` | SKILLS_TABLE/current inventory | Role/permission source workflow covering creation, inspection, and validation. |
| `skd-compile` | SKILLS_TABLE/current inventory | Data-composition schema workflow covering compile/decompile/edit/inspect/validate. |
| `skd-decompile` | SKILLS_TABLE/current inventory | Data-composition schema workflow covering compile/decompile/edit/inspect/validate. |
| `skd-edit` | SKILLS_TABLE/current inventory | Data-composition schema workflow covering compile/decompile/edit/inspect/validate. |
| `skd-info` | SKILLS_TABLE/current inventory | Data-composition schema workflow covering compile/decompile/edit/inspect/validate. |
| `skd-validate` | SKILLS_TABLE/current inventory | Data-composition schema workflow covering compile/decompile/edit/inspect/validate. |
| `subsystem` | SKILLS_TABLE/current inventory | Subsystem and command-interface workflow covering composition, editing, and validation. |
| `subsystem-compile` | SKILLS_TABLE/current inventory | Subsystem and command-interface workflow covering composition, editing, and validation. |
| `subsystem-edit` | SKILLS_TABLE/current inventory | Subsystem and command-interface workflow covering composition, editing, and validation. |
| `subsystem-info` | SKILLS_TABLE/current inventory | Subsystem and command-interface workflow covering composition, editing, and validation. |
| `subsystem-validate` | SKILLS_TABLE/current inventory | Subsystem and command-interface workflow covering composition, editing, and validation. |
| `template-add` | SKILLS_TABLE/current inventory | Template attachment workflow; body not directly read in this batch. |
| `template-remove` | SKILLS_TABLE/current inventory | Template removal workflow; body not directly read in this batch. |
| `validate` | SKILLS_TABLE/current inventory | Unified explicit validation router across supported 1C artifact types. |
| `web-info` | SKILLS_TABLE/current inventory | Web-environment status/inspection workflow; body not directly read in this batch. |
| `web-publish` | SKILLS_TABLE/current inventory | Web-publication workflow; environment-changing behavior requires isolated targets and was not executed here. |
| `web-session` | SKILLS_TABLE/current inventory | Web-client session automation wrapper; runtime not executed here. |
| `web-stop` | SKILLS_TABLE/current inventory | Web-server stop workflow; environment-changing behavior was not executed here. |
| `web-test` | SKILLS_TABLE/current inventory | Browser-based 1C web-client test workflow; runtime not executed here. |
| `web-unpublish` | SKILLS_TABLE/current inventory | Web-publication removal workflow; environment-changing behavior was not executed here. |
| `codex-test-bridge` | direct body | Test-only HTTP bridge for demo/test 1C environments, with explicit production-exclusion boundary and bundled client/build helpers. |

---

## 4. `muratcankoylan/Agent-Skills-for-Context-Engineering`

### Repository analysis

**Identity and structure.** Public, non-archived repository on `main`, with 17 skills under `skills/`, a root collection `SKILL.md`, template, examples, and a separate `researcher/` validation/research subsystem. The README explicitly says all 17 ship in one plugin.

**Direct content evidence.** `context-fundamentals` is a routing-aware conceptual skill: it defines its own boundary and forwards operational work to specialized siblings. It uses claim identifiers and references rather than pretending every heuristic is self-evident. The repository also exposes benchmark and activation-check scripts in the `researcher/` area.

**Quality / risk.** Strong points are responsibility boundaries, progressive disclosure, and the presence of a separate measurement/research surface. Some numeric heuristics in the body are still guidance rather than truths for every model/workload; downstream users should rely on the repository's own measurement philosophy and target-workload evals.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `context-fundamentals` | direct body | Conceptual foundation with explicit ownership boundaries and routing to operational context skills; uses referenced claim IDs for evidence-oriented guidance. |
| `context-degradation` | README/current skill map | Diagnoses context failure modes such as distraction, clash, poisoning, and lost-in-middle effects. Body not directly read in this batch. |
| `context-compression` | README/current skill map | Operational guidance for compacting long-running agent context while preserving important state. Body not directly read in this batch. |
| `context-optimization` | README/current skill map | Token-efficiency and context-selection tactics; body not directly read in this batch. |
| `latent-briefing` | README/current skill map | Briefing/context-transfer technique for compactly priming downstream work; body not directly read in this batch. |
| `multi-agent-patterns` | README/current skill map | Coordination patterns and context-isolation strategies for multi-agent work. Body not directly read in this batch. |
| `long-horizon-prompting` | README/current skill map | Guidance for prompts and state management across long-running tasks. Body not directly read in this batch. |
| `memory-systems` | README/current skill map | Memory architecture patterns for cross-session persistence and retrieval. Body not directly read in this batch. |
| `tool-design` | README/current skill map | Tool-surface and description-design guidance for agent usability. Body not directly read in this batch. |
| `filesystem-context` | README/current skill map | File-based offloading and durable scratchpad/context patterns. Body not directly read in this batch. |
| `hosted-agents` | README/current skill map | Hosted-agent operational architecture and lifecycle considerations. Body not directly read in this batch. |
| `evaluation` | README/current skill map | Agent-evaluation principles and measurement workflow. Body not directly read in this batch. |
| `advanced-evaluation` | README/current skill map | More advanced evaluation designs beyond basic scoring/LLM-as-judge patterns. Body not directly read in this batch. |
| `harness-engineering` | README/current skill map | Agent harness and environment engineering patterns. Body not directly read in this batch. |
| `self-improvement-loops` | README/current skill map | Controlled feedback/self-improvement loop design with measurement requirements. Body not directly read in this batch. |
| `project-development` | README/current skill map | Project-shaping workflow for LLM-powered systems and pipelines. Body not directly read in this batch. |
| `bdi-mental-states` | README/current skill map | Belief–desire–intention mental-state framing for agent reasoning. Body not directly read in this batch. |

---

## 5. `nimrodfisher/data-analytics-skills`

### Repository analysis

**Identity and structure.** Public repository ID `1131964042`, default branch `main`. The repository-maintained inventory contains 31 skills grouped into six lifecycle-oriented categories from data quality through workflow optimization. Each skill follows a common `SKILL.md` shape and may include scripts, references, or assets.

**Directly read evidence.** `01-data-quality-validation/programmatic-eda/SKILL.md` defines a real staged profiling workflow that delegates repeatable checks to scripts and records outputs in report artifacts. `validate_skills.py` was inspected and checks `SKILL.md` presence, YAML frontmatter, and four required sections across category directories.

**Quality signal.** The collection benefits from a consistent schema and a repository-level structural validator. The validator is deliberately shallow: it verifies packaging and required headings, not statistical correctness, script behavior, or the truth of analytical conclusions.

**Runtime boundary.** The validator and analysis scripts were not executed in this run; their presence and code intent are verified, not their passing state.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `programmatic-eda` | direct body + validator | Systematic dataset profiling pipeline with explicit scripts, thresholds, checklist, and report artifacts. |
| `data-quality-audit` | README/current 31-skill inventory | Data-quality review workflow for checking reliability and surfacing actionable defects. Body not directly read in this batch. |
| `query-validation` | README/current 31-skill inventory | Validation workflow for checking analytical query correctness before trusting results. Body not directly read in this batch. |
| `schema-mapper` | README/current 31-skill inventory | Maps data structures and relationships to make downstream analysis explicit. Body not directly read in this batch. |
| `metric-reconciliation` | README/current 31-skill inventory | Reconciles competing metric definitions or calculations to expose mismatches. Body not directly read in this batch. |
| `semantic-model-builder` | README/current 31-skill inventory | Builds a semantic layer so business terms and metrics have explicit definitions. Body not directly read in this batch. |
| `analysis-documentation` | README/current 31-skill inventory | Captures analytical methods, assumptions, and outputs in durable documentation. Body not directly read in this batch. |
| `data-catalog-entry` | README/current 31-skill inventory | Produces structured catalog documentation for analytical datasets or assets. Body not directly read in this batch. |
| `sql-to-business-logic` | README/current 31-skill inventory | Translates SQL behavior into explainable business rules and metric logic. Body not directly read in this batch. |
| `analysis-assumptions-log` | README/current 31-skill inventory | Maintains explicit assumptions so conclusions can be reviewed and invalidated. Body not directly read in this batch. |
| `cohort-analysis` | README/current 31-skill inventory | Guides cohort-based comparison and retention/adoption analysis. Body not directly read in this batch. |
| `segmentation-analysis` | README/current 31-skill inventory | Structures segmentation analysis around meaningful groups and behavioral differences. Body not directly read in this batch. |
| `funnel-analysis` | README/current 31-skill inventory | Analyzes stage-by-stage conversion and drop-off across a defined funnel. Body not directly read in this batch. |
| `time-series-analysis` | README/current 31-skill inventory | Structures temporal analysis around trend, change, and time-dependent patterns. Body not directly read in this batch. |
| `root-cause-investigation` | README/current 31-skill inventory | Evidence-oriented investigation workflow for explaining surprising analytical outcomes. Body not directly read in this batch. |
| `ab-test-analysis` | README/current 31-skill inventory | Guides controlled-experiment interpretation and decision framing. Body not directly read in this batch. |
| `business-metrics-calculator` | README/current 31-skill inventory | Calculates and interprets common business metrics from defined inputs. Body not directly read in this batch. |
| `insight-synthesis` | README/current 31-skill inventory | Synthesizes multiple analytical findings into a smaller set of decision-relevant insights. Body not directly read in this batch. |
| `visualization-builder` | README/current 31-skill inventory | Turns analytical results into purpose-driven visualizations. Body not directly read in this batch. |
| `executive-summary-generator` | README/current 31-skill inventory | Compresses analysis into decision-oriented executive summaries. Body not directly read in this batch. |
| `dashboard-specification` | README/current 31-skill inventory | Specifies dashboard purpose, metrics, views, and interaction requirements before implementation. Body not directly read in this batch. |
| `data-narrative-builder` | README/current 31-skill inventory | Builds a coherent evidence-backed narrative from analytical outputs. Body not directly read in this batch. |
| `technical-to-business-translator` | README/current 31-skill inventory | Translates technical analytical findings into business-language implications. Body not directly read in this batch. |
| `stakeholder-requirements-gathering` | README/current 31-skill inventory | Structures information gathering for analytical stakeholder needs. Body not directly read in this batch. |
| `analysis-qa-checklist` | README/current 31-skill inventory | Provides a repeatable QA gate for analytical work before delivery. Body not directly read in this batch. |
| `methodology-explainer` | README/current 31-skill inventory | Explains analytical methods, limitations, and interpretation for non-specialists. Body not directly read in this batch. |
| `impact-quantification` | README/current 31-skill inventory | Frames analytical findings in measurable business-impact terms. Body not directly read in this batch. |
| `analysis-planning` | README/current 31-skill inventory | Plans analytical work, scope, dependencies, and effort before execution. Body not directly read in this batch. |
| `context-packager` | README/current 31-skill inventory | Packages relevant analytical context for handoff or reuse. Body not directly read in this batch. |
| `peer-review-template` | README/current 31-skill inventory | Provides a consistent artifact for peer review of analytical work. Body not directly read in this batch. |
| `analysis-retrospective` | README/current 31-skill inventory | Captures what worked, failed, and should change after an analysis. Body not directly read in this batch. |

---

## 6. `NTCoding/claude-skillz`

### Repository analysis

**Identity and structure.** Public repository ID `1096667452`, default branch `main`. The repository mixes three distinct surfaces: 16 README-listed skills, a separate persona/system-prompt library, and plugins/launchers. This batch counts only the current `Available Skills` list rather than treating every prompt or legacy folder as an installable skill.

**Directly read evidence.** `independent-research/SKILL.md` explicitly distinguishes factual questions that should be resolved with tools/research from preference questions that require the user, and requires validation before presenting recommendations. README also documents launcher/persona composition and plugin layers.

**Quality signal.** The separation between reusable skills and composable personas is useful for reducing duplication. Some directives are intentionally very strong and assume particular tools/subagent capabilities, so portability depends on the host environment and those assumptions should not be treated as universal.

**Runtime boundary.** Launcher/plugin behavior and any referenced workflows were inspected through repository content but not executed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `independent-research` | direct body | Requires fact-finding and source/tool verification before recommendations, while reserving user questions for preferences or genuinely unavailable context. |
| `confidence-honesty` | README/current Available Skills | Encourages explicit confidence and uncertainty rather than presenting assumptions as facts. Body not directly read in this batch. |
| `concise-output` | README/current Available Skills | Defines a signal-dense communication style intended to remove redundant output. Body not directly read in this batch. |
| `critical-peer-personality` | README/current Available Skills | Provides a skeptical peer-review communication stance for challenging weak assumptions constructively. Body not directly read in this batch. |
| `questions-are-not-instructions` | README/current Available Skills | Separates literal questions from implied execution requests to reduce accidental action. Body not directly read in this batch. |
| `software-design-principles` | README/current Available Skills | Encodes reusable software-design heuristics for naming, coupling, cohesion, error handling, and object boundaries. Body not directly read in this batch. |
| `lightweight-implementation-analysis-protocol` | README/current Available Skills | Requires tracing relevant execution paths before implementing changes. Body not directly read in this batch. |
| `lightweight-design-analysis` | README/current Available Skills | Applies a repeatable multi-dimension design-review checklist before or during implementation. Body not directly read in this batch. |
| `tdd-process` | README/current Available Skills | Defines a strict red-green-refactor development state machine. Body not directly read in this batch. |
| `writing-tests` | README/current Available Skills | Provides test-design guidance, naming conventions, assertions, and edge-case coverage patterns. Body not directly read in this batch. |
| `observability-first-debugging` | README/current Available Skills | Prioritizes instrumentation and evidence collection before forming or acting on debugging hypotheses. Body not directly read in this batch. |
| `switch-persona` | README/current Available Skills | Supports controlled mid-session switching among repository-defined system-prompt personas. Body not directly read in this batch. |
| `lightweight-task-workflow` | README/current Available Skills | Tracks task state across sessions and constrains implicit state transitions. Body not directly read in this batch. |
| `create-tasks` | README/current Available Skills | Turns requirements into structured, implementation-oriented work items. Body not directly read in this batch. |
| `data-visualization` | README/current Available Skills | Covers chart selection, visual design, implementation, and perceptual considerations for data visualization. Body not directly read in this batch. |
| `typescript-backend-project-setup` | README/current Available Skills | Guides an opinionated TypeScript backend/Nx monorepo setup for AI-assisted development. Body not directly read in this batch. |

---

## 7. `ognjengt/founder-skills`

### Repository analysis

**Identity and structure.** Public repository ID `1148320602`, default branch `main`. The repository is a marketing/founder-oriented skill pack under `skills/`, with optional `references/` and a shared project-level `FOUNDER_CONTEXT.md` for reusable business context.

**Inventory drift.** The README headline says `20+` skills, but the current `Available Skills` table contains 15 named skills. This batch uses the concrete table as the canonical current inventory and records the marketing headline as documentation drift rather than inflating the count.

**Directly read evidence.** `skills/strategic-planning/SKILL.md` has explicit input-resolution and diagnostic logic, reuses `FOUNDER_CONTEXT.md`, asks for missing business facts only when needed, ranks three actions, and performs a self-check before output.

**Risk/limitation.** Several skills are recommendation/growth oriented. Their structure may be useful, but predicted commercial outcomes and confidence language are not empirical validation; later quality comparison should distinguish workflow discipline from evidence that a tactic works.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `sop-creator` | README/current Available Skills table | Turns a business process into a structured standard operating procedure. Body not directly read in this batch. |
| `cro-optimization` | README/current Available Skills table | Reviews landing-page conversion factors against a fixed optimization framework. Body not directly read in this batch. |
| `viral-hook-creator` | README/current Available Skills table | Generates candidate content hooks using repository-defined marketing patterns. Body not directly read in this batch. |
| `lead-magnet-generator` | README/current Available Skills table | Produces lead-magnet-oriented social content and calls to action from business context. Body not directly read in this batch. |
| `strategic-planning` | direct body | Reads available founder context, diagnoses missing inputs, and produces three ranked, resource-aware next moves. |
| `go-to-market-plan` | README/current Available Skills table | Structures go-to-market choices around product readiness, target customer, positioning, and distribution. Body not directly read in this batch. |
| `x-writer` | README/current Available Skills table | Generates X/Twitter post drafts using predefined format and voice patterns. Body not directly read in this batch. |
| `linkedin-writer` | README/current Available Skills table | Generates LinkedIn post drafts using predefined narrative/format patterns. Body not directly read in this batch. |
| `outreach-specialist` | README/current Available Skills table | Builds outreach-message sequences and follow-up structure for business development. Body not directly read in this batch. |
| `competitor-intel` | README/current Available Skills table | Structures competitor research into metrics, strategic differences, and implications. Body not directly read in this batch. |
| `brand-copywriter` | README/current Available Skills table | Applies common copywriting frameworks to marketing assets. Body not directly read in this batch. |
| `pricing-strategist` | README/current Available Skills table | Guides pricing analysis and tier design through interactive business-context gathering. Body not directly read in this batch. |
| `prd-generator` | README/current Available Skills table | Produces a product-requirements document intended for downstream AI-assisted development. Body not directly read in this batch. |
| `product-hunt-launch-plan` | README/current Available Skills table | Creates a launch checklist and sequencing plan for a Product Hunt-style launch. Body not directly read in this batch. |
| `marketing-ideas` | README/current Available Skills table | Selects marketing ideas from a repository-curated strategy set and adapts them to supplied context. Body not directly read in this batch. |

---

## 8. `grp06/useful-codex-skills`

### Repository analysis

**Identity and structure.** Public repository ID `1148255206`, default branch `main`. The live README lists nine skills: a planning/execution chain, goal support, strategic reorientation, and code-explanation workflow. A previous rough count of eight would have missed `explain-code-change`; this batch uses the current README and corrects the inventory to nine.

**Directly read evidence.** `grillcraft/SKILL.md` is a concrete compiler-like handoff: resolved intent becomes `.agent/work/<slug>/decision.md`, `meta.json`, `execplan.md`, then a goal drives implementation with explicit lifecycle state and validation conditions. `publish.sh` is a real distribution helper that moves or symlinks skill directories into the Codex skill home and has checks for naming, duplicates, and relinking.

**Quality signal.** The strongest pattern is provenance/state separation: confirmed decisions, assumptions, open questions, plan state, implementation state, and completion evidence have different artifacts instead of being collapsed into one prompt.

**Risk/limitation.** The workflow is tightly coupled to `.agent/` conventions, Codex goal semantics, and—only for `explain-code-change`—a connected Notion-style integration. Portability requires adapters rather than direct reuse.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `grill-me` | README/current 9-skill inventory | Pressure-tests a plan or design through a focused decision-oriented interview before execution. Body not directly read in this batch. |
| `grillcraft` | direct body + distribution script | Compiles resolved intent into durable decision metadata, an ExecPlan, improvement passes, and a goal-based execution handoff. |
| `execplan-create` | README/current 9-skill inventory | Creates an executable plan from an already-decided brief, RFC, PRD, or refactor. Body not directly read in this batch. |
| `execplan-improve` | README/current 9-skill inventory | Reads an existing plan and referenced code paths to make the plan more concrete and code-grounded. Body not directly read in this batch. |
| `implement-execplan` | README/current 9-skill inventory | Executes a work-item plan while maintaining explicit implementation state and validation evidence. Body not directly read in this batch. |
| `review-recent-work` | README/current 9-skill inventory | Performs a fresh review of recently implemented work and records corrections/results. Body not directly read in this batch. |
| `goalcraft` | README/current 9-skill inventory | Turns a rough task objective into a compact evidence-checked persistent Codex goal. Body not directly read in this batch. |
| `reorient-myself` | README/current 9-skill inventory | Audits a drifting task from first principles and produces a corrective prompt/objective. Body not directly read in this batch. |
| `explain-code-change` | README/current 9-skill inventory | Investigates a code change and publishes a verified learning-oriented explanation through its connected knowledge-workflow dependency. Body not directly read in this batch. |

---

## 9. `aiskilloftheweek/claude-ai-skill-of-the-week`

### Repository analysis

**Identity and structure.** Public repository ID `1182002141`, default branch `main`. The current `skills/` tree contains 14 sequentially numbered skill packages. The repository is primarily Markdown-instruction oriented rather than script-heavy.

**Directly read evidence.** `014-mock-interview-simulator/SKILL.md` defines a phased intake, one-question-at-a-time simulation, follow-up rules, and structured per-answer or end-of-session feedback. The design is operationally specific enough to reproduce a consistent practice flow.

**Quality signal.** Numbered packaging makes publication history easy to inspect, and the individual packages target narrow workflows rather than a single oversized instruction file.

**Risk/limitation.** Claims about realism or predictive value should not be treated as validated hiring outcomes without empirical evaluation. No repository-level deterministic eval/test harness was observed for the current Markdown skills in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `001-email-subject-line-optimizer` | current skills directory/README inventory | Generates and evaluates email subject-line candidates using a focused optimization workflow. Body not directly read in this batch. |
| `002-substack-note-generator` | current skills directory/README inventory | Creates Substack-note drafts from supplied ideas or source material. Body not directly read in this batch. |
| `003-personal-mba-generator` | current skills directory/README inventory | Structures a self-directed learning plan around a user-selected business topic. Body not directly read in this batch. |
| `004-linkedin-hook-generator` | current skills directory/README inventory | Generates opening hooks for LinkedIn posts using repository-defined patterns. Body not directly read in this batch. |
| `005-idea-extractor` | current skills directory/README inventory | Extracts reusable ideas from supplied source material. Body not directly read in this batch. |
| `006-growth-idea-action-plan` | current skills directory/README inventory | Converts a growth idea into a more explicit action plan. Body not directly read in this batch. |
| `007-content-mine` | current skills directory/README inventory | Mines source material for reusable content opportunities. Body not directly read in this batch. |
| `008-sop-writer` | current skills directory/README inventory | Turns a process into an SOP-style document. Body not directly read in this batch. |
| `009-substack-aeo-geo-optimizer` | current skills directory/README inventory | Optimizes Substack-oriented content for answer/generative-engine discoverability using the skill's heuristics. Body not directly read in this batch. |
| `010-honest-thinking-partner` | current skills directory/README inventory | Provides a challenging reasoning partner intended to surface weak assumptions. Body not directly read in this batch. |
| `011-ai-standup` | current skills directory/README inventory | Structures an AI-assisted standup/status update workflow. Body not directly read in this batch. |
| `012-cold-outreach-personalizer` | current skills directory/README inventory | Personalizes outreach drafts using supplied recipient/business context. Body not directly read in this batch. |
| `013-humanaizer` | current skills directory/README inventory | Rewrites text toward the repository's more natural-language style target; folder name is spelled `humanaizer` in the current tree. Body not directly read in this batch. |
| `014-mock-interview-simulator` | direct body | Runs a staged interview-practice workflow with intake, one-question-at-a-time simulation, and structured feedback. |

---

## 10. `phuryn/pm-skills`

### Repository analysis

**Identity and structure.** Public repository ID `1170266927`, default branch `main`. The current README consistently reports 68 skills and 42 chained workflows across nine plugins spanning discovery, strategy, execution, research, analytics, go-to-market, growth, utilities, and AI-shipping review.

**Directly read evidence.** `pm-execution/skills/create-prd/SKILL.md` defines a concrete eight-section requirements workflow with explicit problem, objective, segment, value, solution, assumptions, and release sections. `validate_plugins.py` was inspected: it validates plugin manifests, skill/command frontmatter, directory/name agreement, command-to-skill references, and README expectations. The repository also exposes tests and CI configuration, but those were not executed in this run.

**Architecture.** Skills are reusable building blocks; slash-command workflows compose multiple skills; plugins are the distribution boundary. This separates domain knowledge from orchestration better than repositories that duplicate full workflows inside each command.

**Runtime boundary.** The validator/tests were inspected but not run. Legal-oriented drafting skills are recorded as drafting workflows, not as proof of legal correctness.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `brainstorm-ideas-existing` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `brainstorm-ideas-existing`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `brainstorm-ideas-new` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `brainstorm-ideas-new`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `brainstorm-experiments-existing` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `brainstorm-experiments-existing`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `brainstorm-experiments-new` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `brainstorm-experiments-new`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `identify-assumptions-existing` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `identify-assumptions-existing`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `identify-assumptions-new` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `identify-assumptions-new`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `prioritize-assumptions` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `prioritize-assumptions`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `prioritize-features` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `prioritize-features`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `analyze-feature-requests` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `analyze-feature-requests`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `opportunity-solution-tree` | README/current 68-skill inventory | Builds a Teresa Torres-style outcome → opportunity → solution → experiment tree. Body not directly read in this batch. |
| `interview-script` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `interview-script`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `summarize-interview` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `summarize-interview`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `metrics-dashboard` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `metrics-dashboard`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `product-strategy` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `product-strategy`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `startup-canvas` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `startup-canvas`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `product-vision` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `product-vision`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `value-proposition` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `value-proposition`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `lean-canvas` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `lean-canvas`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `business-model` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `business-model`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `monetization-strategy` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `monetization-strategy`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `pricing-strategy` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `pricing-strategy`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `swot-analysis` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `swot-analysis`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `pestle-analysis` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `pestle-analysis`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `porters-five-forces` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `porters-five-forces`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `ansoff-matrix` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `ansoff-matrix`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `create-prd` | direct body + validator | Uses an eight-section PRD workflow covering problem/background, objectives, market, value proposition, solution, assumptions, and release framing. |
| `brainstorm-okrs` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `brainstorm-okrs`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `outcome-roadmap` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `outcome-roadmap`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `sprint-plan` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `sprint-plan`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `retro` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `retro`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `release-notes` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `release-notes`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `pre-mortem` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `pre-mortem`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `stakeholder-map` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `stakeholder-map`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `summarize-meeting` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `summarize-meeting`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `user-stories` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `user-stories`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `job-stories` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `job-stories`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `wwas` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `wwas`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `test-scenarios` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `test-scenarios`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `dummy-dataset` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `dummy-dataset`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `prioritization-frameworks` | README/current 68-skill inventory | Reference skill covering multiple prioritization methods and their decision contexts. Body not directly read in this batch. |
| `strategy-red-team` | README/current 68-skill inventory | Adversarially stress-tests a strategy or requirements artifact by surfacing load-bearing assumptions and cheaper falsification tests. Body not directly read in this batch. |
| `user-personas` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `user-personas`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `market-segments` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `market-segments`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `user-segmentation` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `user-segmentation`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `customer-journey-map` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `customer-journey-map`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `market-sizing` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `market-sizing`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `competitor-analysis` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `competitor-analysis`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `sentiment-analysis` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `sentiment-analysis`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `sql-queries` | README/current 68-skill inventory | Generates analytical SQL from natural-language requirements across supported dialects. Body not directly read in this batch. |
| `cohort-analysis` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `cohort-analysis`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `ab-test-analysis` | README/current 68-skill inventory | Structures experiment-result analysis around statistical evidence, adequacy, and a decision recommendation. Body not directly read in this batch. |
| `gtm-strategy` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `gtm-strategy`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `beachhead-segment` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `beachhead-segment`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `ideal-customer-profile` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `ideal-customer-profile`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `growth-loops` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `growth-loops`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `gtm-motions` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `gtm-motions`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `competitive-battlecard` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `competitive-battlecard`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `marketing-ideas` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `marketing-ideas`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `positioning-ideas` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `positioning-ideas`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `value-prop-statements` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `value-prop-statements`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `product-name` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `product-name`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `north-star-metric` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `north-star-metric`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `review-resume` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `review-resume`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `draft-nda` | README/current 68-skill inventory | Provides a structured drafting workflow for an NDA; it should be treated as document assistance, not professional legal advice. Body not directly read in this batch. |
| `privacy-policy` | README/current 68-skill inventory | Provides a structured privacy-policy drafting workflow; legal/compliance correctness still requires jurisdiction-specific review. Body not directly read in this batch. |
| `grammar-check` | README/current 68-skill inventory | Repository-defined PM workflow/reference for `grammar-check`, grouped into one of the nine installable product-management plugins. Body not directly read in this batch. |
| `shipping-artifacts` | README/current 68-skill inventory | Defines a durable documentation set that makes an AI-built application reviewable across architecture, permissions, secrets/configuration, and test coverage. Body not directly read in this batch. |
| `intended-vs-implemented` | README/current 68-skill inventory | Compares documented intent with code evidence to identify mismatches rather than trusting either source alone. Body not directly read in this batch. |
