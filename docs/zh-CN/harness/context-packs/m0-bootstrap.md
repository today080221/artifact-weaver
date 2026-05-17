# 上下文包：M0 Bootstrap

## 目标

创建初始 Python-only ArtifactWeaver 仓库、CLI、渲染清单契约、HTML 报告渲染器、双语文档和执行护栏体系。

## 允许修改的路径

- `LICENSE`
- `NOTICE`
- `README.md`
- `README.zh-CN.md`
- `HARNESS.md`
- `HARNESS.zh-CN.md`
- `CONTRIBUTING.md`
- `CONTRIBUTING.zh-CN.md`
- `pyproject.toml`
- `.gitignore`
- `.gitattributes`
- `.githooks/**`
- `.github/**`
- `src/artifact_weaver/**`
- `schemas/**`
- `examples/**`
- `docs/**`
- `tools/**`

## 禁止路径和数据

- 任何私有下游仓库路径。
- 任何 Unity 项目路径。
- 任何真实截图路径。
- 任何真实 QA 报告路径。
- 任何公司路径。
- 任何本仓库之外的文件。
- Steam AppID 或 DepotID 的真实值。
- Jenkins 内网地址。
- 真实技能 ID 或羁绊 ID。

## 验证

交接前运行 `python tools/validate_repo.py` 和最终 M0 命令列表。
