# ArtifactWeaver

ArtifactWeaver renders Markdown and JSON artifacts into static HTML reports and future slides.

It is a small, Python-first rendering layer for projects that already produce structured artifacts and need a readable, shareable, archivable view.

## What It Is

- Static report renderer.
- Artifact viewer.
- AI/CI report presentation layer.
- Downstream consumer contract renderer.

## What It Is Not

- Not a test runner.
- Not a Unity framework.
- Not a QA oracle.
- Not a Feishu connector.
- Not an LLM agent.
- Not a private project adapter.

## Quickstart

```bash
python -m pip install -e .
python -m artifact_weaver --help
python -m artifact_weaver render --manifest examples/qa-report/render_manifest.json --out dist/qa-report
```

Open `dist/qa-report/report.html` after rendering.

## Artifact Philosophy

Markdown, JSON, and render manifest files are the source of truth. HTML is a generated view layer. Do not maintain generated HTML as source.

The built-in Markdown renderer is intentionally minimal for M0 and may be replaced by a CommonMark-compatible parser later.

## Localization

ArtifactWeaver reads `document.locale` from `render_manifest.json` when rendering report UI chrome.

- `zh-Hans`, `zh-CN`, `zh`, and `Chinese` render simplified Chinese labels and `<html lang="zh-Hans">`.
- Missing or unsupported locales fall back to English for backward compatibility.
- Report artifact content is rendered as provided by downstream artifacts; only renderer UI chrome and built-in status labels are localized.

## Downstream Project Integration

Private downstream projects should generate a render manifest and call ArtifactWeaver as a renderer. They remain responsible for producing their own artifacts, evidence assets, and private workflow data.

Do not put private project data into this open-source repository. Do not implement a NoTimeToDie-specific adapter here. Keep adapters in private downstream repositories when they are needed.

## Worker Harness

Every worker must follow `HARNESS.md` and the scoped context pack for the task. The harness defines allowed paths, out-of-scope paths, validation, documentation updates, and handoff rules.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
