# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits already composed into the canonical catalog: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across composed inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across composed inputs: `132`
- New unique repositories composed in this run: `0`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The canonical total remains `2502`. The unpartitioned `agentskills in:name,description` search has persisted its accessible first `1000` results, but pages `17-50` still require full historical identity reconciliation. This run began deterministic created-date partitioning and persisted January 2026 partition page `10` as an additional `20` verified candidate records without promoting them into the canonical total.

## Completed search coverage

- `"agent skills" in:name,description`, pages `1-10`
- `"codex skills" in:name,description`, pages `1-10`
- `"claude skills" in:name,description`, pages `1-10`
- `"mcp skills" in:name,description`, pages `1-10`
- `"skill catalog" in:name,description`, pages `1-10`
- `"skill registry" in:name,description`, pages `1-10`
- `"agent skill" in:name,description`, pages `1-10`
- `"agentskills cli" in:name,description`, page `1`
- `"skill marketplace" in:name,description`, pages `1-10`
- `"agent skills hub" in:name,description`, pages `1-2`
- `"skill hub" in:name,description`, pages `1-10`
- `"agent skills directory" in:name,description`, pages `1-2`
- `"openai skills" in:name,description`, pages `1-10`
- `"anthropic skills" in:name,description`, pages `1-10`
- `"agent skills marketplace" in:name,description`, pages `1-10`
- `"agentskills specification" in:name,description`, page `1`
- `"skill lint" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills validator" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills standard" in:name,description`, pages `1-10`, `20` results per page
- `"agent skills eval" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills benchmark" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills test" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agentskills sdk" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills template" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills examples" in:name,description`, complete accessible pages `1-2`, `50` requested results per page; page `3` returned `0`
- `"agent skills protocol" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills registry" in:name,description`, complete accessible pages `1-41`, `20` requested results per page; page `42` returned `0`

## Unpartitioned `agentskills` staging

Query:

```text
agentskills in:name,description
```

Persisted staging coverage includes pages `1-50`, `20` repository identities per page. Page `51` returns GitHub HTTP `422`:

```text
Only the first 1000 search results are available
```

Therefore pages `1-50` cover only the unpartitioned query's accessible first `1000` results, not the complete query universe.

| Metric | Value |
| --- | ---: |
| Raw identities persisted | `1000` |
| Confirmed cross-staging duplicates in reconciled pages `1-16` | `1` |
| Staged unique identities reconciled through page `16` | `319` |
| Identities unique within unreconciled pages `17-50` batches | `680` |
| Exact prior-catalog duplicates directly confirmed | `3` |
| Unresolved identity records awaiting full reconciliation | `996` |
| Global staged-unique total | `not asserted` |
| Canonical delta asserted | `0` |

The three directly confirmed prior-catalog duplicates remain:

- `agentskills/agentskills`
- `darkrishabh/agent-skills-eval`
- `pratikxpanda/agentskills-sdk`

Across reconciled pages `1-16`, the confirmed cross-staging repeat remains `0xsarawut/agentskills`, which appeared at page `3` rank `20` and page `4` rank `1`.

## Partitioned discovery beyond the 1000-result window

Active partition:

```text
agentskills in:name,description created:2026-01-01..2026-01-31
```

This run persisted page `10` with `20` repository identities. All 20 are distinct under case-insensitive `owner/repository` within the batch. Each exact `repository_full_name` was also searched across the persisted `idaibin/ai-handbook` index artifacts; those lookups returned `0` indexed-text matches.

That negative lookup is recorded only as evidence that no persisted index match was observed. It is **not** treated as proof that all 20 are absent from every historical source batch, so no canonical increment is asserted yet.

Partition probes:

- page `11`: `20` repositories, not persisted in this run
- page `25`: `0` repositories
- page `50`: `0` repositories

This confirms the January 2026 monthly partition is below GitHub Search's 1000-result accessible ceiling and can be exhausted deterministically in later index runs.

Partition artifact:

- [`batches/agentskills-created-2026-01-page-10.json`](batches/agentskills-created-2026-01-page-10.json)

### January 2026 page 10 provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `19` |
| `single_skill_or_domain_package` | `0` |
| `awesome_index` | `0` |
| `skill_tooling` | `1` |
| `adjacent_search_hit` | `0` |
| `unclear_search_hit` | `0` |

The `skill_tooling` candidate is `Flash-Brew-Digital/validate-skill`. Classification is based only on repository identity and GitHub search context and is not added to canonical totals.

## Staging artifacts

- [`batches/agentskills-page-1.json`](batches/agentskills-page-1.json)
- [`batches/agentskills-pages-2-3.json`](batches/agentskills-pages-2-3.json)
- [`batches/agentskills-pages-4-6.json`](batches/agentskills-pages-4-6.json)
- [`batches/agentskills-pages-7-10.json`](batches/agentskills-pages-7-10.json)
- [`batches/agentskills-pages-11-16.json`](batches/agentskills-pages-11-16.json)
- [`batches/agentskills-pages-17-20.json`](batches/agentskills-pages-17-20.json)
- [`batches/agentskills-page-21.json`](batches/agentskills-page-21.json)
- [`batches/agentskills-pages-22-31.json`](batches/agentskills-pages-22-31.json)
- [`batches/agentskills-pages-32-41.json`](batches/agentskills-pages-32-41.json)
- [`batches/agentskills-pages-42-50.json`](batches/agentskills-pages-42-50.json)
- [`batches/agentskills-created-2026-01-page-10.json`](batches/agentskills-created-2026-01-page-10.json)

## Canonical classification totals

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

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classification is provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Current canonical state: `2502 unique / 2088 eligible / 414 held`.
- Unpartitioned `agentskills` raw staging: `1000` identities across pages `1-50`.
- Newly persisted partition records in this run: `20`.
- Internal duplicates in the new partition batch: `0`.
- Persisted-index exact search matches for the 20 new partition records: `0 observed`; historical reconciliation remains pending.
- Partition batch commit: `8a306c5baeacdb3f68595c583cd6aaf513e819f5`.
- Manifest update commit: `640cb452f6612d17aec1cebe6cbc092409b4af31`.
- January partition page `11` probe: `20` repositories; not persisted.
- January partition pages `25` and `50` probes: `0` repositories.
- `2088 + 414 = 2502`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
