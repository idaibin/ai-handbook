# Evaluation rubric

Date basis: 2026-08-13  
Applies to: all development and sealed-holdout cases in this experiment

## 1. Scoring order

For each anonymous candidate:

1. read the task, source material, protected spans, explicit constraints, atomic
   claims, and case-specific criterion;
2. run or inspect deterministic gates;
3. identify semantic hard issues with exact evidence spans;
4. score each leaf independently using its 1/3/5 anchors;
5. compute the weighted quality score;
6. rank all four candidates, allowing a tie when there is no material preference.

Do not infer quality from Skill identity, response position, length, formatting polish,
or apparent authorship. Do not reward additional facts, experience, confidence, or
personality unless the task and source support them.

## 2. Weighted tree

| Parent | Leaf | Weight | Primary question |
| --- | --- | ---: | --- |
| Content | Fidelity and factual support | 30% | Does the answer preserve and support the source's actual claims? |
| Content | Case-specific content criterion | 20% | Does it solve the content problem unique to this case? |
| Form | Instruction and structure | 15% | Does it follow the requested contract and group information meaningfully? |
| Form | Clarity | 10% | Is the result easy to understand without changing meaning? |
| Impression | Naturalness and audience fit | 15% | Does it sound appropriate and non-mechanical for the intended reader? |
| Impression | Restraint | 10% | Does it avoid unsupported expansion, filler, hype, and over-editing? |

The weighted score is:

```text
0.30 × fidelity
+ 0.20 × case_specific_content
+ 0.15 × instruction_structure
+ 0.10 × clarity
+ 0.15 × naturalness_audience
+ 0.10 × restraint
```

All leaves are integers from 1 to 5. The final weighted score may be fractional. Hard
gates are reported separately and determine eligibility; a polished high score cannot
cancel a hard failure.

## 3. Leaf anchors

### 3.1 Fidelity and factual support — 30%

Evaluate atomic claims, actors, modality, uncertainty, negation, quantities, dates,
causal direction, attribution, commands, identifiers, and protected content. For an
open-generation case, evaluate support from the supplied facts and task rather than
similarity to a preferred answer.

- **5 — complete and exact:** preserves all required claims and qualifiers; every new
  factual statement is supported; omissions are explicitly permitted or immaterial;
  protected content is exact.
- **3 — localized weakness:** the central meaning remains intact, but one non-critical
  detail is imprecise, weakly supported, or omitted. No critical claim is reversed.
- **1 — material failure:** invents or reverses a claim, loses a critical qualifier or
  attribution, changes an actor/number/time/command, fabricates evidence, or otherwise
  makes the artifact unsafe to rely on.

### 3.2 Case-specific content criterion — 20%

This leaf is frozen in the case manifest before generation. It must name a content
capability that the generic leaves do not already capture, such as completeness of a
technical comparison, preservation of action/owner/deadline in a handoff, separation
of fact from inference in research, or coverage of prerequisites in a tutorial.

- **5 — fully solves it:** covers all required case-specific content with correct
  relationships and useful emphasis.
- **3 — partial:** addresses the criterion but misses one important component or gives
  it insufficient depth.
- **1 — fails:** largely omits, misunderstands, or contradicts the criterion.

The criterion cannot name a Skill, expected winner, preferred phrase, or stylistic
feature discovered by inspecting outputs. When a case contains multiple frozen
criteria, judges score every `criterion_id` independently. Aggregation first takes the
three-judge median for each criterion, then normalizes the case's positive criterion
weights within the task-specific 20% branch. Missing, duplicate, or unknown criterion
IDs invalidate the judgment; they are never collapsed into one generic score.

### 3.3 Instruction and structure — 15%

Evaluate required language, format, length, scope, audience contract, fields, ordering,
and semantic grouping. More headings or bullets are not inherently better.

- **5 — exact and coherent:** satisfies all explicit constraints and organizes each
  semantic unit at the level the task needs; conditions, limitations, and conclusions
  remain connected.
- **3 — usable with friction:** follows the main contract but has a minor format or
  organization defect, such as an unnecessary split, weak ordering, or small length
  miss.
- **1 — contract failure:** violates a must-have format/language/length/scope rule,
  omits a required field, or fragments/reorders content so severely that relationships
  are lost.

### 3.4 Clarity — 10%

Evaluate local readability, referent clarity, logical flow, and effort required from
the intended reader.

- **5 — immediately clear:** precise wording, unambiguous references, smooth logical
  progression, and appropriate information density.
- **3 — understandable:** meaning can be recovered, but awkward syntax, repetition,
  vague references, or uneven density causes avoidable rereading.
- **1 — difficult or misleading:** ambiguity, incoherence, poor sequencing, or dense
  abstraction materially obstructs comprehension.

### 3.5 Naturalness and audience fit — 15%

Evaluate whether the prose fits its actual audience, channel, and requested voice.
Naturalness means context-appropriate human communication, not forced informality or
invented personality.

- **5 — credible and fitted:** varied but controlled rhythm, direct transitions, and a
  voice appropriate to the target reader and medium; no conspicuous template residue.
