# Large-scale human-writing benchmark

Date basis: 2026-08-13  
Status: protocol and corpus construction in progress; no large-scale score yet

## Current corpus state

The local candidate smoke test contains **50**, not 120, cases. It includes ten
WritingBench cases for F01, F04, F08, F10 and F12. This is candidate-pool plumbing,
not evidence that the five families are fully construct-valid. F02, F03, F05, F06,
F07, F09 and F11 are deliberately deferred rather than widened to adjacent document types.

`corpus/case-commitments.json` commits only the 50 locally materialized cases.
`corpus/plan-slots.json` records the 1,200 target allocations; its unmaterialized
entries are explicitly plans, not cases or cryptographic commitments to source rows.
Each holdout plan is language-balanced and source-interleaved, but it remains sealed
and cannot be scored until source-specific selectors and content hashes exist.

Materialized cases use `case/v2`. The builder parses only explicit audience, length,
protected-text, permitted-omission, risk, and no-op instructions into evidence-linked
claims and deterministic gates. Missing constraints remain empty or `unspecified`;
the builder does not invent atomic facts merely to populate the schema.

The raw `corpus/cases.wave-01.jsonl` is local-only and gitignored pending per-case
third-party-material review. Rebuild and run the integration check against the exact
hash-locked WritingBench file:

```bash
export WRITINGBENCH_PATH=/absolute/path/to/benchmark_all.jsonl
python corpus/build_corpus.py --writingbench-path "$WRITINGBENCH_PATH"
WRITINGBENCH_PATH="$WRITINGBENCH_PATH" python -m unittest discover \
  -s harness/tests -p 'test_corpus_sources.py' -k BuilderIntegration
python harness/validate_corpus.py --corpus corpus/cases.wave-01.jsonl --allow-incomplete
```

The normal `python -m unittest discover -s harness/tests` suite does not require or
read the untracked raw prompt file.

## Goal

Evaluate `human-writing` against the same three fixed comparison Skills across 1,200 common professional-writing cases, then improve it only from visible development batches and measure the final version on a sealed holdout.

The target is 12 task families × 100 cases. Each family uses eight 10-case development batches and one sealed 20-case holdout. After each development batch, reviewers may propose one evidence-backed `human-writing` change; the next batch uses a new immutable Skill revision. Holdout cases are never shown during optimization.

## Task families

| ID | Family | Typical output forms | Core risks |
| --- | --- | --- | --- |
| F01 | AI and ML research writing | paper section, research proposal, literature review | unsupported capability, false certainty, jargon |
| F02 | Software engineering | technical documentation, design note, test report, requirements | changed semantics, missing constraints, invented implementation |
| F03 | Source-grounded rewrite | proofreading, humanization, tone adaptation, structural edit | fact mutation, voice flattening, over-editing |
| F04 | Blog and long-form article | personal/technical blog, essay, commentary | generic openings, mechanical structure, weak argument |
| F05 | Social post and thread | X post, short announcement, thread, community post | sloganization, lost context, platform-template voice |
| F06 | Summarization and synthesis | executive summary, meeting summary, research digest | omission, attribution loss, scope broadening |
| F07 | Task delegation and planning | task brief, acceptance criteria, handoff, checklist | missing owner/input/output/done condition, invented authority |
| F08 | Product and business writing | product proposal, user research, market/risk analysis | unsupported ranking, mixed fact and judgment, vague decision |
| F09 | Collaboration communication | email, status update, decision memo, feedback | wrong tone, buried action, altered commitment |
| F10 | Tutorial and education | tutorial, lesson plan, onboarding, teaching material | skipped prerequisites, unsafe sequence, cognitive overload |
| F11 | Incident and operational writing | incident report, postmortem, runbook, risk notice | invented causality, blame language, hidden uncertainty |
| F12 | Marketing and public copy | product description, campaign copy, landing copy, brand story | fabricated proof, exaggerated claims, generic persuasion |

This taxonomy intentionally includes generation, rewriting, compression, adaptation, and operational writing. It excludes fiction, poetry, formal legal advice, serious news reporting, and AI-detector evasion because those are outside `human-writing`'s declared scope.

## Data split and optimization rule

For every family:

```text
D01-D80: adaptive development
  batch 01 = cases 01-10 → review → optional revision
  ...
  batch 08 = cases 71-80 → review → freeze candidate

H01-H20: sealed final holdout
  no review, prompt inspection, or Skill change before all outputs are complete
```

Development scores describe a sequence of versions and must not be averaged into a single leaderboard. The only cross-Skill headline is the final frozen-revision holdout result. If a later Skill change occurs, all 240 holdout cases must be discarded for that revision and replaced or resealed before another headline score.

## Four fixed competitors

| Skill | Repository | Fixed revision for initial development |
| --- | --- | --- |
| human-writing | `idaibin/skills` | `07d5a6bd21ff69d4bda5cc52b6cb316bbf80506c` |
| humanizer | `blader/humanizer` | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` |
| Humanizer-zh | `op7418/Humanizer-zh` | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` |
| stop-slop | `hardikpandya/stop-slop` | `8da1f030185bdfe8471220585162991eaeb970e9` |

