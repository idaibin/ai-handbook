# Skills / Forgeway 测试反馈与强化闭环 v1

状态：**Approved companion protocol；尚无真实反馈记录**  
基准日期：2026-08-20（Asia/Tokyo）  
主协议：[`README.md`](./README.md)

## 1. 目标

本文件定义真实测试完成后的闭环：

```text
冻结本轮 Basis
→ 执行 Trial
→ 收集反馈
→ 复现与分类
→ 决定是否优化
→ 实施最小修改
→ 增加强化测试
→ 独立重跑
→ 比较前后结果
→ 保留、回滚或继续迭代
```

闭环的目的不是看到失败后立即修改 Prompt、Skill 或 Forgeway，而是把每次优化绑定到可复查证据、明确变更和新的回归测试。

## 2. 基本约束

- 已完成的 Trial、Patch、轨迹、成本和判定结果不得覆盖或重写。
- 每次实现变化必须形成新的 Candidate 版本和 Result Series。
- 同一轮只修改一个主要实验变量；无法隔离时必须明确标记为组合变化。
- 隐藏测试结果不得直接回传给同一个 Trial 的 Agent 继续修复。
- 使用某任务反馈完成优化后，该任务只能证明回归被修复，不能再单独证明泛化能力。
- 对外或晋级结论必须包含未参与该次优化设计的新任务验证。
- 不因一次随机失败扩展架构、增加 Stage、增加 Skill 或提高预算。

## 3. 反馈分类

| 类别 | 典型现象 | 处理对象 | 必须重跑范围 |
| --- | --- | --- | --- |
| `infrastructure` | 镜像、依赖、Harbor、Patch 导出或 Verifier 故障 | `forgeway-eval` / Harness 配置 | A/B/C 全部受影响 Trial |
| `protocol_fairness` | 模型、权限、预算、Prompt 或统计口径不一致 | 实验协议与 Lock | 受影响任务的 A/B/C |
| `task_oracle` | Base 不稳定、测试 Flaky、Oracle 错误或实现耦合 | Task / Verifier | 该任务 A/B/C；必要时退役任务 |
| `skill_injection` | Skill 未注入、未读取或 provenance 缺失 | Harbor 配置 / Adapter | B/C |
| `skill_content` | Skill 规则导致遗漏、冲突、过度修改或错误验证 | `idaibin/skills` | 至少 A/B 配对；C 同时使用该 Skill 时也重跑 |
| `forgeway_orchestration` | Stage 误判、任务分解发散、Gate/Recovery 无效 | `idaibin/forgeway` | 至少 B/C 配对 |
| `instrumentation` | Token、成本、Stage 或轨迹不完整 | Adapter / 采集层 | 所有受影响组；不完整成本结果不得用于 ROI |
| `model_variance` | 相同配置下结果不稳定但无确定性缺陷 | Repeat / 任务难度分析 | 增加 Repeat 或新任务，不立即改产品 |
| `no_actionable_issue` | 失败属于能力边界，暂无重复模式或证据不足 | 无修改 | 保留反馈，继续采样 |

不得把 `infrastructure` 或 `task_oracle` 故障计为 Skills/Forgeway 能力失败，也不得把 Skills/Forgeway 失败归因给模型而缺少轨迹证据。

## 4. 反馈进入优化的门禁

反馈只有满足以下任一条件，才允许进入修改：

1. 同一根因在至少两个独立任务中出现；
2. 同一根因在一个任务的至少两个 Repeat 中复现；
3. 单次即可确定的严重协议、隔离、篡改或成本漏计缺陷；
4. 单次即可稳定复现的编译、测试或运行时阻断。

每条反馈必须有：

```text
固定 Task / Trial / Group / Repeat 身份
相关 Patch、Verifier 结果与轨迹引用
预期行为与实际行为
可复现步骤
反馈类别
影响范围
```

只有描述、猜测或模型自报原因，不能进入优化。

## 5. 优化决策

允许的决策只有：

```text
fix-infrastructure
fix-protocol
fix-task-oracle
optimize-skill
optimize-forgeway
strengthen-tests-only
collect-more-evidence
retire-task
no-change
rollback
```

决策规则：

- `A/B/C` 均出现同类失败，优先检查任务、环境、模型和共同 Harness，不先修改 Skills 或 Forgeway。
- B 相对 A 出现稳定退化，且轨迹显示 Skill 参与，才进入 `optimize-skill`。
- C 相对 B 出现稳定退化，且轨迹能定位到 Stage、Gate、Retry 或 Recovery，才进入 `optimize-forgeway`。
- C 比 B 成功但只依赖更多未计入成本的调用，先修复统计，不记为 Forgeway 增益。
- 结果波动但没有稳定根因时，选择 `collect-more-evidence`，不得通过增加规则掩盖随机性。

## 6. 强化测试要求

每次被接受的代码或规则优化都必须新增或强化测试。测试至少满足：

```text
修改前固定版本：失败
修改后候选版本：通过
连续执行 3 次：结果一致
不依赖目标 Issue 的具体答案或 Reference Patch 结构
```

按缺陷归属选择测试层：

