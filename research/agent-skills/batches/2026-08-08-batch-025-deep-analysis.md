# GitHub Skills Catalog Deep Analysis — Batch 025

Observed: 2026-08-08

## Scope and verification method

This batch deep-analyzed 10 repositories from the persisted indexed repository queue. Repository identity was verified against GitHub repository search, and star counts were verified with owner/name-scoped exact `stars:N` queries rather than copied from prior index metadata. Actual repository contents were read before any repository was marked reviewed: README or equivalent documentation, current skill definitions or project-specific equivalents, scripts, references, and evaluation/test surfaces when present.

No third-party repository scripts, installers, tests, or evals were executed in this batch. `runtime_validation` therefore remains `not_executed`. Repository-authored test claims or test-report files are treated as source evidence only, not as validation performed by this catalog run.

Content-level duplicate/fork detection is part of deep analysis. A repository can therefore be fully content-reviewed yet reclassified as a duplicate or reference-only artifact rather than retained as a unique skill collection.

## Batch summary

| Repository | Stars | Content-level result | Skill/equivalent reports | Catalog action |
|---|---:|---|---:|---|
| `me-pankajmunde/AgentSkills` | 0 | skill collection | 2 | keep as unique collection |
| `shitikovAlexander/AgentSkills` | 0 | single project-specific skill | 1 | keep as unique equivalent skill |
| `ColonelDarcy2018/agentSkills` | 0 | mixed skill collection with imported system skills | 9 | keep local skills; record imported provenance |
| `JiinGalaxy/AgentSkills` | 0 | project-specific skill/agent collection | 10 | keep with portability caveat |
| `Guikingone/php-agent-skills` | 3 | Agent Skills runtime/tooling | 0 | keep as tooling, not skill pack |
| `davila7/agentskills` | 4 | specification + reference SDK snapshot | 0 | reference-only; dedupe from unique skill queue |
| `AsherBond/agentskills` | 0 | synchronized official-spec mirror/fork | 0 | dedupe/hold |
| `devops2626/agentskills` | 2 | frozen official-spec mirror/fork | 0 | dedupe/hold |
| `danielbodnar/agentskills` | 2 | frozen official-spec mirror/fork | 0 | dedupe/hold |
| `XiaoZhengTou/agentSkills` | 1 | multi-agent development skill workflow | 24 | keep as unique collection |

**Batch result:** 10 repositories content-reviewed; 46 individual skill/equivalent definitions directly reviewed. The prior canonical eligible basis is intentionally not rewritten inside this batch; duplicate/reference corrections should be applied by catalog reconciliation rather than silently changing the historical basis.

---

## 1. `me-pankajmunde/AgentSkills`

### Verified identity

- GitHub repository ID: `1207029994`
- Default branch: `main`
- Stars: **0**, verified with an exact owner/name + `stars:0` repository query.
- Current repository is public and not archived.

### README and structure

The root `README.md` is empty, so repository-level discoverability and usage guidance are effectively absent. Actual content inspection shows two large Agent Skills packages:

- `copilot-sdk/SKILL.md`
- `google-adk-skill/SKILL.md`
- `google-adk-skill/templates.md`

The latest observed content commit was `acc11be629ffd58aa72ebb921cead21e265ee59b`.

### Skill findings

`copilot-sdk` is a broad GitHub Copilot SDK application-development guide spanning TypeScript, Python, Go, and .NET, including sessions, streaming, tools, MCP, and custom agents. Its main `SKILL.md` is about 900 lines, so most of its domain detail is loaded at activation rather than progressively disclosed. Several examples use an approve-all permission handler; that is useful as a quick-start illustration but is too permissive to treat as a production-safe default.

`adk-agent-builder` is an even broader Google Agent Development Kit guide covering project scaffolding, tools, multi-agent orchestration, callbacks/guardrails, state, deployment, MCP/A2A, and multiple implementation languages. It splits some reusable material into `templates.md`, but the main skill remains roughly 950 lines and therefore has a high activation-time context cost.

