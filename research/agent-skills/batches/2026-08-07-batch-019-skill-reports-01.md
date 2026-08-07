# Agent Skills individual reports — Batch 019, part 01

- Observed at: 2026-08-07
- Batch: `2026-08-07-batch-019`
- Repository-scoped reports in this part: **105**
- Validation state: `structure-reviewed`
- Runtime validation: `not_executed`
- Counting rule: count current repository-scoped skill identities only. Internal authoring helpers/templates and duplicated distribution copies are not counted twice.

Evidence labels:

- `direct-body-reviewed`: the current `SKILL.md` body was directly read in this run.
- `inventory-verified`: identity and purpose were verified from a repository-maintained inventory or current repository file inventory; representative bodies/support surfaces were directly read.

## `beriberikix/zephyr-agent-skills` — 22 reports

The repository combines one root router skill with 21 current domain skills. `index.json`, `skill-meta.yaml`, catalog/marketplace generation, and `scripts/validate_skills.py` form a generated registry and consistency gate. The internal `.agent/skills/skill-creator` authoring helper is not counted as a public repository skill.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `zephyr-agent-skills` | direct-body-reviewed | Root router delegates selection to `zephyr-cli skills suggest`, then install/read/apply; it explicitly avoids guessing which domain skill to load. |
| `zephyr-index` | direct-body-reviewed | Human navigation fallback with catalog, decision tree, quick reference, keyword router, and explicit validation checklist. |
| `zephyr-foundations` | inventory-verified | Foundational Zephyr workflow guidance kept separate from individual build/devicetree/kernel domains. |
| `build-system` | inventory-verified | West workspace/manifests, Kconfig, CMake, and Sysbuild guidance with supporting references/scripts. |
| `devicetree` | inventory-verified | Devicetree/binding/overlay guidance with matcher metadata for task routing. |
| `native-sim` | inventory-verified | Native simulation workflow separated from hardware-specific bring-up. |
| `board-bringup` | inventory-verified | HWMv2 board definition/porting guidance with templates, references, and lint helper. |
| `zephyr-module` | inventory-verified | External/module integration guidance isolated from application build guidance. |
| `kernel-basics` | inventory-verified | Core scheduling/logging/shell workflow guidance. |
| `kernel-services` | inventory-verified | Advanced Zbus/SMF/work-queue/settings patterns separated from basic kernel use. |
| `hardware-io` | inventory-verified | GPIO/I2C/SPI/ADC/PWM/UART/sensor/pinctrl guidance with hardware matcher metadata. |
| `power-performance` | inventory-verified | Power/performance optimization as a distinct operational domain. |
| `connectivity-ble` | inventory-verified | BLE/GATT/GAP and power-related connectivity guidance. |
| `connectivity-ip` | inventory-verified | MQTT/CoAP/LwM2M/IP-stack and SDK-module integration guidance. |
| `connectivity-usb-can` | inventory-verified | USB-device/CAN integration guidance, including reusable assets and checks. |
| `storage` | inventory-verified | Persistent-storage/filesystem concerns isolated from kernel/settings guidance. |
| `testing-debugging` | inventory-verified | Testing and debugging workflows as an explicit lifecycle capability. |
| `security-updates` | inventory-verified | Security/update/OTA concerns separated from general application guidance. |
| `iot-protocols` | inventory-verified | OpenThread, Matter, LoRaWAN and cloud-oriented IoT integration guidance. |
| `multicore` | inventory-verified | SMP/AMP/IPC/multicore concerns treated as an advanced domain. |
| `industrial` | inventory-verified | Modbus/CANopen/industrial protocol guidance with domain-specific references. |
| `specialized` | inventory-verified | Specialist topics kept behind the common deterministic routing/index layer. |

## `antonarhipov/agentskills` — 9 reports

The repository has no umbrella README; the current root consists of nine skill directories. The first six form a traceable spec-driven pipeline; three additional skills cover PR ownership/review UX and Spring Batch 6.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `spec` | direct-body-reviewed | One-question-at-a-time requirements interview resolves ambiguities and emits stable behavior IDs before implementation. |
| `criteria` | direct-body-reviewed | Converts behavior IDs into EARS acceptance criteria with coverage and route-back rules for unresolved ambiguity. |
| `rules` | direct-body-reviewed | Captures technical design decisions and constraints traceable to acceptance criteria. |
| `spec-review` | direct-body-reviewed | Stress-tests seams among spec pipeline outputs and codebase before implementation. |
| `tasks` | direct-body-reviewed | Produces ordered atomic implementation tasks traceable to acceptance criteria. |
| `execute` | direct-body-reviewed | Executes approved tasks in order, validates each, and stops at checkpoints instead of silently rewriting the plan. |
| `defend-your-pr` | direct-body-reviewed | Two-stage review gates author comprehension/ownership before structural design review; critique is attached to code decisions rather than the person. |
| `review-prototype` | direct-body-reviewed | Method skill for verdict-first review surfaces intended to minimize unnecessary diff reading. |
| `spring-batch-6` | direct-body-reviewed | Focused Spring Batch 6 / Boot 4 implementation and migration reference separated from the generic spec pipeline. |

