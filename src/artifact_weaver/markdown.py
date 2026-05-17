# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import html
import re

from .safety import safe_href


_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
_CODE_RE = re.compile(r"`([^`]+)`")


def _render_links(text: str) -> str:
    parts: list[str] = []
    last = 0
    for match in _LINK_RE.finditer(text):
        parts.append(html.escape(text[last : match.start()]))
        label = html.escape(match.group(1))
        href = safe_href(match.group(2))
        if href is None:
            parts.append(label)
        else:
            parts.append(f'<a href="{html.escape(href, quote=True)}">{label}</a>')
        last = match.end()
    parts.append(html.escape(text[last:]))
    return "".join(parts)


def _render_inline(text: str) -> str:
    parts: list[str] = []
    last = 0
    for match in _CODE_RE.finditer(text):
        parts.append(_render_links(text[last : match.start()]))
        parts.append(f"<code>{html.escape(match.group(1))}</code>")
        last = match.end()
    parts.append(_render_links(text[last:]))
    return "".join(parts)


def render_markdown(markdown_text: str) -> str:
    """Render a deliberately small, escaped Markdown subset."""

    lines = markdown_text.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(f"<p>{_render_inline(' '.join(paragraph))}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append("</ul>")
            in_list = False

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.startswith("```"):
            if in_code:
                output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_paragraph()
                close_list()
                in_code = True
            continue
        if in_code:
            code_lines.append(raw_line)
            continue
        if not line.strip():
            flush_paragraph()
            close_list()
            continue
        if line.startswith("### "):
            flush_paragraph()
            close_list()
            output.append(f"<h3>{_render_inline(line[4:].strip())}</h3>")
            continue
        if line.startswith("## "):
            flush_paragraph()
            close_list()
            output.append(f"<h2>{_render_inline(line[3:].strip())}</h2>")
            continue
        if line.startswith("# "):
            flush_paragraph()
            close_list()
            output.append(f"<h1>{_render_inline(line[2:].strip())}</h1>")
            continue
        if line.startswith("- ") or line.startswith("* "):
            flush_paragraph()
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{_render_inline(line[2:].strip())}</li>")
            continue
        paragraph.append(line.strip())

    if in_code:
        output.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    flush_paragraph()
    close_list()
    return "\n".join(output)
