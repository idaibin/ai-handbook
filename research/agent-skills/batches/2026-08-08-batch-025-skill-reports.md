# GitHub Skills Catalog — Batch 025 Individual Skill Reports

Observed: 2026-08-08

This file records **46 directly inspected skill or skill-equivalent definitions** from Batch 025. A report is included only when an actual skill body or project-specific equivalent was read. Repositories that contain only specification/runtime tooling or content-level upstream duplicates are listed separately with a zero local-skill count.

No third-party skill, script, installer, test, or eval was executed during this review. Runtime behavior remains unverified unless explicitly described as repository-authored evidence.

---

# `me-pankajmunde/AgentSkills` — 2 reports

## 1. `copilot-sdk`

- **Path:** `copilot-sdk/SKILL.md`
- **Format:** canonical-style `SKILL.md` with YAML frontmatter.
- **Purpose:** build agentic applications with the GitHub Copilot SDK across TypeScript, Python, Go, and .NET; includes sessions, streaming, tools, MCP integration, and custom agents.
- **Trigger quality:** broad and explicit; names product/API concepts and common user intents.
- **Supporting resources:** primarily self-contained in the main file; no dedicated eval package observed.
- **Strengths:** cross-language quick starts and a broad lifecycle view make it useful as an implementation reference.
- **Risks/limitations:** the main skill is roughly 900 lines, so activation is context-heavy. Quick-start examples use a globally permissive approval handler; that should be interpreted as demonstration code rather than a safe production default.
- **Portability:** high for Copilot SDK users, low outside that ecosystem.

## 2. `adk-agent-builder`

- **Path:** `google-adk-skill/SKILL.md`
- **Format:** canonical-style `SKILL.md`.
- **Purpose:** construct Google ADK single-agent, multi-agent, workflow, tool, guardrail, state, deployment, MCP, A2A, and streaming solutions in Python/TypeScript/Go/Java.
- **Supporting resource:** `google-adk-skill/templates.md` separates reusable templates from some of the main guidance.
- **Strengths:** unusually broad lifecycle coverage and explicit language-specific entry points.
- **Risks/limitations:** the main file is roughly 950 lines despite the separate templates file, so progressive disclosure is incomplete. Model/framework examples can age quickly.
- **Portability:** high inside Google ADK; intentionally framework-specific.

---

# `shitikovAlexander/AgentSkills` — 1 report

## 3. `AgentDesk Workflow Designer`

- **Path:** `AgentDesk/agentdesk-workflow-designer.md`
- **Format:** project-specific skill-equivalent Markdown; not a canonical `SKILL.md` package.
- **Purpose:** design AgentDesk multi-agent workflows by selecting provider, model, agent role, input context, skill attachments, topology, connection pass type, and output format.
- **Key contract:** distinguishes solo/pipeline/orchestrator/shared-memory shapes and defines downstream context-passing behavior.
- **Strengths:** explicit graph semantics and a concrete proposal output schema make the workflow reproducible.
- **Risks/limitations:** strongly coupled to AgentDesk internals. The document acknowledges that JSON output is not validated/retried and the workflow stops on first agent error. Its architecture notes include a broad permission-bypass execution mode that should be treated as a security risk, not a reusable default.
- **Supporting files/evals:** none observed for this skill-equivalent.

---

# `ColonelDarcy2018/agentSkills` — 9 reports

## 4. `skill-creator` — imported/system

- **Path:** `.system/skill-creator/SKILL.md`
- **Format:** canonical `SKILL.md`, but provenance appears imported/system rather than repository-original.
- **Purpose:** guide creation and maintenance of Agent Skills using frontmatter, progressive disclosure, references/assets/scripts, validation, and optional OpenAI-facing metadata.
- **Supporting resources:** `agents/openai.yaml`, `references/openai_yaml.md`, `scripts/generate_openai_yaml.py`, `scripts/init_skill.py`, `scripts/quick_validate.py`.
- **Strengths:** strong resource separation and deterministic generation/validation workflow.
- **Catalog note:** useful evidence, but do not credit as an original local skill design.

## 5. `skill-installer` — imported/system

