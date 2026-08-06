# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1521`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1525`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1425`
- Exact duplicates removed across current inputs: `100`
- New unique repositories collected in this run: `60`
- Net catalog delta versus the previous published manifest: `+58` (`+60` new identities, `-2` corrected historical double counts)
- Provisionally eligible for later deep analysis: `1058`
- Held as adjacent or unclear search hits: `367`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

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
- `"agent skills standard" in:name,description`, pages `1-6`, `20` results per page

## Composition

The composed catalog consists of the `304`-repository base catalog plus verified delta batches. The current `agent skills standard` portion is:

| Batch | Raw | Duplicates | New |
| --- | ---: | ---: | ---: |
| `agent-skills-standard-page-1.json` | 20 | 2 | 18 |
| `agent-skills-standard-page-2.json` | 20 | 0 | 20 |
| `agent-skills-standard-page-3.json` | 20 | 0 | 20 |
| `agent-skills-standard-pages-4-6.json` | 60 | 0 | 60 |

The full machine-readable composition, including all earlier batches and their commit references, is stored in [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## This run

Query:

```text
"agent skills standard" in:name,description
```

This run collected pages `4-6`, using `per_page=20`.

- Raw repository identities: `60`
- Internal batch duplicates: `0`
- Duplicates against the corrected prior catalog: `0`
- Added as new repositories: `60`
- Corrected prior unique total before these additions: `1365`
- Updated composed catalog: `1425`

All 60 returned repositories have the identity `*/agent-skills-standard`; at the index stage they are provisionally classified as `specification`. The complete page order, GitHub IDs, default branches, sizes, and deduplication status are stored in [`batches/agent-skills-standard-pages-4-6.json`](batches/agent-skills-standard-pages-4-6.json).

## Deduplication correction

During composition, two earlier page-1 entries were found to have been incorrectly counted as new despite already existing in prior authority artifacts:

- `K-Dense-AI/scientific-agent-skills` was already present in the original `304`-repository base catalog.
- `HoangNguyen0403/agent-skills-standard` was already added by `agent-skill-pages-1-10.json`.

The corrected page-1 batch therefore changes from `20` new repositories to `18`, and the global duplicate count changes from `98` to `100`. No repository content was opened to make this correction; it is based only on repository identity evidence already stored in the index artifacts.

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 83 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 483 | Identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 87 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 36 | Identity indicates a curated Skill index. |
| `skill_tooling` | 369 | Identity indicates validation, linting, evaluation, packaging, discovery, registry, marketplace, management, or runtime tooling. |
| `adjacent_search_hit` | 136 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 231 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and query context only. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed.

## Validation

- Corrected page-1 batch commit: `06265e0cca2cd9789ef05fc19e223808b57afe84`.
- Pages `4-6` batch commit: `48d5621001386e1a5cf3309371f54e0a74aa0cd6`.
- Composed latest-manifest commit: `ebf11f7e3f52953444b4283afb8dddff96dc1b38`.
- `1367 - 2 = 1365` corrected prior unique repositories.
- `1365 + 60 = 1425` current unique repositories.
- `1525 - 100 = 1425` raw-to-unique reconciliation.
- Classification totals resolve to `1425`.
- `1058 + 367 = 1425`, matching the eligible and held partitions.
- No README, `SKILL.md`, scripts, references, evaluations, stars, or implementation contents were read during this index-only run.
- The next index run should continue `"agent skills standard" in:name,description` from page `7` when keeping `per_page=20`.
