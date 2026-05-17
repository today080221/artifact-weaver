# Contributing

Thanks for improving ArtifactWeaver. Keep contributions focused on the public rendering contract and avoid private downstream project data.

## Development Setup

```bash
python -m pip install -e .
python tools/validate_repo.py
```

## Rules

- Keep M0 Python-only and stdlib-first.
- Keep examples fake.
- Update English and Simplified Chinese docs together.
- Do not commit generated `dist/` output.
- Do not include Steam AppID or DepotID values.
- Do not include Jenkins internal URLs.
- Do not include actual local or company paths.
- Do not include actual skill IDs or synergy IDs.
- Do not implement private project adapters in this repository.

## Pull Requests

Use the pull request template, link an issue when possible, and include validation results.
