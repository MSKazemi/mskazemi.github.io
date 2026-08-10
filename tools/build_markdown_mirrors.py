#!/usr/bin/env python3
"""Emit a clean Markdown twin of every page, and link it from the HTML.

Why: AI crawlers largely ignore content negotiation and mostly ignore llms.txt, but
they do fetch dedicated `.md` URLs when the HTML advertises one, and they prefer the
Markdown variant — roughly 80% fewer tokens, with no navigation, scripts or styling
to wade through. For a site whose audience is developers and coding agents, this is a
cheap and real lever. The `llms.txt` file stays as a site-level index; these are the
per-page bodies it points into.

    /about/          ->  /about/index.md
    /datasets/       ->  /datasets/index.md
    /                ->  /index.md

Each HTML page gets `<link rel="alternate" type="text/markdown" href="…">` in <head>
so the twin is discoverable rather than guessable.

Usage:
    python3 tools/build_markdown_mirrors.py
    python3 tools/build_markdown_mirrors.py --check    # exit 1 if any twin is stale
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://mskazemi.com/"

# Chrome we never want in the Markdown body.
SKIP_TAGS = {"script", "style", "svg", "nav", "header", "footer", "button", "form", "noscript"}
SKIP_CLASSES = {"skip-link", "nav-inner", "footer-inner", "theme-toggle", "breadcrumb"}


class ToMarkdown(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base = base_url
        self.out: list[str] = []
        self.skip_depth = 0
        self.skip_tag: str | None = None
        self.buf: list[str] = []
        self.mode: str | None = None
        self.href: str | None = None
        self.list_depth = 0
        self.in_pre = False
        self.row: list[str] = []
        self.in_cell = False
        self.table: list[list[str]] = []
        self.in_table = False
        self.header_done = False

    # -- helpers ---------------------------------------------------------
    def flush(self) -> None:
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf.clear()
        if not text:
            self.mode = None
            return
        if self.mode and self.mode.startswith("h"):
            self.out.append("#" * int(self.mode[1]) + " " + text)
        elif self.mode == "li":
            self.out.append("- " + text)
        elif self.mode == "p":
            self.out.append(text)
        self.mode = None

    def handle_starttag(self, tag: str, attrs_list) -> None:
        attrs = dict(attrs_list)
        classes = set((attrs.get("class") or "").split())
        if self.skip_depth:
            if tag == self.skip_tag:
                self.skip_depth += 1
            return
        if tag in SKIP_TAGS or classes & SKIP_CLASSES:
            self.skip_tag, self.skip_depth = tag, 1
            return

        if tag in ("h1", "h2", "h3", "h4"):
            self.flush()
            self.mode = "h" + tag[1]
        elif tag == "p" and not self.in_table:
            self.flush()
            self.mode = "p"
        elif tag == "li":
            self.flush()
            self.mode = "li"
        elif tag == "a":
            self.href = attrs.get("href")
            self.buf.append("[")
        elif tag in ("strong", "b"):
            self.buf.append("**")
        elif tag in ("em", "i"):
            self.buf.append("_")
        elif tag == "code" and not self.in_pre:
            self.buf.append("`")
        elif tag == "pre":
            self.flush()
            self.in_pre = True
            self.out.append("```")
        elif tag == "br":
            self.buf.append(" ")
        elif tag == "table":
            self.flush()
            self.in_table, self.table, self.header_done = True, [], False
        elif tag == "tr" and self.in_table:
            self.row = []
        elif tag in ("td", "th") and self.in_table:
            self.in_cell = True
            self.buf.clear()

    def handle_endtag(self, tag: str) -> None:
        if self.skip_depth:
            if tag == self.skip_tag:
                self.skip_depth -= 1
                if not self.skip_depth:
                    self.skip_tag = None
            return

        if tag == "a" and self.href is not None:
            url = urljoin(self.base, self.href)
            self.buf.append(f"]({url})")
            self.href = None
        elif tag in ("strong", "b"):
            self.buf.append("**")
        elif tag in ("em", "i"):
            self.buf.append("_")
        elif tag == "code" and not self.in_pre:
            self.buf.append("`")
        elif tag == "pre":
            self.out.append("".join(self.buf).strip())
            self.out.append("```")
            self.buf.clear()
            self.in_pre = False
        elif tag in ("td", "th") and self.in_table:
            self.row.append(re.sub(r"\s+", " ", "".join(self.buf)).strip().replace("|", "\\|"))
            self.buf.clear()
            self.in_cell = False
        elif tag == "tr" and self.in_table:
            if self.row:
                self.table.append(self.row)
            self.row = []
        elif tag == "table" and self.in_table:
            self.emit_table()
            self.in_table = False
        elif tag in ("h1", "h2", "h3", "h4", "p", "li"):
            self.flush()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.in_pre or self.mode or self.in_cell:
            self.buf.append(data)

    def emit_table(self) -> None:
        if not self.table:
            return
        width = max(len(r) for r in self.table)
        rows = [r + [""] * (width - len(r)) for r in self.table]
        lines = ["| " + " | ".join(rows[0]) + " |",
                 "|" + "|".join([" --- "] * width) + "|"]
        lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        self.out.append("\n".join(lines))   # one block: rows must stay contiguous
        self.table = []

    def markdown(self) -> str:
        self.flush()
        lines, prev = [], None
        for block in self.out:
            block = block.strip()
            if not block or block == prev:
                continue
            lines.append(block)
            prev = block
        return "\n\n".join(lines) + "\n"


def page_url(rel: Path) -> str:
    parts = rel.as_posix()
    return SITE if parts == "index.html" else SITE + parts.replace("index.html", "")


def title_of(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def description_of(html: str) -> str:
    m = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def convert(path: Path) -> tuple[Path, str]:
    rel = path.relative_to(ROOT)
    html = path.read_text(encoding="utf-8")
    url = page_url(rel)

    body = html.split("<body", 1)[-1]
    parser = ToMarkdown(url)
    parser.feed(body)

    header = (
        f"# {title_of(html)}\n\n"
        f"> {description_of(html)}\n\n"
        f"Source: <{url}> · Author: Mohsen Seyedkazemi Ardebili · "
        f"This is the Markdown twin of the HTML page; the HTML is canonical.\n\n---\n\n"
    )
    md = parser.markdown()
    # The front-matter already carries the page title, so the hero <h1> would read as a
    # second title. Drop the first body-level H1 wherever it appears.
    md = re.sub(r"(?m)^# .*\n\n", "", md, count=1)
    return path.with_suffix(".md"), header + md


ALT_TAG = '  <link rel="alternate" type="text/markdown" href="{url}index.md" />\n'


def ensure_alt_link(path: Path) -> bool:
    """Advertise the twin from <head>; returns True if the file changed."""
    html = path.read_text(encoding="utf-8")
    if 'type="text/markdown"' in html:
        return False
    rel = path.relative_to(ROOT)
    tag = ALT_TAG.format(url=page_url(rel))
    anchor = '  <meta name="robots"'
    if anchor not in html:
        anchor = "</head>"
        html = html.replace(anchor, tag + anchor, 1)
    else:
        html = html.replace(anchor, tag + anchor, 1)
    path.write_text(html, encoding="utf-8")
    return True


def targets() -> list[Path]:
    pages = ["index.html"] + sorted(glob.glob("*/index.html", root_dir=ROOT)) + sorted(
        glob.glob("projects/*/index.html", root_dir=ROOT)
    )
    return [ROOT / p for p in pages if (ROOT / p).exists()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    stale, written, linked = [], 0, 0
    for page in targets():
        out, md = convert(page)
        if args.check:
            if not out.exists() or out.read_text(encoding="utf-8") != md:
                stale.append(str(out.relative_to(ROOT)))
            continue
        if not out.exists() or out.read_text(encoding="utf-8") != md:
            out.write_text(md, encoding="utf-8")
            written += 1
        if ensure_alt_link(page):
            linked += 1

    if args.check:
        if stale:
            print("stale Markdown twins: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"all {len(targets())} Markdown twins are up to date")
        return 0

    print(f"wrote {written} Markdown twin(s), added {linked} alternate link(s), "
          f"{len(targets())} pages covered")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
