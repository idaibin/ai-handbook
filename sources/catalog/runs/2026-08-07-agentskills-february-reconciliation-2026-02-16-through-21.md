# GitHub Agent Skills index run — February reconciliation through 2026-02-21

## Scope

Index-only. No target repository README, `SKILL.md`, scripts, references, evals, stars, implementation code, quality claims, or runtime behavior were inspected.

## Live search

The run executed exact single-day GitHub repository searches for `2026-02-12` through `2026-02-21`:

```text
agentskills in:name,description created:<date>..<date>
per_page=100
page=1 plus explicit page=2 terminal probe
```

A concurrently committed index artifact had already persisted deterministic coverage for `2026-02-12..2026-02-15` before the shared manifest was updated. This run therefore preserved that work and advanced new deterministic coverage for `2026-02-16..2026-02-21`.

## New coverage advanced

| Date | Page 1 | Page 2 |
| --- | ---: | ---: |
| `2026-02-16` | `17` | `0` |
| `2026-02-17` | `16` | `0` |
| `2026-02-18` | `19` | `0` |
| `2026-02-19` | `15` | `0` |
| `2026-02-20` | `14` | `0` |
| `2026-02-21` | `11` | `0` |
| **Total** | **`92`** | **`0`** |

All `92` identities are distinct under case-insensitive `owner/repository` comparison. Daily creation-date shards are mutually exclusive.

## Merge and recovered identity

The three original February paging artifacts contained a deduplicated union of `401` identities. Of the 92 identities in the newly advanced daily shards:

- `91` matched the original February paging staging;
- `1` was absent: `UCTooCom/agentskills-runtime`;
- exact AI-handbook code search for `UCTooCom/agentskills-runtime` returned no match before this run;
- the identity is therefore added to February staging;
- current deduplicated February staging becomes `402` identities.

`UCTooCom/agentskills-runtime` is provisionally classified as `skill_tooling` from repository identity and GitHub repository-search metadata only.

## Classification for 2026-02-16..2026-02-21

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `70` |
| `single_skill_or_domain_package` | `2` |
| `awesome_index` | `1` |
| `skill_tooling` | `13` |
| `adjacent_search_hit` | `6` |
| `unclear_search_hit` | `0` |
| **Total** | **`92`** |

Current February staging classification becomes `313 skill_collection / 16 single_skill_or_domain_package / 3 awesome_index / 36 skill_tooling / 30 adjacent_search_hit / 4 unclear_search_hit`, total `402`.

## Deterministic reconciliation status

```text
completed: 2026-02-01..2026-02-21
completed daily shards: 21
unique identities observed across daily shards: 295
matched original February paging staging: 294
missing from original paging staging: 1
new staged identities: 1
next shard: 2026-02-22
```

February is not marked complete until `2026-02-22..2026-02-28` are reconciled.

Canonical totals remain frozen at `2502 unique / 2088 eligible / 414 held`; no canonical delta is asserted.

## Artifacts and commits

- `39a923cd5a661283f34a68f008928e6df56e5297` — `chore(research): reconcile February agentskills shards 02-12 through 02-21`
  - `sources/catalog/batches/agentskills-created-2026-02-12-through-21-reconciliation.json`
- `9b69bbf78fe935e34470f63592644659ccfcdcfb` — `chore(research): extend February deterministic reconciliation through 02-21`
  - `sources/catalog/github-agent-skills-index-latest.json`
- `4050d69f307c027c0c22497893ad6813642f222c` — `docs(research): record February reconciliation through 02-21`
  - `sources/catalog/github-agent-skills-index.md`

The batch artifact intentionally contains the complete live search evidence for `2026-02-12..2026-02-21`. The pre-existing `agentskills-created-2026-02-12-through-15-reconciliation.json` remains authoritative for the earlier four shards; the superset artifact records the exact searches performed in this run and supplies the newly advanced `2026-02-16..2026-02-21` evidence.
