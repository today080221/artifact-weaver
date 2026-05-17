# Validation

Primary validation command:

```bash
python tools/validate_repo.py
```

The validation script compiles Python files, checks CLI help, renders the fake example, verifies generated output, checks bilingual docs, runs the private-data guard, checks that `dist/` is not tracked, verifies Git hook executable modes, checks Markdown link safety regressions, and checks both working-tree and staged whitespace errors with `git diff --check` and `git diff --cached --check`.

M0 Markdown links only allow safe relative paths and in-page anchors. URI schemes such as `javascript:`, `data:`, `file:`, `http:`, `https:`, `mailto:`, and other scheme forms must not render as HTML links.

M0 rejects backslash path separators instead of normalizing them into forward slashes, so Windows-style traversal such as `..\secret.txt` must not render as a link.

The script sets `PYTHONPATH=src` for subprocess CLI checks so the pre-commit hook remains usable in a fresh checkout before editable install.
