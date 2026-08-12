# Task Routing

本文件将任务类型路由到最小必要的 policy、workflow、instruction 和 prompt。所有重要任务先读取 [`operating-principles.md`](operating-principles.md)，再按下表加载；不得一次加载全部目录。

| 任务类型 | 必须加载 | Prompt |
| --- | --- | --- |
| 来源发现、筛选、一般研究 | `source-management.md`、`state-model.yaml` | 无通用固定 Prompt；按明确研究问题执行 |
| GitHub 仓库索引 | `source-management.md`、`../repository-research/README.md` | `../repository-research/prompts/index.md` |
| GitHub 仓库深度分析 | `source-management.md`、`../repository-research/README.md` | `../repository-research/prompts/deep-analysis.md` |
| Skill 设计或验证 | `skill-validation.md`、`state-model.yaml` | 使用目标 Skill 的 `SKILL.md` 与 eval，不另造重复 Prompt |
| 代码、配置或项目规范变更 | `delivery-recovery.md`、目标仓库最近的 `AGENTS.md` 和项目规范 | 使用目标仓库已有 task/spec；没有时先定义任务合同 |
| 知识内容和公开发布 | `knowledge-publication.md`、`ownership.yaml` | 使用目标内容 workflow 的 Prompt |
| 文件、资产、Drive 或 Library | `storage-policy.md` | 无 |
| 工作流、状态或仓库职责变更 | `workflow.yaml`、`state-model.yaml`、`ownership.yaml`、`evals/`、`CHANGELOG.md` | 无；必须新增或更新回归案例 |

路由规则：

1. 当前用户明确要求优先；
2. 记录加载的 `ai-handbook` 完整 commit SHA；
3. Prompt 只负责具体任务执行，不能覆盖 policy、证据门禁或授权边界；
4. 没有匹配 Prompt 时，不得借用不相关 Prompt；先按 policy 和任务合同执行；
5. 无法读取必须文件时，停止修改和外部写入并报告阻碍。
