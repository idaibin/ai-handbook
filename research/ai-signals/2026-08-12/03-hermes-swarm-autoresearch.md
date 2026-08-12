# 03 — Hermes Swarm 与 Autoresearch

## 信号与来源

- 发现帖：[glitch_ 的 Hermes swarm 实验](https://x.com/glitch_/status/2033175616485286254)，约 12 万浏览。
- 一手代码：[karpathy/autoresearch @ 228791f](https://github.com/karpathy/autoresearch/tree/228791fb499afffb54b46200aca536f79142f117)、[`program.md`](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md)。
- 组件代码：[Hermes Agent @ 036cbdf](https://github.com/hermes-agent-org/hermes/tree/036cbdfa0a3158454a0a2a7a7388cf70353326b4)、[QMD @ e428df7](https://github.com/tobi/qmd/tree/e428df76bc0274d9e93eb7ca3e95673315c42e90)。

## 原帖与可验证事实

原帖描述 Hermes 负责多个角色、QMD 提供共享知识、`program.md` 固定目标和指标、`strategy.md` 可变、`results.tsv` 追加记录，并设置两阶段批准。作者也明确说这是约两天/36 小时的 hackathon，实验 ratchet 仍需 30 次以上循环；“承担 50–75% 重活”是作者估计，不是测量结果，且当时没有公开该整套实现。

可验证的 autoresearch 原型比“蜂群”更窄：只允许改 `train.py`，不许改评估器 `prepare.py`，每次固定训练 5 分钟，以 `val_bpb` 为单一指标，记录 keep/discard/crash。README 明确说明不同硬件的结果不可直接比较。

## 声明—证据账本

| 声明 | 判定 | 证据与边界 |
|---|---|---|
| 多 agent 协作已经被证明优于单 agent | 未验证 | 原帖没有对照组、固定任务集或统计结果 |
| 有界自治循环可以持续筛选改进 | 支持其机制 | 固定修改面、固定时间、固定指标、保留/丢弃规则均在固定 commit 中可查 |
| 追加式试验日志有助于避免重复失败 | 机制支持 | `results.tsv` 记录 commit、指标、内存、状态和描述；实际收益未在本次运行 |
| QMD 可直接作为所有中文知识库的可靠记忆层 | 未验证 | 它提供本地 BM25/向量/重排和 MCP；中文分词曾有公开问题，当前版本未在本任务实测 |
| 蜂群承担了 50–75% 工作 | 不可验证 | 仅为作者估计，缺少工作量定义和测量方法 |

## 对当前仓库的决策

**拒绝把 Forgeway 改成多代理运行时。** Forgeway 有意保持一阶段一个语义 owner，并把运行、模型选择和并发留给宿主；蜂群帖没有提供足以推翻该约束的证据。

可进入候选池的是“有界实验循环”：固定目标和评估器、mutation allowlist、时间/迭代预算、非回归 oracle、追加式 Attempt/Observation、仅在提升时晋级、关键 effect 人工授权。Forgeway 的 Delivery Graph 已有可承载它的事件原语，因此应先做 evaluation/experiment mode，不新增第二套状态机。

`skills` 暂不新增 autoresearch 或 swarm Skill。只有在至少两个不同仓库复用同一输入输出契约、并有固定评估集后，才有资格晋升为 Skill。

## 验证预算

本次只判断设计可迁移性，固定 commit 静态检查足够。后续 PoC 必须实际运行：建立 baseline，至少完成一个 keep、一个 discard、一个 crash/timeout 路径，并验证评估器不可变、预算会终止、日志可回放。无需先运行 Hermes 或 QMD 全栈。

**状态：Complete with gaps**。
