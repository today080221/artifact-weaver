# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import html
import json
import re
from importlib import resources
from pathlib import Path
from typing import Any

from . import __version__
from .i18n import LocaleMessages, label_bool, label_status, resolve_locale
from .manifest import load_manifest
from .markdown import render_markdown
from .safety import safe_join


_HEX_COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")


def _escape(value: Any) -> str:
    return html.escape(str(value))


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON artifact must be an object: {path.name}")
    return value


def _metric_grid(counts: dict[str, Any], messages: LocaleMessages, locale: str) -> str:
    if not counts:
        return f'<p class="muted">{_escape(messages["no_summary_metrics"])}</p>'
    items = []
    for key, value in counts.items():
        items.append(
            '<div class="metric">'
            f'<span class="metric-label">{_escape(label_status(key, locale))}</span>'
            f'<strong>{_escape(value)}</strong>'
            "</div>"
        )
    return '<div class="metrics">' + "".join(items) + "</div>"


def _sections(report: dict[str, Any], messages: LocaleMessages) -> str:
    sections = report.get("sections", [])
    if not isinstance(sections, list) or not sections:
        return f'<p class="muted">{_escape(messages["no_report_sections"])}</p>'
    blocks = []
    for section in sections:
        if not isinstance(section, dict):
            continue
        title = _escape(section.get("title", messages["untitled_section"]))
        body = _escape(section.get("body", ""))
        blocks.append(f"<article><h3>{title}</h3><p>{body}</p></article>")
    return "\n".join(blocks)


def _artifact_index(report: dict[str, Any], messages: LocaleMessages) -> str:
    artifacts = report.get("artifacts", [])
    if not isinstance(artifacts, list) or not artifacts:
        return f'<p class="muted">{_escape(messages["no_artifact_index"])}</p>'
    rows = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        rows.append(
            "<tr>"
            f"<td>{_escape(artifact.get('artifactId', ''))}</td>"
            f"<td>{_escape(artifact.get('label', ''))}</td>"
            f"<td>{_escape(artifact.get('kind', ''))}</td>"
            f"<td><code>{_escape(artifact.get('path', ''))}</code></td>"
            "</tr>"
        )
    return (
        "<table><thead><tr>"
        f"<th>{_escape(messages['artifact_id'])}</th>"
        f"<th>{_escape(messages['label'])}</th>"
        f"<th>{_escape(messages['kind'])}</th>"
        f"<th>{_escape(messages['path'])}</th>"
        "</tr></thead>"
        "<tbody>"
        + "".join(rows)
        + "</tbody></table>"
    )


def _evidence_list(evidence: dict[str, Any], messages: LocaleMessages) -> str:
    items = evidence.get("items", [])
    if not isinstance(items, list) or not items:
        return f'<p class="muted">{_escape(messages["no_linked_evidence"])}</p>'
    cards = []
    for item in items:
        if not isinstance(item, dict):
            continue
        cards.append(
            '<article class="evidence-card">'
            f"<h3>{_escape(item.get('label', messages['untitled_evidence']))}</h3>"
            f"<p>{_escape(item.get('evidenceType', messages['unknown']))}</p>"
            f"<p><code>{_escape(item.get('path', ''))}</code></p>"
            f"<p>{_escape(messages['exists'])}: {_escape(label_bool(item.get('exists', False), messages))}</p>"
            f"<p>{_escape(messages['support_evidence'])}: "
            f"{_escape(label_bool(item.get('isSupportEvidence', False), messages))}</p>"
            f"<p>{_escape(messages['gameplay_oracle'])}: "
            f"{_escape(label_bool(item.get('isGameplayOracle', False), messages))}</p>"
            "</article>"
        )
    return '<div class="evidence-grid">' + "".join(cards) + "</div>"


def _boundaries(
    manifest_source_of_truth: list[str],
    generated_view: list[str],
    policy: str,
    messages: LocaleMessages,
) -> str:
    source_items = "".join(f"<li><code>{_escape(item)}</code></li>" for item in manifest_source_of_truth)
    view_items = "".join(f"<li><code>{_escape(item)}</code></li>" for item in generated_view)
    return (
        "<div class=\"boundary-grid\">"
        f"<div><h3>{_escape(messages['source_of_truth'])}</h3><ul>{source_items}</ul></div>"
        f"<div><h3>{_escape(messages['generated_view'])}</h3><ul>{view_items}</ul></div>"
        f"<div><h3>{_escape(messages['private_data_policy'])}</h3><p><code>{_escape(policy)}</code></p></div>"
        "</div>"
    )


def render_report(manifest_path: Path, out_dir: Path, *, strict: bool = False) -> Path:
    manifest = load_manifest(manifest_path)
    root = manifest.path.parent
    markdown_path = safe_join(root, manifest.sources.markdown, label="markdown source", must_exist=True)
    report_path = safe_join(root, manifest.sources.report_json, label="reportJson source", must_exist=True)
    evidence_path = safe_join(root, manifest.sources.evidence_json, label="evidenceJson source", must_exist=True)

    report = _read_json(report_path)
    evidence = _read_json(evidence_path)
    narrative_html = render_markdown(markdown_path.read_text(encoding="utf-8"))
    locale, messages = resolve_locale(manifest.document.locale)

    out_root = out_dir.resolve()
    out_root.mkdir(parents=True, exist_ok=True)
    output_path = safe_join(out_root, manifest.outputs.html, label="html output")
    if output_path.parent != out_root and strict:
        raise ValueError("Strict mode requires outputs.html to be written directly inside --out.")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    css_text = resources.files("artifact_weaver.templates").joinpath("report.css").read_text(encoding="utf-8")
    css_path = output_path.parent / "report.css"
    css_path.write_text(css_text, encoding="utf-8", newline="\n")

    accent = manifest.theme.accent if _HEX_COLOR_RE.match(manifest.theme.accent) else "#7C3AED"
    template = resources.files("artifact_weaver.templates").joinpath("report.html").read_text(encoding="utf-8")
    html_text = template.format(
        title=_escape(manifest.document.title),
        subtitle=_escape(manifest.document.subtitle),
        generated_at=_escape(manifest.document.generated_at),
        locale=_escape(messages["html_lang"]),
        accent=accent,
        eyebrow=_escape(messages["eyebrow"]),
        generated_label=_escape(messages["generated"]),
        conclusion_label=_escape(messages["conclusion"]),
        summary_metrics_label=_escape(messages["summary_metrics"]),
        markdown_narrative_label=_escape(messages["markdown_narrative"]),
        report_sections_label=_escape(messages["report_sections"]),
        evidence_label=_escape(messages["evidence"]),
        artifact_index_label=_escape(messages["artifact_index"]),
        scope_boundaries_label=_escape(messages["scope_boundaries"]),
        footer=_escape(messages["footer"].format(version=__version__)),
        conclusion=_escape(label_status(report.get("conclusion", "unknown"), locale)),
        metrics=_metric_grid(
            report.get("counts", {}) if isinstance(report.get("counts", {}), dict) else {},
            messages,
            locale,
        ),
        narrative=narrative_html,
        sections=_sections(report, messages),
        evidence=_evidence_list(evidence, messages),
        artifact_index=_artifact_index(report, messages),
        boundaries=_boundaries(
            manifest.boundaries.source_of_truth,
            manifest.boundaries.generated_view,
            manifest.boundaries.private_data_policy,
            messages,
        ),
    )
    output_path.write_text(html_text, encoding="utf-8", newline="\n")
    return output_path
