# GitHub Agent Skills index run — 2026-03-11 through 2026-03-14

## Scope

Index collection only. No deep repository analysis was performed.

Query template:

```text
agentskills in:name,description created:<date>..<date>
```

Deduplication key: case-insensitive `owner/repository`.

## Verified search results

| Date | Page 1 | Page 2 | Persisted |
| --- | ---: | ---: | --- |
| 2026-03-11 | 20 | 0 | yes |
| 2026-03-12 | 29 | 0 | yes |
| 2026-03-13 | 18 | 0 | yes |
| 2026-03-14 | 45 | 0 | yes |
| **Total** | **112** | **0** | **112** |

All four persisted single-day shards terminated on the explicit page-2 probe. The batch contains `112 / 112` distinct identities under case-insensitive `owner/repository` comparison.

The previously persisted March range is `2026-03-01..2026-03-10` with `162` identities. Because GitHub repository creation date is singular, the exact daily creation-date shards are disjoint across the two date ranges. Cumulative persisted March staging is therefore `274` identities through `2026-03-14`.

## Current-run provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 86 |
| `single_skill_or_domain_package` | 12 |
| `awesome_index` | 1 |
| `skill_tooling` | 5 |
| `adjacent_search_hit` | 8 |
| `unclear_search_hit` | 0 |
| **Total** | **112** |

Classification is based only on repository identity/name metadata returned by GitHub search. It is provisional and must not be treated as repository-content verification.

## High-volume next-shard probe

`2026-03-15` was probed separately:

```text
page 1: 100
page 2: 13
page 3: 0
```

That shard was intentionally not merged into authoritative March staging in this run. Since it spans multiple result pages, the next run should persist it from one controlled multi-page snapshot and perform case-insensitive identity deduplication before advancing to later dates. None of those 113 probe results are included in the `274` cumulative March staging count.

## Artifacts written

- `sources/catalog/batches/agentskills-created-2026-03-11-through-14-deterministic.json`
- `sources/catalog/github-agent-skills-index-latest.json`
- `sources/catalog/github-agent-skills-index.md`
- `sources/catalog/runs/2026-08-07-agentskills-march-2026-03-11-through-14.md`

## Evidence boundary

No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. No repository is marked deep-analysis complete from this index run.

Canonical totals remain frozen at `2502 unique / 2088 eligible / 414 held`; canonical delta asserted by this run is `0`.
