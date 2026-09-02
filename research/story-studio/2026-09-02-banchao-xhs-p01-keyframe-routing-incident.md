# 班超｜小红书历史动漫试播 P01 三关键帧生成路由事件记录 v0.1

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_id: story-studio-banchao-xhs-history-anime-3ep-pilot
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
execution_unit: PILOT_EP01_VISUAL_IDENTITY_CONTRACT_AND_THREE_KEYFRAMES
result: PARTIAL_CONTRACT_COMPLETE_KEYFRAMES_BLOCKED
failure_class: FAIL_PROVIDER_OUTPUT_ROUTING
status: active_gate_b_blocked_generation_route
canonical: false
production_ready: false
publication_ready: false
completed_at: 2026-09-02T15:30:47+09:00
```

## 1. 结论

P01 视觉身份合同已经形成并同步；三张目标关键帧没有生成成功。

两次 `image_gen` 调用都返回了 Task/流程信息图，而不是人物关键帧。第二次调用已经在可见上下文中明确写出“三张独立 9:16 人物关键帧、不得信息图、使用 Variant B 身份锚点”，但结果仍然重复路由为项目状态 Dashboard。因此当前会话的该生成路由已打开 circuit breaker，不再继续重试。

Adobe fallback 仅执行了初始化和输入传输检查。三次输入传输均返回 `Forbidden: The asset is not accessible to the user`，因此没有调用 Firefly 图像生成或编辑，也没有产生 Adobe 输出。

当前有效关键帧数量：`0/3`。Gate B 不能执行，也不能判定为通过。

## 2. 已完成产物

### 视觉身份合同

```yaml
artifact_path: research/story-studio/2026-09-02-banchao-xhs-p01-visual-identity-contract.md
github_commit: a55bc5f593f390675da1a1e27171af02f5949b74
content_sha256: 4014cff4147237256a5895c37e3abf7654073a38b68e5107525c3a1dd58716cd
drive_document_id: 1cyl2PbDBbJeA4qksbsDmkvoMravCb9rdF1QqK6UwkqA
drive_folder_id: 18WNl6QhFAlJOC-XeSgCHNfExGQE581wq
```

合同已经固定：

- Variant B 是唯一身份锚点；
- 三个状态分别为佣书、久劳苦、投笔后克制回应；
- 统一为 9:16、手绘硬边二维历史动漫；
- 服装无纹样、无铠甲、无武将化；
- 简牍、低案、朴素毛笔只作为受约束的视觉设计；
- 无可辨识文字、现代物件、报告版式或信息图。

## 3. Attempt 记录

### Attempt 01

```yaml
attempt_id: P01_KEYFRAMES_IMAGE_GEN_ATTEMPT_01
tool: image_gen
requested_outputs: 3 independent 9:16 character keyframes
returned_outputs: 1
provider_generation_id: 5eea2af5-6400-4373-baad-513a14edd24f
edit_op: null
parent_generation_id: null
result: INVALID_OUTPUT_REPORT_INFOGRAPHIC
local_file: /mnt/data/a_detailed_infographic_slide_screenshot_with_a_c.png
sha256: 3f77f302d537435e11af87c3dab037141a9db68de8e01a25c81e777a53456bcc
bytes: 1897525
dimensions: 1024x1536
mode: RGB
drive_evidence_file_id: 1QKCR_n3gT5C7XVF2kTuLx1AXwmGFacvp
```

失败项：

- 没有人物；
- 不是三个输出；
- 不是三张独立 9:16 关键帧；
- 返回内容为带大量文字的项目状态信息图；
- 违反 `no_readable_text`、`no_report_layout`、`single_clear_subject`。

### Attempt 02

```yaml
attempt_id: P01_KEYFRAMES_IMAGE_GEN_ATTEMPT_02
tool: image_gen
requested_outputs: 3 independent 9:16 character keyframes
returned_outputs: 1
provider_generation_id: 2ea2205b-19f8-40e8-8ba7-78ab2cffac8b
edit_op: null
parent_generation_id: null
result: INVALID_OUTPUT_REPORT_DASHBOARD
local_file: /mnt/data/a_detailed_infographic_slide_style_image_with_a_pr.png
sha256: 17deb7f208d96f2f13f205de49d259a3dfd6a9e8e1c59e5a7f4a637d17c6af1c
bytes: 1927738
dimensions: 1536x1024
mode: RGB
drive_evidence_file_id: 1ZoGEc5VztyCxqWsCTV1wsdE7cViBdJZi
```

Attempt 02 前已经显式写入以下可见约束：

```text
三张独立 9:16 人物关键帧
不得拼版、设定表、报告页或信息图
使用附件 Variant B 作为唯一身份锚点
无任何文字、标题、Logo 或现代物件
```

输出仍为横向项目状态 Dashboard，证明问题不是缺少基础约束，而是当前路由没有绑定到人物资产生成意图。

失败项：

- 没有人物；
- 不是三个输出；
- 横向 1536×1024；
- 大量可辨识文字；
- 报告/Dashboard 版式；
- 身份、状态、手部和物质文化均无法验证。

## 4. Adobe fallback 检查

```yaml
tool_init: PASS
skill_name: story-studio-xhs-p01-keyframes
skill_version: 0.1.0
reference_transfer_attempts: 3
reference_transfer_result: FAIL_FORBIDDEN
firefly_generation_called: false
adobe_output_count: 0
```

尝试输入：

1. 当前运行时文件 ID；
2. 原会话附件文件 ID；
3. Google Drive fetch 返回的 sediment file reference。

三次均返回：

```text
Forbidden: The asset is not accessible to the user
```

由于参考输入未能进入 Adobe，未继续执行 `image_instruct_edit` 或 `image_generate`，避免生成无法证明身份绑定的替代图。

## 5. Gate B 状态

```yaml
identity_same_person: NOT_EVALUATED
face_anchor_preserved: NOT_EVALUATED
hair_anchor_preserved: NOT_EVALUATED
body_proportion_preserved: NOT_EVALUATED
costume_system_preserved: NOT_EVALUATED
state_is_distinguishable: NOT_EVALUATED
hand_prop_surface_continuity: NOT_EVALUATED
material_culture_no_obvious_modern_element: NOT_EVALUATED
no_readable_text: FAIL_ON_BOTH_INVALID_OUTPUTS
no_report_layout: FAIL_ON_BOTH_INVALID_OUTPUTS
aspect_ratio_9_16: FAIL_ON_BOTH_INVALID_OUTPUTS
gate_b: BLOCKED_NOT_RUN
```

无有效图片时不得把 Gate B 记为 `REVISE` 或 `PASS`；当前是 provider/output routing blocker。

## 6. 状态变更

```yaml
visual_identity_contract: completed_synced
valid_keyframes: 0/3
invalid_outputs: 2
image_gen_route_current_context: CIRCUIT_OPEN
adobe_reference_transfer: BLOCKED_FORBIDDEN
gate_b: BLOCKED_NOT_RUN
current_execution_unit: PILOT_EP01_VISUAL_IDENTITY_CONTRACT_AND_THREE_KEYFRAMES
next_action: PILOT_EP01_VERIFIED_IMAGE_ROUTE_BINDING_OR_ACCESSIBLE_REFERENCE_TRANSFER
```

下一步只有在以下任一证据发生变化后执行：

1. `image_gen` 能明确返回人物资产而非报告图，并支持正确绑定 Variant B；
2. Adobe 或其他已验证图像 provider 能读取身份参考，并返回原始输出与 provider receipt；
3. 当前附件被重新绑定为 provider 可访问输入，且静态输入检查通过。

在此之前，重复 `继续` 不再调用当前失败的 `image_gen` 路由，不生成第三张无效报告图，也不推进 Gate B、P01 Animatic、P02 或 P03。

## 7. 未改变边界

```text
P01 Gate A 仍为 PASS_WITH_VISUAL_HOLDS
S1 194 张 canonical storyboard reference 未修改
另一条 EP01 16:9 / 105 秒生产链未修改
canonical = false
production_ready = false
publication_ready = false
actual_voice_duration = not_verified
commercial_rights = not_verified
```
