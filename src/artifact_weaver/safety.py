# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import re
from pathlib import Path, PureWindowsPath


_URL_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*://")


class UnsafePathError(ValueError):
    """Raised when a manifest path escapes the artifact boundary."""


def _looks_like_unsafe_path(value: str) -> str | None:
    if not value or value.strip() != value:
        return "path must be non-empty and must not include leading or trailing whitespace"
    if "\x00" in value:
        return "path must not contain NUL bytes"
    if value.startswith("~"):
        return "home-directory expansion is not allowed"
    if _URL_RE.match(value):
        return "URL paths are not allowed"
    if value.startswith("\\\\") or value.startswith("//"):
        return "UNC paths are not allowed"
    if PureWindowsPath(value).drive:
        return "drive-letter paths are not allowed"
    candidate = Path(value)
    if candidate.is_absolute():
        return "absolute paths are not allowed"
    if ".." in candidate.parts:
        return "path traversal is not allowed"
    return None


def assert_safe_relative_path(value: str, *, label: str) -> None:
    reason = _looks_like_unsafe_path(value)
    if reason:
        raise UnsafePathError(f"Unsafe {label} path {value!r}: {reason}.")


def safe_join(root: Path, value: str, *, label: str, must_exist: bool = False) -> Path:
    assert_safe_relative_path(value, label=label)
    root_resolved = root.resolve()
    candidate = (root_resolved / value).resolve()
    try:
        common = os.path.commonpath([str(root_resolved), str(candidate)])
    except ValueError as exc:
        raise UnsafePathError(f"Unsafe {label} path {value!r}: path crosses a drive boundary.") from exc
    if common != str(root_resolved):
        raise UnsafePathError(f"Unsafe {label} path {value!r}: path escapes the artifact root.")
    if must_exist and not candidate.exists():
        raise FileNotFoundError(f"{label} path does not exist: {value}")
    return candidate


def safe_href(value: str) -> str | None:
    try:
        assert_safe_relative_path(value, label="Markdown link")
    except UnsafePathError:
        if value.startswith("#") and len(value) > 1:
            return value
        return None
    return value.replace("\\", "/")
