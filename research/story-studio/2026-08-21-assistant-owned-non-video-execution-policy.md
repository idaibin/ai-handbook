# Story Studio Assistant-Owned Non-Video Execution Policy

状态：`approved`  
生效时间：`2026-08-21`  
最近修订：`2026-09-01`  
适用范围：Story Studio 当前及后续 Task 的非视频工作

## 决策

除实际视频生成外，Research、文档、代码、图像、角色/场景/道具资产、技术图、验证、Dailies、证据打包以及 Google Drive / GitHub 同步，默认均由当前执行助手直接完成。

非视频任务不得再把“新建专用会话”“交给外部 provider”或“由用户下载后执行”作为默认推进条件。只有当前工具确实不能产生目标类型，且不存在可验证的替代执行路径时，才能记录为阻塞。

人物描述、角色 Bible、视觉 Prompt 和助手语气设定只负责内容与表达，不承担 Task 路由、工具选择、源资产绑定、重试预算或失败熔断。上述控制必须由本政策、Active Capsule 和 Current Status 明确记录。

## 执行规则

- 用户无需为非视频任务下载、转发或手工执行 Work Order。
- 同一 Task 控制会话可以直接执行非视频资产，不再要求 fresh asset chat。
- 图像模型输出、确定性 renderer 输出和来源文件直接派生输出都可以形成 `execution-native` 证据；不得把 resize、重编码或 Review derivative 标记为 native。
- 几何布局、机位、灯光、流程图和其他技术型资产可以使用确定性 renderer，但必须保存源码、运行时身份、原始 bytes、精确格式/尺寸、SHA-256，并完成可复现回读。
- 生成失败或错路由的报告图、信息图和无关内容必须记为 `invalid_output`，不得进入资产清单或 Gate。
- 实际视频生成仍可路由到具备视频能力的 provider/session；视频前后的脚本、分镜、提示词、Review、证据和同步仍由助手负责。

## Task Intent Gate

任何工具调用前必须记录并比较：

```yaml
active_task_identifier:
active_next_action:
latest_explicit_user_goal:
intent_matches_active_task: true | false
```

规则：

1. 用户回复“继续”只在 `latest_explicit_user_goal`、active Task 和 `next_action` 一致时推进。
2. 最近明确目标已经指向另一个已登记 Task 时，必须在工具调用前返回 `STOP_TASK_INTENT_CONFLICT`。
3. 冲突时只显示当前 Task、目标 Task 和精确切换标识，不执行旧 Task，不调用生成或编辑工具。
4. 自然语言讨论另一个方向不自动改写 active Task；切换仍须遵守 Task Resolution Protocol。
5. 任务冲突不能通过人物描述、Prompt 加长或上下文猜测解决。

## Image Edit Binding Gate

调用图像编辑工具前必须固定：

```yaml
operation_kind: image_edit
source_asset_id:
source_file_id:
source_sha256:
source_dimensions:
provider:
provider_supports_explicit_source_binding:
binding_verified_before_call:
attempt_budget:
```

只有以下条件全部成立才允许调用：

- 当前会话中存在唯一、可读取的源图；
- 源文件 ID、SHA-256、尺寸和目标 Work Order 一致；
- Provider 的当前接口明确支持源图编辑，而不是仅支持 text-to-image；
- 调用载荷能够显式绑定源图，不能仅依赖“图片曾在聊天中出现”；
- 当前 Task 和图像操作目标一致；
- 同一失败指纹的熔断器尚未打开。

输出后必须立即检查：

- 是否保留源图的人物、构图和场景；
- 是否完成指定 ROI，而不是生成新的 Dashboard、海报或说明图；
- 若 Provider 返回 `edit_op`、`parent_gen_id` 或等价元数据，是否能证明这是编辑操作；
- 原生输出规格是否满足合同。

任何一项失败，输出不得登记为候选资产。

## Provider Circuit Breaker

失败指纹使用：

```text
provider + operation_kind + failure_class + source_asset_id
```

以下任一情况第一次出现后，立即打开当前路线熔断器：

- 图像编辑返回新的无关图片；
- 源图人物、构图和环境全部消失；
- 元数据明确显示未绑定源图；
- Provider 无法读取私有源资产；
- 同一接口再次产生已知错路由类型。

熔断后：

```yaml
circuit_open: true
next_allowed_action:
  - switch_provider_with_verified_binding_capability
  - start_clean_execution_context_with_unique_source_asset
  - stop_or_switch_task
```

仅修改 Prompt、增加负面词、重复上传同一图片或再次回复“继续”，均不构成恢复熔断的证据。

## Invalid Output Quarantine

无效输出默认仅保留临时运行记录：

- 不进入 active assets、mapping、manifest、canonical、production-ready 或视频输入；
- 不为同一失败反复创建 Drive 目录、GitHub 报告和 Registry 行；
- 同一失败指纹只保留一份合并 Incident；
- 只有首次发现新系统性失败、Provider 判断变化或 `next_action` 改变时，才持久化新的事故证据。

## Active Capsule 最低运行保护

每个涉及媒体工具的 Active Capsule 至少包含：

```yaml
routing_guard:
  active_task_identifier:
  latest_explicit_user_goal:
  intent_match:

media_execution_guard:
  operation_kind:
  source_asset_id:
  source_file_id:
  source_sha256:
  provider:
  binding_verified:
  attempt_budget:
  attempts_used:
  circuit_open:
  circuit_reason:

on_guard_failure:
  action: STOP_BEFORE_TOOL
```

缺少上述字段时，媒体调用不授权。

## 证据合同

每个可计数的非视频资产执行至少保存：

1. execution-native 原始文件；
2. execution receipt；
3. 精确格式、尺寸、字节数和 SHA-256；
4. `GenerationAttempt` 或等价执行记录；
5. `Dailies` / 人工验收；
6. Drive file ID 与回读证据；
7. 必要时保存源码和 byte-identical rerender 结果。

失败证据只需证明失败分类、源资产身份、调用身份和资产处置，不要求把重复无效输出包装成完整生产资产包。

## Gate 边界

本政策只改变执行责任和合法执行路径，不降低验收要求。任何输出均不得自行升级为 Production Canon、G07 approved、`production_ready` 或 `publication_ready`。

## 已验证案例

### 有效执行

`VERTICAL_SLICE_02_LUOYANG_MINIMAL_SET / TAKE_02B`：

- execution-native PNG：1920×1080 RGB；
- SHA-256：`95875a2243294872f6defd0d31bd4be51edeacb6a3ccd0de40eba85ec10d13ff`；
- deterministic renderer 源码已保存；
- 两次重渲染 byte-identical；
- 自动校验和 Dailies 通过；
- `verified_G07_asset_executions` 从 `1/10` 更新为 `2/10`。

### 熔断案例

`EP01 K2 Attempt 03` 多次请求 K1 源图编辑，却返回 EP01/G07 状态信息图；返回元数据 `edit_op=null`、`parent_gen_id=null`。该路线按本次修订打开熔断器，不再允许仅靠 Prompt 修改继续重试。无效图只保留为合并 Incident，不具有任何资产状态。
