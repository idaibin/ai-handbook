# Agent Skills deep analysis — Batch 019

- Batch ID: `2026-08-07-batch-019`
- Observed at: 2026-08-07
- Queue basis: existing indexed repository queue from `sources/catalog/batches/agentskills-pages-2-3.json`, excluding repositories already recorded in `research/agent-skills/deep-analysis-progress.json`
- Repositories completed: **10**
- Repository-scoped skill reports: **199**
- Repository status: `structure-reviewed`
- Runtime validation: `not_executed`
- Individual reports:
  - `research/agent-skills/batches/2026-08-07-batch-019-skill-reports-01.md`
  - `research/agent-skills/batches/2026-08-07-batch-019-skill-reports-02.md`

## Scope and completion rule

A repository is counted complete in this batch only after its identity and current star count were checked and actual repository content was read. Review surfaces included repository structure, README/inventory documentation, current `SKILL.md` bodies or equivalent skill definitions, and scripts/references/evaluation surfaces when present. Metadata-only candidates were not marked complete.

`structure-reviewed` means source/content review completed. It does **not** mean installers, scripts, builds, tests, external APIs, browser sessions, model CLIs, hardware, or evaluation runners were executed.

## Repository results

| Repository | Stars observed | Skill reports | Status | Main evidence read |
| --- | ---: | ---: | --- | --- |
| `beriberikix/zephyr-agent-skills` | 59 | 22 | structure-reviewed | root router `SKILL.md`, README/structure, generated `index.json`, `zephyr-index`, `scripts/validate_skills.py` |
| `antonarhipov/agentskills` | 15 | 9 | structure-reviewed | all nine root skill bodies/frontmatter, including the six-stage spec pipeline and three independent skills |
| `JayRHa/AgentSkills` | 3 | 74 | structure-reviewed | README catalog, current tree/search inventory, validator, `code-reviewer`, two current uncatalogued Xquik skill bodies |
| `LeoYeAI/teammate-skill` | 257 | 1 | structure-reviewed | root `create-teammate` skill, source-ingestion/tool map, `privacy_guard.py` |
| `jonkiky/agentskills` | 0 | 24 | structure-reviewed | current `skills/` inventory, QA-framework duplicate/agent surfaces, representative planning/testing skill bodies |
| `PramodDutta/agentskills` | 0 | 15 | structure-reviewed | STLC inventory, `test-plan-generator`, Jira fetch script |
| `olgasafonova/SkillCheck-Free` | 36 | 1 | structure-reviewed | `skill-check` body, repository layout/readme rules surface |
| `Daoming-Chen/AgentSkills` | 9 | 2 | structure-reviewed | both current skill bodies: `prune-abstraction`, `ask-claude` |
| `TrogonStack/agentskills` | 10 | 39 | structure-reviewed | plugin skill inventory, authoring guide, `prd-review`, references and validation workflow surfaces |
| `manykarim/robotframework-agentskills` | 27 | 12 | structure-reviewed | README/current skill inventory, Browser skill, scripts/plugin/install surfaces, `eval/tasks/README.md` and eval code paths |

Stars are point-in-time repository metadata used only to verify repository identity/state. They are not used as a quality score.

## Detailed findings

### 1. `beriberikix/zephyr-agent-skills`

**Verified facts**

- The repository exposes one root routing skill plus 21 current Zephyr-domain skills, for 22 repository-scoped reports.
- The root router explicitly directs the agent to deterministic `zephyr-cli skills suggest` selection instead of guessing a skill.
- `index.json` contains generated matcher metadata, including keywords/aliases/Kconfig patterns/DTS compatibles and bundled file lists.
- `scripts/validate_skills.py` performs repository-level checks for frontmatter, required sections, local links, cross-skill deep links, catalog/marketplace consistency, and matcher metadata.

**Inference**

The main reusable engineering pattern is not only the Zephyr content; it is the combination of progressive disclosure, deterministic routing metadata, generated registries, and repository-level consistency gates. That pattern is directly relevant to a large skill catalog where model-only routing would otherwise become ambiguous.

**Not verified**

`zephyr-cli`, generated registry consistency, builds, hardware workflows, and any skill-specific command were not executed.

### 2. `antonarhipov/agentskills`

**Verified facts**

- The current root contains nine skill directories and no umbrella README.
- Six skills form a traceable pipeline: `spec` → `criteria` → `rules` → `spec-review` → `tasks` → `execute`.
- The pipeline uses stable behavior/acceptance identifiers, route-back rules for ambiguity, implementation checkpoints, and validation against acceptance criteria.
- `defend-your-pr` separates an ownership/comprehension gate from structural review; `review-prototype` is a method skill for verdict-first review UX; `spring-batch-6` is a domain reference.

**Inference**

This is a compact example of splitting a large software-delivery workflow by artifact boundary rather than accumulating one monolithic implementation skill.

**Not verified**

