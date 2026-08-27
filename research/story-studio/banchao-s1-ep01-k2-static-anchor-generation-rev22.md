# 班超 S1 — EP01 K2 静态动作锚点生成报告（Revision 22）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `execution_unit`: `EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_GENERATION`
- `result`: `K2_CANDIDATE_GENERATED_PENDING_REVIEW`
- `canonical`: `194`（不变）
- `production_ready`: `0`（不变）

## 结论

已生成一张独立、干净的 K2 候选：

```text
EP01-K2-TIP-OFF-SURFACE.png
1920×1080 / RGB PNG
SHA-256: f1a6f98b14ae62c0c81a4792f10f5d9ce6500960504a198b52860dd48186a7e6
rights_status: internal_candidate_only
production_ready: false
```

本单元只完成生成与机械门禁，不代替独立 K2 Review；K3 尚未授权。

## 生成路径

三次图像编辑调用均错误路由成 dashboard/report 图，未登记为项目资产。Adobe Firefly 编辑初始化返回 HTTP 403。为避免继续无效重试，本轮采用可复现的确定性局部源图编辑：

- 来源：K1 `EP01-K1-NORMAL-WRITING.png`；
- 保持人物、服装、脸、发型、机位、裁切、书案、纸面、背景、窗光和道具不变；
- 仅在下部笔锋/纸面接触区执行局部处理；
- 清除原接触像素并将现有渐尖笔锋像素上移 10 px；
- 改动边界：`[1015, 825, 1038, 871]`；
- 改动像素：`677`；
- 脚本重跑输出字节完全一致。

## 生成门禁

```text
native spec: PASS_1920X1080_RGB_PNG
single clean frame: PASS
tip visibly clear of surface: PASS_VISUAL_BOUNDED
brush remains near vertical: PASS
paper movement: PASS_NONE
new mark: PASS_NONE
identity/costume/set/camera/lighting outside local bbox: PASS_PIXEL_IDENTICAL
watermark/text added: PASS_NONE
full K2 review: NOT_EXECUTED
K3 authorized: false
```

## 适用边界

这是一张 `production_motion_anchor_internal_candidate_pending_review`，不是 Canon 分镜替换，也不是 Production Ready 资产。完整手腕动作、Hero Brush 几何连续性和局部修复自然度仍由下一单元独立审核。

## 下一动作

```text
EP01_WRITING_SYSTEM_K2_STATIC_ANCHOR_REVIEW
```

## Drive registration

```text
folder: 1pJHzbZTDCJBKcJ3GdvBxRoPAWg736sep
k2_png: 1-1A3NoYCCmY0kUat9jGIDbUzLTiCPxJZ
report: 1xIBtEurtE5PuKQWkpLyaFeZLcmmmrBg2
receipt: 1PDn4yepB0bwVQk6trfFoW3AmYDpeIxVJ
evidence_json: 18JbOsegLE_BoRkF1APQU6QFlQ1WiiN1L
script: 11u0p3olhOSP-zydNnk3QcOM5KfK0L_MC
full_review: 1wcSD3nReI2J9N4bwOgsD-E86d0nuxn13
tip_review: 1Wa9H-TBYorsrZHTWdf5QGrXhgrSpyUdm
checksums: 1W3ajUU4b4EHeIGwmRS0n73UFXSKt_L7G
package: 1IvWidXg-BWyjsPqxs5y53CxtuimnrzIz
```
