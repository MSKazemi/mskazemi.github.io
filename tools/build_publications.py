#!/usr/bin/env python3
"""Generate /publications/index.html from data/publications.json.

The whole page is derived — the citation counts, the DOI links, the BibTeX, and
the schema.org ScholarlyArticle graph all come from one JSON file, so the page
can never drift from the CV. Re-export that file from work/cv/profile/cv.json in the
brain repo, then re-run this.

Usage:
    python3 tools/build_publications.py
    python3 tools/build_publications.py --check    # exit 1 if the page is stale
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "publications.json"
OUT = ROOT / "publications" / "index.html"
SITE = "https://mskazemi.com"
ME = "Mohsen Seyedkazemi Ardebili"
ME_SHORT = {"M. Seyedkazemi Ardebili", "MS Ardebili", "M Seyedkazemi Ardebili"}


def esc(text: object) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def is_me(author: str) -> bool:
    return author == ME or author in ME_SHORT


def authors_html(authors: list[str]) -> str:
    parts = [
        f"<strong>{esc(a)}</strong>" if is_me(a) else esc(a) for a in authors
    ]
    return ", ".join(parts)


def bibkey(pub: dict) -> str:
    first = pub["authors"][0].split()[-1].lower()
    first = re.sub(r"[^a-z]", "", first)
    word = re.sub(r"[^A-Za-z]", "", pub["title"].split()[0]).lower()
    return f"{first}{pub.get('year', 'nd')}{word}"


def bibtex(pub: dict, kind: str) -> str:
    """A BibTeX record a reader can paste straight into a paper."""
    entry = "article" if kind == "journal" else "inproceedings"
    field = "journal" if kind == "journal" else "booktitle"
    lines = [f"@{entry}{{{bibkey(pub)},"]
    lines.append(f"  author    = {{{' and '.join(pub['authors'])}}},")
    lines.append(f"  title     = {{{pub['title']}}},")
    if pub.get("venue"):
        lines.append(f"  {field:<9} = {{{pub['venue']}}},")
    if pub.get("year"):
        lines.append(f"  year      = {{{pub['year']}}},")
    for key in ("volume", "issue", "pages", "publisher"):
        if pub.get(key):
            name = "number" if key == "issue" else key
            lines.append(f"  {name:<9} = {{{pub[key]}}},")
    if pub.get("doi"):
        lines.append(f"  doi       = {{{pub['doi']}}},")
    lines.append("}")
    return "\n".join(lines)


def entry_html(pub: dict, kind: str, index: int) -> str:
    badges = []
    if pub.get("citations"):
        n = pub["citations"]
        badges.append(
            f'<span class="pb pb-cite" title="Google Scholar citations, read 2026-08-10">'
            f'{n} citation{"s" if n != 1 else ""}</span>'
        )
    status = pub.get("status", "")
    if status and status != "Published":
        badges.append(f'<span class="pb pb-status">{esc(status)}</span>')
    if pub.get("doi"):
        badges.append(
            f'<a class="pb pb-doi" href="https://doi.org/{esc(pub["doi"])}" '
            f'target="_blank" rel="noopener">DOI ↗</a>'
        )

    title = esc(pub["title"])
    if pub.get("doi"):
        title = (
            f'<a href="https://doi.org/{esc(pub["doi"])}" target="_blank" rel="noopener">{title}</a>'
        )

    venue_bits = []
    if pub.get("venue"):
        venue_bits.append(esc(pub["venue"]))
    if pub.get("volume"):
        vol = esc(pub["volume"])
        if pub.get("issue"):
            vol += f'({esc(pub["issue"])})'
        venue_bits.append(vol)
    if pub.get("pages"):
        venue_bits.append(esc(pub["pages"]))
    venue = " · ".join(venue_bits)

    year = f'<span class="p-year">{pub["year"]}</span>' if pub.get("year") else '<span class="p-year tbd">—</span>'
    bib = esc(bibtex(pub, kind))

    return f"""        <li class="p-item">
          {year}
          <div class="p-body">
            <h3 class="p-title">{title}</h3>
            <p class="p-authors">{authors_html(pub['authors'])}</p>
            {f'<p class="p-venue">{venue}</p>' if venue else ''}
            <p class="p-badges">{''.join(badges)}</p>
            <details class="p-bib">
              <summary>BibTeX</summary>
              <pre><code id="bib{index}">{bib}</code></pre>
              <button type="button" class="copy-bib" data-target="bib{index}">Copy</button>
            </details>
          </div>
        </li>"""


def section(title: str, blurb: str, pubs: list[tuple[dict, str]], start: int) -> tuple[str, int]:
    if not pubs:
        return "", start
    items = []
    for i, (pub, kind) in enumerate(pubs):
        items.append(entry_html(pub, kind, start + i))
    return (
        f"""      <h2 class="sub-title">{esc(title)}</h2>
      <p class="section-lead">{blurb}</p>
      <ol class="p-list">
{chr(10).join(items)}
      </ol>""",
        start + len(pubs),
    )


def jsonld(data: dict) -> str:
    items = []
    pubs = data["publications"]
    for kind, group in (("journal", "journals"), ("conference", "conferences")):
        for pub in pubs[group]["publishedOrAccepted"]:
            node = {
                "@type": "ScholarlyArticle",
                "name": pub["title"],
                "author": [{"@type": "Person", "name": a} for a in pub["authors"]],
                "datePublished": str(pub.get("year", "")),
                "isPartOf": {
                    "@type": "Periodical" if kind == "journal" else "PublicationEvent",
                    "name": pub.get("venue", ""),
                },
            }
            if pub.get("doi"):
                node["sameAs"] = f"https://doi.org/{pub['doi']}"
                node["identifier"] = f"https://doi.org/{pub['doi']}"
            items.append(node)
    graph = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": f"Publications — {ME}",
        "url": f"{SITE}/publications/",
        "about": {
            "@type": "Person",
            "@id": f"{SITE}/#person",
            "name": ME,
            "sameAs": [
                data["identity"]["scholarUrl"],
                f"https://orcid.org/{data['identity']['orcid']}",
                f"https://openalex.org/{data['identity']['openalexId']}",
            ],
        },
        "hasPart": items,
    }
    return json.dumps(graph, indent=2, ensure_ascii=False)


def render(data: dict) -> str:
    pubs = data["publications"]
    m = data["metrics"]

    published = [(p, "journal") for p in pubs["journals"]["publishedOrAccepted"]]
    published += [(p, "conference") for p in pubs["conferences"]["publishedOrAccepted"]]
    published.sort(key=lambda t: (-(t[0].get("year") or 0), t[0]["title"]))

    review = [(p, "journal") for p in pubs["journals"]["underReview"]]
    review += [(p, "conference") for p in pubs["conferences"]["underReview"]]

    prep = [(p, "journal") for p in pubs["journals"]["inPreparation"]]
    prep += [(p, "conference") for p in pubs["conferences"]["inPreparation"]]

    n = 0
    s1, n = section(
        "Published and accepted",
        "Peer-reviewed journal articles, conference papers and workshop papers. "
        "Citation counts are Google&nbsp;Scholar's, read on " + data["_verifiedOn"] + ".",
        published,
        n,
    )
    s2, n = section(
        "Under review",
        "Submitted and in the review process. Submitted is not accepted — these are listed as "
        "evidence of the current line of work, not as results.",
        review,
        n,
    )
    s3, n = section("In preparation", "Drafts in progress.", prep, n)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script>try{{if(localStorage.getItem('theme')==='dark')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}</script>
  <title>Publications — {ME}</title>
  <meta name="description" content="Complete publication list for {ME}: {m['peerReviewedPublished']} peer-reviewed papers on HPC anomaly detection, LLM agents for Kubernetes, MLOps and datacenter telemetry, with {m['citationsAll']} citations and an h-index of {m['hIndexAll']}. Includes DOIs and BibTeX." />
  <meta name="author" content="{ME}" />
  <meta name="keywords" content="Mohsen Seyedkazemi Ardebili publications, HPC anomaly detection papers, LLM agents Kubernetes, KubeIntellect paper, GRAAFE, HazardNet, ThermADNet, M100 ExaData, PM100, BibTeX" />
  <link rel="canonical" href="{SITE}/publications/" />
  <link rel="alternate" type="text/markdown" href="{SITE}/publications/index.md" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <meta name="theme-color" content="#0A0E14" />

  <meta property="og:title" content="Publications — {ME}" />
  <meta property="og:description" content="{m['peerReviewedPublished']} peer-reviewed papers, {m['citationsAll']} citations, h-index {m['hIndexAll']}. HPC anomaly detection, LLM agents for Kubernetes, MLOps at supercomputer scale." />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{SITE}/publications/" />
  <meta property="og:site_name" content="{ME}" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:image" content="{SITE}/assets/mohsen-portrait.jpg" />
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:image" content="{SITE}/assets/mohsen-portrait.jpg" />

  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230A0E14'/%3E%3Cpath d='M9 16a7 7 0 1 1 2.05 4.95' fill='none' stroke='%23F2A93B' stroke-width='2.4' stroke-linecap='round'/%3E%3Ccircle cx='9' cy='16' r='2.4' fill='%233FD79A'/%3E%3C/svg%3E" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
  <link rel="stylesheet" href="../project.css" />

  <script type="application/ld+json">
{jsonld(data)}
  </script>
</head>
<body>

  <a href="#main" class="skip-link">Skip to content</a>

  <header id="nav">
    <div class="nav-inner">
      <a href="../" class="nav-logo" aria-label="Home">
        <svg class="logo-mark" width="22" height="22" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M9 16a7 7 0 1 1 2.05 4.95" fill="none" stroke="var(--amber)" stroke-width="2.6" stroke-linecap="round"/>
          <circle cx="9" cy="16" r="2.6" fill="var(--mint)"/>
        </svg>
        <span>Mohsen Seyedkazemi</span>
      </a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        <a href="../#impact">Impact</a>
        <a href="../#systems">Systems</a>
        <a href="../projects/kubeintellect/">KubeIntellect</a>
        <a href="../projects/aobench/">AOBench</a>
        <a href="../about/">About</a>
        <a href="../#contact" class="nav-cta">Get in touch</a>
        <button class="theme-toggle" id="themeToggle" type="button" aria-label="Toggle light or dark theme" title="Toggle theme" aria-pressed="false">
          <svg class="ic-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          <svg class="ic-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
        </button>
      </nav>
    </div>
  </header>

  <main id="main">

  <section class="proj-hero">
    <div class="container">
      <p class="breadcrumb">
        <a href="../">home</a><span class="sep">/</span>
        <span class="cur">publications</span>
      </p>
      <p class="proj-eyebrow"><span class="dot-mint" aria-hidden="true"></span>verified {data['_verifiedOn']}</p>
      <h1>Publications</h1>
      <p class="proj-tagline">Every paper, with its DOI and its BibTeX.</p>
      <p class="proj-lede">
        Anomaly detection and thermal-hazard prediction on Tier-0 supercomputers, LLM agents that
        operate Kubernetes, MLOps at supercomputer scale, and the open datasets underneath all of it.
        Counts come from Google&nbsp;Scholar; identifiers from Crossref.
      </p>
      <div class="proj-links">
        <a href="{data['identity']['scholarUrl']}" target="_blank" rel="noopener" class="btn-primary">Google Scholar ↗</a>
        <a href="https://orcid.org/{data['identity']['orcid']}" target="_blank" rel="noopener" class="btn-ghost">ORCID ↗</a>
        <a href="https://openalex.org/{data['identity']['openalexId']}" target="_blank" rel="noopener" class="btn-ghost">OpenAlex ↗</a>
      </div>
    </div>
  </section>

  <section class="panel-section">
    <div class="container">
      <div class="stat-row">
        <div class="stat"><span class="stat-v">{m['citationsAll']}</span><span class="stat-k">citations</span><span class="stat-sub">{m['citationsSince2021']} since 2021</span></div>
        <div class="stat"><span class="stat-v">{m['hIndexAll']}</span><span class="stat-k">h-index</span><span class="stat-sub">i10-index {m['i10All']}</span></div>
        <div class="stat"><span class="stat-v">{m['peerReviewedPublished']}</span><span class="stat-k">peer-reviewed</span><span class="stat-sub">published or accepted</span></div>
        <div class="stat"><span class="stat-v">{m['underReviewOrInPreparation']}</span><span class="stat-k">in the pipeline</span><span class="stat-sub">under review or in preparation</span></div>
      </div>

{s1}

{s2}

{s3}

      <p class="chart-source">
        Citation counts are Google&nbsp;Scholar's, read on {data['_verifiedOn']}; duplicate Scholar
        records for the same work are merged. DOIs are resolved through Crossref. Where a paper has no
        DOI it has not been assigned one by the publisher.
        <a href="../data/publications.json">The JSON behind this page</a> is the same file that
        generates it.
      </p>
    </div>
  </section>

  <section class="contact">
    <div class="container">
      <p class="section-eyebrow">// more</p>
      <h2 class="contact-h">The systems behind the papers.</h2>
      <div class="contact-links">
        <a href="../projects/kubeintellect/" class="clink">KubeIntellect →</a>
        <a href="../projects/aobench/" class="clink">AOBench →</a>
        <a href="../#impact" class="clink">Research impact →</a>
        <a href="../#contact" class="clink">Get in touch →</a>
      </div>
    </div>
  </section>

  </main>

  <footer>
    <div class="container footer-inner">
      <span>&copy; <span id="year"></span> {ME}</span>
      <nav class="footer-nav" aria-label="Site pages">
        <a href="../about/">About the author</a>
        <a href="../hire/">Hire</a>
        <a href="../">Home</a>
      </nav>
      <span class="foot-meta">By <a href="../about/" class="back-link">{ME}</a> &middot; Bologna, Italy</span>
    </div>
  </footer>

  <script src="../script.js"></script>
  <script>
    // Progressive enhancement only — the BibTeX is already selectable text.
    document.querySelectorAll('.copy-bib').forEach(function (btn) {{
      btn.addEventListener('click', function () {{
        var el = document.getElementById(btn.dataset.target);
        if (!el) return;
        navigator.clipboard.writeText(el.textContent).then(function () {{
          var was = btn.textContent;
          btn.textContent = 'Copied';
          setTimeout(function () {{ btn.textContent = was; }}, 1600);
        }});
      }});
    }});
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    data = json.loads(DATA.read_text(encoding="utf-8"))
    html = render(data)
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else None

    if args.check:
        if current != html:
            print("publications/index.html is stale — run tools/build_publications.py", file=sys.stderr)
            return 1
        print("publications/index.html is up to date")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
