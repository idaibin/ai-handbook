# 班超 EP01 前置生产状态（公开投影）

- `document_role`: `human_readable_projection`
- `authoritative_state`: [`banchao-ep01-current-status.json`](./banchao-ep01-current-status.json)
- `authoritative_state_sha256`: `083886366e8632b2417aaa4768f8c4e27cc55e0c8f5aec4f03c56e87fd55b4aa`
- `as_of_utc`: `2026-08-18T14:09:06Z`

本文件只提供人类可读投影。**当前阶段、门禁和下一合法动作以 `banchao-ep01-current-status.json` 为唯一真相源。** 其他旧文档中的状态字段按其生成时间视为历史快照；其内容证据和哈希仍然保留。

## 当前结论

```text
narrative_baseline_complete
+ ep01_static_preproduction_validated
+ candidate_visual_assets_verified
+ visual_research_gate_open
+ visual_canon_gate_blocked
+ keyframe_and_video_gate_blocked
```

| 阶段 | 状态 | 说明 |
|---|---|---|
| 全传 Story Bible / 人物轨迹 / 24 集工作基线 | `complete_working_baseline` | 6 篇章 × 4 集；旧 5 集仅作为第一章试剪 |
| EP01《佣书》剧本 | `frozen_validated_input` | v1.1，SHA-256 `a2ba6bb8cbd094ea65c3cdcdb0e341929f479fb9cbcfe0b2cbdc4c36bad02f0e` |
| Shot List | `pass_static` | 14 个唯一镜头，总时长 105 秒 |
| Asset Manifest / Continuity Contract | `pass_static` | 10 个连续性 anchors、13 条 edges |
| 候选参考图 | `candidate` | 8 张，非 canonical |
| 角色四视图蓝图 | `candidate` | 4 张；AGY 仅通过形态、四视图和身份一致性复核 |
| 视觉考据 | `open` | 19 项 flags 未处置 |
| Visual Canon | `blocked` | 尚未选择最小视觉权威资产 |
| 单视图、Storyboard、Animatic、关键帧、视频、音频 | `not_started / blocked` | 不得跨越当前门禁 |

## 当前唯一合法下一步

```text
建立 EP01 Visual Research Registry
→ 对 19 项 flags 逐项选择：
   resolved_by_evidence / bounded_as_exploratory /
   excluded_from_frame / deferred_out_of_pilot
```

完成后才进入：

```text
最小 Visual Canon
→ 单视图派生资产
→ 14 镜 Storyboard
→ 105 秒 Animatic
→ 3 张关键帧
→ EP01_SHOT_10 单镜视频验证
```

## 历史快照边界

- `banchao-series-bible-first-plan.md`：旧规划稿，不是当前 Bible。
- `banchao__contract__provider-and-production-route__2026-08-18__v01.md`：保留 provider-neutral 路线价值，其中 `Shot List / Continuity not_started` 已被当前状态覆盖。
- `ep01-yongshu-screenplay-v1.1.md`：剧本内容继续作为冻结输入；旧头部状态不再决定当前生命周期。
- 旧 5 集规划：仅作为第一章试剪，不再代表班超全传。

## 公开证据入口

- [唯一当前状态](./banchao-ep01-current-status.json)
- [EP01 公开资产证据清单](./2026-08-18-banchao-ep01-evidence-manifest.json)
- [工作流来源矩阵](./2026-08-18-workflow-source-matrix.md)

完整合同、Prompt、AGY 原始结果、事件日志和 12 张候选 PNG 继续保存在私有 Drive 证据目录。ChatGPT 图像精确模型、使用权利、AGY effective model，以及任何视频 provider 的质量、成本和速度仍为 `Not verified`。
