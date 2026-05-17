# ArtifactWeaver

ArtifactWeaver 会把 Markdown 和 JSON 产物渲染成静态 HTML 报告，并为未来的幻灯片渲染预留边界。

它是一个 Python 优先的轻量渲染层，适合已经能生成结构化产物、并需要可读、可分享、可归档视图的项目使用。

## 它是什么

- 静态报告渲染器。
- 产物查看器。
- AI/CI 报告展示层。
- 下游消费方契约渲染器。

## 它不是什么

- 不是测试运行器。
- 不是 Unity 框架。
- 不是 QA 判定器。
- 不是飞书连接器。
- 不是 LLM 智能体。
- 不是私有项目适配器。

## 快速开始

```bash
python -m pip install -e .
python -m artifact_weaver --help
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

渲染完成后打开 `dist/qa-report/report.html`。

## 产物理念

Markdown、JSON 和渲染清单是事实来源。HTML 是生成出来的视图层。不要把生成的 HTML 当作源文件维护。

M0 内置 Markdown 渲染器是刻意保持最小化的实现，未来可能替换为兼容 CommonMark 的解析器。

## 下游项目接入

私有下游项目应生成渲染清单，然后调用 ArtifactWeaver 作为渲染器。下游项目自己负责生成产物、证据资产和私有流程数据。

不要把私有项目数据放入这个开源仓库。不要在这里实现 NoTimeToDie 专用适配器。如果未来需要适配器，优先放在私有下游项目仓库中。

## 执行护栏体系

每个执行者都必须遵守 `HARNESS.zh-CN.md` 和任务对应的上下文包。执行护栏体系定义允许修改的路径、范围外内容、验证、文档更新和交接规则。

## 许可证

Apache-2.0。参见 `LICENSE` 和 `NOTICE`。