No workflow was run against a real feature or pull request.

### 3. `JayRHa/AgentSkills`

**Verified facts**

- The README catalog states 72 skills across 10 categories and describes a top-level-folder skill model with scripts/references/examples/templates.
- The current repository additionally contains `x-twitter-scraper/SKILL.md` and nested `skills/xquik-social-data/SKILL.md`; both bodies were directly read. Batch 019 therefore records 74 current user-facing identities.
- `0-template/SKILL.md` is an authoring template and is excluded from the count.
- `scripts/validate_skills.py` discovers top-level directories containing `SKILL.md` and checks basic frontmatter/name/description constraints; the nested Xquik skill is therefore outside that validator's top-level discovery rule.
- `code-reviewer` includes intent discovery, minimal code context, correctness/security/maintainability lenses, severity ranking, references/templates, and explicit uncertainty handling.

**Inference**

The repository is useful as a broad pattern library, but the current inventory demonstrates why a generated machine-readable catalog should be authoritative: README counts and validator discovery can drift as layout evolves.

**Not verified**

The install script, validator, any skill runtime behavior, and the external Xquik service were not executed.

### 4. `LeoYeAI/teammate-skill`

**Verified facts**

- The repository maintains one primary `create-teammate` skill.
- The workflow supports multiple source types, dual-track Work Skill/persona analysis, generated teammate artifacts, version/evolution workflows, and a mandatory output quality gate.
- `privacy_guard.py` scans text-like files for a finite set of regex-defined PII/secret patterns and can redact matches.

**Inference**

The most relevant pattern is knowledge distillation with explicit source ingestion + generation gates + evolution/versioning. The privacy scanner is useful defense-in-depth, but its regex coverage should not be treated as complete data-loss prevention.

**Not verified**

No Slack/GitHub/email/Notion/Confluence collector, version operation, generated teammate, or redaction run was executed.

### 5. `jonkiky/agentskills`

**Verified facts**

- Current canonical skill packages are under `skills/`; code search found 24 distinct current identities.
- `QA-framework/skills/` duplicates a subset of those packages and additionally contains agent definitions. Duplicate distribution copies are not double-counted.
- `test-case-generation-workflow` explicitly sequences readiness, scenario design, test data, traceability/coverage and human QA handoff.
- `requirements-to-plan` is planning-only and explicitly separates Observed/Inferred/Unknown evidence.
- The README describes a `skills-lock.json` tracking file, but fetching the current root `skills-lock.json` returned 404.

**Inference**

The repository has useful planning/testing workflows, but duplicated skill copies plus a missing documented lockfile create source-of-truth/provenance ambiguity that a catalog should preserve rather than normalize away.

**Not verified**

No `npx skills` install/update operation, QA framework agent, Playwright flow, scanner or external tool was executed.

### 6. `PramodDutta/agentskills`

**Verified facts**

- The README enumerates 14 manual-testing/STLC skills plus one Playwright locator-repair skill.
- `test-plan-generator` turns a Jira ticket/story into a draft plan, surfaces gaps instead of inventing acceptance criteria, maps scenarios to criteria/gaps, and requires human review before finalization.
- Its `fetch_jira.sh` helper uses environment-provided Jira URL/email/token and a narrow `curl` + `jq` request/transform rather than embedding credentials.

**Inference**

The reusable pattern is lifecycle decomposition with human gates at artifact boundaries rather than an autonomous “generate all QA artifacts” mega-skill.

**Not verified**

Jira access, MCP paths, test generation, execution tracking, and Playwright locator repair were not run.

### 7. `olgasafonova/SkillCheck-Free`

**Verified facts**

- The repository bundles one read-only `skill-check` skill.
- It distinguishes agentskills-spec fields from Claude Code extensions and community extensions, and defines structural/semantic validation rules for frontmatter, naming, descriptions and supporting directories.
- The Free skill explicitly excludes deeper Pro-only checks/eval generation from its scope.

**Inference**

This is useful as a static lint layer for a skill repository, but these checks are not equivalent to behavioral evaluation. A production quality gate should keep syntax/structure lint and agent-behavior evals separate.

**Not verified**

The validator was not run against AI-handbook/skills, and Pro-only capabilities were not inspected or inferred as available here.

### 8. `Daoming-Chen/AgentSkills`

**Verified facts**

- The repository contains two current skills.
- `prune-abstraction` uses repeated helper/topology/smell/readability loops before focused validation and explicitly preserves semantic/domain boundaries.
- `ask-claude` is explicit-user-trigger only, compacts context for an external Claude CLI call, checks git status around repository work, and requires honest failure reporting.

**Inference**

`prune-abstraction` provides a strong anti-overengineering review pattern. `ask-claude` demonstrates an external-review adapter but is tightly coupled to local CLI/model/permission semantics and therefore needs environment-specific hardening before reuse.

**Not verified**

No refactor hook loop or Claude CLI invocation was executed.

