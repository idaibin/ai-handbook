# GitHub Agent Skills Repository Index

## Current verified catalog

- Search queries completed:
  - `"agent skills" in:name,description`, pages `1-10`
  - `"codex skills" in:name,description`, pages `1-10`
  - `"claude skills" in:name,description`, pages `1-10`
  - `"mcp skills" in:name,description`, pages `1-10`
  - `"skill catalog" in:name,description`, pages `1-10`
- Results per page: `10`
- Raw GitHub search hits: `500`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `504`
- Unique repositories after case-insensitive `owner/repository` deduplication: `502`
- Exact duplicates removed across current inputs: `2`
- New unique repositories added in this run: `98`
- Provisionally eligible for later deep analysis: `282`
- Held as adjacent or unclear search hits: `220`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.

## This run

The `"skill catalog" in:name,description` query was collected across pages `1-10`, yielding `100` repository identities. Two were already present in the stored catalog:

- `jMerta/codex-skills`
- `vadimcomanescu/codex-skills`

The remaining `98` identities were added as new repositories.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 22 | 20 |
| `single_skill_or_domain_package` | 1 | 1 |
| `awesome_index` | 1 | 1 |
| `skill_tooling` | 17 | 17 |
| `adjacent_search_hit` | 12 | 12 |
| `unclear_search_hit` | 47 | 47 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 158 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 57 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 26 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 40 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, or runtime tooling. |
| `adjacent_search_hit` | 83 | Search hit is related to agents, MCP, Claude, Codex, catalogs, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 137 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Skill-catalog batch artifact commit: `32a54ab7171c8449832a1271cb639a6ab0f364a4`.
- Composed latest-manifest commit: `e2eb3c0d3a6f86a31bffe486551bf596a170e036`.
- The current batch contains `100` unique case-insensitive keys internally.
- Two identities repeat repositories already present in the prior `404`-repository catalog.
- Prior `404` plus `98` new repositories resolves to `502`.
- Classification totals resolve to `502` repositories.
- `282 + 220 = 502`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
