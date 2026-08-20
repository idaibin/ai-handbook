# Skills / Forgeway 配对评测 v1

状态：**Approved protocol；Phase 0 尚未执行**  
基准日期：2026-08-20（Asia/Tokyo）  
定位：内部配对工程验证，不是公开排行榜或通用学术 Benchmark。

## 1. 决策

本实验只回答两个增量问题：

```text
A → B：固定执行器加入预定义 Skills 后，是否产生可复现的工程收益？
B → C：在相同 Skills 基础上加入 Forgeway 编排后，是否产生可复现的系统收益？
```

首轮不重新实现 SWE-bench 或通用 Agent Harness。容器、Trial、任务适配、Skills
注入、轨迹与 Verifier 优先复用 Harbor；真实 Issue 样本优先使用
Multi-SWE-bench，后续再用 SWE-bench-Live 复验新鲜任务。

## 2. 能验证与不能验证

本实验能够验证：

- 固定 Skills Bundle 作为整体是否改善解决率、局部性、测试行为或成本；
- Forgeway 作为完整编排系统是否改善复杂任务的收敛与恢复；
- 增益是否覆盖额外 Token、时间和工程复杂度；
- 哪些语言、任务层级和任务类型更容易获益或退化。

本实验不能直接证明：

- 每个 Skill 或 Forgeway 内部 Stage 各自贡献多少；
- 15 个 Pilot 任务的结果可推广到全部软件工程任务；
- Forgeway 优于所有其他 Agent Harness；
- 公开历史任务不存在模型训练污染。

## 3. 开源复用边界

| 能力 | 采用方案 | 本项目只补充的部分 |
| --- | --- | --- |
| Agent 评测 Harness | `harbor-framework/harbor` | A/B/C 条件配置与 Forgeway Adapter |
| 多语言 Issue 任务 | `multi-swe-bench/multi-swe-bench` | 固定子集、L1/L2 与 Bugfix/Feature 标签 |
| 新鲜任务复验 | `microsoft/SWE-bench-Live` | 第二阶段固定样本与污染标记 |
| Patch 行为判定 | SWE-bench / Multi-SWE-bench 既有测试语义 | 独立封存、反篡改和结果聚合 |
| Skills 增量方法 | Harbor Skills 注入与 SkillsBench 配对思路 | 静态 Skill 绑定规则和使用证据 |
| 结果与统计 | Harbor Trial/trajectory/result | 配对聚合与内部继续投资门槛 |

禁止自行重写：

- 容器调度、并发 Trial、通用 Agent 协议；
- Skills 安装、来源解析和内容摘要；
- 通用轨迹格式、Token 基础采集；
- Patch 测试 Harness、云 Sandbox 和结果 Dashboard。

若固定 Harbor 版本已有能力不足，只允许实现薄 Adapter 或兼容层；不得复制整套 Harness。

## 4. 三组实验定义

三组必须使用相同：

- Codex CLI 版本、模型快照、reasoning 配置和 Provider；
- Shell、文件、测试工具与网络策略；
- 初始任务镜像、CPU、内存、超时和预算；
- Issue Snapshot、Base SHA 与任务说明；
- Repeat 数量和结果采集口径。

### Group A：Frozen Codex Harness

```text
Issue Snapshot
+ Base Repository Export
+ Harbor Codex Agent
- Skills
- Forgeway
```

A 组不是 Raw Model。Codex CLI 内建提示与执行逻辑属于固定 Harness 的一部分。

运行容器必须使用独立 `CODEX_HOME`，不得读取用户级配置、额外 MCP、Hooks、Plugin、
Skills 或项目外指令。锁文件至少记录：

```text
codex_cli_version
model
reasoning_effort
provider
sandbox_policy
approval_policy
network_policy
config_digest
```

### Group B：Frozen Skills Bundle

```text
Group A
+ Harbor --skill
+ Frozen Skills Bundle
```

Harbor 负责注入 Skill，并记录来源、内容摘要和解析后的 Git Commit。B 组使用预先冻结的
`task_taxonomy → skill_bundle` 规则，不允许针对单个 Issue 临时挑选 Skill。

示例：

```toml
[[skill_bindings]]
id = "rust-l1-bugfix-v1"
language = "rust"
task_type = "bugfix"
complexity = "L1"
skills = [
  "dev-rust@<commit>",
  "repo-map@<commit>"
]
```

首轮只验证“预定义 Skill 内容是否有效”，不验证自动发现或自动路由能力。

### Group C：Frozen Skills + Forgeway

```text
Group B
+ Forgeway Orchestration
```

C 组必须与 B 组使用完全相同的模型、Skills Lock 和工具权限，只增加 Forgeway 的：

- 契约解析；
- 任务分解与状态推进；
- 验证、重试和恢复回环；
- Stage、Gate、Retry 与 Recovery 轨迹。

