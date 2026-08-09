# openai/openai-agents-python agent assessment

- Fixed commit: `e3d7c1727bf43761afbb7954651b7f908a973a3b`
- Content identity: `github:openai/openai-agents-python@e3d7c1727bf43761afbb7954651b7f908a973a3b`
- Default branch: `main`
- License: `MIT`
- Evidence: `source_validated`
- Subtype/topic fit: `agent-orchestration-sdk`; `strong_fit`
- Runtime execution: none

## Verified

- README 将项目描述为轻量级多智能体 SDK；源码验证 Runner/AgentRunner 将模型调用、handoff、工具执行、final output 和 interruption 分离为明确的 run-loop/turn-resolution 模块。
- 公开入口 Runner.run/run_sync/run_streamed 接收 Agent、输入或 RunState；循环在 final output、handoff、tool calls、interruption 间推进，并用 max_turns 限制模型轮次。
- Agent/RunConfig 可指定模型和 provider；MultiProvider/OpenAIProvider 负责按模型名解析，tool planning/execution 支持函数工具、MCP、shell、computer、apply_patch 及 handoff。
- Session 接口和会话持久化模块管理历史；RunState 可序列化中断点、当前 agent、输入/生成项、usage、approval state 并用于恢复，另有 SQLite/Redis/SQLAlchemy/MongoDB/Dapr 等 session 实现。
- FunctionTool.needs_approval、MCP approval request、RunContext approve/reject、输入/输出/tool guardrails 形成调用前审批和内容检查路径；未审批时返回 interruption 而非执行工具。
- max_turns/guardrail tripwire 提供停止边界；RunState 和 session rewind/save 支持审批中断后恢复；模型请求存在 retry 模块，错误处理器可把部分错误转成终局结果。
- 测试覆盖 runner、streaming、max turns、RunState、HITL、approvals、tool guardrails、retry、sessions 和 tracing；仓库提供示例级 eval 脚本，但未发现与 LiveKit JudgeGroup 同级的通用内置 eval harness。
- CI 在 push/PR 上运行格式、类型、Linux/Windows 单元测试和 MCP 兼容测试；release PR、合并后打 tag、GitHub Release 触发 PyPI trusted publishing 的链路均有工作流。

## Inference

- 模块边界、恢复状态和审批测试的组合表明其更适合作为通用 agent orchestration SDK，而非只面向单一聊天界面。
- 权限控制是开发者显式配置的应用层机制，不等同于默认最小权限或操作系统级隔离；sandbox agent 是另一个可选层。

## Not verified

- README 所称支持 100+ LLM 未逐 provider 或运行验证。
- 未验证真实 API、MCP server、sandbox backend、数据库 session 或跨进程恢复行为。
- 未核对线上 PyPI 发布结果、GitHub Actions 历史成功率、覆盖率数值或生产可靠性。

## Limitations

- 只读静态检查固定 commit；未安装依赖、未构建、未运行测试。
- 因此所有行为结论最高为 source_validated，而非 runtime_validated。

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 5 |
| `context_and_state` | 5 |
| `tool_and_permission_boundary` | 5 |
| `stop_and_recovery` | 5 |
| `verification` | 4 |
| `concurrency_and_cost` | 3 |
| `production_readiness` | 5 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/openai/openai-agents-python/tree/e3d7c1727bf43761afbb7954651b7f908a973a3b
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/README.md
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/LICENSE
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/src/agents/run.py
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/src/agents/run_internal/run_loop.py
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/src/agents/run_internal/tool_execution.py
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/src/agents/run_state.py
- https://github.com/openai/openai-agents-python/blob/e3d7c1727bf43761afbb7954651b7f908a973a3b/.github/workflows/tests.yml
