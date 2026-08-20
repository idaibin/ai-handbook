# 班超 EP01 G07 Rebaseline

状态：`approved_vertical_slice_first_asset_outputs_pending`  
日期：`2026-08-20`  
项目：`banchao` · 集数：`EP01`

## 决策

保留 EP01 的 Screenplay、14 Shots、27 Panels、105 秒 Storyboard / G06 Timed Animatic 作为叙事与 Editorial Baseline；停止按“先补齐全部 10 条资产 lane，再开始技术测试”的顺序执行。

G07 改为 **Vertical Slice First**：

1. `VERTICAL_SLICE_01_BAN_CHAO_CAMERA_LIGHT`
2. `VERTICAL_SLICE_02_LUOYANG_MINIMAL_SET`
3. `VERTICAL_SLICE_03_HERO_BRUSH`
4. `VERTICAL_SLICE_04_WRITING_SURFACE`
5. `VERTICAL_SLICE_05_CLMC_CORE_TECHNICAL_PROXY`

该切片先验证“班超身份 + 主场景几何 + 核心书写道具 + Camera/Lighting/Continuity”是否能形成可运行的生产闭环，再决定是否恢复其余 6 条 lane。

## 为什么调整

- G07 master lanes 已静态补齐为 `10/10`，但具备 provider-native bytes、`GenerationAttempt` 与 Dailies 的验证执行仍只有 `1/10`。
- Unified CLMC v2 覆盖 9 个测试单元、14/14 Shots 与 10/10 lanes，但实际执行仍为 `0/9`。
- `PROP_FAMILY_MONEY_POUCH` 是低辨识度连续性道具，不应因为最后补入清单就自动成为最高优先级。
- 旧流程在 Control Chat 无法执行图像生成时持续增加 Work Order、Handoff 与状态 revision，资产数量没有同步增长。

## 保留与延后

### 保留

- EP01 Screenplay v1.1 与史实 / 改编 / 虚构边界。
- 14 Shots、27 Panels、105 秒、16:9、24 fps 的 G06 Editorial Baseline。
- 低饱和冷灰土褐、克制表演、单侧 motivated soft light 的规则级 Visual Direction。
- 既有参考图、蓝图、LookDev 与 Styleframe 作为历史候选和 negative/reference evidence。
- Ban Chao Variant B 作为下一轮 Camera/Lighting 的 identity reference。

### 延后

- `CHAR_BAN_MOTHER`
- `CHAR_BAN_GU`
- `CHAR_UNNAMED_SCRIBE`
- `PROP_BRUSH_POUCH`
- `PROP_FAMILY_MONEY_POUCH`
- `SET_OFFICIAL_DESK_AND_GENERIC_DOCUMENT_PACKET`

延后不表示删除；它们保留既有 Work Order 和证据，但在 Vertical Slice 复核前不作为当前执行入口。

## 规范修正

- 历史 Gate `G05_DESIGN_LOOK_APPROVAL` 保留不改写；当前操作语义使用 `G05_VISUAL_DIRECTION_SELECTED`，明确它只批准规则级 ShowLook，不批准 Production Asset Canon。
- 新合同必须使用 Canonical IDs；旧 Screenplay、Shot List 与 Continuity 中的兼容名称通过单独 Alias Map 解析，不复制新资产。
- 只有一个 Active Capsule 具有当前执行权；Task 文档中的历史 Capsule 仅作为日志。
- provider-native 输出必须保存原始 bytes、精确尺寸和 SHA-256；1920×1080 normalized review derivative 不能标记为 native。
- `13/13 requirements`、`10/10 lanes`、`14/14 Shots referenced` 只表示静态覆盖，不表示交付完成。

## 当前边界

```text
verified G07 asset executions: 1/10
actual CLMC execution: 0/9
Production ShotKeyframes: 0
video shots: 0
production_ready: false
publication_ready: false
rights_status: internal_candidate_only
```

Vertical Slice 只形成 CLMC_T01 / T02 的有界前置证据，不会自动通过完整多角色、Brush Pouch 或全时间线测试。
