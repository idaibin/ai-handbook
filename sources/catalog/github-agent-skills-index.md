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

This run searched pages `13-22`. Pages `13-20` returned `20` repositories each, page `21` returned `2`, and page `22` returned `0`. Pages `13-21` were persisted as `162` raw identities, all distinct within the current batch.

During merge with the previously persisted pages `1-12`, one exact case-insensitive duplicate was found: `irfiacre/agentskills`. The February staged union therefore contains `402` raw staged records and `401` distinct repository identities after deduplication.

The duplicate is important evidence: the repository had previously appeared at the page-12 boundary and reappeared on page `13`, which shows GitHub best-match ordering changed between runs. For that reason, page `22 = 0` is recorded as a verified terminal probe, but a gap-free complete February snapshot is **not** asserted yet. A deterministic reconciliation pass using smaller `created:` shards or a stable full refresh is required before marking the partition complete.

| Metric | Value |
| --- | ---: |
| Persisted pages | `1-21` |
| Raw staged records | `402` |
| Distinct staged identities | `401` |
| Confirmed duplicate removed | `1` |
| Current-run raw / unique | `162 / 162` |
| New unique identities after merge | `161` |
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

### February artifacts

- [`batches/agentskills-created-2026-02-pages-1-2.json`](batches/agentskills-created-2026-02-pages-1-2.json)
- [`batches/agentskills-created-2026-02-pages-3-12.json`](batches/agentskills-created-2026-02-pages-3-12.json)
- [`batches/agentskills-created-2026-02-pages-13-21.json`](batches/agentskills-created-2026-02-pages-13-21.json)
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

Reconcile February using smaller `created:` shards or a stable full refresh so pagination drift cannot create a silent gap. After that, continue the next created-date partition. Canonical `2502 / 2088 / 414` remains unchanged until partition identities are reconciled against unpartitioned staging and the complete historical ledger.
