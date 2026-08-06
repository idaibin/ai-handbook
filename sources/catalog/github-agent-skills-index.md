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
- Results per page: `10`
- Raw GitHub search hits: `700`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `704`
- Unique repositories after case-insensitive `owner/repository` deduplication: `641`
- Exact duplicates removed across current inputs: `63`
- New unique repositories added in this run: `44`
- Provisionally eligible for later deep analysis: `375`
- Held as adjacent or unclear search hits: `266`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.
- Skill-registry delta: [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json), `95` new repositories from `100` raw identities.
- Agent-skill delta: [`batches/agent-skill-pages-1-10.json`](batches/agent-skill-pages-1-10.json), `44` new repositories from `100` raw identities.

## This run

The `"agent skill" in:name,description` query was collected across pages `1-10`, yielding `100` unique identities within the batch.

- Already present in the prior `597`-repository catalog: `56`
- Added as new repositories: `44`
- Updated composed catalog: `641`

The complete ordered result set, per-repository classification, and all `56` duplicate identities are stored in the batch artifact.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 1 | 0 |
| `skill_collection` | 63 | 31 |
| `single_skill_or_domain_package` | 11 | 4 |
| `awesome_index` | 10 | 3 |
| `skill_tooling` | 8 | 6 |
| `adjacent_search_hit` | 5 | 0 |
| `unclear_search_hit` | 2 | 0 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 197 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 61 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 32 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 84 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, or runtime tooling. |
| `adjacent_search_hit` | 90 | Search hit is related to agents, MCP, Claude, Codex, catalogs, registries, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 176 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Agent-skill batch artifact commit: `ae6a4617083ecd49a57b0215339ed309d5082b04`.
- Composed latest-manifest commit: `0125aa7c0b1f61cc8c8de9a21f571301784dbca2`.
- The current batch contains `100` unique case-insensitive keys internally.
- `56` identities repeat repositories already present in the prior `597`-repository catalog.
- Prior `597` plus `44` new repositories resolves to `641`.
- Classification totals resolve to `641` repositories.
- `375 + 266 = 641`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
