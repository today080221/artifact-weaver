# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yml",
    ".yaml",
}
SKIP_DIRS = {".git", ".venv", "__pycache__", "build", "dist", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


FORBIDDEN_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("specific private project path", re.compile(r"N:[/\\]GameDemo[/\\]CodeTime3D", re.IGNORECASE)),
    ("local user home path", re.compile(r"C:[/\\]Users[/\\][^/\\\s]+", re.IGNORECASE)),
    ("Windows company drive path", re.compile(r"\b[A-Z]:[/\\](?:Company|Corp|Internal|GameDemo)[/\\]", re.IGNORECASE)),
    ("actual Steam AppID value", re.compile(r"\bSteam\s+AppID\s*[:=]\s*\d{3,}\b", re.IGNORECASE)),
    ("actual DepotID value", re.compile(r"\bDepotID\s*[:=]\s*\d{3,}\b", re.IGNORECASE)),
    ("steam_appid file", re.compile(r"\bsteam_appid\.txt\b", re.IGNORECASE)),
    ("Jenkins internal URL", re.compile(r"https?://[^\s)\"']*jenkins[^\s)\"']*", re.IGNORECASE)),
    ("Feishu webhook URL", re.compile(r"https?://[^\s)\"']*feishu[^\s)\"']*/hook[^\s)\"']*", re.IGNORECASE)),
    ("Lark webhook URL", re.compile(r"https?://[^\s)\"']*larksuite[^\s)\"']*/hook[^\s)\"']*", re.IGNORECASE)),
    ("actual skill ID", re.compile(r"\bskill_[A-Za-z0-9-]{6,}\b")),
    ("actual synergy ID", re.compile(r"\bsynergy_[A-Za-z0-9-]{6,}\b")),
]


def _iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name in {"LICENSE", "NOTICE"}):
            files.append(path)
    return files


def main() -> int:
    findings: list[str] = []
    for path in _iter_text_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for label, pattern in FORBIDDEN_PATTERNS:
            for match in pattern.finditer(text):
                findings.append(f"{rel}: {label}: {match.group(0)}")

    if findings:
        print("Private scope check failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("Private scope check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
