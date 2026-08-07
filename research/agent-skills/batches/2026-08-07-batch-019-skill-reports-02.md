# Agent Skills individual reports — Batch 019, part 02

- Observed at: 2026-08-07
- Batch: `2026-08-07-batch-019`
- Repository-scoped reports in this part: **94**
- Validation state: `structure-reviewed`
- Runtime validation: `not_executed`
- Counting rule: count canonical repository-scoped skill identities once; duplicated packaging/framework copies are not counted twice.

Evidence labels:

- `direct-body-reviewed`: the current `SKILL.md` body was directly read in this run.
- `inventory-verified`: identity and purpose were verified from repository-maintained/current file inventory; representative bodies and support surfaces were directly read.

## `LeoYeAI/teammate-skill` — 1 report

| Skill | Evidence | Finding |
| --- | --- | --- |
| `create-teammate` | direct-body-reviewed | End-to-end teammate-knowledge distillation workflow with source ingestion, Work Skill + layered persona generation, evolution/versioning and mandatory output quality gates. The repository also includes `privacy_guard.py`, a regex-based PII/secret scanner/redactor; it is a useful guard but cannot be treated as a complete privacy guarantee. |

## `jonkiky/agentskills` — 24 reports

The canonical current identities are under `skills/`. `QA-framework/skills/` contains duplicate copies of several of these plus separate `.agent.md` agent definitions, so those duplicates are not double-counted. The README describes `skills-lock.json` as version tracking, but a fetch of the current root `skills-lock.json` returned 404; this is recorded as a repository-state/documentation mismatch rather than silently assuming the lockfile exists.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `image-comparison` | inventory-verified | Image comparison capability; a duplicated QA-framework copy exists and is not counted twice. |
| `site-crawl` | inventory-verified | Site crawling/discovery capability with a duplicated QA-framework distribution copy. |
| `git-commit` | inventory-verified | Git commit workflow packaged as an installable skill. |
| `code-reviewer` | inventory-verified | General code-review workflow in the installed-skill collection. |
| `scanning-docker-images-with-trivy` | inventory-verified | Container-image vulnerability scanning workflow with supporting reference material. |
| `git-commit-push` | inventory-verified | Commit-and-push workflow distinct from commit-only guidance. |
| `superpowers-executing-plans` | inventory-verified | Imported/adapted plan-execution workflow; provenance/duplication should remain explicit when aggregating catalogs. |
| `bio-ai-product-manager` | inventory-verified | Domain product-management skill with an OpenAI agent metadata surface. |
| `implementation-executor` | inventory-verified | Implementation execution workflow separated from planning. |
| `email-generator` | inventory-verified | Email-generation workflow in the shared collection. |
| `requirements-to-plan` | direct-body-reviewed | Planning-only workflow that separates Observed/Inferred/Unknown, maps current code leverage, compares alternatives, builds impact/validation/rollback handoff, and explicitly avoids source edits. |
| `codebase-doc-writer` | inventory-verified | Codebase documentation capability with agent metadata. |
| `os-vulnerability-fix` | inventory-verified | OS vulnerability remediation workflow; source presence does not establish patch correctness. |
| `biotech-requirements-review` | inventory-verified | Biotech-specific requirements review, also duplicated in QA-framework. |
| `scan-website-to-prd` | inventory-verified | Website discovery-to-PRD workflow, also duplicated in QA-framework. |
| `brainstorming` | inventory-verified | Brainstorming workflow with an additional visual-companion artifact. |
| `snyk-fix` | inventory-verified | Snyk remediation workflow with supporting README/reference surface. |
| `superpowers-writing-plans` | inventory-verified | Imported/adapted planning workflow; should retain provenance when reused. |
| `junit5-spring-testing` | inventory-verified | JUnit 5/Spring testing guidance with OpenAI agent metadata. |
| `technical-interview-question-generator` | inventory-verified | Structured technical interview question generation. |
| `tpm-jira-status-reporting-skill` | inventory-verified | TPM/Jira status-reporting workflow. |
| `site-snapshots` | inventory-verified | Website snapshot workflow with a QA-framework duplicate copy. |
| `test-case-generation-workflow` | direct-body-reviewed | Requirement readiness → test design → data needs → traceability/coverage → human QA handoff; keeps generated cases draft until human review. |
| `playwright-generate-test` | inventory-verified | Playwright test-generation workflow duplicated into QA-framework distribution. |

## `PramodDutta/agentskills` — 15 reports

