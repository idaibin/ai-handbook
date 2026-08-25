# Execution Record

## Unit

`VISUAL_REGISTRY_MVP_01 / UNIT_02_STATIC_COMPILER`

## Entry basis

- `idaibin/ai-handbook@dc8925bd7b5760a1a591c77e8e9e69abcbacb722`
- user-authorized continuation without confirmation
- existing experiment rules in `experiments/README.md`

## Scope

- audit six named repositories at fixed commits;
- define one provider-neutral Schema;
- create three original Golden Candidate contracts;
- implement Gemini, Flux, and Midjourney text adapters;
- run deterministic static tests;
- persist generated evidence.

## Execution history

1. Initial TypeScript build failed because the `50mm` lexicon key was not quoted.
2. The syntax defect was fixed and the complete test command passed.
3. Architecture self-review found that `category` incorrectly named consumers; it was changed to provider-neutral visual domains while consumers remain metadata.
4. Runtime self-review found that an unknown adapter target could fall through the switch; explicit target and empty-subject guards were added with negative tests.
5. The final suite passed in the working copy and in a clean copied directory with generated evidence removed before execution.
6. The clean-copy and working-copy compiler output hashes matched exactly.

## Final result

```text
status: passed_static_validation
validation_level: static_and_unit_tests
contracts: 3
consumer_cases: 3
adapters: 3
compilations: 9
compiler_output_sha256: 46b3be7e6600c8e7284324e1a85cd1ee6cf6093fce365a7fc187efe346b01edb
```

## Gate decision

The static compiler prototype may remain in `ai-handbook/experiments` for a real provider trial. It is not authorized for promotion into `skills`, and no public website is authorized.

## Not verified

- real Gemini, Flux, or Midjourney image generation;
- cross-provider visual similarity;
- quality against a manually authored prompt baseline;
- runtime integration with Story Studio or UI Spec.

## Next action

Run one controlled image-generation comparison for `historical_han_realism` and one UI mockup comparison for `saas_bento_dashboard`, preserving provider receipts, inputs, outputs, and review criteria.
