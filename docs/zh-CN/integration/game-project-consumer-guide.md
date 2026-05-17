# 游戏项目接入指南

私有游戏项目可以在已经生成渲染清单、Markdown 叙述、报告 JSON 和证据资产 JSON 之后调用 ArtifactWeaver。

对私有 Unity 游戏项目来说，Unity、Jenkins、Codex、QA 逻辑、视频录制和项目专用适配器都留在 ArtifactWeaver 之外。ArtifactWeaver 不运行游戏、不判断玩法、不发现报告、不上传文件，也不调用外部服务。

请把游戏项目专用适配器放在私有下游仓库中。这个开源仓库只能包含使用假数据的通用示例。
