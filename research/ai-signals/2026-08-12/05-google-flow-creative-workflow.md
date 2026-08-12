# 05 — Google Flow 的统一创作工作流

## 信号与来源

- 发现帖：[Flow by Google X 帖](https://x.com/FlowbyGoogle/status/2026704701069074603)，发现快照约 41.32 万浏览。
- 一手资料：[2026 年 2 月 Flow 更新](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/)、[2026 年 5 月 Flow 更新](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates/)。

## 核心提炼

Flow 把图像、视频、素材管理和精确编辑放在连续工作区中，并把 Whisk/ImageFX 能力迁入同一产品。真正值得迁移的不是某个生成模型，而是资产生命周期：源素材、提示、变体、选择、局部编辑、审核和导出保持在同一上下文，用户可以沿谱系继续创作。

Google 宣称用户已创建超过 15 亿图像和视频。这是厂商披露的使用量，不是质量、生产率或商业成功的独立证据。统一 UI 也不会自动解决版权、来源追踪或错误传播。

## 声明—证据账本

| 声明 | 判定 | 证据与边界 |
|---|---|---|
| Flow 已统一图像与视频生成、编辑和素材管理 | 支持 | Google 两篇官方更新明确描述功能整合 |
| 统一工作流让资产上下文连续 | 支持其产品机制 | 功能设计支持连续编辑；效率提升未做独立对照测试 |
| 超过 15 亿次生成证明输出质量高 | 不支持 | 数量是厂商采用指标，不包含质量定义或独立审计 |
| agent 可以替代创作者控制 | 反驳其强版本 | 2026 年 5 月官方更新反而强调 creator 保持控制 |

## 对当前仓库的决策

Forgeway 已有统一索引和独立 owner，不应为了“连续体验”合并语义权威。可借鉴的是 UI 层用一个 Delivery Graph 展示素材及变体，同时仍让每阶段按 Artifact 契约交接；当前不改核心契约。

最直接的候选在 `knowledge-distillation`：为多模态来源增加稳定身份与派生关系，例如 `source -> excerpt/frame -> generated variant -> review -> selected/exported artifact`，并保存生成参数、模型、时间和证据等级。现有 Knowledge IR 已区分 evidence 和 maturity，可扩展而不把仓库变成图像/视频生成工具。

`feeds-hub` 只应保存这次发布为一条 event，并显式交接为 handbook candidate；不得把长篇研究复制进 feed，也不得自动晋升为 Skill。

## 验证预算

当前是契约候选，官方文档与仓库静态检查足够。若实施，第一阶段只需 schema 正反例、谱系遍历和迁移测试；第二阶段若增加可视化工作区，再验证上传、生成变体、选择、撤销和导出的浏览器路径。无需先完整构建 Forgeway 或 feeds-hub。

**状态：Complete with gaps**。
