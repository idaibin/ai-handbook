# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1817`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1821`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1719`
- Exact duplicates removed across current inputs: `102`
- New unique repositories collected in this run: `54`
- Net catalog delta versus the previous verified snapshot: `+54`
- Provisionally eligible for later deep analysis: `1314`
- Held as adjacent or unclear search hits: `405`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the immutable `1665`-repository snapshot with the verified `agent skills examples` discovery batch. The `1665` snapshot already includes the completed `agent skills template` pages `2-3` batch, so the earlier canonical-write conflict no longer blocks the published catalog chain.

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

## This run

Query:

```text
"agent skills examples" in:name,description
```

GitHub returned `50` repositories on page `1`, `4` on page `2`, and `0` on page `3`, so this query is complete at `per_page=50`.

- Raw repository identities: `54`
- Internal batch duplicates: `0`
- Duplicates against the prior verified catalog: `0`
- Added as new repositories: `54`
- Previous verified catalog snapshot: `1665`
- Updated composed catalog: `1719`
- Added to provisional deep-analysis queue: `45`
- Added to held-for-review: `9`

Provisional classification for the new identities is `41 skill_collection`, `3 single_skill_or_domain_package`, `1 skill_tooling`, `2 adjacent_search_hit`, and `7 unclear_search_hit`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-examples-search.json`](batches/agent-skills-examples-search.json).

The dominant `agent-skills-examples` name cluster, the `Codex-is-all-you-need` cluster, and selected exact-owner candidates were checked against the current AI-handbook code-search snapshot; no prior exact identity match was returned. The immutable `1665` snapshot was used as the composition base.

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 531 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 92 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 37 | Identity indicates a curated Skill index. |
| `skill_tooling` | 491 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 149 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 256 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- `agent skills template` pages `2-3` batch commit: `03c39a037d83cb4ca41ec6bdc47e312a30bb892c`.
- Immutable `1665` snapshot commit: `0c6b9fb8b4395f17088f27cbf7be08c4127619de`.
- `agent skills examples` batch commit: `353b358153afe465c77c4962c909cddb0d08b175`.
- Composed latest-manifest commit: `43c5def72f278eef4c44487d66e31edc254c81d1`.
- `1665 + 54 = 1719` current unique repositories.
- `1821 - 102 = 1719` raw-to-unique reconciliation.
- Classification totals resolve to `1719`.
- `1314 + 405 = 1719`, matching the eligible and held partitions.
- Page `3` returned zero results; `"agent skills examples"` is complete at `per_page=50`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