The README organizes 14 manual-testing skills across STLC phases plus one Playwright locator-repair skill. The directly reviewed test-plan skill uses a mandatory human-review gate and a minimal `curl` + `jq` Jira fetch helper that takes credentials from environment variables.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `jira-requirement-analyzer` | inventory-verified | Requirements analysis at STLC intake. |
| `test-plan-generator` | direct-body-reviewed | Jira/story → gap analysis → draft test plan with traceability, no fabricated acceptance criteria, and mandatory human sign-off. |
| `test-scenario-designer` | inventory-verified | Test-scenario design separated from plan generation. |
| `api-test-designer` | inventory-verified | API test design as a distinct STLC capability. |
| `test-case-writer` | inventory-verified | Detailed test-case writing after scenario design. |
| `test-data-generator` | inventory-verified | Test-data generation separated from case authoring. |
| `automation-script-generator` | inventory-verified | Automation script generation as an implementation phase. |
| `regression-suite-selector` | inventory-verified | Regression scope selection isolated from test execution. |
| `test-execution-tracker` | inventory-verified | Test execution/status tracking workflow. |
| `bug-reporter` | inventory-verified | Structured defect-report generation. |
| `bug-triage-assistant` | inventory-verified | Defect triage/prioritization workflow. |
| `rca-analyzer` | inventory-verified | Root-cause analysis after defects/failures. |
| `test-coverage-analyzer` | inventory-verified | Coverage analysis as a closure/quality signal. |
| `test-closure-reporter` | inventory-verified | Test closure reporting at the end of the STLC flow. |
| `pw-locator-fixer` | inventory-verified | Playwright locator repair kept separate from the manual-testing STLC chain. |

## `olgasafonova/SkillCheck-Free` — 1 report

| Skill | Evidence | Finding |
| --- | --- | --- |
| `skill-check` | direct-body-reviewed | Read-only SKILL.md validator covering frontmatter, naming, descriptions, structure and semantic/design rules while explicitly separating agentskills spec fields, Claude extensions and community extensions. Its deterministic/heuristic rules are static quality signals, not empirical proof that an agent will perform well. |

## `Daoming-Chen/AgentSkills` — 2 reports

| Skill | Evidence | Finding |
| --- | --- | --- |
| `prune-abstraction` | direct-body-reviewed | Refactor workflow targets semantic density rather than line count, repeatedly audits helper topology, preserves real domain/invariant boundaries, and validates only after the prune loop converges. |
| `ask-claude` | direct-body-reviewed | Explicit-only external-model delegation via Claude CLI with minimal-context handoff, git-status checks and failure honesty. It depends on local CLI/model/permission semantics, so portability and permission behavior remain runtime/environment risks. |

## `TrogonStack/agentskills` — 39 reports

The repository is a plugin-oriented skill system. `docs/skill-authoring-guide.md` defines frontmatter/routing/workflow/checklist guidance, including negative routing boundaries; GitHub workflows include plugin and frontmatter validation. `.agents/skills/scaffold-plugin` is an internal authoring helper and is not included in the 39 public plugin skill identities.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `diataxis-gen-readme` | inventory-verified | Diataxis-oriented README generation. |
| `ask-question` | inventory-verified | Focused question/clarification workflow. |
| `otel-name-span` | inventory-verified | OpenTelemetry span naming guidance. |
| `gh-enrich-pr-description` | inventory-verified | GitHub PR-description enrichment with a distinct routing boundary. |
| `otel-name-metric` | inventory-verified | OpenTelemetry metric naming guidance. |
| `event-definition` | inventory-verified | Event definition workflow with quality and boundary references. |
| `diataxis-organize-docs` | inventory-verified | Reorganizes existing docs by Diataxis type. |
| `nats-design-subject` | inventory-verified | NATS subject design with patterns, JetStream and security references. |
| `prd-personas` | inventory-verified | Persona section authoring inside the product-requirements suite. |
| `frd-review` | inventory-verified | Functional-requirements review. |
| `frd-split` | inventory-verified | Functional-requirements decomposition/splitting. |
| `prd-review` | direct-body-reviewed | Audits default/custom PRD files for completeness, source-of-truth conflicts, module-boundary drift and downstream impact with explicit Pass/Gap/Risk/Missing/N/A checks. |
| `frd-write` | inventory-verified | Functional-requirements authoring. |
| `prd-current-state` | inventory-verified | Current-state product documentation. |
| `eventmodeling-plotting-events` | inventory-verified | Event-model plotting step. |
| `prd-getting-started` | inventory-verified | Entry workflow for the PRD suite. |
| `prd-custom-overview` | inventory-verified | Custom product-overview document authoring with suite boundaries. |
| `datadog-design-dashboard` | inventory-verified | Datadog dashboard design. |
| `frd-getting-started` | inventory-verified | Entry workflow for functional requirements. |
| `prd-success-metrics` | inventory-verified | Product success-metric definition. |
| `prd-business-problem` | inventory-verified | Business-problem definition. |
| `prd-product-description` | inventory-verified | Product-description authoring. |
| `eventmodeling-translating-external-events` | inventory-verified | External-event translation in event models. |
| `prd-technical-requirements` | inventory-verified | Product-level technical requirements. |
| `eventmodeling-integrating-legacy-systems` | inventory-verified | Legacy-system integration in event-model design. |
| `eventmodeling-identifying-inputs` | inventory-verified | Input identification step. |
| `eventmodeling-slicing-event-models` | inventory-verified | Event-model slicing/decomposition. |
| `eventmodeling-storyboarding-events` | inventory-verified | Event storyboard step. |
| `eventmodeling-optimizing-stream-design` | inventory-verified | Stream-design optimization. |
| `eventmodeling-identifying-outputs` | inventory-verified | Output identification step. |
| `eventmodeling-applying-conways-law` | inventory-verified | Team/architecture boundary analysis using Conway's law. |
| `eventmodeling-brainstorming-events` | inventory-verified | Event discovery/brainstorming. |
| `requirements-operating-model` | inventory-verified | Shared source-of-truth/module-boundary operating model used across requirements skills. |
| `eventmodeling-orchestrating-event-modeling` | inventory-verified | Orchestrates the event-modeling workflow across specialized steps. |
| `eventmodeling-checking-completeness` | inventory-verified | Completeness gate for event models. |
| `eventmodeling-elaborating-scenarios` | inventory-verified | Scenario elaboration. |
| `eventmodeling-designing-event-models` | inventory-verified | Core event-model design workflow. |
| `eventmodeling-validating-event-models` | inventory-verified | Event-model validation workflow. |
| `eventmodeling-validating-event-models-checklist` | inventory-verified | Checklist-oriented validation companion kept separate from the main validator. |

