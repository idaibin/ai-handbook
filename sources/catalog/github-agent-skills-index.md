# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1989`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1993`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1877`
- Exact duplicates removed across current inputs: `116`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous verified manifest: `+20`
- Provisionally eligible for later deep analysis: `1463`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1857`-repository canonical manifest with page `8` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-8` complete at `20` results per page; page `9` was probed and returned `20` repositories, so the next merge boundary is page `9`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `8` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Confirmed duplicates against the prior verified catalog: `0`
- Added as new repositories: `20`
- Previous verified catalog: `1857`
- Updated composed catalog: `1877`
- Added to provisional deep-analysis queue: `17`
- Added to held-for-review: `3`

All page-8 identities were directly compared against persisted `agent-skills-registry` pages `1-7`, plus directly inspected overlapping `skill-registry` pages `1-10`, `agent-skills-hub` pages `1-2`, and `skill-hub` pages `1-10` batch artifacts. No exact case-insensitive `owner/repository` identity was found in those persisted overlap sets.

Exact AI-handbook code search was also attempted for page-8 identities and returned no positive prior identity matches. Because earlier runs demonstrated code-search false negatives for known persisted identities, empty code-search results were not treated as uniqueness proof.

The 20 new identities were provisionally classified only from repository identity and GitHub search context: `4 skill_collection`, `1 single_skill_or_domain_package`, `12 skill_tooling`, and `3 unclear_search_hit`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-8.json`](batches/agent-skills-registry-page-8.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 609 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 549 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `abf814fecb382bdaef545e805339106602089d32` (`1857` repositories).
- `agent skills registry` page-8 batch commit: `2f5013ca8bf86dd3975345fcfdd83b4b8fa889a9`.
- Composed latest-manifest commit: `5c3fc57cfd8c5d9b1fc006dde306a08fc477c8dc`.
- `1857 + 20 = 1877` current unique repositories.
- `1993 - 116 = 1877` raw-to-unique reconciliation.
- Classification totals resolve to `1877`.
- `1463 + 414 = 1877`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `9`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
