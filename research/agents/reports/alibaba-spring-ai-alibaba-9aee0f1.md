# alibaba/spring-ai-alibaba agent assessment

- Fixed commit: `9aee0f1a86f59fcf284628a922d68ef71a4e2c85`
- Content identity: `github:alibaba/spring-ai-alibaba@9aee0f1a86f59fcf284628a922d68ef71a4e2c85`
- Default branch: `main`
- License: `Apache-2.0`
- Evidence: `source_validated`
- Subtype/topic fit: `graph-agent-framework`; `strong_fit`
- Runtime execution: none

## Verified

- README 描述 Agent Framework 构建在 Graph runtime 之上；源码验证 ReactAgent 将 LLM node、tool node、hooks/interceptors 编译为 StateGraph，CompiledGraph 支持条件边、并行节点、子图和 checkpoint。
- ReactAgent.call/stream 进入已编译 graph；模型节点产生 tool calls 后路由至 tool node，再回到模型或 END，CompiledGraph 用 recursionLimit/maxIterations 防止无限执行。
- Builder 注入 Spring AI ChatModel 与 ToolCallback/MCP；ToolSelectionInterceptor 可用独立 selectionModel 按用户问题筛选工具，失败时回退为全部工具；另有 routing/parallel/loop agent 和 model fallback interceptor。
- Graph state 使用 key strategy 合并；CheckpointSaver 提供 Memory、filesystem、Redis、JDBC、Mongo 等实现并支持历史/time travel；Store 接口明确区分跨 session 长期记忆与短期 checkpoint。
- HumanInTheLoopHook 可按工具名配置 approvalOn，在工具执行前中断并处理 approved/edited/rejected feedback；未列入 approvalOn 的工具会自动批准。
- Graph recursion limit、model/tool call limit hooks、interrupt/resume、checkpoint 和 time travel 提供停止与恢复；模型与工具分别有 retry interceptor，模型还有 fallback interceptor。
- 单元/集成测试覆盖 ReactAgent、flow agents、HITL、limits、retry/fallback、tool selection、checkpoint savers、stores、interruptions 与 time travel；在核心 Agent Framework/Graph 模块未发现专门通用 eval harness。
- build-and-test 在 push/PR 上执行 format、checkstyle 和 make test，并有 license/secret/lint 工作流；pom 配置 Maven Central 发布插件，但固定 commit 的 GitHub workflows 中未发现自动 release/publish 工作流。

## Inference

- Graph、checkpoint、store 和 flow-agent 的组合使其更偏向 JVM 企业工作流和长运行有状态 agent，而非最小化 SDK。
- HITL 是显式 allowlist-by-tool-name；若调用方漏配 approvalOn，工具会自动通过，因此不能推断默认最小权限。

## Not verified

- README 的 production-ready、一站式平台、可观测性与评估能力未作端到端验证。
- 未运行 Maven 测试，未连接 Redis/JDBC/Mongo/MCP/A2A，也未验证并行状态合并的运行时一致性。
- 未验证 Maven Central 发布历史、CI 成功率、性能或生产规模。

## Limitations

- 只读静态检查固定 commit；未构建或运行 Java 测试。
- Admin/Studio/示例生态只做 README 层定位，评分聚焦 Agent Framework 与 Graph Core。
- 因此所有行为结论最高为 source_validated。

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 5 |
| `context_and_state` | 5 |
| `tool_and_permission_boundary` | 4 |
| `stop_and_recovery` | 5 |
| `verification` | 4 |
| `concurrency_and_cost` | 3 |
| `production_readiness` | 3 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/alibaba/spring-ai-alibaba/tree/9aee0f1a86f59fcf284628a922d68ef71a4e2c85
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/README.md
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/LICENSE
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/spring-ai-alibaba-agent-framework/src/main/java/com/alibaba/cloud/ai/graph/agent/ReactAgent.java
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/spring-ai-alibaba-agent-framework/src/main/java/com/alibaba/cloud/ai/graph/agent/hook/hip/HumanInTheLoopHook.java
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/spring-ai-alibaba-graph-core/src/main/java/com/alibaba/cloud/ai/graph/CompiledGraph.java
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/spring-ai-alibaba-graph-core/src/main/java/com/alibaba/cloud/ai/graph/store/Store.java
- https://github.com/alibaba/spring-ai-alibaba/blob/9aee0f1a86f59fcf284628a922d68ef71a4e2c85/.github/workflows/build-and-test.yml
