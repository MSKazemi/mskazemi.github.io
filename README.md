# mskazemi.github.io

Personal homepage of Mohsen Seyedkazemi Ardebili — the **canonical** public homepage,
served via **GitHub Pages** at <https://mskazemi.github.io>.

Plain static site (HTML/CSS/JS, no build step). The GitHub Actions workflow
`.github/workflows/deploy-pages.yml` deploys the repository contents to Pages on every
push to `main` (and can be run manually via *workflow_dispatch*).

Source of truth for the content lives in the lab at `cv/homepage/`. A GitLab Pages copy
(`mskazemi.gitlab.io`) may be kept as a mirror, but GitHub is canonical: all canonical
tags, Open Graph URLs, `sitemap.xml`, `robots.txt`, and `llms.txt` point at
`https://mskazemi.github.io/`.
