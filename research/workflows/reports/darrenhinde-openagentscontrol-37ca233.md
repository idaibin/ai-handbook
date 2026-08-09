# darrenhinde/OpenAgentsControl workflow assessment

- Fixed commit: `37ca233fa5597a5abb90cba73165deafffe0344f`
- Tree/content: `git-tree:9ceb47db95cf21570f29244e5ab9c59a7610d312`
- Observed: 4,701 Stars; `main`; not forked or archived
- License: MIT
- Evidence: `source_validated` for definitions, task CLI and evaluators; runtime not validated
- Subtype/topic fit: `prompt-orchestrated-coding-workflow`; fit with partial persistent state

## Verified

The primary agent prompt defines analyze, discover context, approve, execute/delegate, validate, summarize and cleanup stages. Bash defaults to ask, sensitive operations are denied, and failure guidance says stop and request direction. A JSON task model persists task/subtask states, dependencies, acceptance criteria and deliverables. The task CLI computes next/parallel/blocked work, detects missing dependencies and cycles, marks completion and archives only fully completed tasks.

Core stages are enforced mainly by prompt and host permissions, not a compiled state machine. No claim, lease, attempt, automatic retry or idempotency contract was found. Approval rules conflict: the primary prompt calls approval absolute, while `ApprovalGateEvaluator.shouldSkipApproval` accepts phrases such as “just do it” as a bypass. The checked-in latest evaluation is from an older commit and records zero passes from one test, so it is not current success evidence.

## Inference

The reusable value is a prompt/skill protocol plus a useful task ledger. Model compliance and host configuration remain the behavioral control plane; text alone cannot prove approvals or verification are obeyed.

## Not verified

Installation, agent runs, crash/resume, multi-agent concurrency, current evaluations and CI results were not run or verified.

Evidence: [agent definition](https://github.com/darrenhinde/OpenAgentsControl/blob/37ca233fa5597a5abb90cba73165deafffe0344f/.opencode/agent/core/openagent.md), [task CLI](https://github.com/darrenhinde/OpenAgentsControl/blob/37ca233fa5597a5abb90cba73165deafffe0344f/.opencode/scripts/task-cli.ts), [approval evaluator](https://github.com/darrenhinde/OpenAgentsControl/blob/37ca233fa5597a5abb90cba73165deafffe0344f/evals/framework/src/evaluators/approval-gate-evaluator.ts).
