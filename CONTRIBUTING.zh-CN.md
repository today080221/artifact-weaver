# 贡献指南

感谢你改进 ArtifactWeaver。贡献内容应聚焦公开的渲染契约，不要包含私有下游项目数据。

## 开发准备

```bash
python -m pip install -e .
python tools/validate_repo.py
```

## 规则

- M0 保持 Python-only，并优先使用标准库。
- 示例只能使用假数据。
- 英文和简体中文文档要同步更新。
- 不要提交生成的 `dist/` 输出。
- 不要写入 Steam AppID 或 DepotID 的真实值。
- 不要放入 Jenkins 内网地址。
- 不要写入真实本地路径或公司路径。
- 不要写入真实技能 ID 或羁绊 ID。
- 不要在这个仓库中实现私有项目适配器。

## 拉取请求

请使用拉取请求模板，尽量关联 issue，并附上验证结果。
