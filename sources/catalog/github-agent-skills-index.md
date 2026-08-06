# GitHub Agent Skills Repository Index

## Current verified catalog

- Search queries completed:
  - `"agent skills" in:name,description`, pages `1-10`
  - `"codex skills" in:name,description`, pages `1-10`
  - `"claude skills" in:name,description`, pages `1-10`
- Results per page: `10`
- Raw GitHub search hits: `300`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Unique repositories after case-insensitive `owner/repository` deduplication: `304`
- Exact duplicates removed across current inputs: `0`
- New unique repositories added in this run: `100`
- Provisionally eligible for later deep analysis: `203`
- Held as adjacent or unclear search hits: `101`

Machine-readable authority: [`github-agent-skills-index.json`](github-agent-skills-index.json).

## This run

The `"claude skills" in:name,description` query was collected across pages `1-10`, yielding `100` repository identities. All `100` were new relative to the existing `204`-repository catalog.

| Classification | Added this run |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 54 |
| `single_skill_or_domain_package` | 9 |
| `awesome_index` | 11 |
| `skill_tooling` | 5 |
| `adjacent_search_hit` | 7 |
| `unclear_search_hit` | 14 |

## Classification totals

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 118 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 46 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 23 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 15 | Repository identity indicates Skill discovery, validation, scanning, packaging, management, or runtime tooling. |
| `adjacent_search_hit` | 33 | Search hit is related to Claude, agents, or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 68 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub connector results verified that the repository identities existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are provisional and must not be treated as deep-analysis results.

## Validation

- Machine-readable catalog update commit: `faefb042813b2b61d76ae63bfd75f774b7d9befb`.
- Stored progress totals and category counts both resolve to `304` repositories.
- All repository keys are unique under case-insensitive `owner/repository` comparison.
- `203 + 101 = 304`, matching the eligible and held partitions.
- The next index run must merge by case-insensitive `owner/repository`, preserve query origins, and add only genuinely new repositories.
