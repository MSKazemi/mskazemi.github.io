# About Mohsen Seyedkazemi Ardebili — AI Infrastructure &amp; MLOps Engineer, Bologna

> Mohsen Seyedkazemi Ardebili, Research Fellow at the University of Bologna: AI SRE, AIOps, MLOps and HPC, after seven years running a 1,000 MW plant's IT.

Source: <https://mskazemi.com/about/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

Research Fellow · University of Bologna · Bologna, Italy

AI infrastructure engineer. I build systems that operate infrastructure, not systems that talk about it.

I spent seven years as the IT and network administrator of a combined-cycle power plant of more than 1,000 MW, where an outage is measured in megawatts rather than in error budgets. Then I did a PhD in high-performance computing at the **University of Bologna** and stayed on as a research fellow. Today I work at the seam between those two worlds: **AI SRE** and **AIOps** for Kubernetes, **MLOps** that survives contact with production, and machine learning that predicts failures on **Tier-0 supercomputers**.

- BASED Bologna, Italy · remote worldwide

- BASED Bologna, Italy (CET) · remote worldwide

- LANGUAGES Persian · Azerbaijani · Turkish (native) · English (professional) · Italian (A2)

// the short version

## Operations first, research second, and the two keep arguing.

Most people arrive at AI infrastructure from machine learning and discover operations later. I arrived the other way round. My first career was keeping an industrial plant's networks, servers and control systems alive — a place with no staging environment, where the cost of a bad change is not a rolled-back deploy but a unit off the grid. That background is why I am sceptical of autonomy without a gate, and why the systems I build ask a human before they do anything they cannot undo.

The research half came second. My doctorate at the University of Bologna was on the design, analysis and management of high-performance computing systems, working with the operational telemetry of CINECA's Tier-0 supercomputers. That work has continued through a run of EU-funded projects — DECICE, Graph-Massivizer, EUROPEAN PILOT, REGALE, EPI SGA1 and, currently, the EuroHPC-JU project **SEANERGYS**, where I am the architect and lead developer of the MLOps platform and a work-package task lead.

What connects the two is a single question I keep coming back to: _how much of an operator's judgement can a machine take over, and how do you prove afterwards that it was right to?_ Every project below is one attempt at an answer.

// what i actually do

## Four things, and they are all the same thing.

### AI SRE & AIOps for Kubernetes

Agents that investigate a live cluster with real tools — logs, metrics, the API surface — reach a root cause, and then apply the fix only after a human approves it. Built as [KubeIntellect](https://mskazemi.com/projects/kubeintellect/), peer-reviewed in the _Journal of Grid Computing_.

### Evidence and audit for AI systems

Capturing what an AI run actually did, sealing it, and replaying it later — so a decision can be re-examined rather than merely trusted. Built as [NovaFabric](https://mskazemi.com/projects/novafabric/).

### Measuring agents on real operations work

Benchmarks are usually chat transcripts. [AOBench](https://mskazemi.com/projects/aobench/) is trace-driven and role-aware, with permissions enforced, because an agent that cannot be told "no" is not deployable.

### Anomaly prediction on supercomputers

Graph and sequence models that anticipate node failures and thermal hazards on Tier-0 machines, published in _FGCS_ and built on datasets my group released through _Nature Scientific Data_.

### MLOps that survives production

Registry, serving, drift detection, governed retraining, observability. The stack I run for a EuroHPC project, not a diagram from a blog post.

### Open source, on purpose

Everything above ships publicly. [YazSes](https://mskazemi.com/projects/yazses/), an offline voice-dictation tool, is the outlier — it exists because Linux still has no decent dictation, and it is the project with real outside contributors.

// record

## Published, reviewed, and used by other people.

Selected work: _M100 ExaData_, a data-collection campaign on CINECA's Marconi100 Tier-0 supercomputer (_Nature Scientific Data_, 2023) · _PM100_, a job power-consumption dataset of a large-scale production HPC system (SC'23 workshops) · _GRAAFE_, graph anomaly anticipation for exascale HPC (_FGCS_, 2024) · _HazardNet_, thermal hazard prediction for datacenters (_FGCS_, 2024) · multi-level anomaly prediction in a Tier-0 datacenter (_ACM Computing Frontiers_, 2022) · _KubeIntellect_ (_Journal of Grid Computing_, 2026). The complete and current list is on [Google Scholar](https://scholar.google.com/citations?user=xP64pZsAAAAJ) and [ORCID](https://orcid.org/0000-0002-1166-6559).

**Impact, read from Google Scholar on 2026-08-10:** 218 citations, h-index 8, i10-index 7, across 17 published or accepted peer-reviewed works. The shape of it matters more than the total — 9 citations in 2022, 15 in 2023, 24 in 2024, 76 in 2025, and 65 in the first seven months of 2026. More arrived in the last twenty months than in the preceding eighteen years combined. (OpenAlex reports a lower figure because it indexes fewer venues; both are correct for their own index.)

On the service side: programme-committee member for PDP 2025, PDP 2026 and AsHES 2026, and a reviewer for IEEE TCAD, _FGCS_, the _Journal of Grid Computing_, SC, ACM CF, DATE, PDP and AsHES. I co-advise two PhD students and have supervised five completed MSc theses at the Lab of Big Data Architectures in Bologna.

// elsewhere

## The same person, everywhere.

If you found a profile that claims to be me, this is the list it should be on. Anything not here is not mine.

- [GitHub — MSKazemi](https://github.com/MSKazemi) · [GitLab](https://gitlab.com/mskazemi) · [PyPI](https://pypi.org/user/MSKazemi/)

- [LinkedIn](https://www.linkedin.com/in/mskazemi/) · [Mastodon](https://mastodon.social/@mskazemi) · [X](https://x.com/mohsenardebili)

- [Google Scholar](https://scholar.google.com/citations?user=xP64pZsAAAAJ) · [ORCID 0000-0002-1166-6559](https://orcid.org/0000-0002-1166-6559) · [dblp](https://dblp.org/pid/282/6179) · [OpenAlex](https://openalex.org/A5013086540) · [Semantic Scholar](https://www.semanticscholar.org/author/2046824417)

- [University of Bologna staff page](https://www.unibo.it/sitoweb/mohsen.seyedkazemi/en) · [Wikidata Q140935575](https://www.wikidata.org/wiki/Q140935575)

- [Publications](https://mskazemi.com/publications/) — the full list, with DOIs, citation counts and BibTeX

// next

## Got infrastructure that needs to run itself?

I take remote freelance and consulting engagements worldwide — starting small, on a fixed price, so neither of us has to guess.
