# 班超 EP01 当前状态（公开投影）

- `authoritative_state`: `banchao-ep01-current-status.json`
- `authoritative_state_sha256`: `ad5d52d69e298ab758d284e80d00ff7483c2cdfa94163057a03318328360cfdb`
- `active_format`: `16:9 / 1920x1080`
- `rights_posture`: `internal_candidate_only`
- `round3_lookdev`: `paused`
- `as_of_utc`: `2026-08-19T05:30:00Z`

## 9 个 P0 缺口处理结果

```text
前 8 项：稳定 Artifact 已创建，等待对应 Gate 审批
第 9 项 VisualCanon：仍为 G05 revise
新图片 / Storyboard / ShotKeyframe / Video / Final Audio：0
```

已建立：

- Development Greenlight Package
- SourceLedger
- Narrative Authority Package
- 活动 EP01 Screenplay（只修正 16:9 元数据和术语）
- EP01 Script Lock Package（3 Scene / 8 Beat / 模拟 TimingRead）
- EP01 HOD Breakdown Package（14 Shot 部门映射）
- Rights & Provenance Package
- LookDev Input Package
- Round-3 LookDev Work Order

## 当前 Gate

| Gate | 状态 |
|---|---|
| `G01_DEVELOPMENT_GREENLIGHT` | `review_ready_approval_pending` |
| `G02_SCRIPT_LOCK` | `review_ready_approval_pending` |
| `G03_HOD_BREAKDOWN_COMPLETE` | `review_ready_approval_pending` |
| `G04_RESEARCH_RIGHTS_CONSTRAINTS_LOCK` | `review_ready_for_internal_candidate_only_approval` |
| `G05_DESIGN_LOOK_APPROVAL` | `revise`；Styleframe / CameraLightingTests / VisualCanon 尚未通过 |

下一合法动作：按顺序对 G01→G04 作 `approve/revise/blocked` 决定；通过后只授权 Round-3 Phase A 的 3 个 Styleframe/Camera/Lighting Test，不直接批量生成 9 个资产。
