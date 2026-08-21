# 班超 EP01 G07 Rebaseline

状态：`approved_vertical_slice_first_unit02_completed_unit03_active`  
首次批准：`2026-08-20`  
最近更新：`2026-08-21`  
项目：`banchao` · 集数：`EP01`

## 决策

保留 EP01 的 Screenplay、14 Shots、27 Panels、105 秒 Storyboard / G06 Timed Animatic 作为叙事与 Editorial Baseline；停止按“先补齐全部 10 条资产 lane，再开始技术测试”的顺序执行。

G07 采用 **Vertical Slice First**：

1. `VERTICAL_SLICE_01_BAN_CHAO_CAMERA_LIGHT`
2. `VERTICAL_SLICE_02_LUOYANG_MINIMAL_SET`
3. `VERTICAL_SLICE_03_HERO_BRUSH`
4. `VERTICAL_SLICE_04_WRITING_SURFACE`
5. `VERTICAL_SLICE_05_CLMC_CORE_TECHNICAL_PROXY`

该切片先验证“班超身份 + 主场景几何 + 核心书写道具 + Camera/Lighting/Continuity”是否能形成可运行的生产闭环，再决定是否恢复其余 6 条 lane。

## 2026-08-21 执行机制更新

除实际视频生成外，Story Studio 的 Research、文档、代码、图像/资产、验证、证据打包和 Drive/GitHub 同步均由助手直接执行。旧的 external-provider-only、fresh asset chat 和 control-chat image prohibition 不再作为非视频任务的合法性前提。

执行证据统一使用 `execution-native` 语义：

- 图像模型原始输出、确定性 renderer 原始输出或来源文件直接派生输出均可作为 native；
- 必须保存原始 bytes、精确格式/尺寸、SHA-256、receipt、执行记录和 Dailies；
- Review derivative、resize 或重编码文件不得标记为 native；
- 几何/技术资产采用 deterministic renderer 时，必须同时保存源码和可重复的 byte-identical rerender 证据。

完整政策见 [`2026-08-21-assistant-owned-non-video-execution-policy.md`](./2026-08-21-assistant-owned-non-video-execution-policy.md)。

## 当前执行结果

`VERTICAL_SLICE_02_LUOYANG_MINIMAL_SET` 的 `LOC_LUOYANG_COPYING_COMPOSITE_SET__TAKE_02B` 已完成：

- execution-native PNG 为 1920×1080 RGB；
- SHA-256 为 `95875a2243294872f6defd0d31bd4be51edeacb6a3ccd0de40eba85ec10d13ff`；
- 顶视与三分之四视图、A/B/C 分区、单一 180° 动作线、4 个稳定机位、单侧光方向、简化建筑和一张主书案均通过；
- renderer 源码、receipt、return evidence、GenerationAttempt、Dailies 和完整回传包已保存并完成 Drive 回读；
- 该结果仅为 `internal_candidate_only`，未提升为 Production Canon 或 G07 approved。

当前合法入口为 `VERTICAL_SLICE_03_HERO_BRUSH`。`VERTICAL_SLICE_01_BAN_CHAO_CAMERA_LIGHT` 仍阻塞且未豁免。

## 保留与延后

### 保留

- EP01 Screenplay v1.1 与史实 / 改编 / 虚构边界。
- 14 Shots、27 Panels、105 秒、16:9、24 fps 的 G06 Editorial Baseline。
- 低饱和冷灰土褐、克制表演、单侧 motivated soft light 的规则级 Visual Direction。
- 既有参考图、蓝图、LookDev 与 Styleframe 作为历史候选和 negative/reference evidence。
- Ban Chao Variant B 作为 Camera/Lighting 的 identity reference。

### 延后

- `CHAR_BAN_MOTHER`
- `CHAR_BAN_GU`
- `CHAR_UNNAMED_SCRIBE`
- `PROP_BRUSH_POUCH`
- `PROP_FAMILY_MONEY_POUCH`
- `SET_OFFICIAL_DESK_AND_GENERIC_DOCUMENT_PACKET`

延后不表示删除；它们保留既有 Work Order 和证据，但在 Vertical Slice 复核前不作为当前执行入口。

## 规范边界

- 历史 Gate `G05_DESIGN_LOOK_APPROVAL` 保留不改写；当前操作语义使用 `G05_VISUAL_DIRECTION_SELECTED`，只批准规则级 ShowLook，不批准 Production Asset Canon。
- 新合同使用 Canonical IDs；旧 Screenplay、Shot List 与 Continuity 中的兼容名称通过 Alias Map 解析。
- 只有一个 Active Capsule 具有当前执行权；Task 文档中的历史 Capsule 仅作为日志。
- `13/13 requirements`、`10/10 lanes`、`14/14 Shots referenced` 只表示静态覆盖，不表示交付完成。
- Unit 02 通过不自动证明 Ban Chao identity、完整 CLMC 或剩余资产 lane。

## 当前边界

```text
verified G07 asset executions: 2/10
active execution unit: VERTICAL_SLICE_03_HERO_BRUSH
Unit 01 Camera/Lighting: blocked_not_waived
actual CLMC execution: 0/9
Production ShotKeyframes: 0
video shots: 0
production_ready: false
publication_ready: false
rights_status: internal_candidate_only
```
