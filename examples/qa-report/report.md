# 私有下游项目 R1 烟测

本报告使用虚构数据验证私有下游项目可以生成 ArtifactWeaver 输入。

## 验证内容

- ArtifactWeaver 可以把 Markdown、JSON 和证据元数据渲染为静态 HTML。
- 生成的 HTML 是视图层，不是事实来源。
- 本示例只覆盖虚构且已脱敏的 R1 烟测数据。

## 示例命令

```text
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

## 边界

- 不包含真实 QA 报告。
- 不包含真实截图。
- 不包含技能 ID、羁绊 ID、公司路径、本机绝对路径或内部 prompt。
- 私有下游项目应在自己的仓库中生成私有 artifacts，再调用 ArtifactWeaver 作为 CLI renderer。
