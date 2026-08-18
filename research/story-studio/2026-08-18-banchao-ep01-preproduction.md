# 班超 EP01 前置生产状态（公开投影）

- `document_role`: `human_readable_projection`
- `authoritative_state`: `banchao-ep01-current-status.json`
- `authoritative_state_sha256`: `8c7962401a8c927a712a54c4dc27b9c88d28a06c6fe34d1fd1928d1e9efd4ef7`
- `hod_review`: `banchao-ep01-minimum-visual-canon-hod-review-v1.yaml`
- `hod_review_sha256`: `9e12aac52cb454a51e66978c6f989c95ce11b6f3d4484a1c191995c6c909d476`
- `lookdev_revision_work_order`: `banchao-ep01-lookdev-revision-work-order-v1.yaml`
- `lookdev_revision_work_order_sha256`: `2129d863a10c5924beae4c92fe3003ad8b71a4ff7f55b0cc4f979c43a5319df8`
- `as_of_utc`: `2026-08-18T15:40:00Z`

当前阶段、门禁和下一合法动作以唯一状态 JSON 为准。

## 当前结论

```text
P0 visual research: 7/7 closed
P1 visual research: 5 open
HOD Review round 1: revise required
12 assets reviewed: 2 component-select / 5 revise / 5 reject
Full canonical asset approvals: 0
Storyboard / Animatic / Keyframe / Video: blocked or not started
```

## HOD Review 主要发现

- 班超与班母参考图只保留脸部、表演和部分质感方向；完整画面不进入 Canon。
- 四张蓝图的身份结构可作为修订输入，但共同存在花纹衣袍、发饰、鞋履和手持道具过度锁定问题，全部需要 v2。
- 班固参考图与班超过于相似且错误重复佣书动作；无名抄书人参考图过于主角化，两者拒绝。
- 场景参考图使用过多格窗、竹帘、密集书架和“古风书房”陈设，拒绝为布景/空间 Canon，只保留光线和纵深气氛。
- Writing Set 混合竹木简、纸张/卷轴、册页/书本、伪文字和多种容器，拒绝；Hero Brush、Writing Surface、Brush Pouch 必须分别设计。
- Brush Pouch 可保留磨损软包轮廓，但必须删除珠饰/流苏并建立 open/closed/worn 状态。
- Official Desk 因 5 个 P1 考据项仍开放而拒绝并延后。

## 工业电影部门结论

`G05 LookDev & Visual Canon` 当前为 `revise_required`。本轮完成的是 HOD LookDev Review，不是 Canon 批准。后续修订仍需导演、历史研究、美术、摄影、灯光、服装妆发、道具、场记、VFX、剪辑和权利共同复核。

## 下一合法动作

```text
关闭 5 个 P1 flags
→ 将结论写回 LookDev Revision Work Order
→ 分资产生成 v2 LookDev Takes
→ Dailies + HOD Review Round 2
```

在此之前，不裁切单视图，不生成关键帧、视频或最终音频。
