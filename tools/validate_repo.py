# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


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
        _run(["git", "diff", "--check"])
    except Exception as exc:  # noqa: BLE001 - validation entrypoint should print one clear failure.
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
