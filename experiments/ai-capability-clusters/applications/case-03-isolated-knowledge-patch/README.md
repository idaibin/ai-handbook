# Case 03 — Isolated knowledge patch

输入固定为 [knowledge-distillation 的 agent-runtime IR](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/agent-runtime-orchestration/knowledge.yaml)。`KNOWLEDGE_DISTILLATION_ROOT` 可指定该仓库本地 clone；未设置时按 ai-handbook 的 sibling `knowledge-distillation` 推导。唯一可变目标固定为相对 case 的 `workspace/input/knowledge.yaml`，oracle 同时冻结 `workspace_relative=workspace` 和 `target_relative=workspace/input/knowledge.yaml`。

脚本在任何 `mkdir`、`rmtree`、copy 或 write 前 fail-closed 验证 CASE/workspace/target 的 canonical containment：workspace 与 target 不得为 symlink，target 必须在 `CASE/workspace/input`，并且 oracle relative target 必须等于 `TARGET.relative_to(CASE)`。absolute、sibling、`..` 或 symlink 目标均应非零退出，且不得删除或写入。

原始 IR 和 validator 绝不写入。treatment 只在隔离副本末尾追加一条 `APPLICATION-MARK`，再以 scoped diff、validator、forbidden path hash 与 target/workspace match 评分。`oracle.json` 为只读冻结输入；篡改会非零退出且 hash 不变。浏览器、外部凭据、MCP session 和生产副作用均为 Not verified。

从本 case 目录运行：`KNOWLEDGE_DISTILLATION_ROOT=/path/to/knowledge-distillation python3 run_experiment.py`。若未设置环境变量，要求 sibling repository 与源 IR、validator 存在；缺失时脚本清晰失败。
