# Story Studio MVP — 班超《投笔》10 秒视频验证

- `mvp_id`: `story-studio/banchao/toubi-10s-v0.2`
- `status`: `ready_for_real_video_generation`
- `supersedes`: `story-studio/banchao/toubi-30s-v0.2`
- `scope`: Story Studio only; Forgeway and Skills remain frozen

## Smallest Result

使用已有班超与洛阳抄书空间参考，只生成一段严格 10 秒的视频，验证“停笔—抬眼—决断”。输入缩减为 `EP01_SHOT_08`—`EP01_SHOT_10`。

## Acceptance

- 一个真实视频模型生成的 10 秒 MP4；
- 班超身份、服装和场景无明显漂移；
- 完成停笔、抬眼、放下毛笔三个连续动作；
- 不出现现代物品、军装、兵器、乱码或额外人物；
- 用户作出 `keep / change / stop` 决策。

最多生成 3 次。仍失败则停止增加资产和镜头，记录问题并更换模型。

## Current Evidence

- [10 秒分镜时序代理](https://drive.google.com/file/d/1VDLeFcj671TyRuGrm6sp0Xki45Cota8M/view)
- [MVP Brief](https://drive.google.com/file/d/1TBsWkH3ArwheSvjo0PW_r7vwczFK7X1a/view)
- [技术证据](https://drive.google.com/file/d/19EFmYc6ebkaMsG1VStGRK2rjTUmswnrn/view)

分镜时序代理规格：H.264，1920×1080，24fps，10.000 秒；SHA-256 `b9c17ce3db13bb932b439f8f49b4ae877a1c1dd2066f8c9e24343912683c569a`。它只用于视频模型输入和节奏参考，不是已生成的真实视频。

## Archived Result

原 30 秒文件降级为历史分镜预览，不再是 MVP，也不构成 production-ready 证据。

## Excluded

不做 30 秒成片、不做配音字幕、不补齐 G07 十单元、不扩展 EP01 或 24 集。
