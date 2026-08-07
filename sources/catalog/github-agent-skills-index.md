# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across current inputs: `132`
- New unique repositories collected in this run: `1`
- Net catalog delta versus the previous verified manifest: `+1`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `2501`-repository canonical manifest with page `41` of the `agent skills registry` discovery query.

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

## In-progress search coverage

No partially merged query remains. A next high-recall index query candidate is `agentskills in:name,description`; it has not been merged yet.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `41` at `per_page=20` and probed page `42`.

- Raw repository identities: `1`
- Internal batch duplicates: `0`
- Confirmed duplicates in directly inspected prior sets: `0`
- Added as new repositories: `1`
- Previous verified catalog: `2501`
- Updated composed catalog: `2502`
- Added to provisional deep-analysis queue: `1`
- Added to held-for-review: `0`
- Terminal probe: page `42` returned `0`, so this query is now complete.

The page-41 identity `kms9/skillhub` was directly compared against persisted `agent-skills-registry` pages `31-40`, `skill-hub` pages `1-10`, `skill-registry` pages `1-10`, and the original canonical inventory snapshot. No exact case-insensitive `owner/repository` duplicate was present in those directly inspected sets. Earlier catalog coverage remains inherited through the verified `2501`-repository canonical manifest; code-search emptiness was not used as uniqueness proof.

The repository was provisionally classified from repository identity and GitHub search context as `skill_tooling` and added to the provisional deep-analysis queue. Page, rank, GitHub repository ID, default branch, repository size, archived state, classification, eligibility, duplicate status, terminal coverage, and verification notes are stored in [`batches/agent-skills-registry-page-41.json`](batches/agent-skills-registry-page-41.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 611 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 1172 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identity and accessibility. Classification is provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `233dc8e631f9dfdde42c16449371a6fc290ebe71` (`2501` repositories).
- `agent skills registry` page-41 batch commit: `9f40936da4f182a4c65ee56c7e7cf41cd0140102`.
- Composed latest-manifest commit: `e80ed29a775828ed74cc2613464cd50ca597e5a5`.
- `2501 + 1 = 2502` current unique repositories.
- `2634 - 132 = 2502` raw-to-unique reconciliation.
- Classification totals resolve to `2502`.
- `2088 + 414 = 2502`, matching the eligible and held partitions.
- Query terminal boundary: `"agent skills registry" in:name,description`, page `42`, `per_page=20`, returned `0`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
