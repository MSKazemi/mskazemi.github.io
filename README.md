# Personal website — mskazemi.com

The public personal website of **Mohsen Seyedkazemi Ardebili**, AI Platform & Agentic Systems
Engineer · Independent Consultant. **Canonical URL:** https://mskazemi.com/

This repository is the source of the site. It is static HTML/CSS/JavaScript with no build step,
deployed to GitHub Pages by `.github/workflows/deploy-pages.yml` on every push to `main`.
`mskazemi.github.io` redirects to the custom domain, and every canonical tag, Open Graph URL,
`sitemap.xml`, `robots.txt` and `llms.txt` points at `https://mskazemi.com/`.

## Content conventions

- Each HTML page has a same-path `index.md` Markdown alternative; change both together, and keep
  `llms.txt` / `humans.txt` in step when availability or location copy changes.
- Location: **Italy** in headlines, quick facts and social previews (remote across Europe and
  internationally); the city, **Bologna, Italy**, in detailed biography text and `Person` address data.
- Time zone: **Europe/Rome (CET/CEST)**.
- Project claims link to their primary evidence (repository, documentation, paper or DOI).
- Update a page's `sitemap.xml` `lastmod` only when its content changes.

## Checks

```bash
python3 tools/check_site.py   # identity, claims, JSON-LD, Markdown twins, sitemap dates
```

The same check runs on every pull request (`.github/workflows/check.yml`).

## Review before merging

Check the homepage, About and Hire pages at desktop and mobile widths, and confirm that copy, social
descriptions, Markdown alternatives and JSON-LD agree. Merging into `main` deploys publicly.
