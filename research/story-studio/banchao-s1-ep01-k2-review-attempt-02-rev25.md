# 班超 S1 — EP01 K2 静态动作锚点独立审核 Attempt 02（Revision 25）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `execution_unit`: `EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REVIEW_ATTEMPT_02`
- `reviewed_at_utc`: `2026-08-27T14:39:08Z`
- `precondition_status_revision`: `24`
- `precondition_task_revision`: `30`

## 结论

```text
K2 Attempt 02:
FAIL_IMPLEMENTATION_REPAIR_REQUIRED

asset disposition:
REJECTED_REVIEW_RETAINED_AS_EVIDENCE

K3:
NOT_AUTHORIZED

canonical:
194 unchanged

production_ready:
0 unchanged
```

审核对象是 K1 与 K2 Attempt 02 的原生关键帧，不是 Prompt。Prompt 与 Motion Contract 只提供验收语义，不能替代像素级结果证据。

## Verified passes

```text
native 1920×1080 RGB PNG: PASS
single clean frame: PASS
face changed pixels: 0
outside changed bbox pixel identity: PASS
hand/wrist region changed pixels: 24856
byte identity of inputs: PASS
```

Attempt 02 已修复 Attempt 01 的“手腕区域完全不动”问题，但只是证明手腕区域发生变化，不证明动作自然。

## Independent review failures

### 1. 笔毫

```text
single soft gathered bristle tip:
FAIL_RIGID_SOLID_WEDGE
```

分叉轮廓基本消除，但当前笔毫仍表现为刚性的实心三角尖锥，缺少柔软毛丝、聚锋和受力后的连续形变。

### 2. 手部与手腕状态

```text
hand/wrist state naturalness:
FAIL_TRANSLATED_PATCH_GHOSTING
```

手、袖口与毛笔被作为局部贴片共同上移。手腕下缘和袖口边界存在重影、拖影及局部涂抹，动作更像图层平移，不是自然的关节抬升。

### 3. 离纸间隙

```text
tip-to-surface air gap:
FAIL_AMBIGUOUS_OR_CONTACT
```

10×最近邻放大中，没有出现清晰、连续、可确认的纸面背景像素带。笔尖仍近似接触纸面，不能作为明确的 K2 终态。

### 4. 局部修补自然度

```text
local patch naturalness:
FAIL_BLUR_SMEAR_EDGE_HALO
```

原接触区和袖口下方出现低频模糊、纹理断裂和边缘光晕。该问题在全画面不显著，但在动作锚点与视频插值输入中会被放大。

### 5. 插值适用性

```text
static interpolation input suitability:
FAIL_RISK_DOUBLE_EDGE_AND_GHOSTING

real video temporal continuity:
NOT_VERIFIED
```

确定性 optical-flow proxy 在手指、袖口、笔杆和笔尖处产生双边缘及拖影。该 proxy 只用于输入风险筛查，不是视频模型结果；当前没有执行真实 Provider 视频生成，因此不能验证真实时间连续性。

Mechanical proxy metrics:

```text
changed_bbox_xyxy: [884, 538, 1057, 900]
changed_pixel_count: 31520
hand_wrist_changed_pixel_count: 24856
face_changed_pixel_count: 0
flow_proxy_residual_mae: 7.1086
flow_proxy_residual_p95: 48.0000
```

## Failure classification

```text
FAIL_IMPLEMENTATION_HAND_BRUSH_LOCAL_TRANSFORM_ARTIFACT
FAIL_IMPLEMENTATION_HERO_BRUSH_GEOMETRY
FAIL_IMPLEMENTATION_TIP_SURFACE_STATE_AMBIGUOUS
FAIL_IMPLEMENTATION_INTERPOLATION_INPUT_RISK

FAIL_CONTRACT: false
FAIL_DEPENDENCY: false
FAIL_ARCHITECTURE: false
```

现有 Prompt 与 Motion Contract 不需要修改。失败属于 Attempt 02 的实现质量。

## Asset disposition

```text
Attempt 02 Drive file: unchanged
status: REJECTED_REVIEW_RETAINED_AS_EVIDENCE
delete: false
silent overwrite: false
canonical mutation: 0
mapping mutation: false
manifest mutation: false
K3 authorized: false
```

## 下一修复单元

```text
EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REPAIR_ATTEMPT_03_FULL_ROI_REGEN
```

Attempt 03 约束：

1. 不再对 Attempt 02 做继续平移或小块像素修补；
2. 从 K1 重新生成/编辑完整的手—手腕—笔杆—笔毫 ROI；
3. 显示真实的轻微腕部抬升与稳定握持点；
4. 只保留一个连续、柔软、聚锋的笔毫；
5. 笔尖与纸面之间必须存在清晰连续的背景带；
6. 无袖口重影、边缘接缝、纸面模糊或克隆纹理；
7. 人物、服装、场景、机位、光线及其他道具保持不变；
8. 通过独立 Review Attempt 03 后才允许 K3。

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