Comparison Skills remain fixed. Every `human-writing` revision is stored by immutable commit and content tree. A development batch is regenerated for all four Skills only when the prompt/corpus changes; when only `human-writing` changes, comparator artifacts remain immutable and all anonymous judgments are regenerated.

## Corpus policy

The first source is WritingBench, inspected at repository commit `ae2d5176449b7b769815482641d35926f26793eb`. It contains 1,000 English/Chinese writing queries across six domains and 100 subdomains under Apache-2.0. It supplies broad generation tasks and dynamic per-query checklists, but it does not by itself provide enough source-grounded rewriting, task delegation, or incident operations. Some prompts embed open-source or quoted third-party material; repository-level Apache-2.0 metadata does not by itself prove that every embedded passage can be republished. Publication therefore remains blocked on per-case third-party-material review.

Additional cases must satisfy all of these gates:

- stable upstream identity, revision, license, and source locator;
- exact prompt and any source material stored or reproducibly materialized;
- no private, personal, secret, or access-controlled content;
- no case selected after seeing a candidate Skill output;
- deduplication by normalized prompt/source hashes and semantic near-duplicate review;
- balanced Chinese/English target, operation, length, and output format per family;
- case-specific deterministic constraints and reviewer criteria frozen before generation;
- no benchmark reference answer exposed to generators.

Raw third-party corpora may remain source-addressed rather than copied when redistribution terms are narrower than experiment use. The manifest stores immutable locators and content hashes either way.

## Evaluation protocol

Each case has hard gates and quality criteria.

Hard gates fail independently of prose preference:

- protected strings, numbers, commands, names, and required fields;
- explicit format, language, length, and scope constraints;
- claim/actor/modality/uncertainty preservation for source-grounded tasks;
- no unsupported personal experience, metric, result, attribution, or authority;
- exact no-op where the prompt explicitly requires preserving an already-effective artifact.

Anonymous judges score fidelity, instruction/structure, clarity, naturalness, restraint, and task-specific criteria with frozen 1/3/5 anchors. Candidate positions use seeded balanced permutations. Every batch has at least three independent judge contexts; ties split first share. Hard-issue text is parsed separately from numeric quality.

The headline report includes paired per-case differences, bootstrap 95% confidence intervals, win/tie/loss counts, hard-issue rates, and family macro-average. `human-writing` reaches parity with a comparison Skill only when:

1. the paired holdout mean difference is no worse than −0.10/5;
2. the 95% confidence interval's lower bound is above −0.15/5;
3. its hard-issue rate is not higher by more than one percentage point;
4. no family has a material safety or fidelity regression hidden by the macro-average.

These are experiment decision thresholds, not a claim of universal equivalence.

## Review and change control

Every 10-case development review stores:

- raw four-Skill artifacts and judge packets;
- deterministic-gate failures and exact hard issues;
- per-case and dimension differences;
- one failure taxonomy with representative evidence;
- proposed change, affected files, expected general behavior, and counterexample;
- forward tests on a fresh batch plus regression and anti-overfitting checks;
- 每个 120-case wave 必须保存 12 份 `family_slice` Review（每类恰好 10 例），再保存唯一一份覆盖完整 wave 的 `global_wave` decision；
- decision 使用机器合同中的 `no_change`、`candidate`、`accepted`、`reverted` 或 `blocked`。只有 global decision 可以接受或回滚行为变更，每个 wave 最多接受一次。

A weak batch score alone is not authorization to change the Skill. A change requires a recurring, generalizable failure and a regression case. The same case that motivated a rule may verify the defect but cannot establish generalization.

## Execution scale and persistence

Full scope is at least 4,800 generated artifacts before retries, plus anonymous judgments. It is a multi-stage experiment, not one interactive turn. The harness must support content-addressed artifacts, resumable jobs, immutable batch manifests, atomic state transitions, and fail-closed validation before aggregation.

GitHub is the durable evidence store for manifests, prompts permitted for redistribution, hashes, scripts, scores, review records, and compact artifacts. Large raw corpora or output bundles may be stored as release assets or external content-addressed objects, but GitHub must retain their checksums and retrieval contract. Google Drive is not the canonical benchmark store.

## Completion contract

The benchmark is complete only when:

- all 1,200 cases pass corpus and license validation;
- all 80 development cases per family have eight saved review decisions;
- a final immutable `human-writing` revision is frozen before holdout access;
- all 240 holdout cases have four outputs, hard gates, three anonymous judgments, and parsed rankings;
- confidence intervals and family macro-results are reproducible from stored records;
- an independent reviewer finds no version, leakage, mapping, arithmetic, or claim blocker;
- all artifacts and exact fixed revisions are accessible from GitHub.

Until then, status remains `in_progress`; no 1,200-case result or broad superiority claim is valid.
