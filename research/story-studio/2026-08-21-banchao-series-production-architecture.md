# Story Studio —《班超：定远》系列短剧生产架构 v1.0

状态：`approved_for_persistence_and_execution_binding`  
架构 ID：`BANCHAO_SERIES_PRODUCTION_ARCHITECTURE_V1`  
UTC 基线时间：`2026-08-21T16:03:39Z`  
本地日期：`2026-08-22`（Asia/Tokyo）  
GitHub 读取基线：`idaibin/ai-handbook@aa7aa9b3fe61206c235af2f21184b118f60b42c7`

## 1. 结论

采用双闭环：

```text
设计闭环：Evidence → Architecture → Review → Freeze
执行闭环：Work Order → Execute → Validate → Gate → Next Unit
```

系列生产遵循以下约束：

- 先锁定全季因果与单集合同，再进入单集媒体生产；
- EP01 是生产闭环验证样片，不代表 24 集已完成；
- 24 集共用角色、地点、道具、视觉和声音连续性，但每集保持独立 Gate 与证据链；
- 失败先分类为实现、合同、依赖、架构、权利/Provider 或基线变化，再决定重试还是改架构；
- 关系图、地图、时间线和报告是只读投影，不得改写 Story Bible、剧本或生产状态；
- 除实际视频生成外，Research、文档、代码、图像资产、验证、证据与同步由助手执行。

本架构不替代现有 EP01 G06/G07 合同，而是把当前单集试验接入完整系列路径。

## 2. 权威与范围

| 事实类型 | 权威来源 | 本架构处理方式 |
|---|---|---|
| 系列历史与剧情 | Drive 中的 Source Ledger、Story Bible、24 集处理稿 | 只读取和版本化引用 |
| 版本化架构与公开投影 | GitHub `ai-handbook/main` | 以路径、commit、SHA 固定 |
| 当前 Task 状态 | Drive `Current Status` | 唯一动态状态源 |
| 当前执行入口 | Drive `Active Capsule` | 同一时刻只有一个入口 |
| Work Order、原始媒体和证据 | Drive | 保留 file ID、原始 bytes、SHA-256 |
| 关系图与报告 | GitHub + Drive | 只读衍生资产 |

### 系列叙事来源

- 文件：`banchao__script__24-episode-treatment__2026-08-18__v01.md`
- Drive file ID：`1wlDngVD09q7sbL4IPtAKMiwaV-a9HP88`
- SHA-256：`e6ea119124678d1de69a53b3e9bb65abe6a982a69a73583c2155977e44550a05`
- 状态：`working_series_treatment`，不是逐集对白或媒体生成稿。

### 当前 EP01 边界

```text
EP01《佣书》
1920×1080 / 16:9 / 24 fps
105 秒 / 14 Shots / 27 Panels
G06 approved_with_conditions
G07 2/10 verified executions
VERTICAL_SLICE_03_HERO_BRUSH active
Production ShotKeyframes = 0
Video Shots = 0
```

架构同步不得修改以上锁定内容，也不得把系列设计完成解释为 EP01 或全季生产完成。

## 3. 系列故事骨架

当前 24 集处理稿已覆盖六篇章：

| 篇章 | 集数 | 名称 | 主要因果任务 |
|---|---|---|---|
| 1 | EP01–EP04 | 投笔出塞 | 从佣书、从军到鄯善破局，建立主动选择与越权责任 |
| 2 | EP05–EP08 | 西域立足 | 于阗、疏勒立足并面对陈睦遇害后的断援 |
| 3 | EP09–EP12 | 孤城五年 | 放弃归途、稳定疏勒、组织联盟并上疏请兵 |
| 4 | EP13–EP16 | 联盟与背叛 | 援军、毁谤、莎车与康居/月氏外交 |
| 5 | EP17–EP20 | 破龟兹、立都护 | 忠再叛、莎车决战、白霸与西域都护治理 |
| 6 | EP21–EP24 | 焉耆、封侯与归乡 | 焉耆终局、定远侯、交接与返洛阳病逝 |

每集进入 Screenplay 前，必须具备以下机器可读合同：

```text
episode_id
chapter_id
duration_seconds（建议 90–120；短剪另建版本）
aspect_ratio
location_ids
character_ids
prop_ids
historical_fact_refs
adaptation_notes
visual_continuity_anchors
audio_cue_placeholders
```

## 4. 最终系列关系路径

