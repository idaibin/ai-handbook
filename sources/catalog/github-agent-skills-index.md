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
  - `"skill hub" in:name,description`, pages `1-10`
- Raw GitHub search hits: `926`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `930`
- Unique repositories after case-insensitive `owner/repository` deduplication: `850`
- Exact duplicates removed across current inputs: `80`
- New unique repositories added in this run: `87`
- Provisionally eligible for later deep analysis: `543`
- Held as adjacent or unclear search hits: `307`

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
- Skill-hub delta: [`batches/skill-hub-pages-1-10.json`](batches/skill-hub-pages-1-10.json), `87` new repositories from `100` raw identities.

## This run

The focused `"skill hub" in:name,description` query collected pages `1-10`, with `10` repository identities per page.

- Raw repository identities: `100`
- Internal batch duplicates: `0`
- Already present in the current `763`-repository catalog: `13`
- Added as new repositories: `87`
- Updated composed catalog: `850`

The batch was rebased after the concurrently collected `"agent skills hub"` batch was committed. This prevented seven repositories present in that newer catalog state from being incorrectly counted as new.

Exact duplicates removed:

- `0x-Professor/Agent-Skills-Hub`
- `agent-skills-hub/agent-skills-hub`
- `binance/binance-skills-hub`
- `ddtcorex/dev-skills-hub`
- `Kucoin/kucoin-skills-hub`
- `llsenyue/Agent-Skills-Hub`
- `lza6/Agent-Skills-Hub`
- `qycnet/mcp-skill-hub`
- `rkorus/skills-hub`
- `saker-ai/skillhub`
- `tmolavi/mcp-agent-skills-hub`
- `youzaiAGI/agent-skills-hub`
- `zhuyansen/agent-skills-hub`

The complete ordered result set, provisional classification, and per-identity new/duplicate status are stored in the batch artifact.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 25 | 25 |
| `single_skill_or_domain_package` | 0 | 0 |
| `awesome_index` | 1 | 1 |
| `skill_tooling` | 50 | 37 |
| `adjacent_search_hit` | 8 | 8 |
| `unclear_search_hit` | 16 | 16 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 250 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 63 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 35 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 194 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, hub, client, CLI, or runtime tooling. |
| `adjacent_search_hit` | 105 | Search hit is related to agents, MCP, Claude, Codex, catalogs, registries, marketplaces, hubs, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 202 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Initial Skill-hub batch creation commit: `4fa2a58c70ca82ad12632e643e5dae4794cc762b`.
- Rebased Skill-hub batch artifact commit: `241f4e112dde44df0818bbc766e71dbb6c256ba2`.
- Composed latest-manifest commit: `60028b83ca23274fec0e5085f1e0856857e0c07e`.
- The current batch contains `100` unique case-insensitive keys internally.
- Exact identity comparison found `13` repositories in the current `763`-repository catalog.
- Prior `763` plus `87` new repositories resolves to `850`.
- Classification totals resolve to `850` repositories.
- `543 + 307 = 850`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