### Scripts, references, evals

No dedicated eval suite or bundled executable script set was observed for these two skill packages in the inspected current content. `templates.md` is the primary separated supporting resource.

### Verdict

A real two-skill collection with useful breadth, but weak repository documentation and oversized main skill bodies. Keep as a unique collection; recommend future modularization rather than treating the current files as progressive-disclosure exemplars.

---

## 2. `shitikovAlexander/AgentSkills`

### Verified identity

- GitHub repository ID: `1192041092`
- Default branch: `main`
- Stars: **0**, exact GitHub query verified.
- Latest observed commit: `08c81e5a0d7cc80b2ba84d20eaaff2b113664200`.

### README and structure

The root README contains only the repository title, so the actual skill intent must be recovered from repository content. The significant skill-equivalent artifact is:

- `AgentDesk/agentdesk-workflow-designer.md`

The repository also contains project material under `Curb/`; that content was not counted as an Agent Skill.

### Skill findings

`agentdesk-workflow-designer.md` is a project-specific workflow-design skill rather than a canonical `SKILL.md` package. It documents AgentDesk provider choices, agent fields, skill injection, directed-graph workflow positions, connection pass types, pipeline/orchestrator/shared-memory patterns, input resolution, layered prompt construction, limitations, and a concrete output contract for workflow proposals.

The strongest aspect is its explicit graph and interface contract: the agent is told exactly how to select topology, provider, model, inputs, and output shape. The main weaknesses are platform coupling and reliability gaps acknowledged in the document itself: JSON output is not validated/retried and a workflow stops on the first agent failure. The architecture notes also contain a very broad permission-bypass execution mode; it should be treated as a risk to isolate rather than a reusable safety default.

### Scripts, references, evals

No dedicated scripts, references, or eval suite associated with this skill-equivalent were observed.

### Verdict

A unique, single, project-specific workflow-design skill. Keep as an equivalent-skill example, with clear portability and safety caveats.

---

## 3. `ColonelDarcy2018/agentSkills`

### Verified identity

- GitHub repository ID: `1129469948`
- Default branch: `main`
- Stars: **0**, exact GitHub query verified.
- Observed repository commit: `e516018beb5a590c41da41040390b644ce46f2c2`.
- Root `README.md` is absent.

### Structure and provenance

This repository mixes imported/system skills with locally authored KCOS-oriented skills. That distinction matters for catalog originality.

Imported/system packages inspected:

- `.system/skill-creator/SKILL.md`
- `.system/skill-installer/SKILL.md`

The skill-creator package includes `agents/openai.yaml`, `references/openai_yaml.md`, initialization/generation/validation scripts, and creation guidance. The installer package includes GitHub-oriented installer helpers. These appear to be imported system tooling and should not be credited as original repository skill design.

Local or repository-specific definitions inspected:

- `game-requirement-innovation/SKILL.md`
- `kcos-protocol-bootstrap/SKILL.md`
- `mobile-rpa-script-dev/SKILL.md`
- `上下文管理/SKILL.md`
- `业务逻辑图谱/SKILL.md`
- `代码审查/SKILL.md`
- `任务分解/SKILL.md`

### Skill design findings

The local KCOS skills have better responsibility boundaries than the repository-level packaging suggests. Several definitions explicitly state both trigger and non-trigger conditions, which reduces routing ambiguity. `业务逻辑图谱` and `任务分解` also define how they cooperate rather than duplicating one another.

`kcos-protocol-bootstrap` has meaningful executable/supporting structure, including protocol assets and scripts such as `init_kcos_protocol.py` and `kcos_p0.py`. `mobile-rpa-script-dev` is reference-heavy and contains a dedicated helper script, showing a more progressive-disclosure-oriented shape than a single giant prompt.

The primary catalog concern is provenance mixing: imported system skills and original local skills sit in one repository without a root README explaining ownership or reuse boundaries.

### Scripts, references, evals

