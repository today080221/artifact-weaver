# 快速开始

以可编辑模式安装：

```bash
python -m pip install -e .
```

查看 CLI 帮助：

```bash
python -m artifact_weaver --help
```

渲染假数据示例：

```bash
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

打开 `dist/qa-report/report.html`。

生成的 HTML 不是事实来源。请把 Markdown、JSON 和 `render_manifest.json` 作为源产物维护。
