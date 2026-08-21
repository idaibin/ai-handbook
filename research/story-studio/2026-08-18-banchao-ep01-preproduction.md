# 班超 EP01 前置生产状态（公开索引）

首次记录：2026-08-18（Asia/Shanghai）  
最近更新：2026-08-22（Asia/Tokyo）  
项目：`banchao` · 集数：`EP01` · 剧本：`ep01-yongshu-screenplay-v1.1`

这是一份可公开版本化的状态索引。完整任务证据、原始事件日志、候选媒体、execution-native bytes、音视频和私有 Work Order 保存在 Google Drive；GitHub 只保存公开状态、映射、Drive ID、哈希和验证边界。

## 系列级架构绑定

EP01 现作为《班超：定远》24 集系列短剧的生产闭环 Pilot，已绑定项目级“设计先行、证据驱动”架构：

```text
设计闭环：Evidence → Architecture → Review → Freeze
执行闭环：Work Order → Execute → Validate → Gate → Next Unit
```

- 架构 ID：`BANCHAO_SERIES_PRODUCTION_ARCHITECTURE_V1`
- 六篇章 / 24 集处理稿已通过静态结构核对：`6/6`、`24/24`
- 24 集处理稿 Drive file ID：`1wlDngVD09q7sbL4IPtAKMiwaV-a9HP88`
- 处理稿 SHA-256：`e6ea119124678d1de69a53b3e9bb65abe6a982a69a73583c2155977e44550a05`
- 关系路径图 Drive SVG：`1Fp8aqDtqtZIBg4DnPQoWjpmKP8GPRnVJ`
- 关系路径图 1920×1080 PNG：`1b-EvPlg1-M_1UYD1IHrAzQUmKD7TWsHi`
- 静态验证 Drive file ID：`1QHR2bhAzMtPS-KezDJvXbC9ZPDB7RmUx`

该绑定不改变 EP01 的 Screenplay、Shot、Storyboard、时长、格式、Gate 或当前执行单元；系列设计完成也不表示 EP01 或 24 集媒体生产完成。

## 当前进度

| 阶段 | 状态 | 说明 |
|---|---|---|
| 全传故事背景 / Bible / 24 集工作基线 | completed | 史实、推断、改编和虚构边界分层记录 |
| EP01 剧本 | validated | v1.1，SHA-256 `a2ba6bb8cbd094ea65c3cdcdb0e341929f479fb9cbcfe0b2cbdc4c36bad02f0e` |
| Shot List / Storyboard | locked_for_preproduction | 14 Shots、27 Panels、105 seconds |
| G06 Timed Animatic | approved_with_conditions | 1920×1080、24 fps、105.0 seconds；最终配音/声音未批准 |
| 候选参考图 | archived_candidate | 8 张，全部 `candidate_not_canonical` |
| 角色四视图蓝图 | archived_candidate | 4 张，均非历史肖像或 Production Canon |
| LookDev 审查对 | archived_candidate | 8 组 provider-native / 1920×1080 review 文件存在 |
| G07 资产清单 | reconciled | HOD `13/13` accounted；10 个 master lanes + 1 no-full-set waiver |
| G07 执行策略 | **rebaseline_approved** | Vertical Slice First；非视频工作由助手直接执行 |
| G07 资产执行 | in_progress | `2/10` 有完整验证执行；Unit 02 已完成，Unit 03 active |
| Camera / Lighting / Motion / Continuity | subset_authorized_not_executed | 完整 CLMC v2 为 `0/9`；Unit 01 仍 blocked 且未豁免 |
| Production ShotKeyframe / 视频 | prohibited | G07 尚未批准 |

## 当前 Vertical Slice

1. Ban Chao Camera / Lighting — `blocked_not_waived`
2. Minimal Luoyang Camera-safe Set — `completed_internal_candidate_only`
3. Hero Brush — `active`
4. Writing Surface — `queued`
5. 有界 CLMC Core Technical Still；通过后才评估 5–10 秒 Motion Proxy

`PROP_FAMILY_MONEY_POUCH`、班母、班固、无名抄书人、Brush Pouch 和 Official Desk Package 保留既有合同，但暂不作为当前最高优先级。

## 非视频执行机制

除实际视频生成外，Research、文档、代码、图像/资产、验证、证据打包和 Drive/GitHub 同步均由助手完成。非视频任务不再要求用户下载 Work Order、转交外部 provider 或新建专用会话。

技术型资产可以采用确定性 renderer，但必须保存源码、execution-native bytes、格式/尺寸、SHA-256、receipt、执行记录、Dailies 和可复现的 byte-identical rerender。该机制不改变 Canon、G07 和 production-ready 的 Gate。

## Unit 02 已验证结果

`LOC_LUOYANG_COPYING_COMPOSITE_SET__TAKE_02B`：

- 1920×1080 RGB PNG；
- SHA-256 `95875a2243294872f6defd0d31bd4be51edeacb6a3ccd0de40eba85ec10d13ff`；
- A/B/C、动作线、4 个机位、单侧光、简化建筑和主书案通过；
- renderer 源码、receipt、return evidence、GenerationAttempt、Dailies 和回传包已保存并回读；
- 状态仅为 `internal_candidate_only`。

## 边界

- “资产清单完整”不等于“资产媒体完成”。
- G05 当前只表示 `VISUAL_DIRECTION_SELECTED`；没有 Production Asset Canon 批准。
- Ban Chao Variant B 的 Camera/Lighting Test 尚未通过。
- execution-native 精确尺寸必须保留；normalized review derivative 不得写成 native。
- 公开/商业权利与 WAV source lineage 仍为 `Not verified`。
- `rights_status=internal_candidate_only`；`production_ready=false`；`publication_ready=false`。

## 公开证据入口

- [系列短剧生产架构](./2026-08-21-banchao-series-production-architecture.md)
- [系列生产机器合同](./2026-08-21-banchao-series-production-architecture.yaml)
- [系列关系路径确定性 Renderer](./2026-08-21-render-banchao-series-production-path.py)
- [系列架构静态验证](./2026-08-21-banchao-series-production-architecture-validation.json)
- [G07 Rebaseline](./2026-08-20-banchao-ep01-g07-rebaseline.md)
- [G07 Rebaseline 机器状态](./2026-08-20-banchao-ep01-g07-rebaseline.yaml)
- [Assistant-Owned Non-Video Execution Policy](./2026-08-21-assistant-owned-non-video-execution-policy.md)
- [Canonical ID Alias Map](./2026-08-20-banchao-ep01-canonical-id-alias-map.yaml)
- [G07 资产清单对账](./2026-08-20-banchao-ep01-g07-asset-reconciliation.md)
- [G07 机器可读映射](./2026-08-20-banchao-ep01-g07-asset-reconciliation.yaml)
- [历史候选资产证据清单](./2026-08-18-banchao-ep01-evidence-manifest.json)
- [G07 当前证据清单](./2026-08-20-banchao-ep01-g07-evidence-manifest.json)
- [工作流来源矩阵](./2026-08-18-workflow-source-matrix.md)
