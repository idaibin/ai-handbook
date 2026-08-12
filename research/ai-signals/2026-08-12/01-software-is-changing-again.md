# 01 — Software Is Changing (Again)

## 信号与来源

- 发现帖：[Mckay Wrigley 转发](https://x.com/mckaywrigley/status/1935513106823922133)，发现快照约 46.97 万浏览。
- 原始内容：[Andrej Karpathy 演讲视频](https://www.youtube.com/watch?v=LCEmiRjPEtQ)。
- 辅助定位：[视频转写](https://videotobe.com/play/youtube/LCEmiRjPEtQ)。转写仅用于定位，不高于原视频。

## 核心提炼

Karpathy 把软件分成三种可编程层：Software 1.0 是显式代码，2.0 是神经网络权重，3.0 是用自然语言配置大模型。真正可迁移的观点并非“prompt 会替代代码”，而是软件必须把不确定的模型能力包进确定性的接口、监督和回退中。

“autonomy slider”尤其重要：同一能力应允许从建议、准备执行到经授权执行逐级提升自治，而不是把是否使用 agent 做成二元开关。演讲同时强调 agent 需要可读文档、结构化命令/API 和可审计结果。

## 声明—证据账本

| 声明 | 判定 | 证据与边界 |
|---|---|---|
| 自然语言已成为新的可编程界面 | 支持为设计框架 | 演讲直接提出 1.0/2.0/3.0；这是概念模型，不是行业占比统计 |
| LLM 应被当作会犯错的计算组件 | 支持 | 演讲反复要求监督、校验和不同自治等级 |
| 所有软件都应改写为 prompt/agent | 不支持 | 原演讲没有给出这种普遍结论；确定性代码仍承担边界和验证 |
| agent-friendly 基础设施能降低操作摩擦 | 有条件支持 | Markdown、API、结构化工具有清楚机制，但具体收益需在任务上测量 |

## 对当前仓库的决策

Forgeway 已把这个方向落实得比帖子更具体：每阶段唯一语义 owner、最小 Artifact 包、结构校验、证据与状态分离、外部 effect 需授权。结论是**确认现有方向，不新增“通用 agent 层”**。

若以后需要暴露自治等级，应绑定 stage/effect，而非绑定模型：`suggest`、`prepare`、`execute-after-approval` 可以成为 UX 表达，但现有授权门已经覆盖核心安全语义，当前无需改契约。

`skills` 继续保持明确 description、机器可读输出和宿主可调用入口即可。把“Software 3.0”单独做成 Skill 没有稳定任务边界，也没有必要。

## 未验证与验证预算

未做演讲主张的行业规模统计，也未测试不同自治 UI 的完成率。当前只是架构解释与筛选，静态核验足够；只有真正改 Forgeway 交互时才需要任务级可用性测试和浏览器验证。

**状态：Complete with gaps**。
