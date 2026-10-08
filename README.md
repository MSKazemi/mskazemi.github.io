# Personal website — mskazemi.com

The public personal website of **Mohsen Seyedkazemi Ardebili**, hosted by
GitHub Pages from this repository. **Canonical URL:** https://mskazemi.com/

This is a static HTML/CSS/JavaScript site with no build step. The workflow
`.github/workflows/deploy-pages.yml` deploys the root to GitHub Pages after
a merge/push to `main`. `mskazemi.github.io` redirects to the custom domain.

## Source of truth and review

- The canonical professional headline is **AI Platform & Agentic Systems Engineer · Independent Consultant**. Career facts, confidentiality boundaries, and current positioning are governed by the private Brain repository, especially `work/playbook/BRAND.md` and `work/playbook/cv.json`.
- Use **Italy** as the primary *display* location in the homepage hero, commercial page headings, quick facts and social previews. The work model is **remote across Europe and internationally**, with working-hour overlap agreed individually.
- Keep the accurate city **Bologna, Italy** in detailed About prose, relevant factual FAQs and `Person`/address structured data. Display-location choices must never change the underlying factual residence or invent a second office.
- Use **Europe/Rome (CET/CEST)** for timezone information; “CET” alone is seasonally misleading.
- Synchronize HTML pages and their same-path `index.md` alternatives, plus `llms.txt` and `humans.txt` when availability or location copy changes.
- Claims about technologies, project status, and outcomes must be checked against the corresponding project source/approved claims. Do not publish confidential current-client details.
- The root `sitemap.xml` and `robots.txt` identify the canonical website and additional independently deployed documentation sitemaps. Update `lastmod` when substantive content changes, not to manufacture freshness.

## Review before merging

Check the visible homepage, About and Hire pages at desktop and mobile widths.
Confirm that the copy, social descriptions, Markdown alternatives and JSON-LD
agree, the structured data remains valid, and no client-identifying information
was introduced. Pull requests are review-only: merging into `main` deploys
publicly through GitHub Actions.
