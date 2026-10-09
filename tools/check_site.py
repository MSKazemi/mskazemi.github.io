#!/usr/bin/env python3
"""Identity, claims and consistency checks for the static site.

Run from the repository root: ``python3 tools/check_site.py``. Exit 0 = clean, 1 = findings.

Checks:
  * every JSON-LD block parses;
  * the current title appears on the homepage, About and Hire pages;
  * retired or unapproved wording does not reappear (see BANNED);
  * every page with an ``index.html`` has its ``index.md`` twin;
  * every sitemap URL that belongs to this repository maps to a file, and its ``lastmod``
    is not older than the page's JSON-LD ``dateModified``.

Optional: ``SITE_PRIVATE_BANLIST=/path/to/file`` adds one case-insensitive term per line that must
never appear (for example confidential names). Keep that file outside this public repository.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://mskazemi.com/"
TITLE = "AI Platform &amp; Agentic Systems Engineer"
TITLE_PAGES = ["index.html", "about/index.html", "hire/index.html"]

# (pattern, why) — matched case-insensitively against HTML, Markdown twins and text files.
BANNED = [
    (r"remote across the EU\b", "location is Italy, remote across Europe and internationally"),
    (r"remote worldwide, from Bologna", "location is Italy, remote across Europe and internationally"),
    (r"available · remote · EU\b", "location is Italy, remote across Europe and internationally"),
    (r"AI Platform &(amp;)? MLOps Engineer · (Bologna|Agentic AI Systems on Kubernetes)", "retired lead title"),
    (r"currently as architect and lead developer", "university-era role written as current"),
    (r"each one runs against a real cluster", "live-cluster claim belongs to KubeIntellect only"),
    (r"\b12 scorers\b", "scorer count is not an approved claim; use 7 scored dimensions"),
    (r"\b(six|6) (evaluation )?dimensions\b", "AOBench is scored on 7 dimensions"),
    (r"Code-Generator agent synthesises", "runtime tool synthesis is paper architecture, not current"),
    (r"^Generates new Python tools at runtime", "runtime tool synthesis is paper architecture, not current"),
    (r"\b\d[\d,]* citations?\b", "citation counts are not shown on the site"),
    (r"\bh-index\b", "citation metrics are not shown on the site"),
    (r"unibo\.it/sitoweb/", "the University of Bologna staff page no longer exists"),
]


def text_files() -> list[Path]:
    skip = {".git", "node_modules", "tools", "data"}
    out = []
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix in {".html", ".md", ".txt"} and not skip & set(p.relative_to(ROOT).parts):
            if p.name != "README.md":
                out.append(p)
    return sorted(out)


def main() -> int:
    problems: list[str] = []
    rel = lambda p: str(p.relative_to(ROOT))  # noqa: E731

    banned = [(re.compile(pat, re.I | re.M), why) for pat, why in BANNED]
    private = os.environ.get("SITE_PRIVATE_BANLIST")
    if private:
        for line in Path(private).read_text().splitlines():
            if line.strip() and not line.startswith("#"):
                banned.append((re.compile(re.escape(line.strip()), re.I), "private ban-list term"))

    for p in text_files():
        s = p.read_text(encoding="utf-8")
        for rx, why in banned:
            for m in rx.finditer(s):
                line = s.count("\n", 0, m.start()) + 1
                shown = "<private term>" if why == "private ban-list term" else m.group(0)
                problems.append(f"{rel(p)}:{line}: '{shown}' — {why}")
        if p.suffix == ".html":
            for i, block in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)):
                try:
                    json.loads(block)
                except json.JSONDecodeError as e:
                    problems.append(f"{rel(p)}: JSON-LD block {i + 1} does not parse ({e})")
            if p.name == "index.html" and p.parent != ROOT / "404" and not (p.parent / "index.md").exists():
                problems.append(f"{rel(p)}: no index.md twin")

    for page in TITLE_PAGES:
        if TITLE not in (ROOT / page).read_text(encoding="utf-8"):
            problems.append(f"{page}: current title '{TITLE}' missing")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for loc, lastmod in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", sitemap):
        path = loc.removeprefix(SITE)
        page = ROOT / path / "index.html"
        if not page.exists():
            continue  # a separately deployed project site, not this repository
        m = re.search(r'"dateModified":\s*"(\d{4}-\d{2}-\d{2})', page.read_text(encoding="utf-8"))
        if m and m.group(1) > lastmod:
            problems.append(f"sitemap.xml: {loc} lastmod {lastmod} is older than dateModified {m.group(1)}")

    for line in problems:
        print(line)
    print(f"check_site: {len(problems)} finding(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
