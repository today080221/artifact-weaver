# CLI Reference

## Help

```bash
python -m artifact_weaver --help
artifact-weaver --help
```

## Render

```bash
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

Arguments:

- `--manifest`: path to `render_manifest.json`.
- `--out`: output directory for generated static HTML.
- `--strict`: optional stricter M0 validation.

M0 does not run tests, call LLMs, start Unity, scan disks, call GitHub, call Feishu, or upload files.