Observed support includes skill-creator generation/validation scripts, installer scripts, KCOS initialization/sync code, mobile-RPA references and a document-splitting helper, and multiple requirement-innovation references. No repository-wide runtime/eval execution was performed in this batch.

### Verdict

A real mixed collection. Keep the seven local/project-specific skills as unique catalog material; record the two `.system` skills as imported provenance rather than unique inventions. Nine individual reports are retained because they were directly inspected, but provenance is explicit.

---

## 4. `JiinGalaxy/AgentSkills`

### Verified identity

- GitHub repository ID: `1172397516`
- Default branch: `main`
- Stars: **0**, exact GitHub query verified.
- Repository size is large (`197714` in the indexed GitHub snapshot), driven in part by assets and generated/reference material.
- Observed content commit: `def93ca5e371cf8d28ae7345f4349ea2ee23c2e3`.

### Structure

This is an integrated, organization/domain-specific product workflow rather than a portable standards-oriented skill library. Ten skill/equivalent definitions were directly reviewed:

- `DemoMaking/demo_making_skill.md`
- `HiveAgents/demo_developer_agent.md`
- `HiveAgents/market_insight_agent.md`
- `HiveAgents/prd_writer_agent.md`
- `HiveAgents/prototype_designer_agent.md`
- `HiveCommander/hive_commander.md`
- `LarkDocWriting/lark_doc_skill.md`
- `PRDWriting/prd_write_skill.md`
- `ProductPlan/product_plan.md`
- `WarningAnalyze/warning_analyze_skill.md`

The repository also contains a shared `common/` configuration layer and a separate Claude agent definition (`.claude/agents/sebu-prd-writer.md`), which was not double-counted as a skill.

### Skill design findings

The strongest pattern is workflow integration: product planning, PRD creation, prototype/demo creation, and commander/worker roles are connected to concrete internal references and assets. `PRDWriting` is especially resource-rich, including database relation assets, a PRD template, schema/diagram extraction utilities, and Markdown-to-PDF tooling. `WarningAnalyze` likewise combines data assets, reference documentation, and multiple processing scripts.

The tradeoff is portability. Many skills depend on internal SEBU/energy-domain concepts, internal-style assets, shared configuration, or application-specific data. Several main skill bodies are very large; `WarningAnalyze` is roughly 700+ lines, for example. These are useful examples of domain-rich skills but not ideal drop-in cross-project packages.

### Scripts, references, evals

The repository contains substantial Python tooling for schema export, Mermaid/image generation, warning-data extraction and classification, PDF generation, shared configuration, and other workflow support. Repository-authored config/test reports exist, but this run did not execute or independently validate those scripts or reports.

### Verdict

A substantive project-specific collection with strong artifact integration and weak portability. Keep as a domain-specific case study, not as a generic Agent Skills baseline.

---

## 5. `Guikingone/php-agent-skills`

### Verified identity

- GitHub repository ID: `1178847775`
- Default branch: `main`
- Stars: **3**, verified by exact `stars:3`; adjacent exact/range probes excluded other counts.
- Latest observed commit: `499a4219f82ba45eeee8091b03098e34e6849de7`.

### README and structure

The README describes a Composer package (`guikingone/agent-skills`) that loads Agent Skills standalone and integrates them with Symfony and Laravel. This is infrastructure for consuming skills rather than a local production skill collection.

Key implementation surfaces directly inspected or observed in the current commit include:

- `src/SkillParser.php`
- `src/FilesystemSkillLoader.php`
- `src/GithubSkillLoader.php`
- validation classes
- evaluation runner/grader/workspace/aggregator classes
- Symfony and Laravel bridges
- examples
- broad unit/integration-style test coverage in `tests/`

### Implementation findings

`SkillParser` reads `SKILL.md`, extracts YAML frontmatter, requires `name` and `description`, enforces the parent-directory/name match, and exposes scripts/references/assets through loaders. It also parses optional metadata such as `allowed-tools` and `compatibility`.

