# Agent Skills Individual Reports — Batch 028

Batch: `2026-08-08-batch-028`  
Direct skill bodies reviewed: **27**  
Validation mode: source/content review only; runtime/build/evals were **not executed**.

## `RisorseArtificiali/agent-ready-skill`

Reviewed revision: `364fba90748b69379bb27b6fd05cff3dbda0ae2b` · observed stars: **8**.

### 1. `agent-ready`

- Path: `skills/agent-ready/SKILL.md`
- Role: router for `scan`, `fix`, `report`, `diff`, and `init`; parses targets and `--agents`, `--mode`, `--format`.
- Design: delegates scoring details to canonical `references/scoring.md`; supports portable posture and target-specific agent artifacts.
- Resources: scoring/remediation references plus seven signal scripts under the router package.
- Assessment: strong orchestration boundary and explicit source-of-truth references; duplicated quick-reference material still requires sync discipline.
- Status: source-reviewed; runtime not executed.

### 2. `agent-ready-scan`

- Path: `skills/agent-ready-scan/SKILL.md`
- Role: seven-dimension evidence scan for agentic-codebase readiness.
- Workflow: discover → optional read-only helper-script signals → score → persist → summarize.
- Evidence model: canonical 0/25/50/75/100 rubric with portable/target `na` handling and a v2 machine-readable schema.
- Assessment: notably careful about evidence, target-layer denominators and read-only script fallback. Results still depend on heuristic signal quality for some languages and artifacts.
- Status: source-reviewed; scan not executed.

### 3. `agent-ready-fix`

- Path: `skills/agent-ready-fix/SKILL.md`
- Role: remediate gaps from prior v2 scores.
- Safety/control: reads project context, prioritizes by impact, respects `fixable_by`, never overwrites existing files, and has an explicit confirmation gate before writes.
- Output scope: `AGENTS.md`, bridges, CI, pre-commit, execution policy, secret templates, specs/ADR, repo map and other scaffolds.
- Assessment: good separation between automatically fixable, partially fixable and manual work; brownfield behavior is safer than unconditional scaffolding.
- Status: source-reviewed; generation/re-scan not executed.

### 4. `agent-ready-report`

- Path: `skills/agent-ready-report/SKILL.md`
- Role: renderer for persisted v2 scores; explicitly does not re-score.
- Output: layered Markdown report, badge, optional self-contained HTML, per-subcriterion evidence and remediation.
- Assessment: clear ownership boundary between scan and render reduces score drift; report quality depends on correctness of persisted scan evidence.
- Status: source-reviewed; renderer not executed.

### 5. `agent-ready-diff`

- Path: `skills/agent-ready-diff/SKILL.md`
- Role: compare current v2 readiness state with a previous v2 baseline.
- Guard: refuses v1-to-v2 forced comparison; archives previous scores before fresh scan and reports dimension/layer deltas.
- Assessment: schema-version gate is a strong correctness feature and avoids invalid longitudinal comparisons.
- Status: source-reviewed; diff not executed.

### 6. `agent-ready-init`

- Path: `skills/agent-ready-init/SKILL.md`
- Role: greenfield-only minimal agent-ready scaffold.
- Guard: detects populated projects and defers them to scan/fix; creates only missing files and uses a confirmation gate.
- Assessment: useful separation from brownfield remediation; TODO placeholders are explicitly permitted only because greenfield commands may not yet exist.
- Status: source-reviewed; scaffold/quick scan not executed.

## `dglijin-oss/xuanji-five-skills`

Reviewed revision: `3f685a97b6ec634171394ec4823f70924983cb90` · observed stars: **7**.

### 7. `ze-ri-skill` (bundled collection copy)

- Path: `ze-ri-skill/SKILL.md`; implementation `ze-ri-skill/index.js`.
- Role: traditional date-selection guidance.
- Evidence: v1.0 skill text with implementation and testing still described as in-progress; referenced helper `jiechu.js` was not present at the pinned revision.
- Static issue: implementation contains full-width punctuation in JavaScript source, making the source suspect before runtime.
- Assessment: real skill artifact but implementation reliability is not established.
- Status: source-reviewed; runtime not executed.

### 8. `ziwei-skill` (bundled collection copy)

- Path: `ziwei-skill/SKILL.md`; implementation `ziwei-skill/index.js`.
- Role: 紫微斗数 chart/interpretation workflow.
- Evidence: v1.0 skill definition and compact JS implementation.
- Static issue: malformed/full-width punctuation tokens are visible in the implementation source.
- Assessment: declared workflow materially exceeds verified implementation quality.
- Status: source-reviewed; runtime not executed.

### 9. `taiyi-skill` (bundled collection copy)

- Path: `taiyi-skill/SKILL.md`; implementation `taiyi-skill/index.js`.
- Role: 太乙神数 calculation/interpretation.
- Evidence: v1.0 definition, compact JS implementation, validation not complete in skill text.
- Static issue: full-width punctuation appears inside JavaScript call syntax.
- Assessment: content is identifiable as a skill, but source requires correction before capability claims can be trusted.
- Status: source-reviewed; runtime not executed.

