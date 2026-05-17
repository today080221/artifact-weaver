# Quickstart

Install the package in editable mode:

```bash
python -m pip install -e .
```

Show CLI help:

```bash
python -m artifact_weaver --help
```

Render the fake example:

```bash
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

Open `dist/qa-report/report.html`.

The generated HTML is not source of truth. Keep Markdown, JSON, and `render_manifest.json` as source artifacts.
