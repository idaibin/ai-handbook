# Agent Skills deep analysis — Batch 015

- Observed at: 2026-08-07 14:18 +08:00
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Repositories completed: **10**
- Repository-scoped individual skill reports: **274**
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`
- Rule: no repository in this batch is counted complete from metadata alone.

## Batch summary

| Repository | Displayed stars | Repository classification | Skill reports | Content evidence reviewed |
| --- | ---: | --- | ---: | --- |
| `jMerta/codex-skills` | 130 | `skill_collection` | 19 | `skills.json`, `plan-work/SKILL.md`, `scripts/check_invisible_chars.py`, README/tree |
| `kangarooking/kangarooking-skills` | 438 | `skill_collection` | 13 | README inventory, `harness-engineering/SKILL.md`, `task-harness/SKILL.md`, scaffold script |
| `keinsaasforever/gtm-pipeline-skills` | 64 | `skill_collection` | 10 | README, `skills/gtm-pipeline/SKILL.md`, `docs/ARCHITECTURE.md`, skills directory |
| `Tyuts/xiaobai-skills` | 47 | `skill_collection` | 2 | README, root `SKILL.md`, repo-local `self-improving-agent`, installer script |
| `lordsarcastic/skills` | 10 | `skill_collection` | 6 | README, `build-my-apps`, `build-microservices`, installer script |
| `ReScienceLab/opc-skills` | 1.3k | `skill_collection` | 10 | README inventory, `archive`, `seo-geo`, references/scripts contract |
| `jezweb/claude-skills` | 805 | `skill_collection` | 60 | current README inventory, `SKILL_SHAPE.md`, `project-docs/SKILL.md`, repo conventions |
| `Jeffallan/claude-skills` | 10.9k | `skill_collection` | 66 | `SKILLS_GUIDE.md`, `architecture-designer/SKILL.md`, `scripts/validate-skills.py` |
| `oaustegard/claude-skills` | 137 | `skill_collection` | 87 | marketplace inventory, `verifying-claims/SKILL.md`, deterministic context bundler, report reference |
| `vercel-labs/skills` | 28.2k | `skill_tooling` | 1 | README, only current `skills/find-skills/SKILL.md`, discovery parser, add-command tests |

Stars are the GitHub-displayed values observed during this run. Abbreviated GitHub displays (`1.3k`, `10.9k`, `28.2k`) are preserved rather than converted into invented exact counts.

## Repository findings

### 1. `jMerta/codex-skills`

Identity was verified as the public `jMerta/codex-skills` repository. The maintained `skills.json` is a useful machine-readable catalog and declares 19 skills across development, documentation, operations, and planning. It also records provenance for imported skills rather than presenting every entry as first-party. `plan-work/SKILL.md` uses a repo-research → analysis → question gate → implementation-plan flow and explicitly anchors plans in repository files and external authoritative documentation when needed. `scripts/check_invisible_chars.py` is a deterministic repository hardening utility that scans path names, text, diffs, and Unicode control/invisible characters without executing scanned code.

**Useful pattern:** machine-readable skill inventory with provenance plus deterministic repository hygiene tooling.

### 2. `kangarooking/kangarooking-skills`

The current README enumerates 13 skills. The collection mixes media/content workflows with agent-engineering workflows, and the repository documents the conventional `SKILL.md` + optional `references/`, `scripts/`, and `assets/` structure. `harness-engineering` is scaffold-oriented: it generates planner/generator/evaluator roles, commands, hooks, contracts, and documentation; the reviewed scaffold script preserves existing files unless explicitly replaced and merges settings rather than blindly replacing the whole settings document. `task-harness` uses JSON as the task state source, a progress log, an initialization script, and explicit verification-before-completion rules.

**Useful pattern:** persistent task state and machine-verifiable acceptance gates for long-running agents.

### 3. `keinsaasforever/gtm-pipeline-skills`

The repository contains 10 current GTM pipeline skill packages under `skills/gtm-*`. The actual orchestrator skill was read, not inferred from the README. Its design is a staged pipeline with explicit CSV handoffs, cost/quality checkpoints, and user approval before paid provider steps. `docs/ARCHITECTURE.md` documents Company-First and Signal-First flows and the exact files passed between stages. The README also establishes privacy boundaries: API keys and local identifiers stay in ignored local configuration; contact lists, CRM exports, client names/domains, and commercial terms are not intended to be committed.

**Useful pattern:** explicit artifact handoffs and budget/quality gates between composable skills.

### 4. `Tyuts/xiaobai-skills`

Two repository skill definitions were counted: the root `xiaobai-skills` curator and the repo-local `skills/self-improving-agent`. The root skill intentionally chooses one default per need and backs alternatives up rather than deleting them. The PowerShell installer confirms that behavior, writes an inventory, skips existing installs unless `-Force` is supplied, and moves selected alternatives to a dated backup tree. The self-improving skill is deliberately repo-local and only activates after meaningful repeated friction or feedback rather than after every task.

**Useful pattern:** reversible skill-library curation with a written inventory; narrowly scoped self-improvement instead of permanent reflection loops.

### 5. `lordsarcastic/skills`

The README lists six instruction packs, each with `SKILL.md` as source of truth and optional `agents/openai.yaml`. `build-my-apps` defines cross-stack defaults, request-level observability, explicit API/data boundaries, documentation, testing, and deployment conventions; `build-microservices` makes service identity, permission contracts, manifests, registration, API contracts, and generated clients explicit. The installer enumerates top-level skill directories and asks before replacing the destination copies.

**Concrete portability issue:** `build-my-apps` includes an author-local absolute Temporal reference under `/Users/lordsarcastic/...`; that reference is not portable to other environments and should be treated as a local convention, not a generally resolvable dependency.

### 6. `ReScienceLab/opc-skills`

The maintained README enumerates 10 current skills and documents inter-skill dependencies. Direct reads included `archive` and `seo-geo`. `archive` uses a local `.archive/` hierarchy plus `MEMORY.md` as a cross-session index and requires concise, searchable records. `seo-geo` demonstrates progressive disclosure through scripts, references, and examples rather than placing every supporting detail in one file.

**Useful pattern:** explicit dependency declarations and a small canonical `SKILL.md` surface backed by optional references/scripts/examples.

### 7. `jezweb/claude-skills`

The current top-level inventory states **10 plugins / 60 skills** and enumerates all 60. The repository's `SKILL_SHAPE.md` treats `SKILL.md` as an execution contract: critical-path information stays inline; optional/variant material moves to references with explicit load triggers; recurring deterministic logic belongs in scripts. `project-docs/SKILL.md` was directly reviewed and requires documentation to reflect actual code, versions, routes, schemas, and configuration rather than aspirational architecture.

**Documentation drift:** the current README headline/table says 10 plugins / 60 skills, while the README history section still labels v13 as “current” with 11 plugins / 52 skills. Batch 015 uses the current explicit 60-skill inventory and records the stale history statement as drift instead of averaging the counts.

### 8. `Jeffallan/claude-skills`

`SKILLS_GUIDE.md` enumerates 66 repository skills across language, backend, frontend/mobile, infrastructure, API/architecture, quality, DevOps, security, data/ML, platform, specialized, and workflow categories. `architecture-designer/SKILL.md` was directly read: it uses requirements → pattern selection → design → ADR documentation → review, with optional references loaded by topic. `scripts/validate-skills.py` validates structure, YAML/frontmatter, metadata, reference/cross-reference consistency, workflow definitions, and catalog count consistency, with machine-readable JSON output support.

**Useful pattern:** repository-level validator that checks both per-skill contracts and cross-file catalog consistency.

### 9. `oaustegard/claude-skills`

The current `.claude-plugin/marketplace.json` defines 11 plugin groups whose keyword inventories resolve to **87 repository skill identities**. `verifying-claims/SKILL.md` was directly reviewed. Its notable boundary is explicit: deterministic tests own behavioral gating, while the skill performs fallible semantic prose-vs-code-vs-test review. `scripts/gather_context.py` uses Python AST parsing without importing target modules, and the bundled reference demonstrates PASS / FAIL / UNSUPPORTED / STALE reporting.

**Useful pattern:** clean separation between deterministic evidence gathering and non-deterministic semantic review.

### 10. `vercel-labs/skills`

This repository is primarily the **Skills CLI/tooling implementation**, not a catalog comparable to `vercel-labs/agent-skills`; Batch 015 therefore reclassifies it to `skill_tooling`. The current `skills/` directory contains one bundled public skill, `find-skills`, which was directly read and is counted as one individual report. `src/skills.ts` implements recursive skill discovery, frontmatter validation, duplicate-name handling, internal-skill filtering, plugin-manifest integration, and path-traversal protection. `src/add.test.ts` contains install/list/filter/path-deduplication regression tests using temporary skill fixtures.

**Classification correction:** repository-level role = `skill_tooling`; bundled skill count = 1. Do not treat this repository as the separate `vercel-labs/agent-skills` skill collection.

## Individual report artifacts

The 274 repository-scoped identities are recorded once each in:

- `research/agent-skills/batches/2026-08-07-batch-015-skill-reports-01.md`
- `research/agent-skills/batches/2026-08-07-batch-015-skill-reports-02.md`
- `research/agent-skills/batches/2026-08-07-batch-015-skill-reports-03.md`

Evidence labels used there:

- `direct-body-reviewed`: the current `SKILL.md`/equivalent body was directly read in this run.
- `catalog-verified`: the skill identity was verified from a repository-maintained complete inventory; representative bodies and repository support surfaces were directly read.

These labels intentionally do **not** imply that every large-catalog skill body was read line-by-line.

## Validation boundary

This batch performed source/content review only. No third-party installer, cloud API, browser action, build, test suite, evaluation suite, or repository script was executed. Therefore the batch state is `structure-reviewed`, with `runtime_validation: not_executed`.