### 10. `fengshui-skill` (bundled collection copy)

- Path: `fengshui-skill/SKILL.md`; implementation `fengshui-skill/index.js`.
- Role: simplified 风水 direction/layout analysis.
- Evidence: implementation uses small hard-coded mappings and scoring heuristics.
- Assessment: more internally coherent than several sibling copies, but it remains a simplified implementation rather than evidence for a comprehensive domain engine.
- Status: source-reviewed; runtime not executed.

### 11. `liuren-skill` (bundled collection copy)

- Path: `liuren-skill/SKILL.md`; implementation `liuren-skill/index.js`.
- Role: 六壬 calculation/interpretation.
- Evidence: source explicitly uses simplified algorithms for major calculations.
- Assessment: skill metadata should be catalogued separately from implementation depth; no runtime validation was present.
- Status: source-reviewed; runtime not executed.

## `pinkpixel-dev/agentskills-mcp`

Reviewed revision: `808be83bf4344e4db532e1bb36da9811e7300194` · observed stars: **2**.

### 12. `code-documentation-doc-generate`

- Path: `.codex/skills/code-documentation-doc-generate/SKILL.md`.
- Role: generate API, architecture and user documentation from code.
- Design: compact main procedure with progressive-disclosure reference to `resources/implementation-playbook.md`.
- Safety: explicitly warns against exposing secrets/internal URLs.
- Assessment: focused and portable at the instruction level; actual accuracy validation is delegated to execution context.
- Status: source-reviewed; workflow not executed.

### 13. `project-setup`

- Path: `.codex/skills/project-setup/SKILL.md`.
- Role: scaffold VS Code extensions, Next.js, Vite, MCP server, Python scripts/packages.
- Integration: depends on named Copilot/VS Code tools such as `copilot_getVSCodeAPI`, `copilot_fetchWebPage`, and `copilot_runVscodeCommand`.
- Assessment: concrete scaffolding recipes, but portability is limited despite placement under `.codex/skills`; some instructions require live web/tool support.
- Status: source-reviewed; scaffolds not executed.

### 14. `skill-creator`

- Path: `.codex/skills/skill-creator/SKILL.md`.
- Role: create, validate, package and iterate Agent Skills with progressive disclosure.
- Scripts: `scripts/init_skill.py`, `scripts/quick_validate.py`, `scripts/package_skill.py` were inspected.
- Static finding: initializer help advertises a maximum skill-name length, but `quick_validate.py` does not enforce a length constraint. The packager docstring also retains an older `utils/package_skill.py` path.
- Assessment: strong resource model and reusable tooling, with small validator/documentation contract drift.
- Status: source-reviewed; scripts not executed.

### 15. `mcp-builder`

- Path: `.codex/skills/mcp-builder/SKILL.md`.
- Role: research, design, implement, review and evaluate MCP servers in Python or TypeScript.
- References: protocol/SDK guidance, language-specific implementation references and `reference/evaluation.md`.
- Eval design: the reference requires ten independent, read-only, stable, complex questions with single verifiable answers.
- Assessment: one of the stronger procedural packages in this batch; importantly, the presence of an eval guide is not an executed eval result.
- Status: source-reviewed; MCP build/eval not executed.

### 16. `web-design-review`

- Path: `.codex/skills/web-design-review/SKILL.md`.
- Role: browser-based visual inspection, source fixes, responsive/accessibility checks and re-verification.
- Required capabilities: browser navigation, screenshots, DOM access and source editing; Playwright MCP is given as a reference implementation.
- Control: minimal-change principle and a three-attempt iteration limit before consulting the user.
- Assessment: useful end-to-end verification loop when browser tooling exists; no browser behavior was exercised here.
- Status: source-reviewed; browser/runtime not executed.

## `dglijin-oss/fengshui-skill`

Reviewed revision: `7c84ed48ed4d97319d077f0678d494afa4e3646e` · observed stars: **4**.

### 17. `fengshui-skill`

- Path: `SKILL.md`; implementation `index.js`.
- Declared scope: v5.0.0 with 八宅, 玄空飞星, 二十四山向, 三元九运, 流年飞星, combined scoring and feedback.
- Implementation evidence: source header remains v1.1 with later v2.1/v2.2 helpers; later scoring/advice helpers appear after the export block and are not exported.
- Assessment: strong version/capability drift between SKILL and executable surface.
- Status: source-reviewed; runtime not executed.

## `dglijin-oss/liuren-skill`

Reviewed revision: `a3bbd3890bc9fc4c2fc97ab1d2e7a19a570c26db` · observed stars: **2**.

### 18. `liuren-skill`

- Path: `SKILL.md`; implementation `index.js`.
- Declared scope: v5 features including 金口诀, 天将 relationships, large 毕法赋/case resources and feedback.
- Implementation evidence: v1.1 header; month-general/time, four-lessons, three-transmissions and general placement are explicitly described as simplified.
- Assessment: implementation evidence is substantially narrower than the declared skill version.
- Status: source-reviewed; runtime not executed.

## `Willmo103/AgentSkillsBuilder`

Reviewed revision: `b43c9195880b287a646f23227ff6659c94e6ff9a` · observed stars: **0**.