Forgeway 通过薄 Harbor Agent Adapter 接入。不得为 C 组更换更强模型或增加未计费的
外部 Agent。

## 5. 预算赛道

### Phase 0–1：Equal-budget Track

首轮只运行因果归因赛道。三组统一限制：

```text
total model tokens
wall-clock timeout
tool-call ceiling
CPU / memory
parallelism
network policy
```

C 组预算必须包含所有内部调用：

```text
main-agent
contract parsing
task decomposition
review
sub-agent
context compression
retry / recovery
```

每个 Trial 记录：

```text
token_accounting_status = complete | incomplete
```

Equal-budget Track 中若为 `incomplete`，该 Trial 判为 `Invalid`。

### 延后：Product-mode Track

只有 Phase 1 出现稳定信号后才运行。届时冻结各系统默认模型路由、重试、并行度、
Fallback 和价格日期，并同时报告功能结果与端到端成本。

## 6. 任务集

### Phase 0：Smoke Set

固定 3 个任务：

| 语言 | 数量 |
| --- | ---: |
| Rust | 1 |
| TypeScript / JavaScript | 1 |
| Java | 1 |

Smoke 只验证基础设施，不用于比较能力高低。

### Phase 1：Pilot Set

固定 15 个任务：

| 语言 | 数量 |
| --- | ---: |
| Rust | 5 |
| TypeScript / JavaScript | 5 |
| Java | 5 |

目标分布：

```text
Bugfix        9
Small Feature 6
L1            9
L2            6
```

L1：1–3 个核心文件、参考 Patch 不超过约 200 LOC。  
L2：4–8 个核心文件、参考 Patch 不超过约 500 LOC。

若现有开源任务中 Small Feature 的行为 Oracle 不够确定，首轮先完成 Bugfix Pilot，
不得为满足配额临时制造低质量样本。

任务必须满足：

- Base SHA 可稳定构建或执行目标测试；
- Reference Patch 能通过 Oracle；
- 测试连续运行 3 次无 Flaky；
- 无外部生产服务、真实数据库或不可控网络依赖；
- Issue 不直接泄露修复实现；
- Agent 输入不包含 Base 之后的 Git 历史、评论或 PR 信息。

## 7. 执行与泄露控制

每个任务执行：

```text
3 Groups × 3 Repeats
```

15 个 Pilot 共 135 个 Trial。每次使用全新环境，A/B/C 顺序按任务随机交错。

Agent 阶段只能看到：

```text
Issue Snapshot
Repository export at base_sha
Repository-local instructions available at base_sha
Assigned Skills for B/C
```

Agent 阶段不得看到：

- 隐藏测试、Reference Patch 或 `solution/`；
- Base 之后的 Git Object、Remote Ref、Tag 或 Commit Message；
- 修复后的 Issue 评论、PR 讨论或 CI 结果；
- 其他 Trial 的工作区、轨迹和结果；
- 外部网络中的目标 Issue、PR 或答案。

本实验只能声称“执行环境隔离”，不能声称消除了模型训练污染。每个任务应记录：

```text
contamination_status =
  post_cutoff | likely_clean | public_historical | unknown
```

## 8. Patch 封存与 Verifier

Agent 完成、失败或耗尽预算后立即终止写入。使用一次性工作副本或临时 Index 导出完整
Patch：

```bash
git status --porcelain=v1 -z > /logs/artifacts/git-status.bin
git add -A
git diff --cached --binary --full-index HEAD \
  > /logs/artifacts/candidate.patch
git apply --check /logs/artifacts/candidate.patch
```

`candidate.patch` 必须覆盖修改、新增、删除、重命名、二进制和原未跟踪文件。

Verifier 必须：

1. 从不可变 Base Image 创建全新可写 Worktree；
2. 只注入 `candidate.patch` 与独立测试包；
3. 应用 Patch 后运行核心测试和回归测试；
4. 不把隐藏测试输出返回给 Agent；
5. 将基础设施故障与候选 Patch 失败分开。

状态机：

```text
Resolved
Unresolved
Invalid
InfraError
```

- `Resolved`：核心测试与回归测试全部通过，Patch 可应用且无规避；
- `Unresolved`：候选 Patch 未满足行为 Oracle；
- `Invalid`：测试篡改、答案检索、预算/统计不完整或其他协议违规；
- `InfraError`：评测基础设施失败，按预注册规则重跑，不按模型失败计分。

## 9. 指标

取消 100 分综合评分。

### 主指标

```text
Resolved
```

主要报告：

- 每组每任务 3 次运行的成功比例；
- `pass@3`：3 次中至少成功 1 次；
- 按语言、L1/L2、Bugfix/Feature 的 Resolved Rate；
- A→B、B→C、A→C 的配对 Win / Tie / Loss。

