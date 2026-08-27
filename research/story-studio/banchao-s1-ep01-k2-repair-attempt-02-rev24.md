# 班超 S1 — EP01 K2 静态动作锚点修复 Attempt 02（Revision 24）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `execution_unit`: `EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REPAIR_ATTEMPT_02`
- `executed_at_utc`: `2026-08-27T13:21:14Z`
- `result`: `K2_REPAIR_ATTEMPT_02_CANDIDATE_GENERATED_PENDING_REVIEW`
- `canonical`: `194`（不变）
- `production_ready`: `0`（不变）

## 结论

已从 K1 生成第二版 K2 候选：

```text
EP01-K2-TIP-OFF-SURFACE-ATTEMPT-02.png
1920×1080 / RGB PNG
SHA-256: de3bb9745effca071f25f14e3b50d8c4f7518b195021b8a8176987957dd7e84e
rights_status: internal_candidate_only
production_ready: false
```

该资产只完成修复生成和机械预检，**尚未执行独立 Review Attempt 02**；K3 仍未授权。

## 修复目标

Revision 23 确认 Attempt 01 有两个实现缺陷：

```text
1. 笔毫形成分叉/重复渐尖轮廓；
2. hand/wrist ROI changed pixels = 0，未体现手腕抬起。
```

Attempt 02 将手、手腕和毛笔作为一个局部物理状态共同上移，并用源纸面邻区确定性修复原接触区，不再单独平移笔尖。

## 机械证据

```text
shift_y_pixels: -14
changed_bbox_xyxy: [884, 538, 1057, 900]
changed_pixel_count: 31520
hand_wrist_roi_xyxy: [760, 560, 1080, 825]
hand_wrist_changed_pixel_count: 24856
face_changed_pixel_count: 0
outside_changed_bbox_pixel_identity: PASS
byte_identical_rerun: PASS
```

独立脚本重跑输出 SHA 与候选完全一致：

```text
de3bb9745effca071f25f14e3b50d8c4f7518b195021b8a8176987957dd7e84e
```

## 生成门禁

```text
native 1920×1080 RGB PNG: PASS
single clean frame: PASS
hand/brush coherent state movement: PASS_MECHANICAL_NONZERO_HAND_WRIST_DELTA
face identity: PASS_EXACT_PIXEL_IDENTITY
single continuous bristle tip: PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW
tip off surface: PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW
full independent review: NOT_EXECUTED
K3 authorized: false
```

`PASS_VISUAL_BOUNDED_PENDING_INDEPENDENT_REVIEW` 不是最终质量通过；笔毫连续性、空气间隙、局部修补自然度和 K1→K2 插值适用性仍必须由下一单元独立审核。

## 失败尝试

```text
image_gen_edit_attempt_04:
FAIL_IMPLEMENTATION_OUTPUT_ROUTING_DASHBOARD_REPORT
registered: false
```

错误输出未登记、未上传、未进入任何活动入口。

## Drive registration

```text
folder: 1iI04IOAJnS0Psj0NaSLKBmQ9ZFFDHRai
candidate_png: 1VRvECfjBepkG3VnUPdhaPeuJxvXm2aO4
report: 1Q9f43Nmx-AYNhT1vXm3sUF4qroIqlDfm
receipt: 1Rih94A7Ta4s-ZFmCI37YCpmI03ZXOB9o
rerun_receipt: 1DaEmuUBePn3Xtla4PYXUw_VyP5X4gb_C
evidence_json: 1nSiBxUiLmeQEUY_vYpDGE7i2nunLKGXf
repair_script: 1zYBnPmfLVtOTjtri3oonBUU0iajMYT33
evidence_script: 1b9w9IXaw9rCgRP5-nDMX0J3T6XPav9Ac
review_sheet: 1WXcf12fIksb5eQjHjtS7gJ8AljMfmztN
closeup: 1FBiWtsc1ckqNOy_5tbIpKzKHRVsTdG_-
annotated: 1WoaEcNnImuxSEezsWOPI3C1ZwwOJbym2
changed_mask: 1JSnWv76Fb5lTUOu8icgkx0M5nUwin73B
diff_map: 1hniubiHxSiX9_XdxUFn4ZixjKy3OFDPi
checksums: 1BUIiEcHiubzLp44JtdUhs04VhzvSJmQk
evidence_package: 1MLTa2heov8qkmPWN3Io3GOqRNpzWmB-L
```

## Asset disposition

```text
Attempt 01: REJECTED_REVIEW_RETAINED_AS_EVIDENCE
Attempt 02: production_motion_anchor_internal_candidate_pending_review_attempt_02
silent overwrite: false
delete: false
canonical mutation: 0
mapping mutation: false
manifest mutation: false
K3 authorized: false
```

## Unchanged authority

```text
canonical: 194
production_ready: 0
mapping revision: 10
manifest revision: 10
194 canonical Drive refs: unchanged
F08–F10 canonical_storyboard_reference: unchanged
F03 / F06–F10 production_motion_anchor=false: unchanged
EP01→EP02 boundary: unchanged
```

## Next action

```text
EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REVIEW_ATTEMPT_02
```