### 9. `TrogonStack/agentskills`

**Verified facts**

- Current plugin inventory search identified 39 public plugin skill bodies. `.agents/skills/scaffold-plugin` is an internal authoring helper and is excluded.
- `docs/skill-authoring-guide.md` treats descriptions as routing boundaries, recommends positive and negative trigger conditions, linear numbered workflows, templates/examples and end-of-skill quality checklists.
- The current tree includes GitHub workflows for plugin validation and skill frontmatter.
- `prd-review` reads a structured PRD document set and checks completeness, source-of-truth conflicts, module-boundary drift and downstream impacts.
- The largest suites are product/functional requirements and event-modeling workflows, split into specialized skills instead of a single prompt.

**Inference**

The strongest reusable pattern is plugin-level modularity plus explicit authoring/validation conventions. It is especially relevant to preventing overlap between product-spec, domain-modeling/review, and downstream implementation skills.

**Not verified**

No plugin install, frontmatter CI, NATS/Datadog/GitHub integration, or event-modeling workflow was executed.

### 10. `manykarim/robotframework-agentskills`

**Verified facts**

- The README contains an explicit 12-row skill table: six library-reference skills and six script-backed skills. A nearby sentence says “5 library-reference + 6 script-based”, which conflicts with the table/current files; this batch uses the 12-row inventory.
- The repository includes multi-agent installer adapters, plugin/hooks/MCP surfaces, tests and a dedicated `rf-skill-eval` implementation.
- `eval/tasks/README.md` defines narrow/realistic/adversarial tiers, fresh fixtures, bounded model/tool/turn/time settings, deterministic grader checks, and a primary metric that must be externally grounded. Adversarial results are explicitly non-gating in the documented v1 model.
- The eval documentation records prior regressions and distinguishes observed side effects from misleading telemetry assumptions.

**Inference**

This is the most complete evaluation-oriented engineering example in this batch. The valuable pattern is a separate reproducible eval harness with fixtures, deterministic outcome checks, cost/model bounds and regression canaries, rather than relying on subjective “the skill looks good” review.

**Not verified**

No installer, MCP server, Robot Framework library, browser/mobile/API test, hook, CI workflow, or `rf-skill-eval` task was executed.

## Content-level classification corrections / notes

These are based on current repository content and should be considered in future index reconciliation:

| Repository | Index-level class | Content-level note |
| --- | --- | --- |
| `olgasafonova/SkillCheck-Free` | skill tooling candidate | More precise: `skill_tooling_with_bundled_validator_skill`; it is tooling expressed as one installable Skill. |
| `jonkiky/agentskills` | skill collection | More precise note: collection with duplicated QA-framework distribution copies and separate agent definitions. |
| `JayRHa/AgentSkills` | skill collection | Keep collection classification, but record current catalog/layout drift: README 72 vs 74 current user-facing identities; nested skill outside top-level validator scan. |
| `manykarim/robotframework-agentskills` | skill collection/tooling-adjacent | Keep as skill collection, with substantial installer/plugin/MCP/eval tooling; explicit 12-row inventory overrides the contradictory 11-count prose sentence. |

## Skill-report count reconciliation

```text
beriberikix/zephyr-agent-skills          22
antonarhipov/agentskills                   9
JayRHa/AgentSkills                        74
LeoYeAI/teammate-skill                     1
jonkiky/agentskills                       24
PramodDutta/agentskills                   15
olgasafonova/SkillCheck-Free               1
Daoming-Chen/AgentSkills                   2
TrogonStack/agentskills                   39
manykarim/robotframework-agentskills      12
--------------------------------------------
total                                    199
```

## Reusable engineering lessons

1. **Separate routing from content.** Zephyr's deterministic matcher + generated registry is stronger than relying on model intuition once catalogs become large.
2. **Split workflows by artifact contract.** Antonarhipov, PramodDutta and TrogonStack show that spec/criteria/rules/review/tasks/execution or PRD/FRD/event-model stages can be independently testable and reviewable.
3. **Treat inventory as generated state where possible.** JayRHa and manykarim both expose count/document drift; jonkiky exposes a documented-but-absent lockfile. Manual counts are not sufficient authority.
4. **Static lint and behavioral eval are different gates.** SkillCheck-Free is a structural/semantic linter; manykarim's task fixtures and external graders are a behavioral evaluation layer. Both are useful, but they prove different things.
5. **Keep evidence and runtime status separate.** This batch can verify structure, source logic and declared validation/eval design. It cannot claim the tools actually work until representative workflows are executed in controlled environments.

## Validation boundary

No third-party installer, build, test suite, evaluation runner, external model CLI, API credential flow, browser/mobile session, Robot Framework execution, Zephyr build/hardware workflow, Jira/Slack/GitHub collector, or external SaaS was executed. All ten repositories are therefore recorded as `structure-reviewed`, with `runtime_validation: not_executed`.