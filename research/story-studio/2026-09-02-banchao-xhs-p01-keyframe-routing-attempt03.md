# 班超｜小红书历史动漫试播 P01 关键帧路由 Attempt 03

```yaml
task_identifier: TASK — Story Studio — 班超 小红书历史动漫三集试播验证
task_key: story-studio/banchao/xhs-history-anime-3ep-pilot
execution_unit: PILOT_EP01_VERIFIED_IMAGE_ROUTE_BINDING_OR_ACCESSIBLE_REFERENCE_TRANSFER
attempt_id: P01_KEYFRAMES_IMAGE_GEN_ATTEMPT_03
result: INVALID_OUTPUT_REPORT_INFOGRAPHIC
failure_class: FAIL_PROVIDER_OUTPUT_ROUTING_REPRODUCED
completed_at: 2026-09-02T16:14:47+09:00
canonical: false
production_ready: false
publication_ready: false
```

## 执行

本次只请求 `P01-KF01_SCRIBE_STATE` 一张人物场景图，并在工具调用前明确声明：

- Variant B 是唯一人物身份锚点；
- 只生成一张独立竖屏人物场景；
- 不得出现文字、表格、标题、UI、信息图、边框、Logo 或水印。

## 返回证据

```yaml
tool: image_gen
provider_generation_id: 5d46729a-0206-4114-b4a0-f6f06d0d64c5
edit_op: null
parent_generation_id: null
returned_outputs: 1
local_file: /mnt/data/a_detailed_document_like_infographic_worksheet_im.png
sha256: 9c3dbfe569928161f60e93815c1bf06eba678ccd0e9d3bceff3ec72530e47f09
bytes: 1972510
dimensions: 1178x1335
mode: RGB
drive_evidence_file_id: 1A3dpb1Hmr99KZsb_BY-dYlVPFs_TM6_1
```

## 判定

返回结果仍是项目状态/验收信息图，而不是一张独立人物关键帧。虽然图中嵌入了人物缩略画面，但整体输出包含大量可读文字、表格、状态标签和报告版式，并且比例不是 9:16。

生成元数据继续显示：

```text
edit_op: null
parent_generation_id: null
```

因此 Variant B 并未被验证为实际编辑父图或身份绑定输入。该结果不得拆取、裁切或冒充人物关键帧。

```yaml
valid_keyframes: 0/3
invalid_outputs: 3
gate_b: BLOCKED_NOT_RUN
image_gen_current_context: CIRCUIT_OPEN_HARD_STOP
```

## 下一步

当前会话不得再次调用同一路由。只有以下任一证据变化后才能继续人物关键帧执行：

1. 可确认绑定参考图并返回非报告型人物资产的图像工具；
2. Adobe 或其他 provider 能成功接收 Variant B 原始输入；
3. 用户重新上传一个能被 provider 实际访问的参考文件，并完成输入预检。

P01 Gate A、S1 194 张 canonical storyboard reference 及另一条 EP01 16:9 / 105 秒生产链均未修改。
