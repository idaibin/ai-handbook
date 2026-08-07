# Agent Skills repository index run — March 1–10, 2026

## Scope

Index collection only. The run searched GitHub repository identity results for `agentskills` in repository name/description, merged exact daily shards, removed duplicates case-insensitively by `owner/repository`, assigned provisional index classifications, and persisted the verified staging artifacts.

No repository deep analysis was performed.

## Queries

For each date from `2026-03-01` through `2026-03-10`:

```text
agentskills in:name,description created:<date>..<date>
per_page=100
page=1
page=2 terminal probe
```

All ten page-2 terminal probes returned zero results.

| Date | Page 1 | Page 2 |
| --- | ---: | ---: |
| 2026-03-01 | 12 | 0 |
| 2026-03-02 | 18 | 0 |
| 2026-03-03 | 17 | 0 |
| 2026-03-04 | 25 | 0 |
| 2026-03-05 | 14 | 0 |
| 2026-03-06 | 15 | 0 |
| 2026-03-07 | 10 | 0 |
| 2026-03-08 | 13 | 0 |
| 2026-03-09 | 22 | 0 |
| 2026-03-10 | 16 | 0 |
| **Total** | **162** | **0** |

A supplementary broad-range best-match search for `created:2026-03-01..2026-03-10` was also issued during collection, but it was not used as completeness authority because prior February work proved that best-match pagination can drift. Exact single-day shards are the authority for this run.

## Merge and deduplication

- Raw candidates: `162`
- Case-insensitive unique `owner/repository` identities: `162`
- Internal duplicates: `0`
- March verified coverage after this run: `2026-03-01..2026-03-10`
- Canonical additions asserted: `0`

March identities remain staging data. Canonical totals remain frozen at `2502 unique / 2088 eligible / 414 held` until created-date partition unions are reconciled against unpartitioned staging and the complete historical canonical ledger.

## Provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | 0 |
| `skill_collection` | 116 |
| `single_skill_or_domain_package` | 16 |
| `awesome_index` | 2 |
| `skill_tooling` | 11 |
| `adjacent_search_hit` | 14 |
| `unclear_search_hit` | 3 |
| **Total** | **162** |

Classification uses repository identity/name metadata only and must not be treated as a repository-content finding.

## Persisted artifacts

- Batch: `sources/catalog/batches/agentskills-created-2026-03-01-through-10-deterministic.json`
  - commit: `2aabcaa48b1513f27b2a28372adb8f70557d1499`
- Machine-readable manifest: `sources/catalog/github-agent-skills-index-latest.json`
  - commit: `067e90de9e5041c245dde01ba6f2135a80e6ae49`
- Human-readable index: `sources/catalog/github-agent-skills-index.md`
  - commit: `8fb20226a5e96d755ad9da63917b881aac8eb73d`

## Evidence boundary

No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. No repository is marked deep-analysis complete from this index run.

## Next boundary

Continue with the exact `2026-03-11` single-day shard.
