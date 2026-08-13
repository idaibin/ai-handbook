# Large-scale benchmark protocol

Date basis: 2026-08-13  
Status: preregistered execution contract; no large-scale result yet

## 1. Decision and scope

This experiment compares one evolving Skill, `human-writing`, with three fixed
comparison Skills over 12 professional-writing families and 100 cases per family.
It measures writing quality, instruction compliance, source fidelity, and harmful
semantic changes. It does not measure fiction, poetry, formal legal advice, serious
news reporting, or AI-detector evasion.

The comparison identities are frozen by repository commit and content hash before
generation:

| Skill | Role | Initial revision |
| --- | --- | --- |
| `human-writing` | evolving candidate | `07d5a6bd21ff69d4bda5cc52b6cb316bbf80506c` |
| `humanizer` | fixed comparator | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` |
| `Humanizer-zh` | fixed comparator | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` |
| `stop-slop` | fixed comparator | `8da1f030185bdfe8471220585162991eaeb970e9` |

Repository popularity is selection context only; it is not evaluation evidence.

## 2. Fixed split and round-robin waves

Each family contains 80 visible development cases and 20 sealed holdout cases:

```text
D01-D80: eight development waves of 10 cases per family
H01-H20: two sealed holdout waves of 10 cases per family
```

A wave is round-robin across all 12 families. Development wave 1, for example,
contains `F01-D01..D10`, `F02-D01..D10`, through `F12-D01..D10`, for 120 cases.
All four Skills finish the same wave before review starts. This prevents an early
family from receiving more optimization than a later family.

Every 10-case family slice is balanced by a seeded assignment over language,
operation, input/output length, output form, constraint density, fidelity risk, and
no-op controls. The seed, case IDs, source hashes, and assignment are frozen in the
wave manifest before any output is generated.

### Development waves

After each complete 120-case development wave:

1. validate artifacts and deterministic gates;
2. finish anonymous judging and the required human review;
3. publish a failure taxonomy with exact case evidence;
4. save twelve `family_slice` Reviews, each covering exactly the family's ten cases,
   then one unique `global_wave` decision covering their exact 120-case union;
5. record the machine decision enum `no_change`, `candidate`, `accepted`, `reverted`,
   or `blocked`;
6. if justified, make at most one general `human-writing` change; only the global
   decision may accept or revert that change;
7. freeze its new commit and content hash before opening the next wave.

A low mean alone does not justify a change. A change requires a reproducible hard
failure or a recurring general failure, a stated mechanism, a counterexample, and a
regression case. The motivating case may confirm the defect but cannot establish
generalization.

### Sealed holdout waves

The final `human-writing` revision is frozen after development wave 8. Holdout prompts,
source material, rubrics, protected content, outputs, scores, or partial aggregates
must not be exposed to Skill authors or optimization agents until all 240 holdout cases
have completed all four generations, deterministic gates, three-judge evaluation,
position audits, and artifact validation.

No feedback or Skill change is allowed between holdout waves 1 and 2. Review may begin
only after the complete holdout is locked. Any later Skill change creates a new
candidate: the existing holdout can no longer support a headline score for it and must
be replaced or resealed with fresh cases.

## 3. Version and score isolation

Development scores form a versioned learning curve. They must not be averaged into a
single Skill leaderboard because different waves may use different `human-writing`
commits. Each row of every result stores the exact Skill commit and tree hash.

The only headline cross-Skill result uses one frozen `human-writing` revision and all
240 holdout cases. Comparator outputs remain content-addressed and immutable when only
`human-writing` changes. If the prompt, source, rubric, generator contract, or corpus
changes, all four outputs for the affected cases are invalidated and regenerated.

## 4. Corpus and leakage gates

Every case must be specified before generation with:

- task family, operation, language, target audience, length band, and output form;
- exact prompt and source material or an immutable materialization locator;
- license, provenance, content hash, and redistribution status;
- atomic source claims and their evidence spans where fidelity is applicable;
- protected spans, deterministic constraints, permitted omissions, and forbidden
  additions;
