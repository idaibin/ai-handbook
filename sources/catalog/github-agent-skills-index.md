# GitHub Agent Skills Repository Index

## Current verified catalog

- Search queries completed:
  - `"agent skills" in:name,description`, pages `1-10`
  - `"codex skills" in:name,description`, pages `1-10`
  - `"claude skills" in:name,description`, pages `1-10`
  - `"mcp skills" in:name,description`, pages `1-10`
- Results per page: `10`
- Raw GitHub search hits: `400`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Unique repositories after case-insensitive `owner/repository` deduplication: `404`
- Exact duplicates removed across current inputs: `0`
- New unique repositories added in this run: `100`
- Provisionally eligible for later deep analysis: `243`
- Held as adjacent or unclear search hits: `161`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- Current delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.

## This run

The `"mcp skills" in:name,description` query was collected across pages `1-10`, yielding `100` repository identities. All `100` were new relative to the stored `304`-repository base catalog.

| Classification | Added this run |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 20 |
| `single_skill_or_domain_package` | 10 |
| `awesome_index` | 2 |
| `skill_tooling` | 8 |
| `adjacent_search_hit` | 38 |
| `unclear_search_hit` | 22 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 138 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 56 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 25 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 23 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, or runtime tooling. |
| `adjacent_search_hit` | 71 | Search hit is related to agents, MCP, Claude, Codex, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 90 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- MCP batch artifact commit: `c28dfe4c018f404186925e7ff47384b9aa876367`.
- Composed latest-manifest commit: `6be5882972d41cd839cc2c16078f9a57cb29eb01`.
- The current batch contains `100` unique case-insensitive `owner/repository` keys.
- Base `304` plus delta `100` resolves to `404` repositories.
- Classification totals resolve to `404` repositories.
- `243 + 161 = 404`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
