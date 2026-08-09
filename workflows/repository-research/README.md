# Repository Research Workflow

本目录是 GitHub 主题仓库“索引 → 深度分析 → 批次复盘”的唯一流程权威。定时任务只负责选择主题并读取这里的最新版规则，不复制长提示词。

## 目标

给定一个主题与方向，建立可持续、可审计的研究流水线：

```text
主题配置 → 可复现索引 → 规范化与去重 → 候选队列
        → 固定版本深读 → 证据分级 → 批次复盘 → 下一批改进
```

当前主题：

| Topic | Index output | Deep-analysis output | Schedule lane |
| --- | --- | --- | --- |
| `skills` | `sources/catalog/` | `research/agent-skills/` | `:00` / `:10` |
| `agents` | `sources/catalog/agents/` | `research/agents/` | `:20` / `:30` |
| `workflows` | `sources/catalog/workflows/` | `research/workflows/` | `:40` / `:50` |

## 权威文件

- [`process.md`](process.md)：状态、证据、去重、复盘和提交规则。
- [`prompts/index.md`](prompts/index.md)：索引任务入口。
- [`prompts/deep-analysis.md`](prompts/deep-analysis.md)：深度分析任务入口。
- [`topics/`](topics/)：主题边界、检索词、证据要求和输出目录。
- [`topic-template.toml`](topic-template.toml)：新增主题模板。

## 新主题启动合同

用户只需给出：

```text
主题：<slug>
方向：<一句话范围>
```

执行者必须：

1. 复制 `topic-template.toml`，补齐纳入/排除边界与至少一组可复现查询；
2. 人工执行一次索引 prompt 和一次深度分析 prompt；
3. 验证产物、去重、状态转换和复盘回写；
4. 只有两次手工试运行通过后，才创建两条定时任务；
5. 定时任务引用 `main` 上的 prompt 与 topic 文件，不嵌入流程副本。

当前六条定时任务统一在 Work 执行，以便使用云浏览器、云服务器、依赖安装和运行验证；任务仍必须保持同一 topic 合同和 GitHub 写回格式。

## Quota stop 与 Chat 恢复

只在第一方 usage 状态明确显示周剩余额度处于 `20% <= remaining_percentage < 99%` 时执行研究。以下任一情况触发停止：

- 周剩余额度低于 `20%`：为当前周保留余量；
- 周剩余额度大于等于 `99%`：视为周额度已重置，避免未知情况下消耗新周期额度；
- 无法观测精确周剩余额度：无法证明处于允许区间，按保守规则停止。

停止时，执行者先按 [process.md](process.md) 同步本次 task-owned 产物并验证远端 commit，再暂停全部六条任务，不得伪造额度数值或阈值命中。

需要恢复时，在 Chat 中发送以下指令：

```text
恢复 Repository Research 定时任务。先读取 idaibin/ai-handbook:main 的 workflows/repository-research/README.md、process.md、prompts/index.md、prompts/deep-analysis.md 和三个 topics/*.toml；核对六条任务仍全部暂停、main 上没有未解决的 active claim、canonical state/latest pointer/ready snapshot 一致，并读取当前第一方周 usage 状态。只有精确 remaining_percentage 满足 20 <= remaining_percentage < 99 时，按 Asia/Tokyo 的 :00 Skills Index、:10 Skills Deep、:20 Agents Index、:30 Agents Deep、:40 Workflows Index、:50 Workflows Deep 恢复六条任务；remaining_percentage < 20、remaining_percentage >= 99 或额度不可观测时均保持暂停，并报告原因。恢复后回读六条任务并报告 task ID、运行位置、schedule、enabled 状态和下一次运行时间。
```

## 质量原则

- 索引结果不是深度分析结果。
- Repository identity 与 content identity 分开计数。
- `README` 声明不是行为验证。
- 批量目标是上限，不是降低证据门槛的理由。
- 复盘每批只允许引入一个可验证的方法变化，避免无限优化。