## `JayRHa/AgentSkills` — 74 reports

The README catalog still states 72 skills across 10 categories, but the current repository additionally contains `x-twitter-scraper/SKILL.md` and `skills/xquik-social-data/SKILL.md`. Both bodies were directly read, so this batch records **74 current user-facing skill identities**. `0-template/SKILL.md` is an authoring template and is excluded. The repository validator currently discovers top-level skill directories, so the nested `skills/xquik-social-data` identity is outside that validator's top-level scan; this is an inventory/validation drift risk rather than a runtime failure.

### Engineering

| Skill | Evidence | Finding |
| --- | --- | --- |
| `code-reviewer` | direct-body-reviewed | Diff-scoped correctness/security/maintainability review with intent discovery, minimal context, severity ranking, references/templates, and no fabricated line numbers. |
| `unit-test-author` | inventory-verified | Multi-language unit-test authoring with edge-case and maintainability emphasis. |
| `refactoring-guide` | inventory-verified | Incremental behavior-preserving refactoring protected by tests. |
| `debug-detective` | inventory-verified | Reproduce→isolate→hypothesize→bisect→verify debugging discipline. |
| `api-designer` | inventory-verified | REST/GraphQL API design with contracts, auth, pagination, errors, and idempotency. |
| `regex-architect` | inventory-verified | Regex design/testing with explicit catastrophic-backtracking/ReDoS awareness. |
| `sql-optimizer` | inventory-verified | Query-plan-led SQL diagnosis and index/query/schema tuning. |
| `dockerfile-pro` | inventory-verified | Multi-stage, reproducible and least-privilege Dockerfile authoring. |
| `git-workflow` | inventory-verified | Branching, atomic commits, rebase/conflict/reflog and recovery guidance. |
| `dependency-upgrader` | inventory-verified | Staged dependency upgrades with changelog reading, test gates, and rollback. |
| `performance-profiler` | inventory-verified | Measure/profile/change/benchmark workflow rather than intuition-led optimization. |
| `error-handling-patterns` | inventory-verified | Results/exceptions, retry/backoff, timeout, circuit-breaker and degradation patterns. |

### DevOps & Cloud

| Skill | Evidence | Finding |
| --- | --- | --- |
| `github-actions-builder` | inventory-verified | CI/CD workflow construction with caching, matrices, scoped secrets and concurrency. |
| `terraform-module-author` | inventory-verified | Typed reusable Terraform module design with versioning/state/validation discipline. |
| `kubernetes-manifest-author` | inventory-verified | Production manifest authoring with probes, resources and security contexts. |
| `nginx-config-pro` | inventory-verified | Reverse-proxy/TLS/cache/rate-limit/security-header configuration guidance. |
| `incident-postmortem` | inventory-verified | Blameless timeline/root-cause/action-item postmortem workflow. |
| `observability-setup` | inventory-verified | Logs/metrics/traces linked to SLI/SLO/error-budget/alert design. |
| `secrets-manager` | inventory-verified | Secret detection/handling/rotation and KMS/vault practices. |
| `bash-script-hardening` | inventory-verified | Strict-mode, quoting, traps, temp-file and signal-safe shell guidance. |
| `cron-scheduler` | inventory-verified | Cron/timer validation with timezone, DST, overlap and DOM/DOW semantics. |
| `aws-cost-optimizer` | inventory-verified | Cloud cost analysis focused on right-sizing, idle resources, commitments and tagging. |

### Data & ML

| Skill | Evidence | Finding |
| --- | --- | --- |
| `pandas-data-cleaning` | inventory-verified | End-to-end tabular cleaning, typing, missingness, dedupe/outlier and reshape guidance. |
| `sql-schema-designer` | inventory-verified | Relational schema/constraint/index design with ER/DDL output. |
| `data-pipeline-architect` | inventory-verified | ETL/ELT design covering idempotency, schema evolution, orchestration and quality. |
| `chart-chooser` | inventory-verified | Maps analytical question/data shape to an honest visualization specification. |
| `json-schema-author` | inventory-verified | Draft 2020-12/07 schema authoring and validation guidance. |
| `ab-test-analyzer` | inventory-verified | Experiment design, sample sizing, significance/CI/lift and common-analysis traps. |
| `prompt-engineer` | inventory-verified | Prompt design plus systematic evaluation and explicit output contracts. |
| `rag-pipeline-designer` | inventory-verified | Chunking/embedding/retrieval/reranking/prompt assembly with offline evaluation emphasis. |

### Writing & Communication

