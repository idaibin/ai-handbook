# GitHub Agent Skills Index Run — Authoring

## Search coverage

- Query: `"agent skills authoring" in:name,description`
- Requested results per page: `50`
- Page 1 hits: `14`
- Page 2 hits: `0`
- Query status: complete for the accessible result set
- Deep repository analysis: not performed

## Collected candidates

The run recorded 14 distinct GitHub repository identities and found no duplicate identities inside the batch itself.

Provisional identity-only classification:

| Classification | Candidates |
| --- | ---: |
| `skill_collection` | 4 |
| `single_skill_or_domain_package` | 3 |
| `skill_tooling` | 4 |
| `adjacent_search_hit` | 2 |
| `unclear_search_hit` | 1 |

If all 14 are later proven new against the prior catalog, 11 would be provisionally eligible for later deep analysis and 3 would remain held. These are candidate counts only, not canonical catalog deltas.

Machine-readable batch: [`../batches/agent-skills-authoring-search.json`](../batches/agent-skills-authoring-search.json).

## Deduplication status

Internal case-insensitive `owner/repository` deduplication is complete: `14 raw -> 14 distinct batch identities`.

Exact deduplication against the full existing `1731`-repository catalog is **not verified in this run**. The current canonical manifest stores composed totals and batch references rather than one complete exact-identity array. The available GitHub code-search path also returned no result for an identity that is known to be present in the current catalog, so an empty code-search result cannot safely be used as proof that a candidate is absent.

For that reason this run does **not**:

- claim any of the 14 candidates as new unique repositories;
- change the canonical `1731` unique-repository count;
- change canonical classification totals;
- mark any candidate as deep-analysis complete.

This prevents a false unique-count increase while preserving the verified GitHub search results for later exact batch-level reconciliation.

## Validation boundary

Verified in this run: GitHub repository identity, GitHub repository ID, default branch, repository size metadata, archived flag, search ordering, internal batch uniqueness, and provisional identity/query-context classification.

Not read or assessed: README, `SKILL.md`, scripts, references, evals, stars, implementation code, runtime behavior, or repository quality.

## Commit record

The machine-readable candidate batch was committed as `6ed817fa779d63ef64d339d5ea7e9c939838a1c9` (`chore(research): stage agent skills authoring index batch`). The file was fetched back from `main` after the write and matched the staged 14-candidate result set.
