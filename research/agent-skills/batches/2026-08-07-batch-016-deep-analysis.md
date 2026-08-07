# Agent Skills deep analysis — Batch 016

- Observed at: 2026-08-07 15:09 +08:00
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Repositories completed: **10**
- Repository-scoped individual skill reports: **77**
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`
- Rule: no repository in this batch is counted complete from metadata alone.

## Batch summary

| Repository | Displayed stars | Repository classification | Skill reports | Content evidence reviewed |
| --- | ---: | --- | ---: | --- |
| `c-kick/hnl-agent-skills` | 43 | `skill_collection` | 19 | README, complete top-level skill inventory, `user-review/SKILL.md`, `systematic-debugging/SKILL.md`, `bundles.conf`, shell manager/compatibility scripts |
| `bird-chinese-community/BIRD.skills` | 0 | `skill_collection` | 5 | README inventory, `bird-agent/SKILL.md`, `bird-source-explorer/SKILL.md`, evaluation documentation, `bird-agent/evals/evals.json` |
| `Conway-Research/skills` | 42 | `skill_collection` | 1 | README, `SKILLS.md`, `conway-cloud/SKILL.md` |
| `zeroclaw-labs/zeroclaw-skills` | 51 | `skill_collection` | 18 | README/spec contract, `registry.json`, `skills/code-reviewer/SKILL.md`, `.github/workflows/validate.yml` |
| `tinyhumansai/skill-registry` | 6 | `skill_collection` | 1 | `index.json`, `skills/git-summary/SKILL.md`, repository tree |
| `Jignesh-Ponamwar/skills-mcp` | 5 | `skill_tooling_with_bundled_collection` | 33 | README/category inventory, `master-skill/SKILL.md`, bundled `test-writer/SKILL.md`, `skills-lock.json`, validator, retrieval-calibration dataset |
| `aios-rs/skillhub` | 0 | `skill_tooling` | 0 | README, Rust CLI command implementation in `src/main.rs`, repository code search for local `SKILL.md` |
| `framerslab/agentos-skills-registry` | 0 | `skill_tooling` | 0 | README ecosystem boundary, `src/catalog.ts`, workspace discovery, Vitest catalog/loader tests, repository code search |
| `markusle56/Agent-Skills-Registry` | 0 | `skill_tooling` | 0 | README, architecture document, FastAPI upload/search/version route implementation, dependency surface, repository code search |
| `nvhuy249/agent-skills-registry` | 0 | `skill_tooling` | 0 | README, Express skill route implementation, package test commands, backend end-to-end smoke test, repository code search |

Displayed stars were read from the current GitHub repository pages during this run. No package-level or registry-internal `stars` field is substituted for repository stars.

## Repository findings

### 1. `c-kick/hnl-agent-skills`

Identity was verified as the public `c-kick/hnl-agent-skills` repository and the current repository tree exposes 19 top-level skill directories. The project is a local multi-agent skill manager rather than a flat prompt dump: the README documents shared installation into Claude Code and Codex paths, `bundles.conf` defines named bundles with recursive inheritance, and the shell manager resolves those bundles with cycle detection before creating links. The compatibility loader and full manager are separate scripts rather than one overloaded entry point.

`systematic-debugging/SKILL.md` was directly read and requires evidence gathering, pattern analysis, a single testable hypothesis, and only then implementation/verification. `user-review/SKILL.md` was also directly read and treats actual product observation as the basis for first-time-user review.

**Useful pattern:** keep skill content independent from installation/routing mechanics, and let bundles compose identities without duplicating skill bodies.

**Validation boundary:** no formal evaluation suite was surfaced in the reviewed repository surfaces; the manager scripts were read but not executed.

### 2. `bird-chinese-community/BIRD.skills`

The maintained README enumerates exactly five repository skills and documents a conventional `SKILL.md` plus optional scripts/references layout. Two bodies were directly read. `bird-agent` makes discovery read-only before any write path and delegates repeatable operations to BIRD tooling rather than teaching the model to guess configuration structure. `bird-source-explorer` requires source/revision evidence and gives exact-source evidence priority over generic documentation.

This repository also has a concrete evaluation system, not just prose claiming that evals exist. `docs/evaluation.md` defines a harness-neutral runner/request/artifact model, while `bird-agent/evals/evals.json` contains six named cases with expected outputs and file-based assertions covering safe discovery, syntax diagnosis, format preview, cross-file attribution, legacy-version boundaries, and config-name migration.

**Useful pattern:** eval cases test safety/behavioral boundaries as well as happy-path task output.

**Validation boundary:** the eval definitions were read; no eval runner was executed in this batch.

### 3. `Conway-Research/skills`

`SKILLS.md` distinguishes one currently available skill from planned work, so Batch 016 counts only `conway-cloud`. Its body was directly reviewed. The workflow prefers MCP, permits an HTTP fallback, performs prechecks, uses the minimum required cloud resources, and contains explicit API-key and destructive-operation guardrails.

**Useful pattern:** a small collection can maintain a separate current-vs-planned inventory so roadmap entries do not silently become catalog counts.

### 4. `zeroclaw-labs/zeroclaw-skills`

This is a repository-backed skill registry following the Agent Skills specification. The current `registry.json` contains 18 skill identities, and the README explicitly warns that CI structure/pattern scanning is not a security or correctness audit. That boundary is important because it prevents a passing registry check from being treated as proof that arbitrary third-party skill code is safe.

`code-reviewer/SKILL.md` was directly reviewed and gives a prioritized correctness/security/regression/design/maintainability/test workflow with explicit severity levels. The validation workflow checks registry JSON, required `SKILL.md` files, YAML/frontmatter shape, required metadata, allowed licenses, folder/name equality, registry/folder set equality, and duplicate names.

**Useful pattern:** distinguish schema/registry integrity from runtime trust; make that distinction explicit to users rather than implying that ingestion validation is a security certification.

### 5. `tinyhumansai/skill-registry`

The current registry is intentionally minimal: `index.json` contains one `agentskills` entry, `git-summary`, and its `SKILL.md` was directly read. The skill is explicitly read-only and uses Git commands to report branch, recent commits, working-tree changes, stashes, and remotes without modifying repository state.

**Useful pattern:** the machine-readable index and the actual skill body stay small enough to compare directly; there is no inflated external catalog count.

### 6. `Jignesh-Ponamwar/skills-mcp`

This repository combines an MCP-based semantic discovery service with a local bundled skill corpus. The maintained README currently inventories 32 bundled skills across core engineering, frameworks, document generation, AI APIs, cloud/DevOps, full-stack, services, and design. A separate root `master-skill/SKILL.md` defines the repository's progressive discovery/loading workflow, so the repository-scoped count is 33. `skills-lock.json` is a broader external source/hash lock and is deliberately not counted as the current local bundled corpus.

The repository's validator is substantive: it parses YAML, enforces schema/length/license rules, checks body references to `references/`, `scripts/`, and `assets/`, warns on weak retrieval metadata, and runs a prompt-injection scanner. `tests/eval/threshold_calibration.json` is a real retrieval calibration dataset with strong-match and no-skill cases across the bundled corpus. `test-writer/SKILL.md` was directly read as a representative bundled body.

**Documentation drift:** the README describes seven MCP tools including `list_all`, while the current `master-skill` prose says six and omits `list_all`. Batch 016 records this as documentation drift rather than guessing which count is authoritative for deployed MCP behavior.

**Useful pattern:** retrieval quality is treated as an engineering surface with metadata-quality validation and labeled calibration examples, not only vector-search implementation.

**Validation boundary:** validator and calibration files were inspected but not run.

### 7. `aios-rs/skillhub`

This indexed candidate is correctly treated as `skill_tooling`, not as a local skill collection. The README describes a Rust CLI for a remote SkillHub registry. Direct review of `src/main.rs` confirms a broad CLI surface for discovery, inspection, download/publish, local installation/update, stars/ratings, account/namespace operations, review/lifecycle operations, transfer, and admin commands. The source is separated into application, domain, infrastructure, and TUI modules.

Repository code search surfaced no local `SKILL.md`. Therefore this repository contributes **zero** individual skill reports; remote registry entries are not silently attributed to this source repository.

**Useful pattern:** client/tooling repositories should remain first-class catalog objects but must not inflate the skill-identity count.

**Validation boundary:** README mentions `cargo test`; no Rust build or tests were executed in this source-review batch.

### 8. `framerslab/agentos-skills-registry`

This repository is explicitly a **Catalog SDK**. Its README states that skill content lives in the separate `@framers/agentos-skills` repository/package, while this repository provides query helpers, lazy loading, factories, and workspace discovery. The documented 88 content skills therefore do not become individual reports for this repository.

`src/catalog.ts` resolves the external content package at runtime, lazily loads and parses skill frontmatter/body, and includes a YAML-backed fallback parser when the AgentOS peer dependency is unavailable. `src/workspace-discovery.ts` scans consuming workspaces for `.agents/skills/<name>/SKILL.md` and intentionally gives workspace-local names priority on collisions. `test/skills-registry.spec.ts` checks catalog/content-package count synchronization, query behavior, selected-skill lazy loading, typed metadata, and empty selections.

**Useful pattern:** separate content, catalog SDK, and runtime engine into distinct packages and test the synchronization boundary explicitly.

**Validation boundary:** repository tests were read, not executed.

### 9. `markusle56/Agent-Skills-Registry`

This repository is a full-stack registry application, not a repository of installable Agent Skill packages. The README describes upload/manage/share/version/clone workflows, React/Vite on the frontend, FastAPI/SQLite on the backend, and Markdown as the stored skill artifact. Repository code search surfaced no local `SKILL.md`, so the example block in the README is not counted as an individual skill.

The implementation was checked beyond the README. `backend/app/api/routes/mdfile.py` handles Markdown uploads, search, visibility, cloning, downloads, history, comparisons, and analytics. The reviewed upload route enforces a `.md` extension and receives `name`/`description` as form fields before persisting the file. The README claims automatic frontmatter parsing, but that behavior is **not demonstrated by the reviewed upload route itself**; it may exist deeper in CRUD/model code, so Batch 016 records this as an unresolved implementation/documentation question rather than asserting a defect.

**Useful pattern:** registry applications need separate evidence for content-package inventory versus product features; an example Markdown block is not a bundled skill.

**Validation boundary:** no executable test suite was surfaced in the reviewed search/dependency surfaces and no application was run.

### 10. `nvhuy249/agent-skills-registry`

This is another full-stack registry application with zero local `SKILL.md` packages surfaced by repository code search. Unlike the previous candidate, the skill ingestion path was directly verified in implementation: `backend/src/routes/skills.ts` uses `gray-matter`, requires a frontmatter `name`, extracts `description`, accepts both `allowed-tools` and `allowed_tools`, persists content and versions in SQLite, and applies owner/public checks when reading skills.

The root test command builds/runs the backend test and builds the frontend. `backend/test/smoke.test.js` is a real process-level smoke test: it starts the compiled API on a random local port with an isolated temporary SQLite database and exercises authentication, upload, private/public visibility, tags, downloading, versioning, and cloning with assertions.

**Useful pattern:** product claims about a registry are backed by a bounded end-to-end smoke flow that uses an isolated database and actual HTTP requests.

**Validation boundary:** the smoke test source was read but not executed in this batch.

## Individual report artifact

The 77 repository-scoped identities are recorded once each in:

- `research/agent-skills/batches/2026-08-07-batch-016-skill-reports-01.md`

Evidence labels used there:

- `direct-body-reviewed`: the current `SKILL.md`/equivalent body was directly read in this run.
- `catalog-verified`: the skill identity was verified from a repository-maintained complete inventory; representative bodies and repository support surfaces were directly read.

Four tooling repositories have zero repository-scoped skill definitions and therefore deliberately emit zero individual skill reports. External/package-provided, remotely hosted, user-uploaded, README-example, and dependency-owned skill identities are not reassigned to those repositories.

## Count reconciliation

```text
c-kick/hnl-agent-skills              19
bird-chinese-community/BIRD.skills    5
Conway-Research/skills                1
zeroclaw-labs/zeroclaw-skills        18
tinyhumansai/skill-registry           1
Jignesh-Ponamwar/skills-mcp          33
aios-rs/skillhub                      0
framerslab/agentos-skills-registry    0
markusle56/Agent-Skills-Registry      0
nvhuy249/agent-skills-registry        0
---------------------------------------
total                                77
```

## Validation boundary

This batch performed source/content review only. No third-party installer, cloud API, browser action, application server, build, test suite, evaluation runner, repository validator, or repository script was executed. The correct batch state is therefore `structure-reviewed`, with `runtime_validation: not_executed`.
