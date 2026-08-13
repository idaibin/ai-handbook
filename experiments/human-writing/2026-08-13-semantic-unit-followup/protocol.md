# Protocol

## Authority and isolation

- Repository policy basis: `idaibin/ai-handbook` main commit `fb101496f52bbc1a403f825c8825622c080b3a42`, especially `workflows/ai-engineering-system/README.md`, `skill-validation.md`, and `storage-policy.md`.
- Baseline and candidate Skills were materialized in separate temporary directories.
- Each execution agent could read only its assigned Skill, references that Skill routed for the task, and the neutral input file.
- Execution agents could not read expected criteria, the other Skill, prior outputs, reports, or experiment conclusions.
- Blind judges could read only the randomized review packet and its anchored rubric.
- Adjudicators could read only frozen criteria and the named raw outputs.

Every raw output records its task constraint and files read. Before publication, machine-local absolute paths were mechanically replaced with `<materialized>/...` and `<run-output>/...`; task wording and generated artifacts were otherwise retained. The model was `gpt-5.6-sol` at high reasoning effort in fresh isolated agent contexts. The host did not expose temperature or seed controls.

## Evidence phases

1. **Original rerun:** sensitivity check on the prior ten cases; not used for an improvement estimate because both variants passed the target cases in this sample.
2. **Adversarial development:** used to refine the rule and expose over-grouping; not a holdout.
3. **Frozen holdout:** inputs and exact criteria were written and hashed before three baseline and three candidate generations. The intermediate candidate revision was not retained, so its saved 14/18 result is observational rather than reproducible implementation evidence.
4. **Fixed-revision closure comparison:** three runs each of immutable baseline `aa73fec2f8630886b7d60b066f1de4deff96b60a` (tree `fba2a3cc569c99a15c24ea4e0c0b92067bd44eb0`) and final candidate `aeb4a29e4f3646806542a5eb3891a44b91138f82` (tree `0a06fc4c122bd095cd6527c6102ed20239c26ffd`). The temporary materializations used for these runs were created from those unchanged trees. Criteria codified the intended rule after candidate generation, so this is reproducible regression evidence, not a preregistered holdout.

Holdout SHA-256 values before generation:

- inputs: `b76da422a60a5bfb76d6d3aa3cf731d15f29715ba8419c9347d5594269ef839f`
- criteria: `9a37bc7f9e3b01c420f9cf4cf8e15adf55398dee528a58df212f31c8d28d6434`

## Decision rules

A case passes only when its exact structural condition and every source fact, relation, modality, actor, protected word, and explicit format constraint are preserved. Markdown backticks in a `Protected` declaration identify a literal span; the output need not add backticks when the source did not contain them.

No detector score contributes to the result. Development judge preferences are retained as diagnostic evidence but do not replace the deterministic holdout criteria.

## Claim floor

Allowed: “On the fixed-revision repeated regression comparison, the baseline scored 3/18 and the final candidate 13/18. Two candidate outputs failed for adding an explicit causal connector, and several target cases remained stochastic. An earlier frozen holdout moved from 9/18 to 14/18, but its intermediate candidate revision was not retained and that result is observational only.”

Not allowed: “Semantic-unit recognition is solved,” “the candidate now beats or equals Humanizer-zh,” “the result generalizes to all writing,” or “the Skill is stable.”