A notable implementation tradeoff is that it uses a deliberately simple in-project YAML parser rather than a full YAML implementation. This keeps dependencies small but can diverge from full YAML semantics for more complex frontmatter.

The evaluation subsystem is real code rather than only documentation. `EvalRunner` invokes an injected agent executor and records output, token usage, and duration. The current tree also contains tests for skill parsing/loading/validation, evaluation suites and graders, and framework integrations.

### Local skills, scripts, references, evals

No bundled local production `SKILL.md` collection was observed. The repository provides the machinery to load and evaluate external/user skills. Therefore the correct catalog type is **skill runtime/tooling**, with zero individual local-skill reports.

### Verdict

Keep as ecosystem tooling. It is one of the more technically substantive repositories in this batch because it implements parsing, loading, validation, framework integration, and evaluation rather than merely publishing prompt files. Do not misclassify it as a skill pack.

---

## 6. `davila7/agentskills`

### Verified identity

- GitHub repository ID: `1119211248`
- Default branch: `main`
- Stars: **4**, exact GitHub query verified.

### README and structure

The README explicitly identifies the repository as the Agent Skills specification, documentation, and reference SDK rather than a collection of production skills. `skills-ref/README.md` further states that the reference library is for demonstration/reference use and not production.

Directly inspected:

- `docs/specification.mdx`
- `skills-ref/README.md`
- root `README.md`

The specification covers required `SKILL.md` frontmatter/body, optional `scripts/`, `references/`, and `assets/`, progressive disclosure, file references, and validation with `skills-ref`.

### Findings

This repository is useful historical/reference material, but it is not a unique skill collection. The inspected specification snapshot also contains an internal wording inconsistency around the `name` character set: the summary table includes numbers, while a later bullet narrows the description to letters and hyphens. That inconsistency was subsequently corrected upstream, which reinforces treating this repository as a snapshot rather than current canonical authority.

### Verdict

Reference-only/specification tooling. Fully content-reviewed, but remove/hold it from the unique deep-analysis skill queue during reconciliation. Individual production-skill report count: 0.

---

## 7. `AsherBond/agentskills`

### Verified identity

- GitHub repository ID: `1151654543`
- Default branch: `main`
- Stars: **0**, exact GitHub query verified.

### Content identity finding

The current README blob matches the contemporary Agent Skills upstream README, and the repository's latest observed commit is `217be548739f21d6008915c29aefe320ea1a90af`. That exact commit SHA and the surrounding commit history are also present in the official `agentskills/agentskills` repository.

This is therefore not merely a metadata-name collision: actual content and git history establish it as a synchronized upstream fork/mirror.

### Verdict

Content-level duplicate of the official specification repository. Mark deep analysis complete because the duplicate conclusion required content/history inspection, but do not retain it as a unique skill collection. Individual skill report count: 0.

---

## 8. `devops2626/agentskills`

### Verified identity

- GitHub repository ID: `1266535227`
- Default branch: `main`
- Stars: **2**, exact GitHub query verified.

### Content identity finding

Its README matches the Agent Skills upstream content. The latest observed commit is `5d4c1fda3f786fff826c7f56b6cb3341e7f3a911`, and multiple surrounding commit hashes/messages match the official `agentskills/agentskills` history exactly.

The repository is a frozen fork/mirror at an earlier upstream point rather than an independently authored skill collection.

### Verdict

Content-level upstream snapshot/duplicate. Deep analysis complete; dedupe/hold during catalog reconciliation. Individual skill report count: 0.

---

## 9. `danielbodnar/agentskills`

### Verified identity

- GitHub repository ID: `1248504838`
- Default branch: `main`
- Stars: **2**, exact GitHub query verified.

### Content identity finding

Its README blob matches the same upstream Agent Skills README. A paired commit-history inspection with `devops2626/agentskills` returned the same exact sequence of hashes, including `5d4c1fda3f786fff826c7f56b6cb3341e7f3a911`, `0dd34f7782ff1c393190c86e7b387a931643bc12`, `873ac564e4eec65ceca674d788afe42d19bf595d`, and other commits also present in official upstream history.