- **Path:** `.system/skill-installer/SKILL.md`
- **Format:** canonical `SKILL.md`, imported/system provenance.
- **Purpose:** install skills from GitHub-oriented sources into the local skill environment.
- **Supporting scripts:** GitHub/install helpers including `github_utils.py` and `install-skill-from-github.py`.
- **Strengths:** packages operational installation logic with the instruction layer.
- **Catalog note:** record as imported tooling; runtime not executed here.

## 6. `game-requirement-innovation`

- **Path:** `game-requirement-innovation/SKILL.md`
- **Format:** canonical skill.
- **Purpose:** clarify and expand game requirements using divergence/convergence before converging on implementable requirements.
- **References:** innovation workflow, question bank, and requirement-understanding template.
- **Strengths:** separates reusable questioning/reference material from the core flow.
- **Limitations:** domain-specific; effectiveness depends on the quality of interactive requirement inputs.

## 7. `kcos-protocol-bootstrap`

- **Path:** `kcos-protocol-bootstrap/SKILL.md`
- **Format:** canonical skill.
- **Purpose:** initialize/reset KCOS protocol and knowledge-base structure for a repository.
- **Trigger boundary:** explicitly excludes pure business-flow mapping and pure task decomposition, routing those to sibling skills.
- **Supporting resources:** protocol assets, `ai-playbook.md`, `p0-rules.md`, `scripts/init_kcos_protocol.py`, and KCOS sync/index script material.
- **Strengths:** concrete bootstrap procedure and explicit sibling-skill boundaries reduce routing ambiguity.
- **Limitations:** tightly coupled to the KCOS directory/protocol convention.

## 8. `mobile-rpa-script-dev`

- **Path:** `mobile-rpa-script-dev/SKILL.md`
- **Format:** canonical skill.
- **Purpose:** develop/debug Android mobile-RPA Python scripts inside the repository's RPA platform/tooling environment.
- **References:** workflow, context bootstrap, tooling map, troubleshooting, code patterns, advanced routing/instruction material, and complex-script playbook.
- **Supporting script:** `split_advanced_doc.py`.
- **Strengths:** good reference decomposition for a specialized domain.
- **Limitations:** platform-specific and dependent on project tooling/device context. This catalog review did not execute mobile automation.

## 9. `上下文管理`

- **Path:** `上下文管理/SKILL.md`
- **Format:** canonical skill with Chinese name/frontmatter.
- **Purpose:** save, restore, and manage session/project working context and progress.
- **Strengths:** narrow responsibility and reusable continuity workflow.
- **Limitations:** coupled to the repository's KCOS/session conventions rather than a portable persistence API.

## 10. `业务逻辑图谱`

- **Path:** `业务逻辑图谱/SKILL.md`
- **Format:** canonical skill.
- **Purpose:** create and maintain Mermaid-backed business-logic knowledge documents and persist them into the KCOS knowledge base.
- **Trigger quality:** high-recall intent description plus explicit non-trigger boundaries.
- **Workflow:** visualize logic first, persist structured knowledge second, synchronize the KCOS index after changes.
- **Strengths:** clear artifact destination and coordination boundary with task decomposition.
- **Limitations:** tied to KCOS storage conventions.

## 11. `代码审查`

- **Path:** `代码审查/SKILL.md`
- **Format:** canonical skill.
- **Purpose:** review code changes for quality, correctness, maintainability, and common risk classes, then persist review records through KCOS.
- **Strengths:** a distinct review responsibility rather than mixing review into implementation.
- **Limitations:** no independent runtime/eval evidence was executed by this catalog run.

## 12. `任务分解`

- **Path:** `任务分解/SKILL.md`
- **Format:** canonical skill.
- **Purpose:** transform ambiguous/complex requirements into acceptance criteria, executable sub-tasks, dependencies, risks, questions, and execution order.
- **Contract:** requires a structured output and explicitly cooperates with `业务逻辑图谱` when both are relevant.
- **Strengths:** good boundary management and acceptance-oriented planning.
- **Limitations:** depends on user/project context quality; implementation details are intentionally excluded from the planning artifact.

---

# `JiinGalaxy/AgentSkills` — 10 reports

## 13. `demo_making`

