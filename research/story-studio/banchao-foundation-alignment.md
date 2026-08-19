# 《班超》项目 Artifact → Stage → Gate 映射结论

状态：`mapping_complete_with_blocking_gaps`  
时间：`2026-08-19T04:20:00Z`

## 结论

现有《班超》资料已经形成较强的故事与 EP01 静态前置生产基础，但**不能把“有内容”直接等同于“工业门禁已通过”**。本次按 Story Studio 统一术语、10 个 Stage、11 个 Gate 和职责矩阵重新映射后：

- `EpisodeTreatment` 与 `VisualResearchRegistry` 已达到当前工作范围；
- `NarrativeBible`、`Screenplay`、`ShotList`、`Continuity`、`AssetRequirementList` 均为部分满足；
- `VisualCanonDecision` 已存在，但结论是 `revise`；
- G01、G02、G03、G04 仍有正式 Artifact 缺口；
- Round-3 LookDev 继续暂停。

## 重点判断

| 对象 | Canonical Term | 判断 | 关键缺口 |
|---|---|---|---|
| 全传冻结主稿 | `NarrativeBible`，并包含 `StoryBible` / `WorldBible` / `CharacterBible` 成分 | `partially_satisfies` | 仍写 9:16；混入旧工具路由；缺生产型 World/Character 字段 |
| 全传人物轨迹 | `CharacterArc` / `Treatment` 支撑 | `supports_only` | 不是完整 `CharacterBible` |
| 24 集处理稿 | `EpisodeTreatment` | `satisfies_working_baseline` | 不是 `Screenplay`，缺结构化 Episode Registry |
| EP01 剧本 | `Screenplay` | `partially_satisfies` | 仍写 9:16；header 为 draft；缺 Scene/Beat IDs、TimingRead、ScratchDialogue |
| EP01 Shot List | `ShotList` | `partially_satisfies` | 缺 Scene/Beat、Blocking/Coverage、Lens/FOV、Handles；不是 Storyboard/Animatic |
| EP01 Continuity | Continuity support | `partially_satisfies` | 不是 Daily Continuity Log；缺 Take/Select 状态 |
| Visual Research Registry | `VisualResearchRegistry` | `satisfies` | 只证明考据处置完成，不等于 VisualCanon/rights/production-ready |
| HOD Round 2 | `VisualCanonDecision` | `gate_failed: revise` | 0 approved assets |

## 形式门禁重评

| Gate | 当前正式判断 |
|---|---|
| `G01_DEVELOPMENT_GREENLIGHT` | `blocked_or_incomplete` |
| `G02_SCRIPT_LOCK` | `blocked_or_incomplete`，但已有 working narrative/screenplay content |
| `G03_HOD_BREAKDOWN_COMPLETE` | `blocked_or_incomplete` |
| `G04_RESEARCH_RIGHTS_CONSTRAINTS_LOCK` | Historical/visual research 已完成，Rights/Provenance 未完成 |
| `G05_DESIGN_LOOK_APPROVAL` | `revise` |
| `G06+` | 未开始或被上游门禁阻塞 |

## 当前 P0 缺口

1. 24 集统一 `SeriesFormatContract`；
2. `CreativeBrief`、预算/排期/风险和 `RightsPosture`；
3. claim-level `SourceLedger`；
4. 规范化 `SeriesCreativeConstitution`、`NarrativeBible`、`WorldBible`、`CharacterBible`；
5. EP01 `SceneBeatIndex`、16:9 Screenplay metadata、TimingRead/ScratchDialogue；
6. 正式 HOD Script/Asset/Shot/Department Breakdown 与 Production Plan；
7. `RightsLedger`、`ProviderProvenancePolicy`、`AdaptationExceptionLog`；
8. DirectorTreatment、ProductionDesignBible、LookBook/Styleframes、ColorScript、ShowLook、CameraLightingTests；
9. 通过 `G05_DESIGN_LOOK_APPROVAL`。

## 下一合法动作

先完成 `STAGE_01_DEVELOPMENT_GREENLIGHT` 的稳定基础包，不扩写剧情、不生成图片：

```text
SeriesFormatContract
→ CreativeBrief / PremiseLoglineTheme
→ SourceLedger
→ BudgetScheduleRiskRegister
→ RightsPosture
```

其后按 G02 → G03 → G04 → G05 依赖顺序补齐。完整逐文件映射见 `banchao-artifact-stage-map.yaml`；完整 Required Artifact 覆盖见 `banchao-stage-gap-register.yaml`。
