# 02 — OpenAI Prism Paper Review

## 信号与来源

- 发现帖：[OpenAI X 帖](https://x.com/OpenAI/status/2041581000120267067)，发现快照约 20.98 万浏览。
- 一手资料：[OpenAI Prism](https://openai.com/prism/)、[Prism 故障排查与帮助](https://help.openai.com/en/articles/20001050-troubleshooting-and-getting-help-in-prism)。
- 反向材料：[Ars Technica 对科研 AI slop 与错误引用风险的报道](https://arstechnica.com/ai/2026/01/new-openai-tool-renews-fears-that-ai-slop-will-overwhelm-scientific-research/)。

## 核心提炼

Prism 的价值不在“AI 能审论文”，而在把 AI 放进领域原生工作台：模型读取项目上下文，意见定位到文稿，用户逐项 Keep/Undo，再通过 LaTeX 重编译检查结果。这里形成了一个可靠的人机交互闭环：上下文绑定、可定位建议、显式采纳、可逆操作、确定性检查。

Paper Review 是审阅器，不是事实证明器。语言更专业、结构更顺滑，不能证明引用真实、推理成立或实验可复现。

## 声明—证据账本

| 声明 | 判定 | 证据与边界 |
|---|---|---|
| Prism 是带项目上下文的 AI-first LaTeX 工作台 | 支持 | 官方产品页描述写作、引用、文献和协作能力 |
| Paper Review 可给出行内编辑并由用户接受或撤销 | 支持 | 官方帮助文档说明 Keep/Undo 与重新编译 |
| AI review 能保证论文事实与引用正确 | 反驳 | 官方没有这种保证；反向报道列出幻觉引用与规模化低质稿风险 |
| 产品当前长期路线稳定 | 未解决 | 官方页面仍可访问，但公开报道对团队/产品后续归属存在冲突；不影响模式研究 |

## 对当前仓库的决策

Forgeway 可借鉴的是 Review Artifact 的交互：问题必须定位到具体 artifact/字段，建议与证据分开，接受或拒绝产生可追溯事件，并保留撤销路径。Forgeway 已隔离外部 review 且不把其直接写成状态，因此**不需要架构改动**。

`skills/repo-review` 已承担独立第二视角。不要新增泛化 `paper-review`，除非未来反复出现学术写作任务，且能定义固定输入、引用校验和评估集。

## 未验证与验证预算

未登录 Prism，也未用真实 LaTeX 项目验证 UI、编译和多人协作。若未来实现类似 review 界面，先做 Artifact/event 契约测试，再做接受、拒绝、撤销和重编译的浏览器路径；无需因此完整构建无关仓库。

**状态：Complete with gaps**。
