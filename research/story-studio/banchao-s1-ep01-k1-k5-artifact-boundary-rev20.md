# EP01 K1–K5：Prompt 与视觉资产边界修订（Revision 20）

- `task_identifier`: `TASK — Story Studio — 班超 S1 FINAL GATE`
- `execution_unit`: `EP01_WRITING_SYSTEM_K1_K5_PROMPT_AND_ARTIFACT_CONTRACT_REFINEMENT`
- `performed_at_utc`: `2026-08-27T06:12:18Z`
- `classification`: `FAIL_IMPLEMENTATION_OUTPUT_ROUTING` + `BOUNDED_WORK_ORDER_CLARIFICATION`
- `architecture_change_required`: `false`

## 结论

本轮不生成 K1–K5，不生成项目状态卡片，不修改 194 张 Canon 分镜。

此前出现的卡片式、仪表盘式图片属于错误输出类型，原因是执行层没有严格区分：

```text
Prompt / Contract / Evidence（文字控制与工程记录）
≠
Production Motion Anchor（干净单帧视觉资产）
≠
Review Contact Sheet（审查派生物）
```

处理方式是局部完善当前 Work Order 与 Prompt Package，不修改 Story Studio 顶层架构。

## 唯一正确的产物分层

| 层 | 产物 | 用途 | 是否进入画面 |
|---|---|---|---|
| 1 | `canonical_storyboard_reference` | 人物、场景、构图、叙事参考 | 原图本身是画面，但不改写 |
| 2 | `K1-K5 Prompt Package` | 控制生图模型 | 否 |
| 3 | `K1.png`–`K5.png` | 视频动作物理状态锚点 | 是；每张只包含场景 |
| 4 | Contact Sheet | 人工审核 | 仅审查，不作为正式模型输入 |
| 5 | Evidence / Manifest / Status | file ID、SHA、PASS/FAIL、同步状态 | 否 |

## Prompt 应承载的更新

只把会改变画面的约束写入 Prompt：

```text
人物身份、年龄、服装
场景、机位、光线、构图
Hero Brush 构造
Writing Surface 与低对比非语义墨迹
K1–K5 手部、笔锋、接触、释放和视线状态
BRUSH_LAYDOWN_ZONE
负面视觉约束
```

以下内容只能进入 Evidence、Manifest、Status 或 Task Record：

```text
status_revision / task_revision
Drive file ID / GitHub commit / SHA-256
PASS / FAIL / next_action
表格、箭头、流程图和执行时间
```

## 关键执行约束

1. 每次生成只处理一个 Anchor，禁止“一张图展示 K1–K5”。
2. 模型输入使用 mapping 中的独立 Canon 单帧，不把带标签的联系图直接喂给模型。
3. K1 先通过身份、场景、毛笔和画面洁净度审核，再生成 K2–K5。
4. K2–K5 只允许动作状态变化；人物、服装、镜头、场景、道具与光线保持不变。
5. `BRUSH_LAYDOWN_ZONE` 是现有书案的干燥裸木区域，不增加独立笔搁。
6. 五张原生 PNG 完成后，才确定性生成 Contact Sheet 和 Evidence JSON。
7. 卡片、报告、文字说明、标签、边框、Prompt、状态信息出现在图片内，直接判定 `FAIL_IMPLEMENTATION`。

## 资产状态

```text
K1–K5 native anchors: NOT_STARTED
contact sheet: NOT_STARTED
evidence JSON: NOT_STARTED
canonical: 194 unchanged
production_ready: 0 unchanged
mapping revision: 10 unchanged
manifest revision: 10 unchanged
```

## Next action

```text
EP01_WRITING_SYSTEM_K1_K5_STATIC_ANCHOR_GENERATION
```
