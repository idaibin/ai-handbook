# 班超：历史人物传记型 AI 漫剧生产路线 v1

状态：`declared_route_ready_ep01_script_validated`

项目：`banchao`  
产品路线：`media-production-system`  
定位：以历史人物和重大事件为主线的连续剧情漫剧，同时提供可信的知识解释。

## 1. 内容产品定义

主产品不是泛国学课堂，也不是单个视觉短片，而是：

```text
戏剧层：目标 → 阻力 → 主动策略 → 转折 → 结尾钩子
知识层：可追溯史料 → Fact / Inference / Adaptation / Fiction 标记 → 可信解释
```

初期格式：竖屏 9:16，单集 60—120 秒，每季 12—24 集。第一阶段只验证《班超》前 3 集，不直接生产完整 24 集：

1. EP01《佣书与投笔》；
2. EP02《第一次出征》；
3. EP03《鄯善危局》。

当前班超全传 Bible 和 24 集处理稿已归档；EP01 剧本使用 v1.1 作为后续输入。

## 2. 工具与职责路由

下表是项目声明的 provider-neutral 分工。它定义“谁负责哪类任务”，不把尚未运行的服务写成完成证据。

| 阶段 | 候选工具 | 职责 | 当前证据状态 |
|---|---|---|---|
| 史料研究 | Gemini Deep Research、Notebook、ChatGPT | 找资料、交叉验证、整理来源 | `declared_not_verified` |
| Story Bible | Codex + Qwen3.8-Max | 人物、世界观、时间线、事实标记 | Codex 本地文本已验证；Qwen 路由 `Not verified` |
| 剧本与分镜 | GPT / Qwen3.8-Max | 剧情结构、镜头拆解 | EP01 剧本 v1.1 已验证；具体 provider `Not verified` |
| 研发与 Agent 辅助 | 阿里 Token Plan（Qwen/DeepSeek/GLM 等候选） | 研究整理、结构化提示词、工具协作；不替代成片 provider | 仅声明路线；套餐、模型路由与合规边界 `Not verified` |
| 角色关键帧 | Google Flow、Nano Banana、Wan2.7 Image | 角色、服装、场景、道具 | 候选接口；未生成本项目关键帧 |
| 核心镜头 | Flow + Veo 3.1 | 高质量情绪镜头、摄影机运动 | 候选接口；未调用/未验证 |
| 批量普通镜头 | Wan2.7、HappyHorse、其他视频 API | 过场、补镜、低成本批量镜头 | 候选接口；未调用/未验证 |
| 配音与音频 | 独立 TTS、录音、音频模型 | 旁白、对白、音效 | provider-neutral；未开始 |
| 后期 | 剪辑工具 | 字幕、节奏、调色、声音 | 工具未选定；未开始 |
| 资产管理 | Codex + GitHub/Drive | 版本、提示词、引用、生成记录 | GitHub/Drive 路由已验证 |

阿里 Token Plan 在本合同中只作为研发/Agent 协作候选，不是 Google Flow/Veo 的替代声明；真正批量媒体生产仍需单独的 provider/API 合同和运行证据。模型可替换字段保持为：`provider`、`model`、`version`、`workflow_ref`、`input_ref`、`output_probe`、`rights_ref`。

## 3. EP01 最小生产链

```text
EP01 剧本 v1.1
  → Shot List
  → Asset Manifest
  → Continuity Contract
  → 3 张关键帧
  → 1 个 5—10 秒视频镜头
  → 运行与质量证据
```

### 当前门禁

| Artifact | 当前状态 | 事实 |
|---|---|---|
| EP01 screenplay | `validated_text_v1.1` | 105 秒，9:16；史料压缩句已标 `[F+A]`，历史基线 v1 保留 |
| Shot List | `not_started` | 需要按剧本建立镜头 ID、时长、景别、机位、动作、情绪、提示词字段 |
| Asset Manifest | `planning_ready` | 已有项目 evidence manifest；关键帧 attempt 记录尚未产生 |
| Continuity Contract | `not_started` | 需要锁定班超青壮期、笔囊、手部墨痕/茧痕、洛阳冷灰土褐色调和待核实考据项 |
| 3 keyframes | `not_started` | 生成 surface、rights、prompt、reference、output hash 尚未闭合 |
| 5—10 秒视频镜头 | `not_started` | 不调用 Flow/Veo/Wan，直到关键帧和 provider 条款门禁通过 |
| runtime/quality evidence | `not_started` | 需要 output SHA-256、媒体探针、连续性 Review、失败闭环 |

## 4. 事实与生成边界

- `[F]`：有明确史料支持；`[I]`：合理推断；`[A]`：改编压缩；`[V]`：虚构/合成人物或对白。
- EP01 “大丈夫当立功异域，安能久事笔砚间”使用 `[F+A]`，不是《后汉书》逐字引文。
- 未经考据关闭的洛阳建筑、服饰、简牍/纸张、笔具、马具、兵器、通事制度，不得在视觉提示词中伪装成确定事实。
- 任何 Flow、Veo、Wan2.7、HappyHorse、TTS 或其他 provider 只能产生候选 attempt；没有运行记录、输出 hash、探针和 Review，不得写成已完成。

## 5. 下一最小动作

进入 EP01 的下一阶段：先生成并审查 `Shot List`，再建立 `Asset Manifest` 和 `Continuity Contract`。本阶段不扩写 EP02，不生成关键帧，不生成视频，不改变现有 Bible。