### 19. `python-uv-scripting`

- Path: `python-uv-scripting/SKILL.md`.
- Metadata: version 2.0; optimized for pi-coding-agent and `uv`; target model field names `qwen:3.5:27b`.
- Workflow: create under `~/uv_scripts/`, initialize via `uv init --script`, add dependencies through `uv add --script`, preserve generated metadata by editing instead of replacing.
- Opinionated choice: Typer and Rich are required for CLI tools.
- Verification rule: run/test only when explicitly requested.
- Assessment: compact, deterministic workflow; repository has no root README at the pinned revision and no separate eval/reference package was verified.
- Status: source-reviewed; commands not executed.

## `dglijin-oss/ze-ri-skill`

Reviewed revision: `411081b9713ce541c081e81c71d4114705d95014` · observed stars: **0**.

### 20. `ze-ri-skill`

- Path: `SKILL.md`; implementation `index.js`.
- Declared scope: v5 通胜, annual date table, Bazi linkage, conflict resolution and feedback.
- Implementation evidence: simplified v1.1-era source.
- Static defect: `getYiJi()` returns `{ yi, ji }`, while consumers access `宜`/`忌`; downstream code calls `.includes` on `result.宜`.
- Assessment: concrete source-level contract mismatch plus large declared-version drift.
- Status: source-reviewed; defect not runtime-reproduced in this batch.

## `dglijin-oss/taiyi-skill`

Reviewed revision: `2aafc24a4c10397a3dc7c12e0acd7e918e4e04dd` · observed stars: **1**.

### 21. `taiyi-skill`

- Path: `SKILL.md`; implementation `index.js`.
- Declared scope: v5 fine-grained time calculation, historical-event library, 三式合参 and feedback.
- Implementation evidence: v1.1 header and simplified algorithms.
- Static concern: a call supplies numeric `6` where the callee's second parameter is treated as the yin/yang-dun selector; additional object/string assumptions warrant testing.
- Assessment: declared scope is not supported by the reviewed implementation evidence.
- Status: source-reviewed; runtime not executed.

## `dglijin-oss/ziwei-skill`

Reviewed revision: `2972be97eed709dc2487f1944e9d1b34ae59648b` · observed stars: **0**.

### 22. `ziwei-skill`

- Path: `SKILL.md`; implementation `index.js`.
- Declared scope: v5 flow-month/day, compatibility, 108 auxiliary stars and feedback.
- Documentation drift: README calls the implementation pure Python, but setup/usage uses Node and the API example uses CommonJS `require`.
- Implementation evidence: source header v1.1 and core algorithm explicitly marked simplified.
- Assessment: language documentation and capability-version contracts are both inconsistent.
- Status: source-reviewed; runtime not executed.

## `maeste/agent-ready-skill`

Reviewed revision: `71c2049ffeb0052719ffa6e6263909d714d0319a` · observed stars: **1**.

### 23. `agent-ready`

- Path: `skills/agent-ready/SKILL.md`.
- Role: router for scan/fix/report/diff.
- Model: eight dimensions; fixed 76-point agnostic and 24-point Claude-specific layers.
- Assessment: coherent v1 router, but less vendor-neutral than the later Risorse v2 evolution.
- Status: source-reviewed; not executed.

### 24. `agent-ready-scan`

- Path: `skills/agent-ready-scan/SKILL.md`.
- Role: eight-dimension discovery/scoring pipeline with filesystem searches and persistence to `claudedocs/`.
- Assessment: evidence-oriented for its version, but uses broad heuristics such as directory depth/naming consistency that the later v2 model explicitly moved away from.
- Status: source-reviewed; scan not executed.

### 25. `agent-ready-fix`

- Path: `skills/agent-ready-fix/SKILL.md`.
- Role: generate missing readiness artifacts after score analysis.
- Control: read project first, never overwrite, list proposed files and wait for confirmation.
- Assessment: useful confirmation gate; older design is Claude-first (`CLAUDE.md`, `.claude/settings.local.json`) and does not have the later v2 portable/remediation registry split.
- Status: source-reviewed; fixes not executed.

### 26. `agent-ready-report`

- Path: `skills/agent-ready-report/SKILL.md`.
- Role: detailed report under `claudedocs/`, including eight dimensions, two fixed layers and roadmap.
- Assessment: straightforward renderer, but model/version coupling to v1 means its reports are not directly comparable with v2 reports.
- Status: source-reviewed; report generation not executed.

### 27. `agent-ready-diff`

- Path: `skills/agent-ready-diff/SKILL.md`.
- Role: archive previous scores, rescan and compute per-dimension/overall deltas.
- Assessment: useful longitudinal workflow, but unlike later v2 it does not have an explicit schema-version compatibility gate.
- Status: source-reviewed; diff not executed.

## Batch-level report accounting

- Direct skill reports created here: **27**.
- No repository was marked complete from metadata alone.
- No repository was credited with runtime/build/eval success.
- Repositories with multiple distinct skill bodies received one repository-scoped report per reviewed skill body; content-level duplicates were not invented or inferred where the revisions were materially different.
