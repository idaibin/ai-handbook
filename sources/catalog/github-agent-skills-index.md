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
  - `"skill marketplace" in:name,description`, pages `1-10`
  - `"agent skills hub" in:name,description`, pages `1-2`
- Raw GitHub search hits: `826`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `830`
- Unique repositories after case-insensitive `owner/repository` deduplication: `763`
- Exact duplicates removed across current inputs: `67`
- New unique repositories added in this run: `20`
- Provisionally eligible for later deep analysis: `480`
- Held as adjacent or unclear search hits: `283`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.
- Skill-registry delta: [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json), `95` new repositories from `100` raw identities.
- Agent-skill delta: [`batches/agent-skill-pages-1-10.json`](batches/agent-skill-pages-1-10.json), `44` new repositories from `100` raw identities.
- AgentSkills-CLI delta: [`batches/agentskills-cli-search.json`](batches/agentskills-cli-search.json), `6` new repositories from `6` raw identities.
- Skill-marketplace delta: [`batches/skill-marketplace-pages-1-10.json`](batches/skill-marketplace-pages-1-10.json), `96` new repositories from `100` raw identities.
- Agent-skills-hub delta: [`batches/agent-skills-hub-pages-1-2.json`](batches/agent-skills-hub-pages-1-2.json), `20` new repositories from `20` raw identities.

## This run

The focused `"agent skills hub" in:name,description` query collected pages `1-2`, with `10` repository identities per page.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Already present in the prior `743`-repository catalog: `0`
- Added as new repositories: `20`
- Updated composed catalog: `763`

No exact duplicate repository identities were found in this batch.

Each full `owner/repository` identity was checked against the existing `ai-handbook` catalog before insertion. The complete ordered result set, provisional classification, and per-identity new/duplicate status are stored in the batch artifact.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 3 | 3 |
| `single_skill_or_domain_package` | 1 | 1 |
| `awesome_index` | 0 | 0 |
| `skill_tooling` | 15 | 15 |
| `adjacent_search_hit` | 1 | 1 |
| `unclear_search_hit` | 0 | 0 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 225 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 63 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 34 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 157 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, client, CLI, or runtime tooling. |
| `adjacent_search_hit` | 97 | Search hit is related to agents, MCP, Claude, Codex, catalogs, registries, marketplaces, hubs, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 186 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Agent-skills-hub batch artifact commit: `d9486ad49498ecfed82c0e3fe1d017ed73798d58`.
- Composed latest-manifest commit: `7817f1a48792a55fe414005a4d753befa1adc537`.
- The current batch contains `20` unique case-insensitive keys internally.
- Exact full-name checks found `0` identities in the prior `743`-repository catalog.
- Prior `743` plus `20` new repositories resolves to `763`.
- Classification totals resolve to `763` repositories.
- `480 + 283 = 763`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
