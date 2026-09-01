# 班超 S1 — EP01 K2 Attempt 03 受信图像编辑输入启用（Revision 27）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `execution_unit`: `EP01_WRITING_SYSTEM_K2_ATTEMPT03_TRUSTED_IMAGE_EDIT_INPUT_ENABLEMENT`
- `executed_at_utc`: `2026-09-01T08:18:00Z`
- `result`: `PASS_IMAGE_GEN_INPUT_STAGED_ADOBE_STILL_BLOCKED`
- `canonical`: `194`（不变）
- `production_ready`: `0`（不变）
- `K3_authorized`: `false`

## 结论

K1 原始关键帧已从私有 Google Drive 通过受信 connector 下载到本次会话和运行环境，并完成文件身份、规格与视觉内容回读。该文件现在是当前会话中的明确图像目标，可供下一执行单元调用 `image_gen` 进行 K2 Attempt 03 full-ROI 编辑。

Adobe Creative Cloud / Firefly 输入链路仍返回 `Forbidden: The asset is not accessible to the user`。因此 Adobe 不作为下一单元的可用编辑器；这不再阻断 `image_gen` 路线。

本单元只解决输入可用性，没有执行 K2 生成、没有验证输出路由，也没有生成 K3。

## 已验证输入

```text
Drive file ID:
1VMntzshVFdYTUft1KVW4CmMiPVDZ-Uwg

Drive title:
EP01-K1-NORMAL-WRITING.png

conversation file ID:
file_000000009a14820981dd04f71abbc2f6

runtime path:
/mnt/data/EP01-K1-NORMAL-WRITING.png

size:
2170841 bytes

format:
PNG

dimensions:
1920×1080

mode:
8-bit RGB

SHA-256:
ecc2c27acdc44517296f3b7454a34a107eddbfddbfc1fd8c7aae109b6f76e473
```

该 SHA-256 与 Revision 21 冻结的 K1 身份完全一致。视觉回读确认目标是洛阳抄书场景中的班超正常书写关键帧，不是 dashboard、report 或 infographic。

## 执行尝试

### Google Drive → 当前会话

```text
Google_Drive.fetch(download_raw_file=true, include_base64=false):
PASS

connector file_uri created:
PASS

local runtime materialization:
PASS

SHA/spec readback:
PASS
```

### Adobe 输入链路

按 Adobe 工作流执行并重试：

```text
asset_openai_file_upload(file_id):
FORBIDDEN_ASSET_NOT_ACCESSIBLE_TO_USER

asset_openai_file_upload(local mounted path):
FORBIDDEN_ASSET_NOT_ACCESSIBLE_TO_USER

asset_initialize_file_upload:
FORBIDDEN_ASSET_NOT_ACCESSIBLE_TO_USER
```

Adobe 未创建资产、未返回可用 `presignedAssetUrl`，也未执行图像编辑。

## 状态判断

```text
image_gen trusted input target:
STAGED_IN_CURRENT_CONVERSATION

image_gen edit execution:
NOT_STARTED

image_gen output routing:
NOT_VERIFIED

Adobe input:
BLOCKED_PROVIDER_ACCESS

Attempt 03 valid native output:
NOT_CREATED

K2 independent review Attempt 03:
NOT_STARTED

K3:
NOT_AUTHORIZED
```

## 失败分类

```text
Adobe:
FAIL_RIGHTS_OR_PROVIDER_INPUT_ACCESS

image_gen:
NO_FAILURE_IN_THIS_UNIT
OUTPUT_ROUTING_REQUIRES_NEXT_UNIT_EXECUTION

contract_change_required: false
dependency_change_required: false
architecture_change_required: false
```

## 资产边界

```text
K1 overwritten: false
K2 Attempt 01 overwritten: false
K2 Attempt 02 overwritten: false
mapping changed: false
manifest changed: false
canonical mutation: 0
production_ready mutation: 0
```

## 下一执行单元

```text
EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REPAIR_ATTEMPT_03_FULL_ROI_REGEN
```

下一单元必须：

1. 只使用当前会话已加载的 K1 图像作为编辑目标；
2. 只生成一张 K2 Attempt 03；
3. 重绘完整 `hand–wrist–brush–paper interaction ROI`，不得做像素平移、克隆或手工拼补；
4. 输出必须是单张干净历史画面，不得出现 dashboard、卡片、文字说明或 contact sheet；
5. 生成完成后先登记原生输出和文件身份，再进入独立 Review；
6. K2 未通过前，K3 继续禁止。