```text
历史证据与来源
→ Series Bible / World Bible / Character Bible
→ 六篇章 × 二十四集因果矩阵
→ 单集合同
→ Screenplay / Shot List / Storyboard / Timed Animatic
→ HOD Breakdown / Canonical Asset Reconciliation
→ Vertical Slice / Asset & CLMC Validation
→ G07 或对应资产生产准备 Gate
→ Shot Contracts / Production ShotKeyframes
→ Video GenerationAttempt / Dailies / Selects
→ Picture Lock
→ Dialogue / Foley / SFX / Score / Mix / VFX / Colour / Subtitles
→ Episode QC / Episode Master
→ 篇章连续性复核
→ 24/24 全季连续性与权利复核
→ Series Release Package
```

关系路径图（Drive）：

- SVG：`1Fp8aqDtqtZIBg4DnPQoWjpmKP8GPRnVJ`
- 1920×1080 PNG：`1b-EvPlg1-M_1UYD1IHrAzQUmKD7TWsHi`
- 图像 SHA-256：`33836bce5e33c0d09386e69be1b4b1f4bb0455e07e8e676ed46baafea650652d`

确定性渲染源码：[`2026-08-21-render-banchao-series-production-path.py`](./2026-08-21-render-banchao-series-production-path.py)

## 5. 单集生产合同

每集必须依次通过：

| Phase | 必要产物 | 通过条件 | 失败回退 |
|---|---|---|---|
| `E00_EPISODE_CONTRACT` | 单集目标、阻力、策略、转折、高潮、钩子、历史标记 | 与全季因果及前后集无冲突 | 回到 24 集矩阵 |
| `E01_SCREENPLAY` | Screenplay、对白与场景 | 史实/推断/改编/虚构边界明确 | 修订 Screenplay |
| `E02_EDITORIAL_BASELINE` | Shot List、Storyboard、Timed Animatic | 时长、节奏、对白和镜头顺序可执行 | ChangeRecord 后重锁 |
| `E03_PRODUCTION_DESIGN` | HOD、资产 ID、Alias、Continuity、Work Orders | 无孤立需求或重复资产计数 | 修订对账与合同 |
| `E04_ASSET_TECH_VALIDATION` | Vertical Slice、资产执行、CLMC | 原生证据与 Dailies 通过 | 新 Attempt 或修订 Work Order |
| `E05_SHOT_PRODUCTION` | Shot Contract、ShotKeyframe、视频 Attempt | 身份、构图、动作、镜头和连续性通过 | 返回相关资产或 Shot Contract |
| `E06_PICTURE_LOCK` | Selects、Edit、Picture Lock | 叙事完整、无缺 Shot、时长锁定 | 返回 Shot Production |
| `E07_POST_AND_QC` | 声音、VFX、Colour、字幕、QC | 技术、内容、权利和可访问性通过 | 返回对应 Post lane |
| `E08_EPISODE_MASTER` | Master、SRT、Manifest、Evidence Package | 上传回读与哈希一致 | 修复交付包 |

低层级通过不自动代表高层级完成。

## 6. 共享资产与跨集连续性

系列使用一个共享 `Asset & Continuity Graph`，但不建立与当前任务无关的通用 Artifact Registry。

共享节点包括：

- 班超不同人生阶段的 Character State；
- 班固、班昭、家人、三十六吏士和西域人物；
- 洛阳、伊吾、鄯善、于阗、疏勒、龟兹、莎车、焉耆等 Location State；
- 书写系统、武器、服饰、质子/文书、外交与军旅道具；
- ShowLook、Camera、Lighting、Motion、Sound 和字幕规则；
- 前后集伤痕、年龄、服装、地理、季节、政治关系和道具状态。

共享资产只在实际 Episode Contract 引用时进入生产；不得为理论完整性预制全部资产。

## 7. 分批执行策略

采用“试点 → 篇章批次 → 全季收口”，不同时铺开 24 集媒体生产。

### Batch 0：架构与来源冻结

- 本架构、关系图、24 集处理稿身份和权威引用完成同步；
- EP01 当前状态保持不变；
- 输出可追踪的 GitHub commit 与 Drive readback。

### Batch 1：EP01 生产闭环

```text
Unit 03 Hero Brush
→ Unit 04 Writing Surface
→ Unit 05 CLMC Core Proxy
→ 解决 Unit 01 Camera/Lighting
→ Vertical Slice Review
→ Deferred Lane 决策
→ G07 Gate
→ Production ShotKeyframes
→ Video / Post / EP01 Master
```

