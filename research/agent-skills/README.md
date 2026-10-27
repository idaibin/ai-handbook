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

## 历史证据导航（2026-10-27 补链）

- [历史研究批次](batches/)：保留报告原文与日期；目录可浏览，不把每份报告逐条复制到总入口。
- [仓库记录](repositories/)、[当前研究状态](state.json)、[既有分析汇总](deep-analysis-latest.json)：结构化引用仍由这些原文件拥有。
- [来源索引及采集历史](../../sources/catalog/github-agent-skills-index.md)：元数据发现与内容／运行验证分开。

本节只增加检索入口，不更新历史数量、恢复队列或执行旧 next_action。无 Markdown 入链也不等于没有结构化引用，更不是删除依据。

## Craftway 运营、文案与海报参考

2026-10-27（UTC）有界来源映射：基于本次交接的四仓固定文件核读，不重启旧批量研究。以下版本是研究观察点，不代表实时 HEAD、当前安装或行为验证；取舍是针对 Craftway 的建议，不是上游能力的通用评级。借鉴优先，非必需不新增 Skill。

| 固定来源与读取范围 | 版本 | 许可范围 | Craftway 取舍与下游归属 |
| --- | --- | --- | --- |
| coreyhaines31/marketingskills：[social](https://github.com/coreyhaines31/marketingskills/blob/17772c7a80b7b8c7a47af30f648374cd8bd8adc5/skills/social/SKILL.md)、[content-strategy](https://github.com/coreyhaines31/marketingskills/blob/17772c7a80b7b8c7a47af30f648374cd8bd8adc5/skills/content-strategy/SKILL.md) | `17772c7a80b7b8c7a47af30f648374cd8bd8adc5` | [MIT](https://github.com/coreyhaines31/marketingskills/blob/17772c7a80b7b8c7a47af30f648374cd8bd8adc5/LICENSE) | **candidate：流程择取。** 借定位上下文、选题与写作分离、编辑日历和反馈；归原项目运营入口。不整体导入 SaaS/SEO 优先级、发帖频率、互动或私信流程，不安装整包。 |
| JimLiu/baoyu-skills：[baoyu-xhs-images](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/skills/baoyu-xhs-images/SKILL.md) | `1567581c26ec29f4216c6e6835415bf30343b0e3` | [MIT](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/LICENSE) | **candidate：交接借鉴。** 借准确文案、style/layout 分离、逐图 prompt 与版本留痕；实际生成和图文验收仍归已有图像/设计能力及产物 owner。不照搬多图、并行参数、配置落盘或 provider/CLI fallback，不运行上游脚本。 |
| anthropics/skills：[canvas-design](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/canvas-design/SKILL.md) | `dbd4588f9e1033efb41dad4bef2f7947c8993d44` | [该 Skill 的 Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/canvas-design/LICENSE.txt)；字体/素材另核，不外推整仓许可 | **reference-only。** 借视觉方向、留白和精修思路；不作为默认内容卡流程。艺术自由及少文字偏好不能覆盖获批文案、移动端可读性和图文一致性，不替代已有设计 owner。 |
| blader/humanizer：[SKILL.md](https://github.com/blader/humanizer/blob/8c307f367c91bd974002f10f2be2965d642c13df/SKILL.md) | `8c307f367c91bd974002f10f2be2965d642c13df` | [MIT](https://github.com/blader/humanizer/blob/8c307f367c91bd974002f10f2be2965d642c13df/LICENSE) | **不新增或替换文案 owner。** 仅留结构性模板语气诊断的研究来源；默认标点/输出偏好不覆盖用户约定，通用写作继续归 `human-writing`。 |

交接记录的目标 `SKILL.md` 最后修改日（UTC）分别为 social 2026-10-14、content-strategy 2026-10-15、baoyu-xhs-images 2026-06-13、canvas-design 2025-12-01、humanizer 2026-09-28；仓库其他文件的更新不能冒充这些 Skill 的更新。

已有 [human-writing 固定入口](https://github.com/idaibin/skills/blob/42a244da8e2031bb1b6eac73d6d6e9d855d56610/skills/human-writing/SKILL.md)、[内容模式](https://github.com/idaibin/skills/blob/42a244da8e2031bb1b6eac73d6d6e9d855d56610/skills/human-writing/references/content-modes.md)与[风格诊断](https://github.com/idaibin/skills/blob/42a244da8e2031bb1b6eac73d6d6e9d855d56610/skills/human-writing/references/style-diagnostics.md)覆盖源事实边界、用户编辑范围、多候选语义区分和无收益不改。本次没有证明新的通用规则缺口，故不修改该 runtime，也不在 Handbook 复制实现。

证据仅到固定文本与许可声明：[social evals](https://github.com/coreyhaines31/marketingskills/blob/17772c7a80b7b8c7a47af30f648374cd8bd8adc5/skills/social/evals/evals.json)、[baoyu testing 策略](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/docs/testing.md)与 [humanizer 包校验器](https://github.com/blader/humanizer/blob/8c307f367c91bd974002f10f2be2965d642c13df/scripts/validate-package.py)的存在，不证明中文文案、海报效果、增长或效率已实测。本轮未安装、生成样图或运行这些候选；运行/服务成本未知，不填零。

后续只由原 owner 在已授权项目入口判断是否确有选题去重或图文交接缺口；已有等效能力则 no-change。定位、内容队列与运营策略留在项目层，文案留在 `idaibin/skills`，图像留在现有能力，Handbook 仅留来源、版本、许可、取舍与验证结果索引。草稿或研究批准不等于排期、发帖、互动或新增平台授权；教育、健康内容与变现仍按[三主线规划边界](../../README.md)处理。

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
