# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
HOOK_FILES = [
    ".githooks/pre-commit",
    ".githooks/pre-push",
    ".githooks/post-checkout",
    ".githooks/post-commit",
    ".githooks/post-merge",
]


def _env() -> dict[str, str]:
    env = os.environ.copy()
    src = str(ROOT / "src")
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = src if not existing else src + os.pathsep + existing
    return env


def _run(args: list[str], *, check_output: bool = False) -> str:
    display = " ".join(args)
    print(f"==> {display}")
    completed = subprocess.run(
        args,
        cwd=ROOT,
        env=_env(),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if completed.stdout:
        print(completed.stdout, end="" if completed.stdout.endswith("\n") else "\n")
    if completed.returncode != 0:
        raise RuntimeError(f"Command failed with exit code {completed.returncode}: {display}")
    if check_output and not completed.stdout.strip():
        raise RuntimeError(f"Command produced no output: {display}")
    return completed.stdout


def _assert_no_tracked_dist() -> None:
    tracked = _run(["git", "ls-files", "dist"])
    if tracked.strip():
        raise RuntimeError("Generated dist files are tracked by Git.")
    _run(["git", "status", "--short", "--", "dist"])


def _assert_hooks_executable() -> None:
    output = _run(["git", "ls-files", "-s", *HOOK_FILES], check_output=True)
    modes: dict[str, str] = {}
    for line in output.splitlines():
        parts = line.split(None, 3)
        if len(parts) != 4:
            raise RuntimeError(f"Unexpected git ls-files -s output: {line}")
        modes[parts[3]] = parts[0]

    failures = []
    for hook_file in HOOK_FILES:
        mode = modes.get(hook_file)
        if mode != "100755":
            failures.append(f"{hook_file} has mode {mode or 'missing'}, expected 100755")
    if failures:
        raise RuntimeError("Git hook executable mode check failed: " + "; ".join(failures))


def _assert_markdown_link_safety() -> None:
    src = str(ROOT / "src")
    if src not in sys.path:
        sys.path.insert(0, src)
    from artifact_weaver.markdown import render_markdown

    unsafe_links = [
        "[x](javascript:alert(1))",
        "[x](data:text/html,<svg/onload=alert(1)>)",
        "[x](vbscript:msgbox(1))",
        "[x](file:///C:/secret.txt)",
        "[x](https://example.com)",
        "[x](http://example.com)",
        "[x](mailto:test@example.com)",
        "[x](//example.com)",
        "[x](/absolute/path)",
        "[x](C:\\secret.txt)",
        "[x](..\\secret.txt)",
        "[x](folder\\..\\secret.txt)",
        "[x](screenshots\\placeholder.txt)",
        "[x](\\absolute\\path)",
        "[x](../secret.txt)",
        "[x](~/secret.txt)",
        "[x](#)",
    ]
    for markdown in unsafe_links:
        rendered = render_markdown(markdown)
        if "<a href=" in rendered:
            raise RuntimeError(f"Unsafe Markdown link emitted href: {markdown} -> {rendered}")

    safe_links = {
        "[x](docs/page.md)": '<a href="docs/page.md">x</a>',
        "[x](screenshots/placeholder.txt)": '<a href="screenshots/placeholder.txt">x</a>',
        "[x](#section)": '<a href="#section">x</a>',
    }
    for markdown, expected in safe_links.items():
        rendered = render_markdown(markdown)
        if expected not in rendered:
            raise RuntimeError(f"Safe Markdown link did not emit expected href: {markdown} -> {rendered}")


def main() -> int:
    try:
        python_files = sorted(str(path.relative_to(ROOT)) for path in (ROOT / "src" / "artifact_weaver").glob("*.py"))
        _run([PYTHON, "-m", "py_compile", *python_files])
        _run([PYTHON, "-m", "artifact_weaver", "--help"], check_output=True)
        _run(
            [
                PYTHON,
                "-m",
                "artifact_weaver",
                "render",
                "--manifest",
                "examples/qa-report/render_manifest.json",
                "--out",
                "dist/qa-report",
            ]
        )
        output = ROOT / "dist" / "qa-report" / "report.html"
        if not output.is_file():
            raise RuntimeError("Expected output missing: dist/qa-report/report.html")
        _run([PYTHON, "tools/check_bilingual_docs.py"])
        _run([PYTHON, "tools/check_private_scope.py"])
        _assert_no_tracked_dist()
        _assert_hooks_executable()
        _assert_markdown_link_safety()
        _run(["git", "diff", "--check"])
        _run(["git", "diff", "--cached", "--check"])
    except Exception as exc:  # noqa: BLE001 - validation entrypoint should print one clear failure.
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
