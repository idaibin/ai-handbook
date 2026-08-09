# patched-codes/patchwork workflow assessment

- Fixed commit: `21948cbec44d3b7aec30715923ac7a0cd3fb1155`
- Tree/content: `git-tree:62ece37211e8d9a6790b7e3e36f0b5a627ec8343`
- Observed: 1,571 Stars; `main`; not forked or archived
- License: AGPL-3.0
- Evidence: `source_validated`; Python compile check passed, behavioral runtime not validated
- Subtype/topic fit: `linear-code-orchestration`; fit

## Verified

Patchflows are Python classes containing ordered steps. The CLI resolves YAML/config/CLI inputs, loads a patchflow class and calls `run()`. Step state is in-memory completed, skipped, warning or failed. AutoFix performs Semgrep, extraction, LLM analysis and file modification, then PR creation; PRReview reads a diff, produces a two-stage LLM review and writes a comment; ResolveIssue lets an agent inspect and mutate a repository before PR work.

Effects include editing files, branch switching, commits with `--no-verify`, push/force push, PR create/update, comments and opt-out telemetry. Existing-PR lookup avoids unconditional duplicate PR creation, but there is no workflow-wide idempotency key, checkpoint or recovery mechanism. LLM parsing retries up to three times without durable resume. Debug confirmation is a local pause, not an audited approval state.

## Inference

Patchwork is a useful coding pipeline, but failures can leave partial Git/SCM effects and rerunning may repeat them. It is materially different from a durable engine; branching and parallelism were still roadmap items at the fixed version.

## Not verified

Pytest, Semgrep, LLM calls and real Git/SCM mutations were not run. CI configuration was read, but fixed-commit CI results were not verified.

Evidence: [CLI](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/patchwork/app.py), [AutoFix](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/patchwork/patchflows/AutoFix/AutoFix.py), [PR effect boundary](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/patchwork/steps/CreatePR/CreatePR.py).