- **3 — competent but mechanical:** generally appropriate, with repeated sentence
  patterns, generic transitions, over-uniform bullets, or mild mismatch in tone.
- **1 — conspicuously artificial or wrong for audience:** canned framing, sloganized
  prose, forced intimacy, exaggerated emotion, or a serious register mismatch.

### 3.6 Restraint — 10%

Evaluate whether every addition, emphasis, label, transition, and structural device
earns its place. Concision is task-relative; a long tutorial is not penalized merely
for being long.

- **5 — disciplined:** includes what the task needs, removes genuine filler, preserves
  useful nuance, and avoids unsupported expansion or decorative structure.
- **3 — mildly over/under-edited:** some filler, repetition, unnecessary labels, or
  compression remains, but the result is still usable.
- **1 — materially unrestrained:** adds hype, moralizing, invented experience,
  repetitive conclusions, excessive scaffolding, or compresses away required nuance.

## 4. Hard gates

Hard issues are categorical evidence records, not prose-preference deductions. Each
record contains `type`, `severity`, `source_evidence`, `output_evidence`, and a concise
explanation.

### Critical hard issues

Any of the following makes the output ineligible for a passing result:

- unsupported fact, metric, quotation, attribution, personal experience, authority,
  implementation state, or causal relationship;
- omission, reversal, or material weakening/strengthening of a required atomic claim;
- changed negation, condition, modality, uncertainty, scope, actor, date, quantity,
  identifier, command, URL, or protected span;
- fabricated citation or source;
- violation of a mandatory safety, language, output-form, field, or scope constraint;
- unauthorized change in an explicit exact no-op case.

### Major non-critical hard issues

Record separately when the artifact remains usable but violates a frozen deterministic
contract, such as a material length miss, an omitted secondary required field, or a
non-critical protected-format failure. It still counts in hard-issue rate and must not
be hidden by the quality mean.

Minor style preferences are not hard issues. A judge must quote or locate concrete
evidence; unsupported `hard_issue=true` labels are invalid.

## 5. Family-specific criterion guidance

The manifest chooses one or more concrete checks and then freezes a single scored
case-specific content leaf. Typical checks include:

| Family | Valid case-specific checks |
| --- | --- |
| F01 AI and technical explanation | capability boundaries, uncertainty, comparison basis |
| F02 Software engineering | invariants, interfaces, acceptance evidence, implementation status |
| F03 Source-grounded rewrite | claim coverage, voice preservation, authorized transformation |
| F04 Blog and long-form article | argument progression, concrete support, opening/ending function |
| F05 Social post and thread | context retention, post-level coherence, platform length contract |
| F06 Summarization and synthesis | coverage, attribution, salience, fact/inference separation |
| F07 Task delegation and planning | owner, input, output, constraints, done condition, authority |
| F08 Product and business writing | decision criteria, risk/evidence separation, unresolved choices |
| F09 Collaboration communication | action visibility, commitment strength, tone and recipient fit |
| F10 Tutorial and education | prerequisites, sequence, checks for understanding, safe procedure |
| F11 Incident and operations | observed fact vs hypothesis, timeline, causal uncertainty, recovery |
| F12 Marketing and public copy | supported claims, audience value, proof boundaries, call to action |

These checks guide case authors; they do not authorize adding unstated requirements
after outputs exist.

## 6. Ranking and evidence

After scoring all four candidates independently, rank them by overall task usefulness,
using hard-gate eligibility before small quality-score differences. A critical hard
failure cannot outrank an otherwise comparable eligible answer solely because its
style is more polished. When two answers have no material difference, record a tie
rather than manufacturing a preference.

Every ranking must include:

- a complete `A-D` order with explicit ties;
- leaf scores for all candidates;
- hard-issue evidence or `none`;
- one concise reason grounded in the task/rubric.

Length, extra headings, bullets, bold text, confident tone, and apparent detail are not
independent evidence of quality. Reference overlap is diagnostic only; alternative
wording may receive full credit when it preserves content and satisfies the task.

## 7. Position and review-calibration handling

Judges must follow the seeded anonymous mapping supplied by the evaluator. At least 20%
of cases receive a fresh swapped-order evaluation. If preference reverses after the
swap, mark the pair/case `position_inconsistent`; do not average the contradiction into
a confident win.

Fresh agent review contexts apply the same leaves and hard gates. They must remain
blinded to Skill identity and automated preference. Two separate reviews are required
for selected cases, with a third context adjudicating material disagreement. Holdout
review starts only after both holdout waves and all automated artifacts are locked.
This calibration is not evidence of human review or cross-provider independence.

## 8. Aggregation eligibility

An output enters aggregation only if its case hash, Skill revision, anonymous mapping,
all six leaf scores, hard-issue record, and complete ranking validate. Missing records
fail closed; they are not assigned zero and are not silently dropped.

The headline score uses only one frozen `human-writing` revision over all 240 sealed
holdout cases. Development versions and holdout results are never mixed. Parity,
confidence intervals, hard-issue thresholds, human calibration, and stopping decisions
are defined in `protocol.md`.