### 诊断指标

- Input、Output、Cached 与总 Token；
- 模型 API 成本、容器成本和总成本；
- 端到端耗时、Agent Turn 与工具调用次数；
- 编译/测试失败后的恢复次数；
- 修改文件数、Added/Deleted LOC；
- 是否新增有效测试、是否运行仓库原生测试；
- Forgeway 最后 Stage、Gate 失败与恢复次数；
- `Cost per Resolved Task`。

Pilot 只报告工程信号，不声称统计显著性或跨任务普遍优势。

## 10. 继续投资门槛

### Skills 出现有效信号

必须同时满足：

- B 相比 A 至少在两个不同任务上出现增益；
- 对应任务至少 2/3 Repeat 成功；
- B 的退化任务数不超过其增益任务数；
- 轨迹证明 Skill 被实际读取或使用。

### Forgeway 出现有效信号

必须同时满足：

- C 相比 B 在多个不同任务上出现增益；
- 至少一个 L2 任务只有 C 能稳定解决；
- 增益至少在 2/3 Repeat 中复现；
- 轨迹证明分解、验证或恢复机制实际参与；
- 同时公开 Token、时间和成本增量。

这些是内部工程门槛，不是学术显著性结论。

## 11. Phase 0 硬门禁

开始 3 个 Smoke Task 前必须完成：

1. A/B/C 的 Codex CLI、模型、Reasoning、权限和配置摘要一致；
2. B/C 的 Skills Lock 与静态绑定规则完全一致；
3. Forgeway 所有内部模型调用均进入端到端 Token/成本统计；
4. `candidate.patch` 能完整封存新增、删除、重命名、二进制和未跟踪文件；
5. Agent 阶段无法访问隐藏测试、`solution/` 和未来 Git 历史；
6. Verifier 在全新环境中应用 Patch，且结果不回传 Agent；
7. Harbor、数据集、Skills、Forgeway 和 Codex 均固定 Commit/版本与内容摘要。

Smoke 验收：

```text
Oracle 预验证通过
A/B/C 均能完成 Trial
Skill provenance 可追踪
Forgeway trajectory 可读取
Token accounting = complete
Patch 可独立重放
Verifier 隔离成立
```

任一项失败，停止能力比较，先修复评测基础设施。

## 12. 后续阶段

### Phase 1：15 任务 Pilot

回答 Skills、Forgeway 是否产生稳定正向信号，以及增益是否值得成本。

### Phase 2：能力拆分

仅在 Phase 1 有正向信号后增加：

- Relevant Skill vs Auto Skill Discovery；
- Forgeway Contract-only；
- Forgeway Validation-loop-only；
- 完整 Forgeway；
- Product-mode Track；
- SWE-bench-Live 新鲜任务复验。

### Phase 3：正式 Benchmark

只有需要长期跨模型比较或公开发布时，才增加：

- 密封 Holdout；
- 样本量与统计功效分析；
- Cluster / Paired Bootstrap；
- 人工双盲失败归因；
- 公开报告或 Leaderboard。

## 13. 存储与权威

```text
ai-handbook
  = 本协议、筛选理由、固定 Manifest、汇总结论与决策权威

forgeway-eval（实施时创建）
  = Harbor Adapter、配置、锁文件、任务选择和聚合脚本

Google Drive
  = 大型原始 Trial 包、完整轨迹、截图和可能含敏感信息的运行证据
```

首轮自行维护的实现仅限：

```text
Forgeway Harbor Adapter
任务子集选择脚本
隔离与 Patch 重放验证脚本
配对结果聚合脚本
```

## 14. 当前外部依据

设计时核对的主要开源项目：

- Harbor：<https://github.com/harbor-framework/harbor>
- Multi-SWE-bench：<https://github.com/multi-swe-bench/multi-swe-bench>
- SWE-bench-Live：<https://github.com/microsoft/SWE-bench-Live>
- SWE-bench：<https://github.com/swe-bench/SWE-bench>
- SkillsBench：<https://github.com/benchflow-ai/skillsbench>

Harbor 的 Skills 注入、Skill provenance 和 Multi-SWE-bench Adapter 已在
`harbor-framework/harbor@c3ce0c60bbd2fd1888b327efcc880dbd86d8b7cf` 中核对。
实际运行前仍必须把所用 Release/Commit 写入实验 Lock，不得跟随 `main` 漂移。

## 15. 当前状态

```text
Protocol: Approved
Phase 0 infrastructure: Not implemented
Smoke tasks: Not selected
Trials: Not run
Capability conclusion: Not verified
```

在真实 Trial 和独立 Verifier 结果产生之前，不得宣称 Skills 或 Forgeway 已获得
Benchmark 增益。