| Skill | Evidence | Finding |
| --- | --- | --- |
| `technical-writer` | inventory-verified | Audience/document-type-driven technical documentation with runnable examples. |
| `readme-generator` | inventory-verified | Structured project README generation with quickstart/config/contribution/license sections. |
| `changelog-keeper` | inventory-verified | Keep-a-Changelog/SemVer release-note maintenance. |
| `blog-post-writer` | inventory-verified | Technical blog structure focused on hook, examples and takeaway. |
| `release-notes-writer` | inventory-verified | Converts merged changes into user-facing grouped release notes. |
| `adr-author` | inventory-verified | Context/options/decision/consequences architecture decision records. |
| `email-composer` | inventory-verified | Audience/purpose/tone/call-to-action email drafting. |
| `meeting-summarizer` | inventory-verified | Decision/action-item-oriented meeting summary workflow. |
| `proofreader` | inventory-verified | Grammar/clarity/concision editing while preserving voice/meaning. |
| `api-docs-writer` | inventory-verified | REST reference/OpenAPI documentation with schemas, auth and errors. |
| `public-speaking-coach` | inventory-verified | Talk narrative, opening/closing, delivery, nerves and Q&A coaching. |
| `mermaid-diagram-builder` | inventory-verified | Version-controllable Mermaid diagram construction across common diagram families. |

### Productivity & Business

| Skill | Evidence | Finding |
| --- | --- | --- |
| `okr-writer` | inventory-verified | Outcome-oriented objectives and measurable key results. |
| `swot-analyzer` | inventory-verified | SWOT plus TOWS conversion into prioritized actions. |
| `project-planner` | inventory-verified | WBS, dependencies, estimates, critical path and risk planning. |
| `decision-matrix` | inventory-verified | Weighted option scoring with transparency and sensitivity analysis. |
| `presentation-builder` | inventory-verified | Single-message narrative arc, one-idea-per-slide, and speaker-note planning. |
| `user-story-writer` | inventory-verified | INVEST stories, Gherkin acceptance criteria and vertical slicing. |
| `competitive-analysis` | inventory-verified | Structured competitor/feature/pricing/SWOT/positioning analysis. |
| `job-description-writer` | inventory-verified | Inclusive outcome-oriented role descriptions with requirement tiering. |

### Security

| Skill | Evidence | Finding |
| --- | --- | --- |
| `threat-modeler` | inventory-verified | STRIDE-oriented data-flow decomposition and prioritized mitigations. |
| `security-auditor` | inventory-verified | OWASP-oriented source audit; source review in this batch does not validate exploitability claims. |
| `secure-password-policy` | inventory-verified | Modern authentication/password policy guidance aligned to stated standards. |
| `gdpr-data-mapper` | inventory-verified | Personal-data inventory/flow mapping and compliance-oriented documentation. |
| `vulnerability-triage` | inventory-verified | Vulnerability prioritization/triage workflow. |
| `secure-code-review` | inventory-verified | Security-focused code review distinct from the general code-review skill. |

### Career

| Skill | Evidence | Finding |
| --- | --- | --- |
| `resume-writer` | inventory-verified | Resume structuring and accomplishment-focused writing. |
| `cover-letter-writer` | inventory-verified | Role-targeted cover-letter workflow. |
| `interview-prep` | inventory-verified | Interview preparation and practice guidance. |
| `salary-negotiator` | inventory-verified | Compensation negotiation planning and communication. |

### Learning

| Skill | Evidence | Finding |
| --- | --- | --- |
| `concept-explainer` | inventory-verified | Progressive concept explanation and examples. |
| `flashcard-generator` | inventory-verified | Learning-card generation for retrieval practice. |
| `study-plan-builder` | inventory-verified | Time-bounded study-plan construction. |
| `language-tutor` | inventory-verified | Language-learning practice/tutoring workflow. |
| `book-summarizer` | inventory-verified | Structured book-summary and takeaway extraction. |

### Health

| Skill | Evidence | Finding |
| --- | --- | --- |
| `meal-plan-builder` | inventory-verified | Meal-plan construction; any health suitability still requires context beyond repository metadata. |
| `workout-planner` | inventory-verified | Exercise-plan workflow; source presence is not evidence of health outcome efficacy. |
| `habit-builder` | inventory-verified | Habit design/tracking workflow. |

### Home & Personal

| Skill | Evidence | Finding |
| --- | --- | --- |
| `trip-planner` | inventory-verified | Travel itinerary/planning workflow. |
| `personal-budget-planner` | inventory-verified | Personal budgeting workflow. |
| `event-planner` | inventory-verified | Event planning/logistics workflow. |
| `gift-advisor` | inventory-verified | Gift-selection workflow. |

### Current uncatalogued identities

| Skill | Evidence | Finding |
| --- | --- | --- |
| `x-twitter-scraper` | direct-body-reviewed | Xquik-backed X-data integration workflow; defaults to read-only, gates persistent/write/private operations on approval, treats X-authored content as untrusted, and requires current docs/OpenAPI instead of remembered endpoint shapes. |
| `xquik-social-data` | direct-body-reviewed | Nested Xquik integration skill covering REST/MCP/bulk/webhook/write workflows with approval, secret-handling, pagination and result-verification rules. Its nested location is outside the current top-level validator scan. |

## Part 01 count reconciliation

```text
beriberikix/zephyr-agent-skills  22
antonarhipov/agentskills           9
JayRHa/AgentSkills                74
------------------------------------
part 01 total                    105
```

## Validation boundary

This file records source/content review, not runtime verification. No Zephyr CLI, build, compiler, RTOS board, installer, test suite, external Xquik service, API credential, browser, or repository validation script was executed in this batch.