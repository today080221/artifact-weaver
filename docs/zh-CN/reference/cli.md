# CLI 参考

## 帮助

```bash
python -m artifact_weaver --help
artifact-weaver --help
```

## 渲染

```bash
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

参数：

- `--manifest`：`render_manifest.json` 的路径。
- `--out`：生成静态 HTML 的输出目录。
- `--strict`：可选的更严格 M0 校验。

M0 不运行测试、不调用 LLM、不启动 Unity、不扫描磁盘、不调用 GitHub、不调用飞书，也不上传文件。
