# Render Manifest v1

Render Manifest v1 declares the source artifacts and generated HTML output.

```json
{
  "schemaVersion": "render-manifest/v1",
  "document": {
    "title": "Example QA Report",
    "subtitle": "Fake data demo",
    "generatedAt": "2026-01-01T00:00:00Z",
    "locale": "en"
  },
  "theme": {
    "name": "default",
    "accent": "#7C3AED"
  },
  "sources": {
    "markdown": "report.md",
    "reportJson": "report.json",
    "evidenceJson": "linked_evidence.json"
  },
  "outputs": {
    "html": "report.html"
  },
  "boundaries": {
    "sourceOfTruth": ["report.md", "report.json", "linked_evidence.json", "render_manifest.json"],
    "generatedView": ["report.html"],
    "privateDataPolicy": "fake-data-only"
  }
}
```

All source paths must be relative to the manifest directory. Absolute paths, drive-letter paths, UNC paths, URLs, home-directory expansion, and path traversal are rejected.

M0 supports Markdown, report JSON, evidence JSON, and one HTML output. YAML, slides, PDF, theme packages, external asset downloads, and JavaScript bundling are future work.