- **Path:** `.claude/SKILLS/DemoMaking/demo_making_skill.md`
- **Format:** skill-equivalent with frontmatter.
- **Purpose:** generate high-fidelity HTML prototype/demo pages from PRD page descriptions.
- **References/assets:** multiple visual screenshots used as design references.
- **Strengths:** ties written PRD to concrete visual artifacts.
- **Limitations:** highly organization/style-specific; screenshot-heavy assets reduce portability.

## 14. `demo_developer_agent`

- **Path:** `.claude/SKILLS/HiveAgents/demo_developer_agent.md`
- **Format:** agent-oriented skill-equivalent.
- **Purpose:** act as the Hive execution agent for end-to-end demo implementation, including architecture and frontend/backend/database work.
- **Strengths:** clearly positioned as an executor under a commander.
- **Limitations:** responsibility is broad and may overlap multiple engineering roles; strongly coupled to the repository's Hive workflow.

## 15. `market_insight_agent`

- **Path:** `.claude/SKILLS/HiveAgents/market_insight_agent.md`
- **Format:** agent-oriented skill-equivalent.
- **Purpose:** perform market/product planning, business-goal framing, and roadmap-oriented work for the Hive workflow.
- **Strengths:** distinct planning role.
- **Limitations:** organization-specific assumptions and artifacts reduce generic reuse.

## 16. `prd_writer_agent`

- **Path:** `.claude/SKILLS/HiveAgents/prd_writer_agent.md`
- **Format:** agent-oriented skill-equivalent.
- **Purpose:** produce PRDs from requirement collection through structured document generation inside the Hive workflow.
- **Strengths:** explicit dedicated authoring role.
- **Limitations:** overlaps with the separate `prd_writing` package, increasing maintenance/provenance complexity.

## 17. `prototype_designer_agent`

- **Path:** `.claude/SKILLS/HiveAgents/prototype_designer_agent.md`
- **Format:** agent-oriented skill-equivalent.
- **Purpose:** generate high-fidelity HTML prototypes from PRD page-design descriptions.
- **Strengths:** clean role separation inside the commander/worker pattern.
- **Limitations:** substantial overlap with `demo_making`; reuse boundaries are repository-specific.

## 18. `hive_commander`

- **Path:** `.claude/SKILLS/HiveCommander/hive_commander.md`
- **Format:** skill/agent hybrid with frontmatter.
- **Purpose:** receive user goals, classify work, and dispatch/coordinate specialized Hive execution agents.
- **Supporting docs:** `HiveCommander/README.md` and `EXTENSION_GUIDE.md` explain the pattern and extension mechanism.
- **Strengths:** explicit coordinator role and extensibility model.
- **Limitations:** orchestration correctness depends on the surrounding repository conventions; no runtime orchestration was executed here.

## 19. `LarkDocWriting`

- **Path:** `.claude/SKILLS/LarkDocWriting/lark_doc_skill.md`
- **Format:** project-specific skill document; not fully aligned with canonical Agent Skills packaging.
- **Purpose:** operate on Feishu/Lark multidimensional-table/document workflows.
- **Strengths:** captures concrete domain/tool procedure.
- **Limitations:** product- and organization-specific; portability depends on external API/tool configuration.

## 20. `prd_writing`

- **Path:** `.claude/SKILLS/PRDWriting/prd_write_skill.md`
- **Format:** frontmatter-backed skill-equivalent.
- **Purpose:** produce organization-standard PRDs with database/domain context, diagrams, templates, and generated PDF outputs.
- **References/assets:** SEBU PRD template, schema relationship documents, ER/relationship images, spreadsheets.
- **Scripts:** database schema exporter, Mermaid extraction, schema relation generation, diagram generation, indicator-data helper, Markdown-to-PDF conversion, config access test helper.
- **Strengths:** one of the most complete artifact-backed skill packages in this batch.
- **Limitations:** very domain-specific and around 430+ lines in the main skill; some scripts depend on databases/external configuration that were not executed here.

## 21. `product_planning`

