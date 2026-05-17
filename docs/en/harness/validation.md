# Validation

Primary validation command:

```bash
python tools/validate_repo.py
```

The validation script compiles Python files, checks CLI help, renders the fake example, verifies generated output, checks bilingual docs, runs the private-data guard, checks that `dist/` is not tracked, and runs `git diff --check`.

The script sets `PYTHONPATH=src` for subprocess CLI checks so the pre-commit hook remains usable in a fresh checkout before editable install.