| 缺陷归属 | 强化测试 |
| --- | --- |
| Harness / Adapter | 配置一致性、隔离、Artifact、Patch 重放和成本完整性测试 |
| Task / Oracle | Base/Reference 双向预验证、Flaky 检查和实现无关行为测试 |
| Skill | Skill 包合同、触发输入、反例 Fixture 和真实仓库回归任务 |
| Forgeway | Stage Contract、Gate Projection、Recovery、状态恢复和端到端场景测试 |
| 统计与报告 | 固定 Trial Fixture、配对聚合、Invalid/InfraError 排除和成本守恒测试 |

不得为了让候选实现通过而弱化 Oracle、跳过失败路径或把实现细节写进隐藏测试。

## 7. 重跑与泛化验证

### 回归重跑

优化后首先重跑触发反馈的任务，确认缺陷已被消除。该结果只称为：

```text
regression-fixed
```

不能直接称为能力提升。

### 配对重跑

随后按修改范围重跑：

- Skill 变化：同一 Basis 下至少重跑 A/B；C 消费该 Skill 时同时重跑 C。
- Forgeway 变化：同一 Basis 下至少重跑 B/C。
- 环境、任务、模型、预算或 Oracle 变化：A/B/C 全部重跑。

所有配对组必须在同一时间窗口、相同基础设施和相同 Lock 下执行。

### 新任务确认

使用旧任务完成优化后，必须再运行未参与该修改设计的新任务。只有同时满足以下条件，才能称为正向信号：

```text
旧失败任务回归通过
新任务未出现同类退化
配对组的 Resolved / 成本变化方向一致
```

Phase 1 的 Pilot 结果若已用于优化，只作为 Development Evidence；后续应从未使用任务或 SWE-bench-Live 新鲜任务中取得 Confirmation Evidence。

## 8. 版本与结果管理

每轮记录以下不可变身份：

```text
iteration_id
protocol_commit
harness_commit
model_snapshot
skills_commit
skills_digest
forgeway_commit
adapter_commit
dataset_manifest_digest
task_oracle_digest
budget_profile_digest
```

变更后的结果必须写入新的 Result Series，例如：

```text
iteration-0001 / candidate-v1
iteration-0002 / skill-v2
iteration-0003 / forgeway-v2
```

旧结果只能标记为：

```text
current
superseded
invalidated-by-protocol-defect
retired-task
```

不得删除失败结果，也不得把修改后的重跑覆盖到旧 Trial ID。

## 9. 单条反馈记录合同

真实执行后，每条被采纳或拒绝的反馈使用以下最小结构：

```yaml
feedback_id: FB-0001
iteration_id: iteration-0001
status: observed | reproduced | accepted | rejected | verified | rolled-back
category: infrastructure | protocol_fairness | task_oracle | skill_injection | skill_content | forgeway_orchestration | instrumentation | model_variance | no_actionable_issue
basis:
  task_id: ""
  groups: []
  trial_ids: []
observation: ""
expected_behavior: ""
evidence_refs: []
reproduction:
  repeats: 0
  tasks: 0
root_cause_status: verified | supported-inference | not-verified
decision: ""
change_refs: []
strengthened_test_refs: []
rerun_manifest: ""
before_result: ""
after_result: ""
confirmation_result: ""
verdict: keep | revise | rollback | collect-more-evidence
residual_risk: ""
```

`root_cause_status` 未达到 `verified` 或 `supported-inference` 时，不得宣称已经完成根因修复。

## 10. 阶段闭环

### Phase 0

只闭环基础设施问题：

```text
Smoke → 反馈 → 修 Harness/Adapter/隔离 → 强化基础设施测试 → 重跑 Smoke
```

Phase 0 不根据三个 Smoke Task 优化 Skills 内容或 Forgeway 产品能力。

### Phase 1

闭环真实能力问题：

```text
Pilot → 配对反馈 → 最小 Skill/Forgeway 修改
→ 新增回归测试 → 配对重跑 → 新任务确认
```

若优化导致新任务退化或成本明显恶化，回滚或继续采样，不以旧任务通过作为晋级依据。

### Phase 2 及以后

只有 Phase 1 已显示稳定信号，才进行组件消融、自动 Skill 路由、Product-mode 和正式 Holdout。Holdout 一旦揭示结果，不得继续用于调优；后续版本必须使用新的密封任务集。

## 11. 存储位置

```text
本文件
  = 反馈闭环与治理规则

ai-handbook/experiments/skills-forgeway-paired-evaluation-v1/feedback/
  = 后续迭代摘要、反馈记录和决策索引

forgeway-eval
  = 可执行 Manifest、Adapter、测试与聚合代码

idaibin/skills / idaibin/forgeway
  = 被验证后的实际产品修改与回归测试

Google Drive
  = 大型原始 Trial、完整轨迹和敏感运行证据；GitHub 保存摘要、哈希与索引
```

在首次真实 Trial 之前不创建空反馈记录。Phase 0 完成后，以 `iteration-0001` 开始记录。

## 12. 当前状态

```text
Feedback loop: Defined
Real feedback records: None
Optimization evidence: None
Strengthened tests from benchmark feedback: None
Next input: Phase 0 Smoke results
```

当前不得根据方案推演继续优化 Skills 或 Forgeway。下一次修改必须由真实 Trial、独立 Verifier 和可复现反馈触发。
