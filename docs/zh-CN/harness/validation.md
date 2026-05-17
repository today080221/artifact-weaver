# 验证

主要验证命令：

```bash
python tools/validate_repo.py
```

验证脚本会编译 Python 文件、检查 CLI 帮助、渲染假数据示例、确认生成输出、检查双语文档、运行私有数据护栏、检查 `dist/` 没有被 Git 跟踪，并运行 `git diff --check`。

脚本会为子进程 CLI 检查设置 `PYTHONPATH=src`，因此在尚未执行可编辑安装的新检出仓库中，预提交钩子也可以使用。
