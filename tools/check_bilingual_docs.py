# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _markdown_files(root: Path) -> set[Path]:
    return {path.relative_to(root) for path in root.rglob("*.md") if path.is_file()}


def main() -> int:
    en_root = ROOT / "docs" / "en"
    zh_root = ROOT / "docs" / "zh-CN"
    errors: list[str] = []

    en_files = _markdown_files(en_root)
    zh_files = _markdown_files(zh_root)

    for missing in sorted(en_files - zh_files):
        errors.append(f"Missing Simplified Chinese doc for docs/en/{missing.as_posix()}")
    for missing in sorted(zh_files - en_files):
        errors.append(f"Missing English doc for docs/zh-CN/{missing.as_posix()}")

    top_level_pairs = [
        ("README.md", "README.zh-CN.md"),
        ("HARNESS.md", "HARNESS.zh-CN.md"),
        ("CONTRIBUTING.md", "CONTRIBUTING.zh-CN.md"),
    ]
    for en_name, zh_name in top_level_pairs:
        if not (ROOT / en_name).is_file():
            errors.append(f"Missing top-level {en_name}")
        if not (ROOT / zh_name).is_file():
            errors.append(f"Missing top-level {zh_name}")

    if errors:
        print("Bilingual documentation check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Bilingual documentation check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