- **Path:** `.claude/SKILLS/ProductPlan/product_plan.md`
- **Format:** frontmatter-backed skill-equivalent.
- **Purpose:** produce product roadmaps, version planning, prioritization, and periodic planning documents.
- **References/assets:** large product-planning document/PDF and UI-style images.
- **Strengths:** grounded in concrete internal reference artifacts.
- **Limitations:** organization-specific source material and a large main document reduce portability.

## 22. `Warning Analyze`

- **Path:** `.claude/SKILLS/WarningAnalyze/warning_analyze_skill.md`
- **Format:** skill-equivalent.
- **Purpose:** analyze/classify operational warnings and build/augment warning knowledge for energy/equipment contexts.
- **References/assets:** warning-category README and multiple CSV datasets.
- **Scripts:** data fetch/join/fill utilities, semantic/classification optimization variants, knowledge-base helpers, dependency requirements.
- **Strengths:** strong coupling of instructions, datasets, and executable analysis support.
- **Limitations:** the main file is roughly 700+ lines and the package is highly domain-specific. Runtime/data-quality claims were not independently validated.

---

# `XiaoZhengTou/agentSkills` — 24 reports

All current definitions use a consistent custom contract around `agent`, `inputs`, and `outputs`, usually reading `.claude/project-context.json` and writing `.claude/handoffs/*` artifacts.

## 23. `a11y-check`

- **Path:** `.claude/commands/a11y-check.md`
- **Agent:** frontend.
- **Purpose:** scan frontend components/pages for accessibility issues and produce a severity-graded report with remediation examples.
- **Strengths:** concrete output contract and framework adaptation.
- **Limitations:** some checks, such as visual contrast or interaction behavior, cannot be reliably proven by static prompt inspection alone.

## 24. `acceptance-check`

- **Path:** `.claude/commands/acceptance-check.md`
- **Agent:** reviewer.
- **Purpose:** compare implementation against PRD acceptance criteria, tasks, API contracts, and selected non-functional requirements.
- **Output:** `.claude/handoffs/acceptance-report.md`.
- **Strengths:** ties review to explicit upstream requirements rather than generic code taste.
- **Limitations:** actual evidence acquisition is left to the executing agent; this batch did not run it.

## 25. `animation-spec`

- **Path:** `.claude/commands/animation-spec.md`
- **Agent:** frontend.
- **Purpose:** define interaction animation timing/easing and generate implementation examples for the detected styling/animation stack.
- **Strengths:** consistent motion baseline and framework adaptation.
- **Limitations:** values are opinionated defaults, not a validated design-system source of truth.

## 26. `api-design`

- **Path:** `.claude/commands/api-design.md`
- **Agent:** backend.
- **Purpose:** transform PRD data models and user flows into an OpenAPI-oriented REST contract.
- **Output:** `.claude/handoffs/api-spec.yaml`.
- **Strengths:** machine-readable handoff target.
- **Limitations:** authentication/framework mapping is heuristic and must be reconciled with real project constraints.

## 27. `api-integration`

- **Path:** `.claude/commands/api-integration.md`
- **Agent:** frontend.
- **Purpose:** implement typed frontend API clients, authentication headers, data-fetching integration, and unified errors from the API spec.
- **Strengths:** explicit backend-to-frontend handoff.
- **Limitations:** framework/library choices are template defaults and can become stale.

## 28. `code-review`

- **Path:** `.claude/commands/code-review.md`
- **Agent:** reviewer.
- **Purpose:** review code quality, reliability, maintainability, performance, and common security-risk classes with blocker/major/minor severity.
- **Strengths:** independent role and severity contract.
- **Limitations:** the prompt alone cannot establish that every issue will be grounded in executed evidence.

## 29. `component-design`

- **Path:** `.claude/commands/component-design.md`
- **Agent:** frontend.
- **Purpose:** derive component trees, props/events, state ownership, and data flow from PRD requirements.
- **Strengths:** separates design contract from page implementation.
- **Limitations:** framework conventions are heuristic templates.

## 30. `component-variant`

- **Path:** `.claude/commands/component-variant.md`
- **Agent:** frontend.
- **Purpose:** enumerate and implement UI state variants such as loading/error/empty/disabled/selected; optionally add Storybook stories.
- **Strengths:** explicitly addresses state completeness, a common UI omission.
- **Limitations:** does not itself guarantee visual regression or interaction testing.

