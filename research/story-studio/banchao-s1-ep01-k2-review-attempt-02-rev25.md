# 班超 S1 — EP01 K2 静态动作锚点独立审核 Attempt 02（Revision 25）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `task_key`: `story-studio/banchao/s1-final-gate`
- `execution_unit`: `EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REVIEW_ATTEMPT_02`
- `reviewed_at_utc`: `2026-08-27T15:10:35Z`
- `precondition_status_revision`: `24`
- `precondition_task_revision`: `30`
- `review_scope`: `native_static_keyframes_and_static_interpolation_risk_proxy_only`

## 结论

```text
K2 Review Attempt 02: FAIL_IMPLEMENTATION_REPAIR_REQUIRED
K2 Attempt 02 disposition: REJECTED_REVIEW_RETAINED_AS_EVIDENCE
K3: NOT_AUTHORIZED
actual provider video continuity: NOT_VERIFIED
canonical: 194 unchanged
production_ready: 0 unchanged
```

Attempt 02 修复了 Attempt 01 的一个机械问题：手、手腕和毛笔不再是“只有笔尖发生变化”，而是形成约 14 px 的联合位移。但静态原生关键帧仍未通过五项验收，不能作为 K1→K3 的生产动作锚点。

## 审核对象

```text
K1 source:
EP01-K1-NORMAL-WRITING.png
Drive ID: 1VMntzshVFdYTUft1KVW4CmMiPVDZ-Uwg
SHA-256: ecc2c27acdc44517296f3b7454a34a107eddbfddbfc1fd8c7aae109b6f76e473

K2 Attempt 02:
EP01-K2-TIP-OFF-SURFACE-ATTEMPT-02.png
Drive ID: 1VRvECfjBepkG3VnUPdhaPeuJxvXm2aO4
SHA-256: de3bb9745effca071f25f14e3b50d8c4f7518b195021b8a8176987957dd7e84e
```

两张均为 `1920×1080 / RGB PNG`。

## 已验证通过项

```text
native specification: PASS
single clean frame: PASS
face ROI changed pixels: 0
identity / costume / set / camera / lighting outside changed bbox: PASS_EXACT_PIXEL_IDENTITY
new readable text / watermark / dashboard content: PASS_NONE
```

机械差异：

```text
changed_bbox_xyxy: [884, 538, 1057, 900]
changed_pixel_count: 31520
hand_wrist_roi_xyxy: [760, 560, 1080, 825]
hand_wrist_changed_pixel_count: 24856
face_changed_pixel_count: 0
```

## 五项审核结果

### 1. 笔毫：FAIL

```text
hero_brush_bristle_geometry:
FAIL_RIGID_SOLID_WEDGE_NO_SOFT_GATHERED_BRISTLE
```

分叉轮廓较 Attempt 01 减少，但笔毫仍呈实心、刚性三角锥形，缺少柔软毛丝、聚锋和自然受力形变。它仍可能诱发视频模型将笔毫解释为硬塑料锥或继续发生融化、分裂。

### 2. 手部状态：FAIL

```text
hand_wrist_state:
FAIL_COHERENT_TRANSLATION_BUT_UNNATURAL_CUTOUT_AND_CUFF_GHOST
```

非零手腕像素变化只证明局部区域移动。视觉上更接近“手—袖口—毛笔剪切块整体平移”，而不是自然的腕关节抬起、指节控制和笔杆受力变化。袖口下方存在明显暗色残影和涂抹边界。

### 3. 离纸间隙：FAIL

```text
tip_to_surface_gap:
FAIL_AMBIGUOUS_CONTACT_NO_CONTINUOUS_PAPER_TONED_AIR_BAND
```

在原生 100% 与 8× nearest-neighbour 放大下，最低笔锋与纸面之间未形成清晰、连续的纸面色背景带；视觉上仍近似接触或仅有不可可靠辨认的亚像素间隙。

### 4. 局部修补自然度：FAIL

```text
local_patch_naturalness:
FAIL_DARK_GHOST_BAND_BLUR_AND_TEXTURE_DISCONTINUITY
```

原接触区和袖口下方出现横向暗带、模糊区域及纹理连续性破坏。该区域不是自然纸面与自然阴影的连续变化。

