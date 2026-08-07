# Agent Skills Deep Analysis — Batch 024

Observed: 2026-08-07
Status: `structure-reviewed`
Runtime validation: `not_executed`
Repositories completed: **10**
Repository-scoped skill reports: **23**

## Method

This batch used the existing indexed repository queue and completed ten qualified repositories. A repository was counted only after content-level inspection. Identity was verified through current GitHub repository metadata, exact stars were checked with GitHub repository search constrained to the repository owner/name and exact star count, and actual repository files were read: README/guide when present, current `SKILL.md` or equivalent definitions, and scripts/references/eval surfaces when available.

No repository was marked complete from index metadata alone. No third-party skill, CLI, test suite, API workflow, browser workflow, mobile build, Cloudflare request, or agent loop was executed in this batch. `structure-reviewed` therefore means source/content review only.

## Repositories

| Repository | GitHub repository ID | Default branch | Stars | Skill reports | Content-level classification |
|---|---:|---|---:|---:|---|
| `jeffy-w/AgentSkills` | 1257039210 | `main` | 2 | 2 | `skill_collection_tooling` |
| `juncaifeng/agentskills` | 1213345688 | `master` | 0 | 2 | `skill_authoring_collection` |
| `danecwalker/agentskills` | 1308852554 | `main` | 1 | 4 | `skill_collection_engineering` |
| `gustavhartz/agentskills` | 1309700550 | `main` | 0 | 1 | `single_skill_observability` |
| `cifuentescossio/agentskills` | 1139380541 | `main` | 0 | 1 | `single_skill_writing` |
| `DragonL641/AgentSkills` | 1151788458 | `main` | 0 | 1 | `single_skill_product_architecture_workflow` |
| `A2Y-D5L/agentskills` | 1315390178 | `main` | 0 | 1 | `single_skill_epic_orchestration` |
| `svier0/agentskills` | 1274244634 | `main` | 0 | 2 | `small_skill_collection_utilities` |
| `MarieEustace/AgentSkills` | 1174325091 | `main` | 1 | 8 | `skill_collection_coding_workflows` |
| `Eshwari07/AgentSkills` | 1179185595 | `main` | 0 | 1 | `single_skill_critical_reasoning` |

## Content-level findings

1. `jeffy-w/AgentSkills` is not merely a prompt collection. `ask` has a Node dispatcher that validates provider selection, optionally loads role prompts, launches local Claude/Gemini/Codex CLIs, constrains Codex to read-only mode, captures process output, and persists Markdown artifacts. `ios-device-build-run` has a Python helper with durable sessions, project/scheme/device discovery, build/run log separation, and bounded log retrieval. These implementation surfaces were read, not executed.
2. `juncaifeng/agentskills` currently has no usable root README in the inspected default branch, so its count was derived from actual skill paths rather than README claims. The repository contains `agentskill-builder` plus a standalone `agentskill-builder-lite`; the full version uses references for specification, best practices, evaluation, and trigger-description optimization.
3. `danecwalker/agentskills` contains four current production-oriented engineering skills. Its strongest recurring pattern is progressive disclosure: the entry `SKILL.md` keeps orchestration rules while references carry topology, token/theming, evaluation-board, rendering-stack, accessibility, and performance detail.
4. `gustavhartz/agentskills` contains one Cloudflare Worker observability skill plus a real TypeScript helper. Source inspection confirmed config discovery, target derivation, telemetry filtering/normalization, historical query construction, metrics mode, and Wrangler live-tail delegation. Cloudflare APIs were not called.
5. `cifuentescossio/agentskills` contains one focused grammar-review skill. It explicitly forbids full-document rewriting and protects code, identifiers, and project-specific terms from inappropriate corrections.
6. `DragonL641/AgentSkills` has one large `your-tech-panel` orchestration skill coordinating product, architecture, development, QA, and DevOps questioning. It has meaningful workflow structure but is context-heavy; much of the role/template detail could be split into references for progressive disclosure.
7. `A2Y-D5L/agentskills` contains one `epic` dispatcher with substantial reference and script infrastructure for resumable state, argument/config layering, locks/bounds, phase gates, reviewer polling, findings ledgers, and lesson capture. Source presence is not treated as proof that the orchestration works in a live environment.
8. `svier0/agentskills` has two current skills despite its minimal/empty README surface: `caveman` and `github-proxy`. `caveman` explicitly relaxes terseness for safety/irreversible/sequence-sensitive situations. `github-proxy` relies on third-party mirrors whose privacy, integrity, uptime, and operator trust were not independently established.
9. `MarieEustace/AgentSkills` contains eight current workflow files under `.agent/skills/`. Seven follow the common `name` + `description` frontmatter shape. `spec-interview/SKILL.md` currently lacks a `name` field, so it is best classified as an agent-specific workflow file rather than fully conformant portable Agent Skills metadata.
10. `Eshwari07/AgentSkills` contains one anti-sycophancy/critical-evaluation skill with supporting references and comparison artifacts. The repository's examples are demonstrations, not an executed reusable eval harness; research claims cited by the repository were not independently revalidated in this batch.

## Eval and validation boundary

No dedicated repository eval runner was verified for this batch. Some repositories document evaluation methodology or include comparison/example artifacts, especially `juncaifeng/agentskills`, `danecwalker/agentskills`, and `Eshwari07/AgentSkills`; those materials were treated as source evidence only, not as executed validation results.

Every repository and skill report in Batch 024 therefore remains:

```text
status: structure-reviewed
runtime_validation: not_executed
```

Individual repository-scoped reports are stored in `research/agent-skills/batches/2026-08-07-batch-024-skill-reports.md`.