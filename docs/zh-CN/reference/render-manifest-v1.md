# 渲染清单 v1

渲染清单 v1 声明源产物和生成的 HTML 输出。

```json
{
  "schemaVersion": "render-manifest/v1",
  "document": {
    "title": "Example QA Report",
    "subtitle": "Fake data demo",
    "generatedAt": "2026-01-01T00:00:00Z",
    "locale": "en"
  },
  "theme": {
    "name": "default",
    "accent": "#7C3AED"
  },
  "sources": {
    "markdown": "report.md",
    "reportJson": "report.json",
    "evidenceJson": "linked_evidence.json"
  },
  "outputs": {
    "html": "report.html"
  },
  "boundaries": {
    "sourceOfTruth": ["report.md", "report.json", "linked_evidence.json", "render_manifest.json"],
    "generatedView": ["report.html"],
    "privateDataPolicy": "fake-data-only"
  }
}
```

所有源路径都必须相对于渲染清单所在目录。绝对路径、盘符路径、UNC 路径、URL、用户主目录展开和路径穿越都会被拒绝。

M0 支持 Markdown、报告 JSON、证据资产 JSON 和单个 HTML 输出。YAML、幻灯片、PDF、主题包、外部资产下载和 JavaScript 打包都是未来工作。
