# GitHub Agent Skills index run — February 2026 pages 13–21

## Scope

Index-only collection. No deep repository analysis was performed.

Query:

```text
agentskills in:name,description created:2026-02-01..2026-02-28
```

## Live search results

- Pages `13-20`: `20` repositories each.
- Page `21`: `2` repositories.
- Page `22`: `0` repositories.
- Persisted current-run raw identities: `162`.
- Internal case-insensitive duplicates: `0`.
- Current-run unique identities: `162`.

## Merge and deduplication

The current batch was merged with the previously persisted February pages `1-12` using case-insensitive `owner/repository` identity.

One exact overlap was found and removed from the merged unique set:

```text
irfiacre/agentskills
```

Resulting February staging state:

- Raw staged records: `402`.
- Distinct staged identities: `401`.
- Confirmed cross-batch duplicates removed: `1`.
- New unique identities contributed by this run: `161`.

## Pagination-drift finding

The duplicate above had previously appeared at the earlier page boundary and now appeared again on page `13`. This is direct evidence that GitHub best-match result ordering changed between the two collection runs.

Therefore page `22 = 0` is recorded as a verified terminal probe, but the February partition is not marked gap-free complete. A deterministic reconciliation pass using smaller `created:` shards or a stable full refresh is required before completeness is asserted.

## Provisional classification

Current batch (`162` raw identities):

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `90` |
| `single_skill_or_domain_package` | `15` |
| `awesome_index` | `3` |
| `skill_tooling` | `27` |
| `adjacent_search_hit` | `24` |
| `unclear_search_hit` | `3` |
| **Total** | **`162`** |

Deduplicated February staged union (`401` identities):

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

Classification is based only on repository identity and GitHub repository-search metadata.

## Written artifacts and commits

```text
d9cc8932dd0b0d70aae0b7bb204876d594630687
chore(research): stage February agentskills pages 13-21
sources/catalog/batches/agentskills-created-2026-02-pages-13-21.json

96c30201a9224fdb942d2ba02a2a90ae624fa373
chore(research): extend February agentskills staging through page 21
sources/catalog/github-agent-skills-index-latest.json

6c0bdbc5ededc9c9ae873142ffadea6c3742fbc8
docs(research): record February agentskills pages 13-21
sources/catalog/github-agent-skills-index.md
```

## Canonical boundary

Canonical totals remain unchanged:

```text
unique:   2502
eligible: 2088
held:      414
```

No canonical delta is asserted until deterministic reconciliation against unpartitioned staging and the historical canonical ledger is complete.

## Content boundary

No target repository README, `SKILL.md`, scripts, references, evals, stars, implementation code, or runtime behavior was read in this run.