目标不是继续增加规范，而是获得第一条完整、可复现的 Episode Master 证据链。

### Batch 2：固化可复用模板

从 EP01 实际结果提取：

- Episode Contract 模板；
- Shot Contract；
- Asset/Continuity 引用规则；
- Video Attempt 与 Dailies 合同；
- Post/QC 与 Delivery Manifest；
- 已知失败边界。

只有 EP01 真实通过后才升级为稳定模板。

### Batch 3–8：六篇章生产

每篇章四集按以下顺序推进：

```text
篇章因果复核
→ 4 集 Episode Contract
→ 共享资产影响分析
→ 每集独立 Editorial Baseline
→ 必要资产/Vertical Slice
→ 单集 Shot Production 与 Post
→ 篇章连续性 Review
```

已完成 EP01 的篇章一在 Batch 3 中只补 EP02–EP04，并复核 EP01 与后三集因果、角色和视觉连续性。

### Batch 9：全季交付

必须满足：

- `24/24` Episode Contract 完整；
- `24/24` Episode Master 与 Manifest 可回读；
- 六篇章因果、时间、角色、地点和政治关系连续；
- 无 orphan Event、Shot、Asset、Source 或 Audio Cue；
- 史实、推断、改编和虚构标记可追溯；
- 权利状态满足发布目标；
- Series Master、章节包、字幕、海报/预告等衍生产物不反向污染正片事实源。

## 8. 统一证据链

```text
Requirement
→ Work Order
→ Execution-native Output
→ Receipt
→ Mechanical Validation
→ GenerationAttempt
→ Dailies
→ Evidence Manifest
→ Drive Upload + Readback
→ Current Status
→ GitHub Projection
→ Next Unit Authorization
```

`Dailies Pass ≠ Canon ≠ Gate Approved ≠ Production Ready ≠ Publication Ready`。

## 9. 失败分类

| 分类 | 处理 |
|---|---|
| `FAIL_IMPLEMENTATION` | 保持架构，创建新 Attempt |
| `FAIL_CONTRACT` | 修订当前 Work Order 并重新验证 |
| `FAIL_DEPENDENCY` | 暂停受影响单元，修订依赖关系 |
| `FAIL_ARCHITECTURE` | 冻结执行，建立 Architecture ChangeRecord 与影响分析 |
| `FAIL_RIGHTS_OR_PROVIDER` | 隔离 Attempt，更新 Provider/Rights Contract |
| `BASELINE_CHANGE` | 回到上游 Gate，使受影响下游产物失效 |

单次生成质量差通常不是架构失败。只有依赖、权威、状态或 Gate 无法真实表达生产时才修改顶层架构。

## 10. 当前执行入口

架构生效后，EP01 仍从以下单元继续：

```text
VERTICAL_SLICE_03_HERO_BRUSH
PROP_HERO_BRUSH__TAKE_02A
```

成功只授权 `VERTICAL_SLICE_04_WRITING_SURFACE`，不得直接推进 G07、Production Shotkeyframe 或视频。


## 11. 持久化身份

| 产物 | Google Drive file ID | SHA-256 |
|---|---|---|
| 架构 Markdown | `1_3t-Ff5yzNkxWwyLtM3yZruvfitw-Vew` | GitHub commit + Drive readback 见同步回执 |
| 机器合同 YAML | `1lz2elTRETKl15ep1kEjdHHDljblyqoGO` | `627df01e18c0c50c2a86434bb8733824cb372a8e937a3dc4a9c9f8a994b8048d` |
| Renderer | `1zO8VrgGhWsdsinWBCx3MRnX7O02ErrJT` | `4fcab550988770e577f0b9b75cac0450357aa146710e8de866a45b6bb1951301` |
| SVG | `1Fp8aqDtqtZIBg4DnPQoWjpmKP8GPRnVJ` | `eedbb5663155d61bcd3bd054d7692071cc2927cae301b45d1e228ea1962573a0` |
| PNG 1920×1080 | `1b-EvPlg1-M_1UYD1IHrAzQUmKD7TWsHi` | `33836bce5e33c0d09386e69be1b4b1f4bb0455e07e8e676ed46baafea650652d` |
| 静态验证 | `1QHR2bhAzMtPS-KezDJvXbC9ZPDB7RmUx` | `3d5ea290edad3e7a444a27e4997fc02b826694d5118661d3083c66f79311194b` |

Drive 资产均位于 `banchao` 项目根目录；原始 bytes 与哈希以 Drive 回读为准。
