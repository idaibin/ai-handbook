# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `2629`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `2633`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2501`
- Exact duplicates removed across current inputs: `132`
- New unique repositories collected in this run: `200`
- Net catalog delta versus the previous verified manifest: `+200`
- Provisionally eligible for later deep analysis: `2087`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `2301`-repository canonical manifest with pages `31-40` of the `agent skills registry` discovery query.

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

## In-progress search coverage

- `"agent skills registry" in:name,description`, pages `1-40` processed at `20` results per page. Page `41` was probed and returned `1` repository; it was not merged in this run, so the next merge boundary is page `41`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed pages `31-40` at `per_page=20`.

- Raw repository identities: `200`
- Internal batch duplicates: `0`
- Confirmed duplicates in directly inspected prior sets: `0`
- Added as new repositories: `200`
- Previous verified catalog: `2301`
- Updated composed catalog: `2501`
- Added to provisional deep-analysis queue: `200`
- Added to held-for-review: `0`

Pages 31-40 were checked for case-insensitive duplicates within the 200-result batch and directly compared against persisted adjacent `agent-skills-registry` pages `25-30` plus the full persisted `skill-hub` pages `1-10`, `agent-skills-hub` pages `1-2`, and `skill-registry` pages `1-10` high-overlap artifacts. No exact `owner/repository` duplicate was found in those directly inspected sets. Earlier catalog coverage is inherited through the verified `2301`-repository canonical manifest; code-search emptiness was not used as uniqueness proof.

All 200 raw results were provisionally classified from repository identity and GitHub search context as `skill_tooling`; all 200 were added to the provisional deep-analysis queue. Page, result ordering, repository identity, classifications, eligibility, duplicate status, coverage, and verification notes are stored in [`batches/agent-skills-registry-pages-31-40.json`](batches/agent-skills-registry-pages-31-40.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 611 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 1171 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `a0f5f1e932ae2f12929dc9317c24d2612cacf2f6` (`2301` repositories).
- `agent skills registry` pages-31-40 batch commit: `a3e3d8912134efb97ce70c6cb4fd2207145eaf1d`.
- Composed latest-manifest commit: `233dc8e631f9dfdde42c16449371a6fc290ebe71`.
- `2301 + 200 = 2501` current unique repositories.
- `2633 - 132 = 2501` raw-to-unique reconciliation.
- Classification totals resolve to `2501`.
- `2087 + 414 = 2501`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `41`, `per_page=20`.
- Page `41` currently returns `1` repository and was not merged in this run.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
