# Story Studio AI 漫剧流程：GitHub 成熟案例核实矩阵

- 观察时间：2026-08-17 Asia/Shanghai
- 搜索范围：公开 GitHub repositories；按功能关键词、stars、默认分支和官方源码/README 复核
- 证据级别：`source-resolved`（固定 commit 的仓库元数据、README、源码/示例路径）；未运行第三方项目
- 目的：为 Story Studio 60 秒 Pilot 选择可借鉴的生产边界，不把仓库热度、论文结果或 README 宣传当成可用生产证据
- 排除：Product UI 权威、Forgeway 产品实现、未授权平台 API、无法固定来源的短视频教程

## 10 个固定案例

| # | Repository / fixed commit | stars（观察值） | 覆盖环节 | 可借鉴模式 | 不能直接推出 |
|---:|---|---:|---|---|---|
| 1 | [HVision-NKU/StoryDiffusion@8de45e4](https://github.com/HVision-NKU/StoryDiffusion/tree/8de45e424887766fdd84dc917436ff8605f00149) | 6,446 | 角色/场景一致性、长序列图片和视频 | README 明确要求多条文本 prompt，并以 consistent self-attention 维持长序列一致性；仓库含 Comic Generation notebook 与 examples | 不证明角色一致性在本 Pilot 上已通过；模型、显存、许可和结果质量仍需实跑 |
| 2 | [smthemex/ComfyUI_StoryDiffusion@c228e19](https://github.com/smthemex/ComfyUI_StoryDiffusion/tree/c228e19289e8ddeab0fa07b72c3eb52d7ce96d0d) | 514 | StoryDiffusion 的 ComfyUI 集成、身份迁移 | `README.md` 和 `InstantCharacter/infer_demo.py` 显示将多个身份/一致性方法接入节点工作流 | 不把第三方 custom node 当核心合同；依赖和模型兼容性需逐个验证 |
| 3 | [Comfy-Org/ComfyUI@0d80858](https://github.com/Comfy-Org/ComfyUI/tree/0d80858061b511bd38c8cef4c235ef8e01040822) | 128,024 | 图片、图生视频、音频节点、可复现图工作流 | 固定 workflow graph；README/blueprints 提供 Image-to-Video、Merge Videos、Audio Generation 等示例 | workflow graph 不等于最终视频质量；GPL 及各模型许可必须分开核查 |
| 4 | [remotion-dev/remotion@e55e72](https://github.com/remotion-dev/remotion/tree/e55e72187be86904e239a2517e201e70bdf84d88) | 56,561 | 脚本化镜头、时间线、批量渲染 | README 以 React code 为 source of truth，支持 data-driven composition、batch rendering 和可编程视频 | 不是剧本/角色一致性系统；许可和商业使用条件不能从 stars 推断 |
| 5 | [blender/blender@9054b90](https://github.com/blender/blender/tree/9054b90d706ceb719e3b4c2de10af82524773340) | 19,740 | 场景、镜头、动画、渲染、合成和视频编辑 | 官方 README 明确覆盖 modeling、rigging、animation、rendering、compositing、motion tracking、video editing；API examples 可作为镜头术语参考 | Gemini Review 判定对 2D/2.5D 60 秒 Pilot 过重；保留为邻近案例，不进入核心执行路径 |
| 6 | [FFmpeg/FFmpeg@426841d](https://github.com/FFmpeg/FFmpeg/tree/426841da9d9167781007e4238583a7c0da5f04c4) | 63,371 | 视频/音频/字幕合成、转码、探针 | README 明确提供 ffmpeg、ffplay、ffprobe；`doc/examples/` 包含 encode/decode/mux/transcode 与 audio/video examples | 不提供剧情、角色或审美判断；编解码成功不等于可发布质量 |
| 7 | [openai/whisper@5f86d1d](https://github.com/openai/whisper/tree/5f86d1d86363843179951550570367b37c5d6f78) | 107,423 | 语音转写、语言识别、初始字幕文本 | README、model card、Colab example 和 `whisper/audio.py` 提供多语言 ASR 入口 | 分段转写不是最终字幕打轴；词级时间、说话人和版式需额外验证 |
| 8 | [m-bain/whisperX@2cfd7b7](https://github.com/m-bain/whisperX/tree/2cfd7b7c5c7bba144954364db747319b50e8232b) | 23,606 | 词级时间戳、forced alignment、diarization、字幕处理 | README/`EXAMPLES.md`/`whisperx/SubtitlesProcessor.py` 体现从 ASR 到词级时间和字幕处理的独立阶段 | 对中文、混音、噪声和当前音频 provider 的表现需本地实测；依赖模型许可和对齐模型 |
| 9 | [coqui-ai/TTS@dbf1a08](https://github.com/coqui-ai/TTS/tree/dbf1a08a0d4e47fdad6172e433eeb34bc6b13b4e) | 45,906 | TTS、声音模型、音频处理和 recipes | README、`docs/source/inference.md`、`TTS/demos/`、`recipes/` 与 TTS tests 提供从推理到样例的结构 | 默认分支为 `dev`；voice cloning、模型和声音授权必须逐项确认，不能复制具体 voice ID |
| 10 | [audacity/audacity@2f42f1c](https://github.com/audacity/audacity/tree/2f42f1c968ad15b5ab871f3bdf56249bd311a84e) | 17,584 | 多轨音频、剪辑、录音与质量检查 | README 定义跨平台 multi-track audio editor/recorder，源码含 audio graph、playback 和单元测试工作流 | 不是 TTS 或 AI 配音系统；Audacity 4 `master` 正在结构变化，不能把开发分支当稳定运行时 |

## 按流程阶段的证据结论

| Story Studio 阶段 | GitHub 证据 | 当前结论 |
|---|---|---|
| Idea / audience / genre / hook | 没有一个成熟仓库能证明创意质量或受众留存 | 由 Story Studio 自己的 brief + Gemini/Grok Review 收敛；结果仍需人工裁决 |
| World Bible / Character Bible | StoryDiffusion、ComfyUI StoryDiffusion | 角色/场景参考、hash、seed/adapter 参数和多图一致性 Review 必须先于视频 |
| Episode plan / Script | 没有选出的成熟仓库能直接证明短剧剧本质量 | 保留 60 秒结构、对白字数、可视化动作和 cliffhanger 门禁；写作质量不由工具 README 证明 |
| Shot List / Storyboard | Remotion、ComfyUI graph 提供镜头/时间线/节点组织参考；Blender 仅作邻近术语参考 | Storyboard 必须成为独立 Artifact；每个 shot 必须有 duration、camera、action、emotion、image/video prompt |
| Keyframe Image | StoryDiffusion、ComfyUI、ComfyUI StoryDiffusion | image attempt、reference hash、dimensions、negative prompt、consistency review 必须留痕 |
| Image-to-Video | ComfyUI blueprints、StoryDiffusion；Remotion/FFmpeg 做后续编排 | 先用已审 keyframe，再写 motion prompt；输出必须有 clip hash、codec、duration、frame probe |
| Voice / Narrator / BGM / SFX | Coqui TTS、Audacity、FFmpeg | provider-neutral adapter；先 rights/voice consent，再生成、混音、loudness/peak probe |
| Subtitle | Whisper、WhisperX | ASR 与 forced alignment 分开；字幕需 SRT/JSON、词级时间、阅读速度、安全区和人工文本 Review |
| Edit / Master | FFmpeg、Remotion、Audacity；Blender 不进入 2D Pilot 核心路径 | timeline、master hash、ffprobe、contact sheet、全片播放和音画同步是发布门禁 |
| Distribution / Feedback | 10 个案例没有共同的可靠平台发布 owner | 只定义 publication receipt、target readback、成本和反馈接口；不伪报已发布或有留存数据 |

## 借鉴后的最小生产链

```text
Story Brief + Source/Rights
  ↓
World/Character Bible
  ↓
Episode Plan + 60s Script
  ↓
Shot List + Storyboard
  ↓
Approved Keyframes + Hash/Probe
  ↓
Image-to-Video Clips + Hash/Probe
  ↓
Voice/Narration + BGM/SFX + Loudness
  ↓
Whisper/WhisperX Subtitle Draft + Human Text Review
  ↓
Timeline + FFmpeg/Remotion Render
  ↓
Master Hash + ffprobe + Full Playback
  ↓
Named Target Publication + Readback + Feedback
```

## 不直接引入的内容

- 不把任何一个仓库的 UI、节点图、模型 checkpoint、provider 或许可证当作 Story Studio 核心产品合同。
- 不把论文/README 的 demo 截图当作角色连续性、口型、音画同步或平台发布证据。
- 不把 ComfyUI/Remotion/FFmpeg/Whisper 等工具直接晋级为 Skill；必须先有真实 Pilot consumer、validator、固定输入和 Review。
- 不为脚本质量、受众留存、平台算法或版权可用性编造成熟度结论。

## 本地验证边界

本研究完成固定版本、源码/README/示例路径核验；10 个第三方项目均未在当前环境安装或运行。下一阶段的每个阶段都必须保留 Gemini Review、Grok Review（若 provider route 可验证）和本地回归证据，并把 `Not verified` 留在阶段结果中。