## `manykarim/robotframework-agentskills` — 12 reports

The README's explicit table contains 12 skills: six library-reference skills and six script-based skills. A nearby prose sentence says “5 library-reference + 6 script-based”, which sums to 11 and conflicts with the table/current files; this batch uses the explicit 12-row inventory. The repository also contains an installer for multiple agent hosts, plugin/hooks/MCP surfaces, tests, and a dedicated `rf-skill-eval` harness. `eval/tasks/README.md` defines narrow/realistic/adversarial tiers, fresh-fixture headless sessions, deterministic grader checks, an externally grounded primary metric, tool/model/turn/time bounds, and historical regression canaries. None of those evals were executed in this batch.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `rf-browser` | direct-body-reviewed | Robot Framework Browser Library/Playwright reference covering browser-context-page hierarchy, auto-waiting, locators, assertions and common web-test operations. |
| `rf-selenium` | inventory-verified | SeleniumLibrary reference skill with supporting WebDriver/JavaScript references. |
| `rf-appium` | inventory-verified | AppiumLibrary/mobile-testing reference skill. |
| `rf-requests` | inventory-verified | RequestsLibrary/API testing reference skill. |
| `rf-restinstance` | inventory-verified | RESTinstance/JSON-schema-oriented API testing reference with troubleshooting docs. |
| `rf-platynui` | inventory-verified | Preview native desktop UI testing reference; repository records separate OpenSpec design/change history for it. |
| `rf-keyword-builder` | inventory-verified | Script-backed Robot Framework user-keyword generator. |
| `rf-testcase-builder` | inventory-verified | Script-backed test-case generator. |
| `rf-resource-architect` | inventory-verified | Script-backed resource/variable-file architecture generator. |
| `rf-libdoc-search` | inventory-verified | Libdoc-backed keyword search skill with script implementation. |
| `rf-libdoc-explain` | inventory-verified | Libdoc-backed keyword argument/documentation explanation. |
| `rf-results` | inventory-verified | Parses Robot Framework `output.xml` into structured summaries; repository documentation states Robot Framework dependency. |

## Part 02 count reconciliation

```text
LeoYeAI/teammate-skill               1
jonkiky/agentskills                 24
PramodDutta/agentskills             15
olgasafonova/SkillCheck-Free         1
Daoming-Chen/AgentSkills             2
TrogonStack/agentskills             39
manykarim/robotframework-agentskills 12
--------------------------------------
part 02 total                       94
```

## Validation boundary

This file records source/content review, not runtime verification. No Slack/GitHub/Jira collector, privacy redactor, external Claude CLI, plugin installer, MCP server, Robot Framework suite, browser/mobile/API test, evaluation runner, CI workflow, or external service was executed. Source files and eval definitions were read; claimed behavior is not promoted to runtime-verified status.