### 5. 插值适用性：FAIL_RISK

```text
static_interpolation_input_suitability:
FAIL_RISK_DOUBLE_EDGES_AND_FLOW_INCONSISTENCY_TAIL
```

静态线性混合代理在手指、袖口、笔杆和笔锋周围形成明显双边缘/残影。Farneback 双向一致性代理显示：

```text
forward flow magnitude p50: 13.80 px
forward flow magnitude p95: 14.20 px
forward-backward consistency error p90: 3.20 px
forward-backward consistency error p95: 5.28 px
forward-backward consistency error p99: 9.82 px
```

这些结果只用于暴露输入对应关系风险，不是视频模型输出，也不能替代 Clip A 的真实逐帧验收。

## 验证边界

```text
Prompt / Motion Contract:
用于定义期望状态和失败条件，不是视觉通过证据。

Static keyframe review:
本轮已执行。

Actual provider video interpolation:
NOT_VERIFIED。
```

没有视频 Provider 时，本轮可以否决不合格静态输入，但不能证明合格关键帧一定能生成稳定视频。

## Failure classification

```text
primary:
FAIL_IMPLEMENTATION_LOCAL_COMPOSITING_ARTIFACTS

secondary:
FAIL_IMPLEMENTATION_PROP_GEOMETRY
FAIL_IMPLEMENTATION_ACTION_STATE_UNNATURAL

FAIL_CONTRACT: false
FAIL_DEPENDENCY: false
FAIL_ARCHITECTURE: false
```

现有 Motion Anchor Contract 无需修改；问题来自实现方式。

## 资产处理

```text
Attempt 02 Drive file remains unchanged
Attempt 02 status becomes REJECTED_REVIEW_RETAINED_AS_EVIDENCE
silent overwrite: false
delete: false
canonical mutation: 0
mapping mutation: false
manifest mutation: false
K3 authorized: false
```

## 下一修复单元

```text
EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REPAIR_ATTEMPT_03_FULL_ROI_REGEN
```

Attempt 03 必须：

1. 不再使用整块 14 px 平移、局部克隆或仅笔尖位移；
2. 对完整“手腕—手指—笔杆—笔毫—纸面接触区”执行一次统一重绘/重建；
3. 保留同一人物、服装、机位、光线、纸面和道具布局；
4. 形成单一、柔软、聚锋的毛笔笔毫；
5. 在原生像素中形成明确、连续的空气间隙；
6. 不出现袖口残影、补丁接缝、纹理断裂或重复边缘；
7. 独立 Review Attempt 03 通过后才允许 K3。

## Drive registration

```text
folder: 1xY09ZvrjX14M09LEuVqVzBCgCi6ctc8b
review_script: 108o5a-qlrfZiIgtaLbPx-aHrHU89h7zt
review_sheet: 1eO2sbirdqlhk-5StZ_HGnVmx-4AsgyHk
hand_brush_compare: 1dV6pBj614henK8JOCRYAbzRcRgEvz0eL
tip_8x: 1N-_wX8PRJmbVbrbf6P51i8jDTUTAW9uY
patch_compare: 1ZEhSd22njvSmCOX3Z-87iR-fZJOtgiol
linear_blend_proxy: 1dX-o3bbWb8mwlLLfgA1xvF-9XUspHcHN
flow_error_heatmap: 1N_Niwmnv4MRFZLhS0_VtUUk0MkOAGR3t
changed_pixel_mask: 1fEVK51nL3soev3aVlswCuL9qQnKpTMDZ
diff_map: 1hc3tS8xBBLeS1hnqaXl5K1kLRMZ-_y3W
mechanical_receipt: 1XyF1XX9tnJn8qarTngX9dyvqHY5Ou9NV
review_report: 1qBJKeHGjIhxP7ual7LgZ6dhpwk1n7BUC
review_evidence_json: 19I51wZwbGDYDm-X1-lcV-cgDNb0xw7Zs
checksums: 1reqJov_AgrDPv5p-l_uaAO1JSmp9URAB
evidence_package: 1E4-W2aaJej19YLsy0a07xvy1R7ER2bnO
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
