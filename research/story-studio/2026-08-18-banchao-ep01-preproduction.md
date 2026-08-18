# 班超 EP01 前置生产状态（公开投影）

- `document_role`: `human_readable_projection`
- `authoritative_state`: [`banchao-ep01-current-status.json`](./banchao-ep01-current-status.json)
- `authoritative_state_sha256`: `9a6884eb11017f3a56385760e142496ef503d6c9d5fb81569eda8ee67f8fa000`
- `visual_research_registry`: [`banchao-ep01-visual-research-registry-v1.yaml`](./banchao-ep01-visual-research-registry-v1.yaml)
- `visual_research_registry_sha256`: `7c4443700a8d4268190ca5b1e6e52c85b41a3d4b49a2dac26d2cb4a0f2153d38`
- `as_of_utc`: `2026-08-18T15:00:00Z`

本文件只提供人类可读投影。**当前阶段、门禁和下一合法动作以 `banchao-ep01-current-status.json` 为唯一真相源。**

## 当前结论

```text
narrative_baseline_complete
+ ep01_static_preproduction_validated
+ candidate_visual_assets_verified
+ visual_research_registry_complete
+ 7_flags_disposed
+ 12_flags_open
+ visual_canon_keyframe_video_blocked
```

| 项目 | 状态 |
|---|---|
| 全传 Story Bible / 人物轨迹 / 24 集基线 | `complete_working_baseline` |
| EP01 剧本 | `frozen_validated_input` |
| Shot List | `14 shots / 105 seconds / pass_static` |
| 候选参考图与四视图 | `8 + 4 / candidate_not_canonical` |
| Visual Research Registry | `19/19 registered / pass_static` |
| 已处置 flags | `7` |
| 仍开放 flags | `12`（P0: 7，P1: 5） |
| Visual Canon / 单视图 / Storyboard lock / Keyframe / Video | `blocked` |

## 本步已处置

| Flag | Disposition |
|---|---|
| `room_to_gate_spatial_relation` | `excluded_from_frame` |
| `clothing_and_room_shape` | `resolved_by_evidence` |
| `pouch_material` | `resolved_by_evidence` |
| `family_money_pouch_form` | `bounded_as_exploratory` |
| `door_gap_and_wind_visualization` | `bounded_as_exploratory` |
| `luoyang_gate_visibility` | `excluded_from_frame` |
| `seat_removal_visualization` | `bounded_as_exploratory` |

其中 `clothing_and_room_shape` 与 `pouch_material` 只是依赖/别名归一化，不代表其历史形制已被证明；对应镜头继续继承规范化后的开放 flags。

## 当前开放项

**P0，最小 Visual Canon 前必须关闭：**

`room_architecture`、`shared_copying_space_layout`、`early_eastern_han_clothing`、`writing_surface_material`、`brush_form`、`brush_pouch_material`、`temporary_residence_layout`

**P1，14 镜 Storyboard 锁定前必须关闭：**

`writing_batch_format`、`official_space_architecture`、`official_desk_form`、`official_document_material`、`doorway_architecture`

## 下一合法动作

```text
收集并核对 7 个 P0 flags 的一手或权威视觉证据
→ 回写 Registry 的 evidence_refs 与 disposition
→ 不生成新图片、关键帧、视频或音频
```

## 公开证据入口

- [唯一当前状态](./banchao-ep01-current-status.json)
- [Visual Research Registry](./banchao-ep01-visual-research-registry-v1.yaml)
- [EP01 公开资产证据清单](./2026-08-18-banchao-ep01-evidence-manifest.json)
- [工作流来源矩阵](./2026-08-18-workflow-source-matrix.md)

完整合同、Prompt、事件日志和 12 张候选 PNG 继续保存在私有 Drive。ChatGPT 图像精确模型、使用权利、AGY effective model，以及任何视频 provider 的质量、成本和速度仍为 `Not verified`。
