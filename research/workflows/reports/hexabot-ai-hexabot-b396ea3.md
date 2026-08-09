# hexabot-ai/Hexabot workflow assessment

- Fixed commit: `b396ea3de8ac19b78a1ab7829598d27d4bf3c2d5`
- Tree/content: `git-tree:8bdbf11cfba3b8de559c0e4d9732d15d7598254f`
- Observed: 1,148 Stars; `main`; not forked or archived
- License: FCL-1.0-ALv2 with competing-use restrictions, changing to Apache-2.0 per version after two years
- Evidence: `runtime_validated` for core runner tests only
- Subtype/topic fit: `durable-workflow-engine`; strong fit

## Verified

`Workflow.fromYaml/fromDefinition` validates and compiles a typed workflow. Sequential, conditional, loop and parallel control flow are implemented. Runs move through idle, running, suspended, finished and failed; step state includes pending, completed, cancelled and skipped. Start/resume returns snapshots containing execution and suspension metadata. Rebuild detects replay drift and throws a nondeterminism error. Parallel suspension is explicitly rejected.

Actions wrap execution in configurable timeout and exponential backoff with cap/jitter. Human interaction is a host-defined suspension, not a built-in approval policy. Deterministic replay exposes recorded results, but action authors must explicitly avoid replaying pre-suspension effects; no universal side-effect idempotency key was found.

Core runtime command executed: Jest completed 16 suites and 144 tests successfully, covering runner control flow, suspension/rebuild, retry and timeout. Node 24.14.0 was below the package's declared 24.17.0 minimum, so the result is scoped to this environment.

## Inference

Durable suspension metadata and nondeterministic-replay detection are especially reusable. Exactly-once external effects still belong to action and host design.

## Not verified

The real host persistence layer, process-crash windows, providers, email/ticket effects, cross-version recovery and multi-process load were not exercised.

Evidence: [agentic package](https://github.com/hexabot-ai/Hexabot/tree/b396ea3de8ac19b78a1ab7829598d27d4bf3c2d5/packages/agentic), [runner](https://github.com/hexabot-ai/Hexabot/blob/b396ea3de8ac19b78a1ab7829598d27d4bf3c2d5/packages/agentic/src/workflow-runner.ts), [runtime control](https://github.com/hexabot-ai/Hexabot/blob/b396ea3de8ac19b78a1ab7829598d27d4bf3c2d5/packages/agentic/src/runner-runtime-control.ts).
