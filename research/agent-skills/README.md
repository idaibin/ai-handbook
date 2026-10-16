# Agent Skills Ecosystem Research

## Scope

Research catalog for GitHub repositories related to AI Skills, Agent Skills, skill specifications, and skill workflows.

## Current Status

- Stage: paused as of 2026-08-11.
- Discovery: paused.
- Sequential deep analysis: paused.
- Active claims: none.
- Repository write: enabled only for reconciliation, synthesis, experiments and explicit corrections.

The catalog and historical reports are retained. Broad scanning must not resume until
historical content-identity reconciliation, runtime-evidence inventory and adoption
mapping can measure marginal value. See the
[repository research stage closure](../stage-reviews/2026-08-11-repository-research-stage-closure.md).

## 新批准维护范围（2026-10-16）

[Skills 优化记录](skills-optimization.md)：维护当前建议、优先级、上游 Skills 与模型能力变化、精简方案及真实对照结果。仅此文档及本入口获准新增维护；旧研究继续 paused，不恢复批量扫描、顺序深研或其它项目。实现与测试仍归 `idaibin/skills`，通过链接关联；建议不代表已执行或已证实收益。

## Verified Candidates

| Repository | Category | Evidence | Notes |
| --- | --- | --- | --- |
| anthropics/skills | Official Skills Collection | GitHub repository | Skill examples, templates and reusable resources |
| openai/skills | Official Skills Collection | GitHub repository | Codex related skills collection |
| agentskills/agentskills | Specification | GitHub repository | Agent Skills format and conventions |
| NVIDIA/skills | Skills Governance | GitHub repository | Skills, evaluation and supply-chain related patterns |

## Research Rules

Each repository record should include:

- Repository identity
- Source URL
- Star count at collection time
- Purpose
- Directory structure
- Skill format
- Reusable patterns
- Evidence references
- Verification status

## Status Model

Discovery does not mean reviewed.

Statuses:

- discovered
- metadata-verified
- structure-reviewed
- pattern-extracted
- integrated

## Next Steps

1. Reconcile repository identity with unique content identity across historical reports.
2. Inventory actual runtime-validated evidence and downgrade unsupported aggregate claims.
3. Map reusable patterns to current adoption in `idaibin/skills`.
4. Distill only the permission, declaration-to-consumption, checkpoint/side-effect,
   semantic-drift and evidence-promotion patterns selected by the stage closure.
5. Run controlled and real-project experiments before promoting any new production Skill.

Do not expand candidates or resume the remaining sequential queue during this stage.