## 31. `deploy-verify`

- **Path:** `.claude/commands/deploy-verify.md`
- **Agent:** reviewer.
- **Purpose:** verify environment configuration, service health, database/migration state, smoke scenarios, and logs after deployment.
- **Strengths:** deployment is treated as a verification phase, not merely a build step.
- **Limitations:** success examples are templates; real deployment evidence must come from execution.

## 32. `design-token`

- **Path:** `.claude/commands/design-token.md`
- **Agent:** frontend.
- **Purpose:** extract/normalize color, typography, spacing, radius, shadow, and related tokens and emit JSON/Tailwind/CSS/Style Dictionary forms.
- **Strengths:** machine-readable token handoff.
- **Limitations:** generated token semantics need design-source validation; scanning hard-coded values alone is not authoritative.

## 33. `detect-project`

- **Path:** `.claude/commands/detect-project.md`
- **Agent:** common.
- **Purpose:** inspect repository markers/dependencies to identify language, framework, ORM, test framework, package manager, and project type, then write `.claude/project-context.json`.
- **Strengths:** centralizes technology detection so sibling skills do not duplicate framework guessing.
- **Limitations:** monorepo handling is deliberately simplified and detection rules require ongoing maintenance.

## 34. `integration-test`

- **Path:** `.claude/commands/integration-test.md`
- **Agent:** tester.
- **Purpose:** generate integration tests spanning API requests, authentication/authorization behavior, database persistence, and cleanup using the detected stack.
- **Strengths:** explicitly requires test isolation and real persistence checks.
- **Limitations:** generated examples do not prove the repository under test actually wires the suggested test server/database correctly.

## 35. `langchain-chain`

- **Path:** `.claude/commands/langchain-chain.md`
- **Agent:** backend.
- **Purpose:** construct LangChain JS/Python model chains, structured outputs, RAG, and tool/agent flows.
- **Strengths:** stack-adaptive implementation route.
- **Limitations:** model IDs and framework API examples are highly time-sensitive; this skill requires frequent updating.

## 36. `page-implement`

- **Path:** `.claude/commands/page-implement.md`
- **Agent:** frontend.
- **Purpose:** implement pages from component/API artifacts with framework-adaptive data fetching, loading/error boundaries, and responsive behavior.
- **Strengths:** consumes explicit upstream artifacts rather than regenerating requirements.
- **Limitations:** implementation advice includes framework-specific assumptions that must be checked against the actual project.

## 37. `parallel-dispatch`

- **Path:** `.claude/commands/parallel-dispatch.md`
- **Agent:** common/orchestration.
- **Purpose:** read `tasks.json` execution waves, decide which tasks can run in parallel, dispatch sub-agents by wave, and collect results.
- **Strengths:** pairs directly with `task-decompose`'s dependency graph and makes concurrency an explicit artifact-level contract.
- **Limitations:** correctness depends on the task graph accurately representing shared-file and other hidden dependencies.

## 38. `prd-generate`

- **Path:** `.claude/commands/prd-generate.md`
- **Agent:** analyst.
- **Purpose:** transform structured requirements into a PRD with stories, data model, API draft, flow diagrams, and acceptance criteria.
- **Strengths:** creates downstream-readable artifacts and acceptance criteria early.
- **Limitations:** API/data-model material remains a draft and should not silently become architecture authority.

## 39. `prisma-schema`

- **Path:** `.claude/commands/prisma-schema.md`
- **Agent:** backend.
- **Purpose:** map PRD/API entities to database schemas across Prisma, TypeORM, Drizzle, SQLAlchemy, Hibernate, or raw SQL.
- **Strengths:** broader than its name and explicitly adapts to detected ORM.
- **Limitations:** the skill name is misleading for non-Prisma projects; database constraints/migrations still require project-specific review.

## 40. `requirements-parse`

- **Path:** `.claude/commands/requirements-parse.md`
- **Agent:** analyst.
- **Purpose:** turn raw user requirements into structured functional/non-functional requirements, constraints, entities/rules, edge cases, and acceptance criteria.
- **Strengths:** useful first normalized handoff artifact.
- **Limitations:** it can introduce technology assumptions if project-context is treated as a requirement rather than contextual constraint.

