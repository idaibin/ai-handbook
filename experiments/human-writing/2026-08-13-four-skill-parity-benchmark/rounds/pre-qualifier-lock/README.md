# Pre-qualifier-lock round

This saved round tested `human-writing` commit `aeb4a29e4f3646806542a5eb3891a44b91138f82` against the same three fixed comparison skills. All generation and judgment artifacts are preserved in this directory.

| Skill | Repair mean / 5 | Fidelity | Structure | Naturalness | Hard-issue flags / 18 | Repair first-place share / 18 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| human-writing | **4.878** | 4.889 | **5.000** | 4.667 | 1 | 6.667 |
| humanizer | 4.833 | 4.889 | 4.833 | **4.722** | 1 | **7.667** |
| stop-slop | 4.411 | 3.778 | 4.722 | 4.611 | 10 | 2.333 |
| Humanizer-zh | 3.922 | 4.444 | 3.611 | 3.833 | 5 | 1.333 |

The one `human-writing` hard issue was a judge-flagged omission of the scope qualifier `主要` in C03. This result triggered the qualifier-lock revision; it is not the final parity result.