- a frozen rubric tree and hard gates;
- split and wave assignment.

Exact normalized prompt/source hashes cannot cross cases. Semantic near-duplicates are
flagged by the corpus tooling and manually resolved before split freeze; no threshold
alone is treated as proof of duplication. Cases cannot be selected, rewritten, or
reweighted after seeing a candidate output. Reference answers, expected winners, Skill
identities, split labels, and source benchmark metadata are hidden from generators.

## 5. Generation contract

Every Skill receives a fresh isolated context containing only:

1. the common system and user task contract;
2. its fixed Skill tree;
3. the current neutral case packet.

The generator model, exact revision, decoding parameters, tool access, token limit,
and retry policy are identical. A Skill cannot read another Skill, output, judgment,
mapping, review, or expected result. Generated artifacts contain only the requested
answer plus machine-written run metadata outside the judged text.

The base run produces exactly:

```text
12 families × 100 cases × 4 Skills = 4,800 generated outputs
```

Retries and stochastic-repeat samples are additional artifacts and are never silently
substituted. A stratified 10% sample is generated a second time with the preregistered
second seed. If its mean absolute score difference exceeds 0.10/5 or more than 10% of
sampled cases reverse the leading Skill, repeat generation expands to the complete
holdout and the added variance is reported.

## 6. Deterministic gates and scoring

The rubric in `rubric.md` is authoritative. Deterministic gates run before LLM
judging and fail closed on missing input, unparsable records, invalid mappings, absent
protected spans, or impossible constraints. Quality scores do not erase hard issues;
both uncapped quality and gate eligibility are retained.

The score tree is:

```text
Overall
├── Content 50%
│   ├── Fidelity and factual support 30%
│   └── Case-specific content criterion 20%
├── Form 25%
│   ├── Instruction and structure 15%
│   └── Clarity 10%
└── Impression 25%
    ├── Naturalness and audience fit 15%
    └── Restraint 10%
```

Each generic leaf uses frozen 1/3/5 anchors. Every case-specific criterion is generated
and reviewed before outputs exist and receives its own judge score keyed by
`criterion_id`. For each criterion, aggregation takes the three-judge median; the
case's positive criterion weights are then normalized within the task-specific 20%
branch. Reference text is evidence for content and style requirements, not a unique
valid answer.

## 7. Anonymous judge protocol

Each case receives three independent judge evaluations. The required configuration is
three distinct model families from at least two providers, with exact model revisions
and prompts recorded. A single provider/model family in three contexts is not a
cross-model evaluation and cannot satisfy the completion gate. If the required models
are unavailable, execution pauses or the limitation is explicitly approved and human
review is expanded to at least 20%; the result cannot be described as independently
cross-model verified.

Judges see anonymous candidates `A-D`; they do not see Skill names, commits, stars,
development history, prior scores, or expected rankings. Candidate positions are
seeded and balanced within judge, family, wave, language, and length band. Each judge
first scores every candidate independently by rubric leaf, then records hard issues,
evidence spans, and a complete ranking with ties allowed.

At least 20% of cases, stratified by family and split, receive a swapped-order audit.
The candidate order is reversed in a fresh judge context without revealing the first
decision. A reversed preference is marked position-inconsistent and cannot be forced
into a win; it enters human review. Holdout swap results remain sealed with all other
holdout evidence.

The parser fails unless every expected candidate appears exactly once per judge/case,
all scores are in range, mappings are bijective, rankings are complete, and hard-issue
records are parseable.

## 8. Human review

For each development wave, sample at least 12 cases (10%), stratified to include at
least one case from every family. Add all deterministic/semantic hard issues, swapped-
order reversals, high judge disagreements, malformed artifacts, and cases near a
decision boundary.

After the complete holdout is locked, review at least 24 holdout cases (10%), with at
least two cases per family, plus all mandatory escalations. Two blinded reviewers
independently inspect all four outputs for each selected case. A third reviewer
adjudicates disagreements. Reviewers see the task, source evidence, constraints, and
rubric, but not Skill identities or automated preferences.