## 41. `responsive-layout`

- **Path:** `.claude/commands/responsive-layout.md`
- **Agent:** frontend.
- **Purpose:** analyze layout weaknesses and generate responsive implementations across named breakpoints.
- **Strengths:** explicitly preserves business logic while changing layout.
- **Limitations:** breakpoint assumptions are Tailwind-like defaults and may not match the project's design system.

## 42. `route-implement`

- **Path:** `.claude/commands/route-implement.md`
- **Agent:** backend.
- **Purpose:** implement backend routes/controllers from API and database contracts, including input validation, errors, authentication integration, and subsequent unit-test handoff.
- **Strengths:** connects implementation immediately to a test skill.
- **Limitations:** generated route patterns are framework templates; correctness requires reading actual project architecture and middleware conventions.

## 43. `task-decompose`

- **Path:** `.claude/commands/task-decompose.md`
- **Agent:** analyst.
- **Purpose:** decompose PRD work into role-owned tasks with dependencies, inputs, outputs, priority, required skills, parallelizability, and execution waves.
- **Strengths:** one of the collection's strongest machine-readable coordination contracts.
- **Limitations:** file-conflict checks capture only one type of hidden dependency; domain/state conflicts may still exist.

## 44. `test-report`

- **Path:** `.claude/commands/test-report.md`
- **Agent:** tester.
- **Purpose:** run/collect test suites, summarize pass/fail/skip counts, coverage, failures, and low-coverage risks into a Markdown report.
- **Strengths:** clearly distinguishes evidence/reporting from implementation.
- **Limitations:** threshold and coverage conventions are policy defaults, not proof of adequate behavioral coverage.

## 45. `unit-test`

- **Path:** `.claude/commands/unit-test.md`
- **Agent:** tester.
- **Purpose:** generate unit tests using the detected framework, mock external dependencies, cover normal/boundary cases, and target a stated coverage threshold.
- **Strengths:** stack selection is centralized through project context.
- **Limitations:** coverage percentage is an incomplete quality proxy; execution is required to establish evidence.

## 46. `wireframe-generate`

- **Path:** `.claude/commands/wireframe-generate.md`
- **Agent:** frontend.
- **Purpose:** generate desktop/mobile ASCII wireframes, layout notes, responsive behavior, and component mappings from PRD page requirements.
- **Strengths:** lightweight artifact that bridges product requirements and component design without requiring a design tool.
- **Limitations:** low-fidelity output cannot validate visual quality or real interaction behavior.

---

# Repositories with zero local production-skill reports

## `Guikingone/php-agent-skills`

Zero local production skills. This repository implements Agent Skills parsing/loading/validation/evaluation and Symfony/Laravel integration. It is reported at repository level as **skill tooling/runtime**.

## `davila7/agentskills`

Zero local production skills. This repository is a specification/reference-SDK snapshot and is reported as **reference-only**.

## `AsherBond/agentskills`

Zero unique local production skills. Actual README and git history match official `agentskills/agentskills`; reported as a **content duplicate/mirror**.

## `devops2626/agentskills`

Zero unique local production skills. Actual content/history match a frozen official upstream snapshot; reported as a **content duplicate/mirror**.

## `danielbodnar/agentskills`

Zero unique local production skills. Actual content/history match a frozen official upstream snapshot; reported as a **content duplicate/mirror**.

---

## Batch skill-report totals

| Repository | Reports |
|---|---:|
| `me-pankajmunde/AgentSkills` | 2 |
| `shitikovAlexander/AgentSkills` | 1 |
| `ColonelDarcy2018/agentSkills` | 9 |
| `JiinGalaxy/AgentSkills` | 10 |
| `Guikingone/php-agent-skills` | 0 |
| `davila7/agentskills` | 0 |
| `AsherBond/agentskills` | 0 |
| `devops2626/agentskills` | 0 |
| `danielbodnar/agentskills` | 0 |
| `XiaoZhengTou/agentSkills` | 24 |
| **Total** | **46** |