### Verdict

Another frozen upstream fork/mirror. Deep analysis complete; dedupe/hold from the unique catalog. Individual skill report count: 0.

---

## 10. `XiaoZhengTou/agentSkills`

### Verified identity

- GitHub repository ID: `1167193164`
- Default branch: `main`
- Stars: **1**, exact GitHub query verified.
- Current organization of skill definitions was observed after commit `baf33f0f643cd7289b8aaeba1a2a2fd80a7e3a9f`, which migrated skill definitions into `.claude/commands/` and added parallel dispatch.

### README and architecture

The repository describes an AI-driven development workflow organized around project detection, requirements/PRD/task planning, backend and frontend implementation, testing, and independent review. The central architectural idea is a shared machine-readable project context plus explicit handoff artifacts under `.claude/handoffs/`.

All 24 current command/skill definitions were directly read or inspected:

`a11y-check`, `acceptance-check`, `animation-spec`, `api-design`, `api-integration`, `code-review`, `component-design`, `component-variant`, `deploy-verify`, `design-token`, `detect-project`, `integration-test`, `langchain-chain`, `page-implement`, `parallel-dispatch`, `prd-generate`, `prisma-schema`, `requirements-parse`, `responsive-layout`, `route-implement`, `task-decompose`, `test-report`, `unit-test`, and `wireframe-generate`.

### Skill design findings

The collection is unusually consistent in its custom metadata contract: each skill declares a role/agent plus `inputs` and `outputs`, which makes cross-skill dependencies explicit. `detect-project` centralizes environment detection into `.claude/project-context.json`, reducing repeated framework guessing. `task-decompose` emits dependency-aware `execution_waves`, while `parallel-dispatch` consumes those waves, giving the collection an actual orchestration protocol rather than an informal list of prompts.

The review/test/deployment skills are also connected to concrete upstream artifacts such as PRD, API specs, tasks, test results, and deployment state. That gives the collection a clearer end-to-end workflow than many isolated skill repositories.

Weaknesses are mostly maintainability-related. Many skills contain framework-specific templates and version-sensitive conventions that require active updating. Some examples contain hard-coded model/tool assumptions. No dedicated repository-wide eval suite was observed in the inspected skill surfaces, and this batch did not execute the workflow.

### Verdict

Keep as a unique multi-agent workflow collection. It is a strong example of explicit input/output contracts and skill-to-skill handoffs, though its framework templates should be treated as evolving implementation guidance rather than stable specification.

---

## Cross-repository conclusions

1. **Content reading changed classification.** Three indexed `agentskills` repositories were proven to be upstream mirrors/forks through matching content and commit history. They are not retained as unique skill collections merely because the index metadata labeled them as collections.
2. **Tooling deserves a separate category.** `Guikingone/php-agent-skills` has significant engineering value but packages runtime/parser/evaluation infrastructure rather than local skills.
3. **Large skill bodies remain common.** `me-pankajmunde/AgentSkills` and parts of `JiinGalaxy/AgentSkills` load very large domain guides into the main skill body, weakening progressive disclosure.
4. **Explicit contracts improve composability.** `XiaoZhengTou/agentSkills` and the local KCOS skills in `ColonelDarcy2018/agentSkills` are strongest where triggers, exclusions, inputs, outputs, and handoffs are made explicit.
5. **Repository provenance must be recorded.** Imported system skills, project-specific agent documents, specification snapshots, and original portable skills should not be flattened into one undifferentiated quality score.

## Progress after Batch 025

- Repositories structure/content reviewed this batch: **10**
- Individual skill/equivalent bodies directly reviewed this batch: **46**
- Repositories structure/content reviewed total: **250**
- Repository-scoped skill reports total: **2746**
- Canonical eligible basis carried forward: **2088**
- Remaining estimate: **1838**
- Runtime validation: **not executed**
