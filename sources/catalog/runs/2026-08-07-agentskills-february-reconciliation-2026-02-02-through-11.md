# GitHub Agent Skills index run — February reconciliation 2026-02-02 through 2026-02-11

## Scope

Index-only repository discovery and deterministic reconciliation. No deep repository analysis was performed.

Queries used one exact `created:` day at a time:

```text
agentskills in:name,description created:YYYY-MM-DD..YYYY-MM-DD
per_page=100
page=1, followed by page=2 terminal probe
```

Dates processed: `2026-02-02` through `2026-02-11` inclusive.

## Results

- Daily shards completed: `10`
- Page-1 repository hits: `144`
- Page-2 probes: `10`
- Page-2 hits: `0`
- Raw identities persisted: `144`
- Unique identities under case-insensitive `owner/repository`: `144`
- Internal duplicates removed: `0`
- Matches to prior February staging: `144`
- Missing from prior February staging: `0`
- New unique identities after merge: `0`
- Canonical delta asserted: `0`

Together with the previously verified `2026-02-01` shard, deterministic February reconciliation now covers `2026-02-01..2026-02-11`: `153` unique identities observed, all `153` already present in prior February staging.

## Classification

Existing provisional classifications were preserved for exact identity matches.

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `113` |
| `single_skill_or_domain_package` | `9` |
| `awesome_index` | `0` |
| `skill_tooling` | `10` |
| `adjacent_search_hit` | `10` |
| `unclear_search_hit` | `2` |
| **Total** | **`144`** |

## Merge and deduplication evidence

The live daily-shard identities were compared with the three previously persisted February pagination artifacts:

- `sources/catalog/batches/agentskills-created-2026-02-pages-1-2.json`
- `sources/catalog/batches/agentskills-created-2026-02-pages-3-12.json`
- `sources/catalog/batches/agentskills-created-2026-02-pages-13-21.json`

All `144` current identities were present. No new identity was discovered in these ten daily shards. Daily shards are mutually exclusive by repository creation date, so there are no legitimate cross-day duplicates.

## Artifacts

- `sources/catalog/batches/agentskills-created-2026-02-02-through-11-reconciliation.json`
- `sources/catalog/github-agent-skills-index-latest.json`
- `sources/catalog/github-agent-skills-index.md`

## Evidence boundary

No target repository README, `SKILL.md`, scripts, references, evals, stars, implementation code, or runtime behavior was inspected. This run does not mark any repository as deep-analysis complete.

February remains incomplete because dates `2026-02-12..2026-02-28` have not yet received the same deterministic daily-shard reconciliation. The next index boundary is `2026-02-12`.
