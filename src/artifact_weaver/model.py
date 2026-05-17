# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Document:
    title: str
    subtitle: str = ""
    generated_at: str = ""
    locale: str = "en"


@dataclass(frozen=True)
class Theme:
    name: str = "default"
    accent: str = "#7C3AED"


@dataclass(frozen=True)
class Sources:
    markdown: str
    report_json: str
    evidence_json: str


@dataclass(frozen=True)
class Outputs:
    html: str = "report.html"


@dataclass(frozen=True)
class Boundaries:
    source_of_truth: list[str] = field(default_factory=list)
    generated_view: list[str] = field(default_factory=list)
    private_data_policy: str = "fake-data-only"


@dataclass(frozen=True)
class RenderManifest:
    schema_version: str
    document: Document
    theme: Theme
    sources: Sources
    outputs: Outputs
    boundaries: Boundaries
    path: Path
    raw: dict[str, Any]
