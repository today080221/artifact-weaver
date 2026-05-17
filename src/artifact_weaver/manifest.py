# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .model import Boundaries, Document, Outputs, RenderManifest, Sources, Theme
from .safety import safe_join


SUPPORTED_SCHEMA_VERSION = "render-manifest/v1"


class ManifestError(ValueError):
    """Raised when a render manifest is malformed."""


def _object(raw: dict[str, Any], key: str) -> dict[str, Any]:
    value = raw.get(key)
    if not isinstance(value, dict):
        raise ManifestError(f"Manifest field {key!r} must be an object.")
    return value


def _string(raw: dict[str, Any], key: str, *, default: str | None = None) -> str:
    value = raw.get(key, default)
    if not isinstance(value, str):
        raise ManifestError(f"Manifest field {key!r} must be a string.")
    return value


def _string_list(raw: dict[str, Any], key: str) -> list[str]:
    value = raw.get(key, [])
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ManifestError(f"Manifest field {key!r} must be a list of strings.")
    return list(value)


def load_manifest(path: Path) -> RenderManifest:
    manifest_path = path.resolve()
    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ManifestError("Render manifest must be a JSON object.")

    schema_version = _string(raw, "schemaVersion")
    if schema_version != SUPPORTED_SCHEMA_VERSION:
        raise ManifestError(
            f"Unsupported schemaVersion {schema_version!r}; expected {SUPPORTED_SCHEMA_VERSION!r}."
        )

    document_raw = _object(raw, "document")
    theme_raw = _object(raw, "theme")
    sources_raw = _object(raw, "sources")
    outputs_raw = _object(raw, "outputs")
    boundaries_raw = _object(raw, "boundaries")

    sources = Sources(
        markdown=_string(sources_raw, "markdown"),
        report_json=_string(sources_raw, "reportJson"),
        evidence_json=_string(sources_raw, "evidenceJson"),
    )
    outputs = Outputs(html=_string(outputs_raw, "html", default="report.html"))
    boundaries = Boundaries(
        source_of_truth=_string_list(boundaries_raw, "sourceOfTruth"),
        generated_view=_string_list(boundaries_raw, "generatedView"),
        private_data_policy=_string(boundaries_raw, "privateDataPolicy", default="fake-data-only"),
    )

    root = manifest_path.parent
    safe_join(root, sources.markdown, label="markdown source", must_exist=True)
    safe_join(root, sources.report_json, label="reportJson source", must_exist=True)
    safe_join(root, sources.evidence_json, label="evidenceJson source", must_exist=True)
    safe_join(root, outputs.html, label="html output")
    for item in boundaries.source_of_truth:
        safe_join(root, item, label="sourceOfTruth entry")
    for item in boundaries.generated_view:
        safe_join(root, item, label="generatedView entry")

    return RenderManifest(
        schema_version=schema_version,
        document=Document(
            title=_string(document_raw, "title"),
            subtitle=_string(document_raw, "subtitle", default=""),
            generated_at=_string(document_raw, "generatedAt", default=""),
            locale=_string(document_raw, "locale", default="en"),
        ),
        theme=Theme(
            name=_string(theme_raw, "name", default="default"),
            accent=_string(theme_raw, "accent", default="#7C3AED"),
        ),
        sources=sources,
        outputs=outputs,
        boundaries=boundaries,
        path=manifest_path,
        raw=raw,
    )
