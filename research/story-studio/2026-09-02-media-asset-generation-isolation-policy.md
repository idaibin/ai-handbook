# Story Studio Media Asset Generation Isolation Policy

状态：`approved`  
生效时间：`2026-09-02`  
适用范围：Story Studio 当前及后续 Task 的媒体资产执行边界

## 决策

除实际视频生成外，Research、文档、代码、角色/场景/道具资产设计、技术图、验证、Dailies、证据打包以及 Google Drive / GitHub 同步，仍由当前执行助手负责完成。

**助手负责完成，不等于媒体生成必须发生在 Task 控制会话。** Story Studio 从本修订起采用两个执行面：

```text
Control Project
  Task / Research / Contract / Review / Evidence / Sync

Isolated Media Context
  Image Generation / Image Edit / Video Generation
```

控制 Project 负责定义资产、准备输入、验收输出和记录证据；图片或视频的实际生成与编辑必须进入独立 Image Assets Project 或纯媒体会话。控制 Project 禁止直接调用任何会生成或编辑媒体的工具。

## 执行面路由

```yaml
execution_surfaces:
  control_project:
    owns:
      - source_loading
      - research
      - task_state
      - work_order
      - media_input_preparation
      - review_and_dailies
      - evidence_and_sync
    media_tool_calls: prohibited

  isolated_media_context:
    owns:
      - image_generation
      - image_editing
      - video_generation
    context_isolation_required: true
    one_asset_per_execution: true
```

用户无需为非视频任务重新设计 Prompt、整理证据或手工维护状态。执行助手必须准备完整、可直接使用的媒体输入包，并在输出返回后继续完成 Review、证据和同步。

当前控制面不能自行创建另一个 ChatGPT Project 或会话时，状态只能推进到 `media_capsule_ready_waiting_isolated_execution`；不得以控制会话直接生图作为替代，也不得把未生成的资产包装为完成。

## Media Asset Generation Isolation

媒体生成输入只允许包含：

```yaml
context_allowlist:
  - asset_id
  - current_visual_target
  - required_reference_images
  - identity_or_asset_contract
  - camera_and_composition_contract
  - style_requirements
  - negative_constraints
```

以下治理信息不得进入媒体生成上下文或成为画面内容：

```yaml
context_denylist:
  - task_state
  - gate
  - registry
  - execution_record
  - commit
  - sha256
  - github_status
  - drive_status
  - evidence_report
  - next_action
```

一次只生成一个资产。需要参考图时，必须先确认参考图已经实际绑定；未取得绑定证据时执行 `STOP_BEFORE_TOOL`。

输出中出现表格、Dashboard、报告页、UI、标题、状态标签或说明文字，立即判定为 `invalid_output`。无效输出不得裁切、拆取、升级或继续作为下一张图片的参考。

## Media Binding Gate

调用媒体工具前必须固定：

```yaml
operation_kind:
asset_id:
reference_required:
reference_asset_id:
reference_file_identity:
provider:
provider_supports_explicit_reference_binding:
binding_verified_before_call:
active_asset_count:
context_allowlist_check:
context_denylist_check:
attempt_budget:
```

只有以下条件全部成立才允许调用：

- 当前媒体上下文只处理一个 `asset_id`；
- 参考图是当前上下文中唯一、可读取的图像输入；
- Provider 接口明确支持参考图绑定或图像编辑；
- 调用载荷能够显式绑定参考图，不能仅依赖图片曾在其他聊天或 Project 中出现；
- 生成上下文不包含 Task、Gate、Registry、Evidence 等控制材料；
- 同一失败指纹的熔断器尚未打开。

缺少任一条件：

```yaml
on_guard_failure:
  action: STOP_BEFORE_TOOL
```

## Provider Circuit Breaker

失败指纹使用：

```text
provider + operation_kind + failure_class + reference_asset_id
```

以下任一情况第一次出现后，立即打开当前路线熔断器：

- 输出为报告、Dashboard、说明页或无关图片；
- 源图人物、构图和环境全部消失；
- 元数据明确显示未绑定参考图；
- Provider 无法读取私有参考资产；
- 同一接口再次产生已知错路由类型。

熔断后，仅以下变化可以恢复：

```yaml
next_allowed_action:
  - isolated_media_context_with_clean_input
  - different_provider_with_verified_binding_capability
  - newly_accessible_reference_binding
  - stop_or_switch_task
```

仅修改 Prompt、增加负面词、重复上传同一图片或再次回复“继续”，均不构成恢复熔断的证据。

## Invalid Output Quarantine

无效输出只作为失败证据：

- 不进入 active assets、mapping、manifest、canonical、production-ready 或视频输入；
- 不得从报告图中裁切人物区域冒充关键帧；
- 同一失败指纹只保留一份合并 Incident，除非 Provider、绑定方式或失败分类发生实质变化；
- 不为重复失败持续制造新的报告、Registry 行或版本。

## 证据合同

每个可计数的媒体资产执行至少保存：

1. execution-native 原始文件；
2. execution receipt 或 Provider 元数据；
3. 精确格式、尺寸、字节数和 SHA-256；
4. `GenerationAttempt` 或等价执行记录；
5. `Dailies` / 人工验收；
6. Drive file ID 与回读证据；
7. 必要时保存源码和 byte-identical rerender 结果。

失败证据只需证明失败分类、参考资产身份、调用身份和资产处置，不要求把重复无效输出包装成生产资产包。

## Gate 边界

本政策只调整媒体执行边界，不降低验收要求。任何输出均不得自行升级为 Production Canon、G07 approved、`production_ready` 或 `publication_ready`。

## 当前迁移规则

旧政策中的以下规则自本修订起失效：

```text
同一 Task 控制会话可以直接执行图片生成
separate_chat_required_for_non_video_work: false
control_chat_image_generation_hard_prohibition: removed
```

新的解释为：

```text
assistant_owned = 责任归属
isolated_media_context = 媒体执行位置
```

历史 Task、Work Order 和 Evidence 不删除；下一次媒体调用前，当前 Active Capsule 或媒体 Work Order 必须完成本政策迁移。
