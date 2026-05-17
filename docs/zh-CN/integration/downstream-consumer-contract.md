# 下游消费方契约

私有下游项目负责生成产物。ArtifactWeaver 负责渲染产物。

推荐的产物目录：

```text
artifact-root/
  render_manifest.json
  report.md
  report.json
  linked_evidence.json
  screenshots/
    placeholder-or-real-private-file.png
```

渲染命令：

```bash
python -m artifact_weaver render --manifest artifact-root/render_manifest.json --out artifact-root/html
```

下游项目继续负责收集证据资产、写入 JSON，并决定报告含义。ArtifactWeaver 只接收已经生成好的产物。

不要把私有产物提交到这个仓库。不要写入 Steam AppID 或 DepotID 的真实值。不要放入 Jenkins 内网地址。不要写入真实本地路径或公司路径。不要写入真实技能 ID 或羁绊 ID。
