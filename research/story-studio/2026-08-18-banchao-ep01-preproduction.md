# 班超 EP01 前置生产状态（公开索引）

首次记录：2026-08-18（Asia/Shanghai）  
最近更新：2026-08-20  
项目：`banchao` · 集数：`EP01` · 剧本：`ep01-yongshu-screenplay-v1.1`

这是一份可公开版本化的状态索引。完整任务证据、原始事件日志、候选媒体、provider-native bytes、音视频和私有 Work Order 保存在 Google Drive；GitHub 只保存公开状态、映射、哈希和验证边界。

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
| G07 执行策略 | **rebaseline_approved** | Vertical Slice First；4 条核心 lane 优先，6 条 lane 延后 |
| G07 资产执行 | in_progress_blocked | 仅 `1/10` 有完整验证执行 |
| Camera / Lighting / Motion / Continuity | subset_authorized_not_executed | 完整 CLMC v2 为 `0/9`；Vertical Slice 有界子集已授权 |
| Production ShotKeyframe / 视频 | prohibited | G07 尚未批准 |

## G07 Rebaseline

保留 Screenplay、14 Shots、27 Panels、105 秒 Storyboard / G06 Editorial Baseline；暂停“完成全部 10 条资产后才运行技术测试”的批量顺序。

当前 Vertical Slice：

1. Ban Chao Camera / Lighting
2. Minimal Luoyang Camera-safe Set
3. Hero Brush
4. Writing Surface
5. 有界 CLMC Core Technical Still；通过后可选 5–10 秒低成本 Motion Proxy

`PROP_FAMILY_MONEY_POUCH`、班母、班固、无名抄书人、Brush Pouch 和 Official Desk Package 保留既有合同，但不再作为当前最高优先级。

## 已关闭的结构缺口

- 新增 `PROP_FAMILY_MONEY_POUCH` master lane，绑定 `EP01_SHOT_03–04`。
- 将 `SET_ABSTRACT_OFFICIAL_WORKSPACE`、`PROP_GENERIC_OFFICIAL_DOCUMENT_PACKET`、`PROP_LOW_WRITING_DESK` 显式合并到 `SET_OFFICIAL_DESK_AND_GENERIC_DOCUMENT_PACKET`。
- 将 `SET_ABSTRACT_TRANSITION` 显式记录为 `no_full_set_required` waiver。
- Canonical ID Alias Map 已覆盖当前 Screenplay、Shot List、Continuity、HOD 与 G07 中的资产标识漂移。
- G06 音频 lineage 已纠正：当前可验证的是 4 个 FLAC 派生 stem；4 个 WAV 原件未在 Drive 中找到，source-fidelity 仍未验证。

## 边界

- “资产清单完整”不等于“资产媒体完成”。
- G05 当前只表示 `VISUAL_DIRECTION_SELECTED`；没有 Production Asset Canon 批准。
- Ban Chao Variant B 仅有条件选中；Camera/Lighting Test 尚未通过。
- provider-native 精确尺寸必须保留；1920×1080 normalized review derivative 不得写成 native。
- exact image provider/model、账户数据控制状态、历史构造细节和公开/商业权利仍为 `Not verified`。
- `rights_status=internal_candidate_only`；`production_ready=false`；`publication_ready=false`。

## 公开证据入口

- [G07 Rebaseline](./2026-08-20-banchao-ep01-g07-rebaseline.md)
- [G07 Rebaseline 机器状态](./2026-08-20-banchao-ep01-g07-rebaseline.yaml)
- [Canonical ID Alias Map](./2026-08-20-banchao-ep01-canonical-id-alias-map.yaml)
- [G07 资产清单对账](./2026-08-20-banchao-ep01-g07-asset-reconciliation.md)
- [G07 机器可读映射](./2026-08-20-banchao-ep01-g07-asset-reconciliation.yaml)
- [历史候选资产证据清单](./2026-08-18-banchao-ep01-evidence-manifest.json)
- [G07 当前证据清单](./2026-08-20-banchao-ep01-g07-evidence-manifest.json)
- [工作流来源矩阵](./2026-08-18-workflow-source-matrix.md)
