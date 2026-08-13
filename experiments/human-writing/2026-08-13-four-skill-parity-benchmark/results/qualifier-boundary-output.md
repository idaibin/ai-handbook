## Q1

- 该恢复机制主要处理短时网络中断。
- 该恢复机制通常不承担跨日任务的状态保存；必要时，调用方仍需自行持久化记录。

## Q2

核心告警会实时发送给值班人员。

## Q3

The tool usually processes local drafts first and retains at least one review record; only administrators may publish.

## Run metadata

- Isolation constraint: Read only `/tmp/hw-round2d/human-writing/SKILL.md`, the task-relevant references explicitly routed by that file, and the assignment message; do not read workspace experiments, outputs, reports, expected results, git history, or any other skill.
- Output constraints: Produce finished artifacts for Q1–Q3; add or remove no facts in Q1 and make every list item a complete conclusion; compress Q2 into one sentence containing only the core behavior an on-call operator must know; adapt Q3 into concise English for an operations handbook without changing facts; write this file with `apply_patch` under headings `## Q1` through `## Q3` and `## Run metadata`; return completion only.
- Files read:
  - `/tmp/hw-round2d/human-writing/SKILL.md`
  - `/tmp/hw-round2d/human-writing/references/fact-integrity.md`
  - `/tmp/hw-round2d/human-writing/references/reasoning-and-explanation.md`
  - `/tmp/hw-round2d/human-writing/references/quality-rubric.md`
