# GitHub Agent Skills Repository Index

## Current verified catalog

- Search queries completed:
  - `"agent skills" in:name,description`, pages `1-10`
  - `"codex skills" in:name,description`, pages `1-10`
  - `"claude skills" in:name,description`, pages `1-10`
  - `"mcp skills" in:name,description`, pages `1-10`
  - `"skill catalog" in:name,description`, pages `1-10`
  - `"skill registry" in:name,description`, pages `1-10`
  - `"agent skill" in:name,description`, pages `1-10`
  - `"agentskills cli" in:name,description`, page `1`
- Raw GitHub search hits: `706`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `710`
- Unique repositories after case-insensitive `owner/repository` deduplication: `647`
- Exact duplicates removed across current inputs: `63`
- New unique repositories added in this run: `6`
- Provisionally eligible for later deep analysis: `381`
- Held as adjacent or unclear search hits: `266`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.
- Skill-registry delta: [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json), `95` new repositories from `100` raw identities.
- Agent-skill delta: [`batches/agent-skill-pages-1-10.json`](batches/agent-skill-pages-1-10.json), `44` new repositories from `100` raw identities.
- AgentSkills-CLI delta: [`batches/agentskills-cli-search.json`](batches/agentskills-cli-search.json), `6` new repositories from `6` raw identities.

## This run

The focused `"agentskills cli" in:name,description` query returned `6` repository identities on page `1`.

- Already present in the prior `641`-repository catalog: `0`
- Added as new repositories: `6`
- Updated composed catalog: `647`

Each full `owner/repository` identity was searched against the existing `ai-handbook` catalog before insertion. No exact case-insensitive duplicates were found.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 0 | 0 |
| `single_skill_or_domain_package` | 1 | 1 |
| `awesome_index` | 0 | 0 |
| `skill_tooling` | 5 | 5 |
| `adjacent_search_hit` | 0 | 0 |
| `unclear_search_hit` | 0 | 0 |

New repository identities:

- `mysticmind/agentskills-cli`
- `alerundev/cloudtype-skill`
- `blackwell-systems/agentskills-cli`
- `liujilongObject/agentskills-client`
- `jahonn/agentskills-cli`
- `zhuyansen/agentskillshub-cli`

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 197 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 62 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 32 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 89 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, client, CLI, or runtime tooling. |
| `adjacent_search_hit` | 90 | Search hit is related to agents, MCP, Claude, Codex, catalogs, registries, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 176 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- AgentSkills-CLI batch artifact commit: `4fa0269bb7ded288e6f2f72eaa0dee3bd88b105d`.
- Composed latest-manifest commit: `d32029bc009d0b1e0b4053c06971e8dbbabff5fe`.
- The current batch contains `6` unique case-insensitive keys internally.
- Exact full-name searches found `0` identities in the prior `641`-repository catalog.
- Prior `641` plus `6` new repositories resolves to `647`.
- Classification totals resolve to `647` repositories.
- `381 + 266 = 647`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
