# Example QA Report

This fake report demonstrates how ArtifactWeaver renders Markdown and JSON artifacts into a static HTML report.

## Highlights

- The data is synthetic.
- The generated HTML is a view, not the source of truth.
- The built-in Markdown renderer supports a small M0 subset.

## Example Command

```text
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

### Notes

Use private downstream repositories for private artifacts. Keep this open-source example fake.
