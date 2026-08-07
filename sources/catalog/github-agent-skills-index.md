# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits already composed into the canonical catalog: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across composed inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across composed inputs: `132`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Canonical totals remain frozen while the newer `agentskills` staging and created-date partitions are reconciled against the complete historical ledger. Machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## Unpartitioned `agentskills`

```text
agentskills in:name,description
```

- Persisted pages: `1-50`
- Requested results per page: `20`
- Raw staging records: `1000`
- Page `51`: GitHub first-1000-results limit
- Full historical reconciliation: pending for the unreconciled staging tail

## January 2026 created-date partition — complete

```text
agentskills in:name,description created:2026-01-01..2026-01-31
```

Pages `1-19` are persisted: `368` raw identities / `368` unique identities. Page `20` returned `0` repositories.

| Classification | Count |
| --- | ---: |
| `specification` | `2` |
| `skill_collection` | `275` |
| `single_skill_or_domain_package` | `32` |
| `awesome_index` | `11` |
| `skill_tooling` | `21` |
| `adjacent_search_hit` | `12` |
| `unclear_search_hit` | `15` |
| **Total** | **`368`** |

## February 2026 created-date partition — terminal observed, reconciliation still required

```text
agentskills in:name,description created:2026-02-01..2026-02-28
```

The persisted February pagination run searched through page `22`. Pages `1-21` produced `402` raw staged records, and page `22` returned `0`. After case-insensitive identity deduplication, the staged union contains `401` distinct repositories.

One exact cross-run duplicate was confirmed: `irfiacre/agentskills`. It had appeared at the prior page-12 boundary and then reappeared on page `13`, proving GitHub best-match ordering changed between runs. For that reason, page `22 = 0` is a verified terminal probe, but a gap-free complete February snapshot is **not** asserted from the pagination run alone.

| Metric | Value |
| --- | ---: |
| Persisted pages | `1-21` |
| Raw staged records | `402` |
| Distinct staged identities | `401` |
| Confirmed duplicate removed | `1` |
| Page `22` probe | `0` results |
| Pagination drift detected | `yes` |
| Partition completeness asserted | `no` |
| Canonical additions asserted | `0` |

### February provisional classification, deduplicated staged union

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `313` |
| `single_skill_or_domain_package` | `16` |
| `awesome_index` | `3` |
| `skill_tooling` | `35` |
| `adjacent_search_hit` | `30` |
| `unclear_search_hit` | `4` |
| **Total** | **`401`** |

Classification is provisional and uses only repository identity plus GitHub repository-search metadata. It is not merged into canonical classification totals.

### Deterministic February reconciliation — verified through 2026-02-15

To remove best-match pagination-drift risk, reconciliation uses exact single-day `created:` shards with `per_page=100` plus an explicit page-2 terminal probe.

Verified coverage now spans:

```text
2026-02-01 .. 2026-02-15
```

| Metric | Value |
| --- | ---: |
| Completed daily shards | **`15`** |
| Unique identities observed | **`203`** |
| Matches to prior February staging | **`203`** |
| Missing from prior February staging | **`0`** |
| New staged identities after merge | **`0`** |
| Page-2 terminal probes | **`15 / 15 = 0 results`** |

The current run reconciled `2026-02-12` through `2026-02-15`: **50 raw / 50 unique identities**, all 50 already present in the persisted February staging union. No cross-day duplicate can occur because repository creation dates are mutually exclusive, and all current identities were checked against the prior February staging artifacts.

Current-run provisional classifications, preserving the existing staging classifications for exact identity matches:

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `43` |
| `single_skill_or_domain_package` | `0` |
| `awesome_index` | `0` |
| `skill_tooling` | `4` |
| `adjacent_search_hit` | `3` |
| `unclear_search_hit` | `0` |
| **Total** | **`50`** |

This verifies that the first fifteen February date shards have no observed gap relative to the existing staged union. Dates `2026-02-16` through `2026-02-28` remain unreconciled, so February is still **not** marked complete.

### February artifacts

- [`batches/agentskills-created-2026-02-pages-1-2.json`](batches/agentskills-created-2026-02-pages-1-2.json)
- [`batches/agentskills-created-2026-02-pages-3-12.json`](batches/agentskills-created-2026-02-pages-3-12.json)
- [`batches/agentskills-created-2026-02-pages-13-21.json`](batches/agentskills-created-2026-02-pages-13-21.json)
- [`batches/agentskills-created-2026-02-01-reconciliation.json`](batches/agentskills-created-2026-02-01-reconciliation.json)
- [`batches/agentskills-created-2026-02-02-through-11-reconciliation.json`](batches/agentskills-created-2026-02-02-through-11-reconciliation.json)
- [`batches/agentskills-created-2026-02-12-through-15-reconciliation.json`](batches/agentskills-created-2026-02-12-through-15-reconciliation.json)
- [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json)

## Canonical classification totals

These remain unchanged until deterministic historical reconciliation completes.

| Classification | Count |
| --- | ---: |
| `specification` | `163` |
| `skill_collection` | `611` |
| `single_skill_or_domain_package` | `104` |
| `awesome_index` | `38` |
| `skill_tooling` | `1172` |
| `adjacent_search_hit` | `152` |
| `unclear_search_hit` | `262` |

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue deterministic February reconciliation with the `2026-02-16` single-day created-date shard. After all February dates are reconciled, compare the verified union against unpartitioned staging and the complete historical ledger. Canonical `2502 / 2088 / 414` remains unchanged until that reconciliation is complete.
