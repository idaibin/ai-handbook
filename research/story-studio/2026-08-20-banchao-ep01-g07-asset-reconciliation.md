# 班超 EP01 G07 资产清单对账

状态：`inventory_reconciled_asset_outputs_pending`  
更新时间：`2026-08-20T11:19:11Z`  
项目：`banchao` · 集数：`EP01`

## 结论

HOD 的 `13` 项资产需求已经建立确定性映射：`9` 项直接进入 G07 master lane，`3` 项合并到一个 SetPropPackage，`1` 项按既有镜头规则记录为不需要完整 Set 的 waiver。G07 master work item 从 `9` 增至 `10`，补入 `PROP_FAMILY_MONEY_POUCH`。

这只关闭**资产清单与路由缺口**，不表示资产图像、技术测试或 G07 Gate 已完成。当前具备完整 `GenerationAttempt + Dailies` 的 G07 资产执行仍只有 `1/10`。

## HOD → G07 映射

| HOD requirement | G07 resolution |
|---|---|
| `CHAR_BAN_CHAO_STATE_01_LUOYANG_SCRIBE` | direct lane |
| `CHAR_BAN_MOTHER` | direct lane |
| `CHAR_BAN_GU` | direct lane |
| `CHAR_UNNAMED_SCRIBE` | direct lane |
| `LOC_LUOYANG_COPYING_COMPOSITE_SET` | direct lane |
| `PROP_HERO_BRUSH` | direct lane |
| `PROP_WRITING_SURFACE` | direct lane |
| `PROP_BRUSH_POUCH` | direct lane |
| `PROP_FAMILY_MONEY_POUCH` | **new direct lane**, required by `EP01_SHOT_03–04` |
| `SET_ABSTRACT_OFFICIAL_WORKSPACE` | consolidated into `SET_OFFICIAL_DESK_AND_GENERIC_DOCUMENT_PACKET` |
| `PROP_GENERIC_OFFICIAL_DOCUMENT_PACKET` | consolidated into `SET_OFFICIAL_DESK_AND_GENERIC_DOCUMENT_PACKET` |
| `PROP_LOW_WRITING_DESK` | consolidated into `SET_OFFICIAL_DESK_AND_GENERIC_DOCUMENT_PACKET` |
| `SET_ABSTRACT_TRANSITION` | `no_full_set_required` waiver; technical continuity remains tested |

## 静态验证

- HOD requirements：`13/13` accounted
- G07 master lanes：`10/10` present and unique
- Unified CLMC tests：`9` test units
- Locked Shots：`14/14` referenced
- Master lanes referenced by tests：`10/10`
- Test execution：`not_started`
- Production ShotKeyframe / video：仍禁止

## 音频来源纠正

G06 Review Package 中可验证的是四个 FLAC 派生 stem。此前清单中的四个 WAV 文件在当前 Drive 审查中未找到，因此 WAV 名称与哈希仅保留为历史声明，不再声称原件已保存或 source-fidelity 已验证。

可访问 FLAC：

- `DX_SCRATCH.flac` — `2250e8f12c61bb6c278b59ed323d54204159158d81c61fad90687dad614921eb`
- `FX_PRELAY.flac` — `c222fcbf5db3a46eb600cc5b083efaa9d3e15ebcbb291427a0c89cae43cefca7`
- `MIX_SCRATCH.flac` — `cb81381f5f6576351c31a91b214801a1e4c25b69a665ce4eefd2e9ce16357a86`
- `MUSIC_TEMP.flac` — `468371c433d5dc35c9ffacf02db269f5db8cd2f68705b8056833947f56302021`

## 权威边界

- GitHub：保存公开、可版本化的映射、状态、哈希和验证结果。
- Google Drive：保存完整私有合同、候选媒体、原生输出、音视频与执行证据。
- `PROP_FAMILY_MONEY_POUCH__TAKE_01A` 尚未生成，不得写成已有图片资产。
- `rights_status` 仍为 `internal_candidate_only`；`production_ready=false`，`publication_ready=false`。

## 公开入口

- [EP01 当前前置生产状态](./2026-08-18-banchao-ep01-preproduction.md)
- [历史候选资产证据清单](./2026-08-18-banchao-ep01-evidence-manifest.json)
- [G07 当前证据清单](./2026-08-20-banchao-ep01-g07-evidence-manifest.json)
- [机器可读资产对账](./2026-08-20-banchao-ep01-g07-asset-reconciliation.yaml)
