# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .render import render_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="artifact-weaver",
        description="Render Markdown and JSON artifacts into static HTML reports.",
    )
    parser.add_argument("--version", action="version", version=f"ArtifactWeaver {__version__}")
    subparsers = parser.add_subparsers(dest="command")

    render = subparsers.add_parser("render", help="Render a static HTML report from a render manifest.")
    render.add_argument("--manifest", required=True, help="Path to render_manifest.json.")
    render.add_argument("--out", required=True, help="Output directory for the generated static HTML report.")
    render.add_argument("--strict", action="store_true", help="Enable stricter M0 validation.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "render":
        try:
            output_path = render_report(Path(args.manifest), Path(args.out), strict=args.strict)
        except Exception as exc:  # noqa: BLE001 - CLI should present concise user-facing errors.
            print(f"artifact-weaver: error: {exc}", file=sys.stderr)
            return 2
        print(f"Wrote {output_path}")
        return 0
    parser.print_help()
    return 0