Report pairwise human agreement, weighted Cohen's kappa for ordinal leaves, judge-human
preference agreement, and position consistency. The operational calibration targets
are at least 75% judge-human pairwise agreement, weighted kappa at least 0.50, and 90%
position consistency. These are experiment thresholds, not universal standards. If a
target fails, automated preference claims are blocked until the disagreement is
resolved or the result is explicitly limited to descriptive evidence.

## 9. Aggregation and uncertainty

The primary unit is a holdout case, not an individual judge row. Leaf scores are first
aggregated across the three judges by the preregistered median and then combined by the
fixed rubric weights. Ties split first-place share. Report per Skill and per family:

- weighted quality mean and distribution;
- paired per-case differences;
- win/tie/loss and first-place share;
- hard-issue count and rate by severity/type;
- no-op preservation and deterministic-gate pass rate;
- family macro-average and language/length slices.

Confidence intervals use 10,000 seeded, stratified cluster-bootstrap resamples of
holdout cases. A case and all its candidates/judgments move together. The primary
overall interval is stratified by family; family intervals resample within family.
Twelve family-level secondary comparisons use Holm correction. Missing or invalid
cases block aggregation rather than being dropped.

For each fixed comparator, let `d = human-writing - comparator` on the 1-5 weighted
scale. `human-writing` reaches experiment parity only if all of these preregistered
conditions hold:

1. paired holdout mean `d >= -0.10`;
2. the bootstrap 95% confidence interval lower bound is greater than `-0.15`;
3. the hard-issue rate is no more than one percentage point above the comparator;
4. no family contains a material safety or fidelity regression hidden by aggregation.

All three comparisons are reported. `Parity` is an experiment-level non-inferiority
decision, not proof of universal equivalence. `Superior` requires a two-sided 95%
confidence interval wholly above zero, the same hard gates, and no family blocker.
Merely including zero in a confidence interval is not evidence of equality.

## 10. Review, change, and stop rules

Each development review stores raw artifacts, judge packets, mappings, hard issues,
dimension differences, the failure taxonomy, the proposed change, expected mechanism,
counterexample, regression checks, commit, and decision. One review wave permits at
most one accepted behavior change.

Stop or pause optimization when any condition holds:

- development wave 8 is complete; freeze the candidate;
- two consecutive waves produce no reproducible general failure that justifies a
  change;
- a proposed change causes a critical fidelity regression; revert it;
- corpus, judge, or mapping integrity fails; repair before continuing;
- 80% of the approved budget is consumed before holdout starts; preserve the sealed
  holdout rather than shrinking it;
- a required cross-model judge or human-calibration gate is unavailable.

The experiment completes only after all 4,800 base outputs, 240 holdout three-judge
records, position audits, human reviews, bootstrap results, exact revisions, manifests,
and an independent integrity review are durably accessible. Until then, no large-scale
parity or superiority claim is valid.

## 11. Method sources and limits

- [WritingBench](https://arxiv.org/html/2503.05244) supplies the primary precedent for
  broad domain coverage, query-dependent criteria generated before scoring, rubric-
  based evaluation, and explicit human-alignment validation.
- [TH-Bench](https://arxiv.org/html/2503.08708) motivates keeping semantic preservation,
  fluency/readability, and cost separate. Its detector-evasion objective is explicitly
  outside this experiment and is not used as a quality target.
- [ExPerT](https://aclanthology.org/2025.findings-acl.900/) motivates atomic claim/aspect
  extraction with evidence and separate content/style alignment for source-grounded
  writing.
- [HoWToBench and Tree-of-Writing](https://arxiv.org/html/2604.19071) motivates explicit
  hierarchical weights and hybrid rule/LLM evaluation rather than an unconstrained
  overall impression.
- [Judging the Judges](https://aclanthology.org/2025.ijcnlp-long.18/) directly supports
  measuring position consistency and balancing candidate positions.

The score weights, non-inferiority margins, calibration targets, sampling rates, and
stop rules are this experiment's preregistered decisions. The cited papers do not
establish them as universal objective standards.
