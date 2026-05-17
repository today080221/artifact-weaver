# 验证

主要验证命令：

```bash
python tools/validate_repo.py
```

验证脚本会编译 Python 文件、检查 CLI 帮助、渲染假数据示例、确认生成输出、检查双语文档、运行私有数据护栏、检查 `dist/` 没有被 Git 跟踪、确认 Git hook 文件具备可执行权限、检查 Markdown 链接安全回归，并通过 `git diff --check` 和 `git diff --cached --check` 同时检查工作区与暂存区的空白字符问题。

M0 的 Markdown 链接只允许安全相对路径和页面内锚点。`javascript:`、`data:`、`file:`、`http:`、`https:`、`mailto:` 以及其他带 URI scheme 的形式都不能渲染成 HTML 链接。

脚本会为子进程 CLI 检查设置 `PYTHONPATH=src`，因此在尚未执行可编辑安装的新检出仓库中，预提交钩子也可以使用。
