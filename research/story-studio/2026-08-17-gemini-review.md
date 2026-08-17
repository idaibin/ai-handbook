# Gemini AI Review：Story Studio 10 案例与 60 秒流程

- Provider: Google Antigravity CLI
- Model: `gemini-3.7-flash-high`
- Session: `a382cd7c-4a22-410a-b9b7-de531161826b`
- Basis: ai-handbook `5d9153459ab4f895a0d4cee37dd6d6327b879af4` + fixed GitHub case matrix
- Terminal: `review_complete`
- Verdict: `revise`

## Review 已确认的可保留模式

- StoryDiffusion：多 prompt、参考图和一致性门禁；实际人物/角度漂移仍需 Pilot 证据。
- ComfyUI：可序列化 graph 和 I2V/音频 blueprints；custom node、checkpoint、CUDA 和许可证不能进入核心合同。
- Remotion：程序化时间线、字幕/overlay 和批量渲染；商业许可证与渲染资源需单独核验。
- FFmpeg：ffprobe、容器/流/时长/音频响度验证；不能替代语义画面 Review。
- Whisper + WhisperX：ASR 与 forced alignment 必须分开；原始 Whisper segment timestamp 不能直接作为最终字幕。
- Audacity：A1 dialogue/voice、A2 BGM、A3 SFX 多轨结构；自动化门禁应由 CLI/FFmpeg 完成。

## Review 要求的收敛

1. Blender 从 2D/2.5D 60 秒 Pilot 核心路径移除，仅保留为邻近案例。
2. Coqui TTS 不作为生产锚点；Voice adapter 必须 provider-neutral，并先满足 voice consent、商业权利和有效模型记录。
3. ComfyUI custom node 只属于 worker 内部；核心合同只接受 prompt/reference 输入和 PNG/MP4/hash/probe 输出。
4. 保留 rights、keyframe consistency、motion continuity、audio loudness/sync、forced alignment、master ffprobe/playback、publication readback 门禁。
5. 9 个角色可以由小团队或 agent personas 承担，但生成者与独立 reviewer 的职责不能合并。

## 未验证边界

- 第三方仓库没有在当前环境安装或运行；`verified-external` 仅表示固定版本源码/README/示例路径支持该工具用途。
- 没有生成图片、视频、语音、BGM、字幕或 master。
- 没有执行外部平台发布、账户授权、成本结算或受众指标回读。

这份 Review 是外部意见与收敛证据，不是产品验收或生产批准。
