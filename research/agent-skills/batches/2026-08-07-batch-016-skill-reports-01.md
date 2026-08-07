# Agent Skills deep analysis — Batch 016 individual reports

- Batch: `2026-08-07-batch-016`
- Repository-scoped skill identities: **77**
- Evidence labels:
  - `direct-body-reviewed`: the current `SKILL.md`/equivalent body was directly read in this run.
  - `catalog-verified`: the skill identity was verified from a repository-maintained complete inventory; representative bodies and repository support surfaces were directly read.
- Boundary: `catalog-verified` does not mean every skill body was read line-by-line.
- Runtime validation: `not_executed`.

## `c-kick/hnl-agent-skills` — 19

The current top-level repository inventory contains 19 skill directories. `user-review` and `systematic-debugging` were directly read; the remaining identities were verified from the complete repository tree and the repository's bundle/install surfaces.

| Skill | Evidence | Report |
| --- | --- | --- |
| `browser-eyeballs` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `bug-hunter` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `commit-message-this` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `commit-message` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `critical-mode` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `factual-mode` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `hostile-review` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `humanize` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `i18n-standards` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `js-standards` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `php-documentation-standards` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `project-ambassador` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `reflect` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `sanity-check` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `scss-standards` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `spec-website` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `staff-review` | `catalog-verified` | Identity confirmed from the current top-level skill inventory. |
| `systematic-debugging` | `direct-body-reviewed` | Four-phase root-cause workflow: investigate evidence, analyze patterns, test one hypothesis at a time, then implement and verify the fix. |
| `user-review` | `direct-body-reviewed` | First-time-user review workflow that emphasizes observing the actual product experience and reporting concrete UX friction. |

## `bird-chinese-community/BIRD.skills` — 5

The README maintains a five-skill inventory. `bird-agent` and `bird-source-explorer` were directly read; the repository's evaluation documentation and `bird-agent/evals/evals.json` were also inspected.

| Skill | Evidence | Report |
| --- | --- | --- |
| `bird-agent` | `direct-body-reviewed` | BIRD configuration workflow with read-only discovery before writes, explicit validation, and safety gates. |
| `bird-source-explorer` | `direct-body-reviewed` | Source/revision-oriented investigation workflow that prioritizes exact repository evidence over generic assumptions. |
| `bird-troubleshooting` | `catalog-verified` | Identity and purpose verified from the maintained five-skill README inventory. |
| `birdcc-installer` | `catalog-verified` | Identity and purpose verified from the maintained five-skill README inventory. |
| `birdcc-cicd` | `catalog-verified` | Identity and purpose verified from the maintained five-skill README inventory. |

## `Conway-Research/skills` — 1

`SKILLS.md` lists one currently available skill; planned items were not counted.

| Skill | Evidence | Report |
| --- | --- | --- |
| `conway-cloud` | `direct-body-reviewed` | Operates Conway Cloud sandboxes with MCP preferred, HTTP fallback, prechecks, minimal-resource execution, teardown guidance, and secret/destructive-action guardrails. |

## `zeroclaw-labs/zeroclaw-skills` — 18

The current `registry.json` contains 18 repository skill identities. The registry metadata is used only as repository-scoped inventory; its per-skill `stars` fields are not GitHub repository-star counts. `code-reviewer` was directly read and the repository validation workflow was inspected.

| Skill | Evidence | Report |
| --- | --- | --- |
| `auto-coder` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `web-researcher` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `telegram-assistant` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `discord-moderator` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `code-reviewer` | `direct-body-reviewed` | Structured review workflow ordered around correctness, security, regression risk, architecture, maintainability, performance, and tests, with explicit severities. |
| `zeroclaw-simplify-review` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `data-analyst` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `doc-writer` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `api-tester` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `knowledge-base` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `email-responder` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `git-assistant` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `self-improving-agent` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `multi-agent-router` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `slack-connector` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `inboxapi` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `x-twitter-scraper` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |
| `sql-executor` | `catalog-verified` | Identity verified from current `registry.json`; body not directly read in this batch. |

## `tinyhumansai/skill-registry` — 1

The current `index.json` contains exactly one skill.

| Skill | Evidence | Report |
| --- | --- | --- |
| `git-summary` | `direct-body-reviewed` | Read-only Git repository summary using branch, recent commits, status, stashes, and remotes; explicitly prohibits state changes. |

## `Jignesh-Ponamwar/skills-mcp` — 33

Count reconciliation: the README's current bundled category inventory contains **32** skills under `skill_mcp/skills_data/`; the repository also contains a separate root `master-skill/SKILL.md` meta-skill, producing **33 repository-scoped reports**. `skills-lock.json` tracks a broader external source/hash set and is not treated as the local bundled inventory. `master-skill` and `test-writer` were directly read.

| Skill | Evidence | Report |
| --- | --- | --- |
| `master-skill` | `direct-body-reviewed` | Meta-skill for the repository's progressive MCP discovery/loading workflow. |
| `api-integration` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `code-review` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `data-analysis` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `git-commit-writer` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `readme-writer` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `sql-query-writer` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `test-writer` | `direct-body-reviewed` | Testing skill covering unit, integration, and endpoint tests, deterministic isolation, edge/error cases, and multiple language test frameworks. |
| `web-scraper` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `django-web-framework` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `vue-framework` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `docx-creator` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `pdf-processing` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `pptx-creator` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `xlsx-creator` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `claude-api` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `gemini-api` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `openai-api` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `llm-prompt-engineering` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `mcp-server-builder` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `cloudflare-workers` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `docker-containerization` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `github-actions` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `terraform` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `nextjs-best-practices` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `react-best-practices` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `fastapi` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `graphql-api` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `typescript-patterns` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `stripe-integration` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `supabase-integration` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `frontend-design` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |
| `web-artifacts-builder` | `catalog-verified` | Bundled identity verified from the maintained README category inventory. |

## Tooling repositories with zero local skill definitions

The following four repositories were deeply reviewed as **registry/tooling implementations**. Repository/code search found no repository-scoped `SKILL.md` content packages in these repositories, so zero individual skill reports are emitted rather than counting remote, user-uploaded, or dependency-provided skills as local artifacts.

| Repository | Local skill reports | Evidence boundary |
| --- | ---: | --- |
| `aios-rs/skillhub` | 0 | Rust SkillHub CLI implementation; current repository content is client/tooling code and no `SKILL.md` was surfaced. |
| `framerslab/agentos-skills-registry` | 0 | Catalog SDK; its documented 88 skills live in the separate `@framers/agentos-skills` content repository and are not counted here. |
| `markusle56/Agent-Skills-Registry` | 0 | Full-stack upload/share registry app; no repository-scoped `SKILL.md` package was surfaced. The README's skill block is an example format, not a local package. |
| `nvhuy249/agent-skills-registry` | 0 | Full-stack upload/version/share registry app; no repository-scoped `SKILL.md` package was surfaced. Its example skill is test/input documentation, not a local package. |

## Count check

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
