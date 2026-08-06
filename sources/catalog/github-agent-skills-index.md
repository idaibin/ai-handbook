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
- Raw GitHub search hits: `806`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `810`
- Unique repositories after case-insensitive `owner/repository` deduplication: `743`
- Exact duplicates removed across current inputs: `67`
- New unique repositories added in this run: `96`
- Provisionally eligible for later deep analysis: `461`
- Held as adjacent or unclear search hits: `282`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.
- Skill-registry delta: [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json), `95` new repositories from `100` raw identities.
- Agent-skill delta: [`batches/agent-skill-pages-1-10.json`](batches/agent-skill-pages-1-10.json), `44` new repositories from `100` raw identities.
- AgentSkills-CLI delta: [`batches/agentskills-cli-search.json`](batches/agentskills-cli-search.json), `6` new repositories from `6` raw identities.
- Skill-marketplace delta: [`batches/skill-marketplace-pages-1-10.json`](batches/skill-marketplace-pages-1-10.json), `96` new repositories from `100` raw identities.

## This run

The focused `"skill marketplace" in:name,description` query collected pages `1-10`, with `10` repository identities per page.

- Raw repository identities: `100`
- Internal batch duplicates: `0`
- Already present in the prior `647`-repository catalog: `4`
- Added as new repositories: `96`
- Updated composed catalog: `743`

Exact duplicates removed:

- `mhattingpete/claude-skills-marketplace`
- `phuryn/pm-skills`
- `ahmedasmar/devops-claude-skills`
- `mediar-ai/skillhubz`

Each full `owner/repository` identity was checked against the existing `ai-handbook` catalog before insertion. The complete ordered result set, provisional classification, and per-identity new/duplicate status are stored in the batch artifact.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 27 | 25 |
| `single_skill_or_domain_package` | 0 | 0 |
| `awesome_index` | 2 | 2 |
| `skill_tooling` | 55 | 53 |
| `adjacent_search_hit` | 6 | 6 |
| `unclear_search_hit` | 10 | 10 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 222 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 62 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 34 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 142 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, client, CLI, or runtime tooling. |
| `adjacent_search_hit` | 96 | Search hit is related to agents, MCP, Claude, Codex, catalogs, registries, marketplaces, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 186 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Skill-marketplace batch artifact commit: `64222e5b71be98b0b661f12dd478415be05e7c26`.
- Composed latest-manifest commit: `8715b7e28e38bd7f4e6fd4d4eabb60da4bd8aa68`.
- The current batch contains `100` unique case-insensitive keys internally.
- Exact full-name checks found `4` identities in the prior `647`-repository catalog.
- Prior `647` plus `96` new repositories resolves to `743`.
- Classification totals resolve to `743` repositories.
- `461 + 282 = 743`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
