# 班超 EP01 前置生产状态（公开索引）

日期：2026-08-18（Asia/Shanghai）
项目：`banchao`  · 集数：`EP01`  · 剧本：`ep01-yongshu-screenplay-v1.1`

这是一份可公开版本化的状态索引。完整任务证据、原始事件日志、提示词和候选 PNG 保存在私有 Drive 证据目录；本文件不包含本机绝对路径、私有 provider file ID 或模型权利推断。

## 当前进度

| 阶段 | 状态 | 说明 |
|---|---|---|
| 全传故事背景 / Bible / 24 集工作基线 | completed | 史实与改编边界分层记录 |
| EP01 剧本 | validated | v1.1，SHA-256 `a2ba6bb8cbd094ea65c3cdcdb0e341929f479fb9cbcfe0b2cbdc4c36bad02f0e` |
| Shot List | validated | 14 个镜头，105 秒 |
| Asset Manifest / Continuity Contract | validated_static | 仅前置资产合同 |
| ChatGPT AI Design 候选参考图 | candidate_verified | 8 张，全部 `candidate_not_canonical` |
| 角色四视图蓝图 | candidate_verified | 4 张 1536×1024 PNG |
| AGY 蓝图图像复核 | pass_candidate_only | 形态、四视图、身份一致性通过；不等于历史/权利/生产通过 |
| 单视图裁切 / 关键帧 / 视频 / 音频 | blocked / not_started | 视觉考据门禁尚未关闭 |

## 事实与生产边界

- 角色蓝图和参考图是探索性候选，不是历史肖像，不是 canonical 资产。
- 合同保留 21 处 `[待核实]` 标记；资产计划保留 19 项未关闭视觉考据 flags。
- ChatGPT 图像模型精确版本、使用权利，以及 AGY effective model 均为 `Not verified`。
- ComfyUI/Wan 仍只是后续 provider/fallback 参考；本索引没有把未运行模型写成视频输出。
- 在考据 flags 关闭前，不生成单视图裁切、关键帧或视频。

## 公开证据入口

- [工作流来源矩阵](./2026-08-18-workflow-source-matrix.md)
- [EP01 公开资产证据清单](./2026-08-18-banchao-ep01-evidence-manifest.json)

完整合同、AGY 原始结构化结果、事件日志和媒体哈希在私有 Drive 证据目录中维护；Drive 的共享状态保持私有。
