# GitHub Agent Skills Repository Index

## Current verified catalog

- Search queries completed:
  - `"agent skills" in:name,description`, pages `1-10`
  - `"codex skills" in:name,description`, pages `1-10`
  - `"claude skills" in:name,description`, pages `1-10`
  - `"mcp skills" in:name,description`, pages `1-10`
  - `"skill catalog" in:name,description`, pages `1-10`
  - `"skill registry" in:name,description`, pages `1-10`
- Results per page: `10`
- Raw GitHub search hits: `600`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `604`
- Unique repositories after case-insensitive `owner/repository` deduplication: `597`
- Exact duplicates removed across current inputs: `7`
- New unique repositories added in this run: `95`
- Provisionally eligible for later deep analysis: `331`
- Held as adjacent or unclear search hits: `266`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The composed catalog currently consists of:

- Base catalog: [`github-agent-skills-index.json`](github-agent-skills-index.json), `304` repositories.
- MCP delta: [`batches/mcp-skills-pages-1-10.json`](batches/mcp-skills-pages-1-10.json), `100` new repositories.
- Skill-catalog delta: [`batches/skill-catalog-pages-1-10.json`](batches/skill-catalog-pages-1-10.json), `98` new repositories from `100` raw identities.
- Skill-registry delta: [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json), `95` new repositories from `100` raw identities.

## This run

The `"skill registry" in:name,description` query was collected across pages `1-10`, yielding `100` repository identities. Five were already present in the stored catalog:

- `majiayu000/claude-skill-registry`
- `zocomputer/skills`
- `tech-leads-club/agent-skills`
- `majiayu000/claude-skill-registry-core`
- `sarveshtalele/mcp-skills-registry`

The remaining `95` identities were added as new repositories.

| Classification | Raw hits | New unique |
| --- | ---: | ---: |
| `specification` | 0 | 0 |
| `skill_collection` | 10 | 8 |
| `single_skill_or_domain_package` | 0 | 0 |
| `awesome_index` | 3 | 3 |
| `skill_tooling` | 41 | 38 |
| `adjacent_search_hit` | 7 | 7 |
| `unclear_search_hit` | 39 | 39 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 166 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 57 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 29 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 78 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, marketplace, catalog, registry, or runtime tooling. |
| `adjacent_search_hit` | 90 | Search hit is related to agents, MCP, Claude, Codex, catalogs, registries, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 176 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Skill-registry batch artifact commit: `afa3cca6e1ebbc245e8dee6e3b6a2b150ea76d32`.
- Composed latest-manifest commit: `89a5ec5a2e5e53b79973de7670fdba20131d8203`.
- The current batch contains `100` unique case-insensitive keys internally.
- Five identities repeat repositories already present in the prior `502`-repository catalog.
- Prior `502` plus `95` new repositories resolves to `597`.
- Classification totals resolve to `597` repositories.
- `331 + 266 = 597`, matching the eligible and held partitions.
- The next index run must compose against [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json), preserve query origins, and add only genuinely new repositories.
