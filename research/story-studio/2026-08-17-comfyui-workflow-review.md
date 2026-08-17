# Story Studio — ComfyUI 开源工作流验证

- task: `story-studio-comfyui-20260817`
- session: `01a01042-2114-7340-a3ba-2336202037ac`
- fixed basis observed by the worker: `ai-handbook/main@0ce25345c3cfdcd5dc7ded02b95224765426d234`
- local runtime: `/Users/daibin/Codex/.codex/comfyui-runtime/story-studio-20260817`
- ComfyUI: `0d80858061b511bd38c8cef4c235ef8e01040822`
- Python: `3.14.6`; torch: `2.13.0`
- host: Mac Studio M2 Ultra, 64 GB unified memory, arm64; MPS available, CUDA unavailable
- execution boundary: no `main.py`/Web UI; low-resolution in-process backend dry-run only
- current result: `partial`

完整原始证据保存在本地任务包：
`/Users/daibin/Codex/.codex/reviews/story-studio-comfyui-20260817/`，其中包括
`result.md`、`verification.md`、`events.jsonl`、原始 JSON、日志和校验脚本。

## Candidate source matrix

| # | 来源 | 类型/用途 | 原始 JSON | 状态 | 主要限制 |
|---:|---|---|---|---|---|
| 1 | [ComfyUI Wan2.1 I2V example](https://comfyanonymous.github.io/ComfyUI_examples/wan/image_to_video_wan_example.json) | 官方原生 I2V | `63a7e71041289d4a7ab92aa6326f4b10f36fb2eca5d4817ff55ac9624feed631` | 下载、结构解析、核心节点注册；执行未通过 | 模型目录为空、输入图缺失、UI→API 参数转换不匹配 |
| 2 | [Kijai WanVideoWrapper I2V](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_1_14B_I2V_example_03.json) | Wan2.1 wrapper I2V | `e9da590389b56825ba61533aa5be3f21d27572328b054384d5fbe4dc775df946` | 下载；headless custom-node 导入失败 | `PromptServer.instance` 依赖，模型/显存未验证 |
| 3 | [Kijai Phantom subject2vid](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_2_1_14B_phantom_subject2vid_example_02.json) | 参考主体视频 | `0757666a6486579b753bc25870c1b7fd324a8ec965fe2dbf906459625be25150` | 下载；依赖节点缺失 | Phantom 权重与 wrapper 运行未验证 |
| 4 | [Comfy-Org Wan2.2 blueprint](https://github.com/Comfy-Org/ComfyUI/blob/master/blueprints/Image%20to%20Video%20%28Wan%202.2%29.json) | 官方 blueprint | `622eb56473d7c21dc0e6ffae0b34b7ce0d941cc28b6a516868ebab7092050029` | 下载；一节点 subgraph，不是 API graph | 高显存/模型依赖未验证 |
| 5 | [Jeff-Emmett Wan2.2 LX2V](https://github.com/Jeff-Emmett/ComfyUI_Workflows/blob/main/video_wan2_2_14B_i2v_lx2v.json) | Wan2.2 I2V/GGUF | `60194e173e95cea124ed36f191d56d3b130bb91dce86ff2fa3424f97eb5da998` | 下载；未选作首轮执行 | 可选 Ollama/custom nodes、模型许可未验证 |
| 6 | [ComfyUI Wan FLF2V docs](https://docs.comfy.org/tutorials/video/wan/wan-flf) | 首尾帧邻近案例 | N/A | 页面/教程可核对；原始 JSON 未独立下载 | 不能作为本轮可复现 JSON |
| 7 | [OpenArt Wan2.2 14B I2V](https://openart.ai/workflows/rocky533/wan-22-14b-image-to-video-fixed/UKQ9BmQs8XVqOHbzDYrm) | 社区工作流 | N/A | 页面存在、Download 控件可见；原始 JSON 未取回 | 作者/模型许可、依赖和 JSON hash 未验证 |
| 8 | [Civitai Wan2.1 GGUF 4GB](https://civitai.work/models/1309674/wan21gguf-only-4gb-vram-comfyui-workflow?modelVersionId=1480645) | 低显存邻近案例 | N/A | 页面可见；JSON/下载未验证 | 4GB 宣称未在本机验证，许可需单独核对 |
| 9 | [Liblib Wan2.1 V3](https://www.liblib.art/modelinfo/7a8e24ec7619494381099900fb2b27c2?from=feed) | 中文社区工作流 | N/A | 页面/版本文字可见；原始 JSON 未取回 | 节点、模型、硬件和许可未验证 |
| 10 | [Kijai WanMove/Stand-In examples](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows) | 参考/动作控制邻近案例 | N/A | 原始目录可下载；未选首轮 | 依赖模型与显存未验证 |
| 11 | Kijai HuMo/FantasyPortrait/FantasyTalking examples | 头像/音频邻近案例 | N/A | 原始目录可下载；未选首轮 | 音频/人脸节点和模型条款未验证 |
| 12 | [JimPresting Wan2.1Setup](https://github.com/JimPresting/Wan2.1Setup) | 安装/Colab 邻近案例 | N/A | 可参考安装路径；无独立 JSON | A100/显存描述不是本机证据 |

其中只有前 5 个原始 JSON 在本地任务包中有独立 SHA-256；OpenArt、Civitai、
Liblib 的页面证据不被升级为“可复现 JSON”。

## Headless validation

- 官方 Wan2.1：14 个 prompt 节点、全部核心 class type 注册；进入
  `prompt_outputs_failed_validation`，原因是模型列表为空、示例输入缺失，且
  转换后的 KSampler widget 顺序/类型不匹配。证明了核心图可加载，不证明可生成。
- Kijai I2V/Phantom：安装 wrapper 后尝试注册；无服务上下文导入在
  `latent_preview.py` 读取 `PromptServer.instance` 时失败，依赖节点未注册。
- 初始 14B/类 wrapper 候选的 HTTP `/prompt`、`/history` 和输出读取仍为
  `Not verified`；本次不启动 Web UI。

## Follow-up: official Wan2.1 Fun InP 1.3B dry-run

- Original template: `official-wan21-fun-inp-1.3b.json`, SHA-256
  `fcaa86b3cd82e7a0bb808949f8a1756fc2d3525a8e71f26f80651c4373c16579`.
- API-format validation copy: `official-wan21-fun-inp-1.3b-api.json`, SHA-256
  `0cbb0a3fed1be4d9d3489b21d576c57056f55d58c23979448d89b22900bef943`.
- Official model source: `Comfy-Org/Wan_2.1_ComfyUI_repackaged`, Apache-2.0
  model-card label; four exact 1.3B Fun InP weights were downloaded and hashed,
  total expected bytes `11,382,899,603`; no 14B weight was downloaded.
- Input: ChatGPT AI Design SHOT_02 candidate, center-cropped/resized to 320×512;
  adapted input SHA-256 `197fa637bc00cb7b2e1878e496c98b76ba557bd4ae55efaddb69d1a574d00935`.
  The same frame was used as start/end only as a dry-run fixture.
- Backend: in-process `PromptQueue.put`/`get`, `validate_prompt=true`, 2 steps,
  320×512, 9 frames, 16 fps; `history` returned success and output file.
- Output: `shot02-fun-inp-dry-run_00001_.mp4`, H.264 High, yuv420p, 320×512,
  0.5625 seconds, 9 frames; SHA-256
  `ae9f39311dbf60b34ce159464ce65fa1dedf7755a7f06be940be4412f169d788`.
- This proves a bounded backend dry-run only. It does not prove 1080×1920,
  production duration, motion continuity, rights, final keyframe approval or
  publication readiness. HTTP `/history` was intentionally not used because no
  server/Web UI was started.

## Story Studio adapter contract

```yaml
provider: comfyui
workflow_ref: immutable_json_sha256
model_ref: provider/model/version
input:
  keyframe_path: approved_chatgpt_ai_design_png
  keyframe_sha256: required
  prompt: production/08-video-motion-prompts.yaml shot motion
  negative_prompt: global_motion_negative
  width: 1080
  height: 1920
  duration_seconds: shot duration
  fps: provider-declared
output:
  media_path: local artifact
  media_sha256: required
  container: mp4-or-declared
  dimensions: required
  fps: required
  codec: required
  probe: ffprobe record
```

当前 SHOT_02 候选图为 941×1672，而 Story Studio 图像合同为 1080×1920；
resize/letterbox 尚未验证。没有模型权重、服务队列或视频输出，不能宣称
Wan/Phantom/ComfyUI 已完成视频生成。

## Next minimum action

低分辨率 dry-run 已完成。下一步是单独授权的生产尺寸/更长 SHOT_02 尝试，
并先关闭权利与连续性 Review；当前仍不得把该片段写成生产视频或最终门禁通过。
