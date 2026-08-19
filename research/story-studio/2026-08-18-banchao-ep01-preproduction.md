# 班超 EP01 当前生产状态（公开投影）

- `authoritative_state`: `banchao-ep01-current-status.json`
- `authoritative_state_sha256`: `6db499373b1088333951a540ddc6250d1490039b4b39571f23d94809ce980e09`
- `active_format`: `16:9 / 1920x1080`
- `current_stage`: `STAGE_05_VISDEV_LOOKDEV_APPROVAL`
- `current_gate`: `G05_DESIGN_LOOK_APPROVAL`
- `gate_decision`: `revise`
- `as_of_utc`: `2026-08-19T03:06:00Z`

## Story Studio 基础权威已统一

以下文件使用稳定路径直接修改，不创建并行 `v2`、`v3`：

- `workflows/story-studio/film-department-gate-matrix-v1.yaml`：10 个 Macro Stages、11 个 Quality Gates 与跨阶段工作线；
- `workflows/story-studio/core-glossary.yaml`：Canonical Terms、术语来源分类、生命周期、证据分类和模糊词禁用规则；
- `workflows/story-studio/stage-artifact-matrix.yaml`：每一步必备 Artifact、Owner、Reviewer、Approver、Pass Condition；
- `workflows/story-studio/role-approval-matrix.yaml`：部门职责、不可自批规则和 Gate 审批关系；
- `workflows/story-studio/conditional-modules.yaml`：历史考据、动作、Crowds、Lip Sync、VFX、Localization、Accessibility 等按触发条件启用。

## 当前术语约束

合同中不再使用未限定的：

```text
脚本
场景
分镜
关键图片
关键帧
审核通过
最终版
```

必须分别使用 `Screenplay`、`Scene/Location/Set`、`ShotList/Storyboard/Animatic`、`ReferenceAsset/Styleframe/ShotKeyframe`、`ShotKeyframe/AnimationKeyframe`，并以 `gate_id + approve/revise/reject/blocked/defer` 记录审查。

## 《班超》当前状态

```text
NarrativeCanon: working_baseline
VisualCanon: not_approved
ProductionCanon: not_established
production_ready: false
publication_ready: false
```

Round-3 LookDev 暂停。下一合法动作是把现有《班超》Story Bible、人物、世界、EP01 剧本、ShotList、Continuity、LookDev 和 Review 逐项映射到新的 Canonical Terms 与 Stage Artifact Matrix，补齐缺失 Artifact 后再恢复生成。
