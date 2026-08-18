# 班超 EP01 前置生产状态（公开投影）

- `document_role`: `human_readable_projection`
- `authoritative_state`: `banchao-ep01-current-status.json`
- `authoritative_state_sha256`: `6cfd654ddde8b9228b3b232f5f9daff633365f616b644faee52dfccbb5d2a373`
- `visual_research_registry`: `banchao-ep01-visual-research-registry-v1.yaml`
- `visual_research_registry_sha256`: `f1bfda9133801cc011d2ce88b8e9d6bb96d54eab0157c8df2cc027457d20acfd`
- `film_department_gate_matrix`: `workflows/story-studio/film-department-gate-matrix-v1.yaml`
- `film_department_gate_matrix_sha256`: `98c071edce1b329aca86f8bc0cad3d04bd8b68d35655ce6552150a7d4cc35290`
- `as_of_utc`: `2026-08-18T15:45:09Z`

本文件只提供人类可读投影。当前阶段、门禁和下一合法动作以 `banchao-ep01-current-status.json` 为唯一真相源。

## 当前结论

```text
narrative_baseline_complete
+ ep01_static_preproduction_validated
+ candidate_visual_assets_verified
+ p0_visual_research_closed
+ 5_p1_flags_open
+ minimum_visual_canon_HOD_review_ready_not_approved
+ single_view_storyboard_lock_keyframe_video_blocked
```

| 项目 | 状态 |
|---|---|
| EP01 剧本 / Shot List | `frozen validated / 14 shots / 105 seconds` |
| 候选参考图与四视图 | `8 + 4 / candidate_not_canonical` |
| Visual Research | `19 total / 14 closed / 5 P1 open` |
| P0 | `7/7 closed` |
| Minimum Visual Canon | `HOD review ready / not approved` |
| Single-view crops | `blocked` |
| Storyboard | `rough previs waits for Canon approval; full lock blocked by 5 P1` |
| Animatic / Keyframe / Video | `not started / blocked` |

## 工业电影部门门禁已引入

后续每一步不再只生成 Prompt，而是要求对应部门产物与签核：

- 编剧/导演：`Director Treatment`、Scene/Beat、Blocking、Coverage；
- 美术/置景/道具：`Production Design Bible`、Set Plan、Property List；
- 摄影/灯光：virtual lens、camera test、Lighting Bible、motivated light；
- 服装/妆发：Costume Plot、camera/light test、continuity book；
- 动作/VFX：Action Previs（需要时）、VFX Breakdown、Turnover；
- 场记/剪辑：continuity log、Storyboard、Animatic、Dailies、Picture Lock；
- 声音/调色/后期：Spotting、Foley/ADR、Show Look、Conform、Master QC。

## P0 结果

- `brush_form`：以汉代约 23 cm 出土毛笔建立通用形制范围；不证明班超本人用同型笔。
- 其余 6 项以明确改编边界关闭：复合布景、共享劳动区、人物服装轮廓、书写表面、笔囊和家庭阈限均不得宣传为精确历史复原。
- 所有候选图片仍为 `candidate_not_canonical`，本步未生成任何新图片、关键帧、视频或音频。

## 当前开放的 5 个 P1

`writing_batch_format`、`official_space_architecture`、`official_desk_form`、`official_document_material`、`doorway_architecture`

## 下一合法动作

```text
Director + Historical Research + Production Designer + DoP + Lighting + Costume/HMU + Props + Continuity + VFX + Editor
→ 对 Minimum Visual Canon Brief 做 HOD Review
→ 逐项 select / revise / reject 当前 8 张参考图与 4 张蓝图
→ 不生成关键帧或视频
```
