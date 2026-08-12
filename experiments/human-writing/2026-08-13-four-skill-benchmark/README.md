# Four-skill source-grounded writing benchmark

Date: 2026-08-13  
Status: completed pilot; not a cross-model statistical benchmark

## Result

On this ten-case, source-grounded pilot, **Humanizer-zh placed first on aggregate blind quality**, while **human-writing and humanizer had perfect blind-judge fidelity scores**. `stop-slop` produced highly readable rewrites but had the most judge-flagged semantic-strength changes. Under an explicit conditional no-op instruction, all four left every already-compact case untouched; that is instruction-following evidence, not proof of unprompted restraint.

| Skill | Repair mean / 5 | Fidelity | Naturalness | Blind first-place share / 18 | Hard-issue flags / 18 | Protected cases | Negative controls unchanged |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Humanizer-zh | **4.856** | 4.889 | 4.667 | **13.000** | 1 | 10/10 | 4/4 |
| stop-slop | 4.367 | 3.333 | **4.833** | 0.500 | 15 | 10/10 | 4/4 |
| human-writing | 4.122 | **5.000** | 3.667 | 3.000 | **0** | 10/10 | 4/4 |
| humanizer | 3.978 | **5.000** | 3.556 | 1.500 | **0** | 10/10 | 4/4 |

`Hard-issue flags` are independent judge flags, not distinct defects: the same output can be flagged by all three judges. They cover fact omission/addition or changed modality/claim strength. First-place share splits a tie evenly.

## Per-case result

Each value is the mean of five dimensions from three anonymous judges. N01–N04 are intentionally unchanged controls; their four-way ties show compliance with the explicit conditional no-op instruction but do not distinguish rewrite quality or prove unprompted restraint.

| Case | Type | 1st | 2nd | 3rd | 4th | Main finding |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | Chinese storage policy | Humanizer-zh 5.00 | stop-slop 4.40 | human-writing = humanizer 3.67 | — | Humanizer-zh kept five coherent units; human-writing/humanizer over-split related constraints. |
| C02 | Chinese learning policy | Humanizer-zh 5.00 | stop-slop 4.33 | human-writing 3.80 | humanizer 2.93 | Humanizer-zh kept paired conditions together; humanizer produced the most fragmented list. |
| C03 | Chinese project assessment | Humanizer-zh 5.00 | stop-slop 4.33 | human-writing = humanizer 3.80 | — | stop-slop changed an interpretation boundary into categorical unusability. |
| C04 | English framework assessment | Humanizer-zh 5.00 | stop-slop 4.00 | humanizer 3.87 | human-writing 3.47 | human-writing was faithful but split four arguments into eight bullets. |
| C05 | Chinese technical process | Humanizer-zh = human-writing 5.00 | — | stop-slop 4.87 | humanizer 4.73 | All four were faithful; paragraph organization created the small difference. |
| C06 | English cross-repo findings | human-writing 5.00 | humanizer 4.87 | stop-slop 4.27 | Humanizer-zh 4.13 | stop-slop removed `automatically`; one judge found Humanizer-zh weakened the human-in-the-loop conclusion. |
| N01 | Chinese negative control | four-way tie 5.00 | — | — | — | All outputs exactly matched the input. |
| N02 | Chinese negative control | four-way tie 5.00 | — | — | — | All outputs exactly matched the input. |
| N03 | Chinese negative control | four-way tie 5.00 | — | — | — | All outputs exactly matched the input. |
| N04 | Chinese negative control | four-way tie 5.00 | — | — | — | All outputs exactly matched the input. |

## What was actually tested

The corpus contains ten excerpts from ten real, version-fixed documents in `idaibin/ai-handbook`:

- six excerpts were mechanically padded with formulaic framing and transitions without intentionally changing claims; the original excerpt is the reference;
- four already-compact excerpts were passed through unchanged to test over-editing;
- seven cases are Chinese and three are English or mixed-language technical prose;
- each case names exact protected terms, numbers, identifiers, or code spans.

Every reference was automatically verified as an exact substring of the source at commit `325c9daeb34df0abaee8f4efa8e715a6f0547887`. These are genuine project documents, not ten independently published magazine articles; the experiment therefore supports source-grounded technical/documentation rewriting, not every form of creative or consumer writing.

## Procedure

1. Freeze the corpus, source commit, four skill commits, instructions, protected spans and negative controls.
2. Give four fresh execution agents only `generator-inputs.md` plus their assigned fixed skill. The generator file uses neutral T01–T10 IDs and contains no source paths, references, condition labels or expected decisions. The execution tasks prohibit reading the rest of the experiment and save those constraints in run metadata.
3. Check all protected spans, exact negative-control preservation, output hashes and reference/input similarity with `evaluate.py`.
4. Build three separate A/B/C/D packets using seed `20260813` and Latin rotations. Across the six repair cases, every skill appears in each position four or five times.
5. Give each fresh judge only its own `results/blind-review-N.md`. The packet embeds dimension definitions, 1/3/5 anchors, the hard-issue/fidelity rule and case-specific criteria. Each judge records five scores, hard issues, evidence and a complete ranking.
6. Unblind and aggregate with `aggregate.py`.

Earlier pilot attempts were invalidated before the final run: one exposed the reference to generators, one contained an ambiguous instruction about preserving list form, one exposed condition labels, and one reused a candidate order across judges. None of those outputs or judgments appear in these results.

The rubric is an experiment-specific synthesis informed by dynamic task criteria in [WritingBench](https://arxiv.org/html/2503.05244v1), source-similarity/readability concepts in [TH-Bench](https://arxiv.org/html/2503.08708v2), and the source-grounded precision/recall emphasis of [ExPerT](https://aclanthology.org/2025.findings-acl.900/); it is not an official implementation of any of those benchmarks. It deliberately excludes AI-detector evasion. ExPerT also documents position and manipulation bias in LLM judges, which is why packets use balanced rotations and deterministic gates are reported separately.

## Skill-by-skill interpretation

### Humanizer-zh

Best aggregate result, winning outright on C01–C04 and tying on C05. It grouped connected conditions into one bullet without losing facts. One judge flagged C06 for weakening the direction of the human-in-the-loop claim. This single-run result does not make the repository independent evidence: Humanizer-zh derives from humanizer and stop-slop, and the earlier source audit still found fact-inventing examples outside this frozen corpus.

### human-writing

Perfect fidelity and no hard-issue flags. It tied first on C05 and won C06, but over-split C01–C04, reducing naturalness and restraint. The concrete improvement target is unchanged: when the user asks for one bullet per claim, treat a condition plus its boundary as one claim rather than atomizing every sentence.

### stop-slop

Highest naturalness score and strong clarity, but the weakest fidelity score and fifteen judge flags. It made one systematic risky edit in five of six repair cases: dropping or strengthening `automatically`, `优先`, the checkpoint interpretation boundary, or the explicit non-automatic durability boundary. Under the anchored rubric, each localized hard issue also reduced restraint. This is the clearest evidence that surface smoothness cannot be the only objective.

### humanizer

Perfect fidelity and no hard-issue flags, with its strongest result on C06. It ranked fourth overall because it split paired claims and follow-up actions into too many bullets on C01–C04. This is a style/structure failure rather than a factual one.

## Limits and decision

- One generation run per skill is too small for a stable leaderboard.
- The runtime did not expose the exact model ID or sampling parameters; the four fresh agents used the same Codex Work Mode context class, but exact sampling equality cannot be proven.
- All three judges are model judges from the same environment, not human editors; their errors may be correlated.
- The corpus is one repository's technical and research prose. It does not cover fiction, marketing, personal essays, news or long-form narrative.
- Reference similarity is diagnostic only and is not included in the quality ranking.

Decision: retain `human-writing` as **pilot**, not `stable`. It did not win aggregate quality, but it preserved every judged claim boundary and exposed a narrow, testable structure weakness. A stable claim would require multiple runs, at least one independent human panel, more genres and at least one different model family.

## Reproduce and inspect

```bash
python3 experiments/human-writing/2026-08-13-four-skill-benchmark/evaluate.py
python3 experiments/human-writing/2026-08-13-four-skill-benchmark/aggregate.py
python3 experiments/human-writing/2026-08-13-four-skill-benchmark/test_aggregate.py
git diff --check
```

- `manifest.yaml`: fixed versions and execution limits
- `protocol.md`: exact effective generator, judge and aggregation contracts
- `cases.md`: sources, references, controlled inputs and protected spans
- `generator-inputs.md`: neutral exact generator input without sources, references or condition labels
- `outputs/`: all forty final outputs and run metadata
- `results/automatic.json`: deterministic per-output checks and hashes
- `results/blind-review-1.md` to `blind-review-3.md`: independently positioned anonymous judge packets
- `results/blind-mappings.json`: deterministic unblinding maps
- `results/judge-1.md` to `judge-3.md`: complete per-case evaluations
- `results/aggregate.json`: machine-readable unblinded scores
