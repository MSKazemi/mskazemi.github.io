# Mohsen Seyedkazemi Ardebili — Autonomous AI for Infrastructure

> Mohsen Seyedkazemi Ardebili builds autonomous AI systems that act on infrastructure — LLM-orchestrated Kubernetes agents, anomaly detection on Tier-0 HPC clusters, and end-to-end MLOps. Research Fellow, University of Bologna.

Source: <https://mskazemi.com/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

Research Fellow · University of Bologna

I build autonomous AI that acts on infrastructure.

Not a chatbot that explains your cluster — systems that observe it, reason about failures, and execute remediation, with a human at the gate. LLM agents for Kubernetes & HPC, anomaly detection on Tier-0 supercomputers, and the MLOps to run it in production.

- LOC Bologna, IT

- EXP 7 yrs critical infra → PhD HPC

- OSS KubeIntellect · AOBench · YazSes

Deep dives [KubeIntellect](https://mskazemi.com/projects/kubeintellect/) [NovaFabric](https://mskazemi.com/projects/novafabric/) [AOBench](https://mskazemi.com/projects/aobench/)

telemetry in → root-cause reasoning → gated action → back to telemetry

// profile

## From a power plant's networks to the control plane of a datacenter.

I spent seven years as the **IT & Network Administrator** of a 1,000+ MW combined-cycle power plant — running the enterprise IT and network infrastructure across eleven operational zones, where downtime is not an abstraction. Then I did a PhD in High-Performance Computing at the University of Bologna.

That path gives me a lens most ML researchers don't have: I care about uptime, observability, and correctness _in production_ — not just benchmark numbers. Today I design autonomous control for infrastructure: systems that detect failures, reason about root cause, and propose or execute remediation behind human-approval gates.

I'm a Postdoctoral Research Fellow at DEI, University of Bologna, working across EU Horizon projects (I led the UNIBO contribution to DECICE; I now lead SEANERGYS work on ExaMLOps). And I ship — open-source tools and products that real people run.

// impact — verified 2026-08-10

## The work is cited, and the citations are accelerating.

More citations arrived in the twenty months from January 2025 than in the preceding eighteen years combined. Every figure below is read from a primary source — Google Scholar, Crossref, the GitHub API, PyPI — and kept in [a single JSON file](https://mskazemi.com/data/metrics.json) that generates this block. Nothing here is typed by hand.

Sources: [Google Scholar](https://scholar.google.com/citations?user=xP64pZsAAAAJ), [ORCID](https://orcid.org/0000-0002-1166-6559), [OpenAlex](https://openalex.org/A5013086540), Crossref, the GitHub API and PyPI — all read on 2026-08-10. The full publication list, with DOIs and BibTeX, is on the [publications page](https://mskazemi.com/publications/); the open datasets behind the research are on the [datasets page](https://mskazemi.com/datasets/).

// systems — research-grade work, in the open

## Things that act, with the receipts.

A modular, LLM-orchestrated multi-agent framework for **end-to-end Kubernetes operations** — root-cause analysis, diagnosis, and human-gated cluster actions across the full API surface (read, write, exec, delete, RBAC, lifecycle). A stateful LangGraph supervisor coordinates domain agents; a Code-Generator agent synthesises and validates new tools at runtime. Published in the _Journal of Grid Computing_ (2026, 24(3):17).

- Stateful LangGraph supervisor + PostgreSQL checkpoints

- Human-in-the-loop approval on every mutating operation

- Runtime tool synthesis with AST validation and a Kubernetes API whitelist

- Deployed on Azure AKS — OpenAI-compatible FastAPI backend

```

$ kq "why is payments-api crashlooping?"
→ inspecting pods, events, logs…
root cause: OOMKilled — memory
  limit 256Mi exceeded on restart.
proposed fix: raise limit to 512Mi
approve? [y/N] ▍

```

Agent Operations Benchmark — a trace-driven, role-aware, RBAC-enforced benchmark for LLM agents that operate HPC systems. It asks the blunt question: _can an autonomous agent be trusted to run a supercomputer?_ — and scores the answer against real operator roles and hard policy constraints.

- 88 tasks across 10 question categories × 5 operator roles

- 29 deterministic environment bundles — 23 synthetic, 6 built from real Marconi100 telemetry

- Permission-enforced: a policy violation hard-fails the task, whatever the answer said

- 12 scorers over 6 dimensions, rolled into a CLEAR scorecard (Cost · Latency · Efficacy · Assurance · Reliability)

- 16 model systems evaluated on the 59-task dev split, every headline number tied to a frozen run ID

Graph anomaly-anticipation for exascale HPC — topology-aware node-failure prediction running in production on CINECA's Tier-0 Marconi100, published in _FGCS_.

- Models the machine as a graph and predicts, per node, the probability of an anomaly in a future window

- Benchmarked by AUC against per-node DNN, gradient-boosting, random-forest and decision-tree baselines

- Trained offline, then served online as a Kubeflow pipeline reading live ExaMon telemetry over MQTT

- The paper reports negligible added overhead versus running the monitoring system alone

Thermal-hazard prediction for datacenters — multi-modal deep learning forecasting thermal failures fast enough to act, with explanations operators trust.

- A year of inlet/outlet temperature and power telemetry from 3,312 nodes of CINECA's Marconi A2

- Temporal Convolutional Network, LSTM and SVM models over a rolling time window

- Six-hour prediction horizon — chosen with the facility manager, not with a grid search

- Training data published openly on Zenodo so the result can be reproduced

An end-to-end MLOps platform for HPC workload management, built for the EuroHPC **SEANERGYS** project and now running in production at LuxProvide on the MeluXina supercomputer. Architect, lead designer and main developer; WP3 task lead at Bologna. It is **model-agnostic and multi-tenant** — any of the sixteen consortium partners registers a model and the platform auto-discovers and operationalises it (train → version → govern → serve → monitor) without ever owning the model code. The whole loop, on a real supercomputer, behind an operator approval gate.

- Auto-discovery training pipelines in Prefect: every registered model × dataset pair runs train → evaluate → log → promote

- Slurm adapter for HPC job orchestration; a DataPlane bridge carries messages off the machine

- MLflow registry with a multi-stage lifecycle and a YAML model registry with per-environment overlays

- Ray Serve multi-model serving with batched inference; MinIO for artifacts

- A sysadmin approval gate stands between a promoted model and the serving fleet — nothing goes live unattended

- Prometheus, Grafana and Loki for metrics and logs; React 19 + FastAPI dashboard; `exa` operator CLI

The operator's companion for KubeIntellect — a CLI and Python SDK (`kq`) exposing the full agent API with streaming output and a human-approval UX, built for CI/CD.

- Full KubeIntellect API coverage from the terminal

- Streaming Rich TUI · pipeline-friendly output

// ships — products under [NovaFabric](https://github.com/NovaFabric)

## Research is half of it. I also ship.

Privacy-first, local-first tools — built to be installed and used, not just cited.

The reproducibility and trust layer for AI systems — an open-source, self-hosted toolkit that turns any agent or model run into a **portable, signed, replayable evidence capsule**, captured with no code changes. Observability tells you what happened; NovaFabric tells you _what would happen if you ran it again, today._

- Zero-instrumentation capture · four honest replay modes (exact / mocked / semantic / forensic)

- Cryptographic seal: DSSE signature + RFC 3161 timestamp + append-only Merkle log

- Structured run-to-run diff as a CI regression gate; signed evidence bundles verify without it installed

- Runs offline from a laptop to an HPC cluster — no cloud, no account

- 36 releases on PyPI · 176 commits · Apache-2.0 — experimental, and labelled as such

Hold a key, speak, release — fully **on-device** voice dictation that types into any app and runs voice commands. No cloud, no subscription, no data leaving your machine. Shipped and maintained across multiple releases.

- On-device faster-whisper (CPU int8) — no GPU, no network, no account

- Also transcribes recordings and captures whole meetings with speaker labels

- Editor/terminal voice commands; Neovim LSP context; accessibility-first design

- Linux · macOS · Windows — APT, Snap, pipx/PyPI

- 23 releases on PyPI · 401 commits · 10 contributors

A meta-framework for taking a vague idea to production without losing context, evidence, or decision rationale — for humans and AI agents alike.

- VisionForge → SOTAForge → DesignForge → BuildForge

- Deterministic verification gates: schema, evidence, traceability — no LLM in the gate

- `v2p` CLI + FastAPI/HTMX governance portal

// research

## Peer-reviewed, in real venues.

- Journal of Grid Computing · 2026 · 13 citations [KubeIntellect: A Modular LLM-Orchestrated Agent Framework for End-to-End Kubernetes Management](https://doi.org/10.1007/s10723-026-09837-6)

- Scientific Data (Nature Portfolio) · 2023 · 64 citations [M100 ExaData: A Data Collection Campaign on CINECA's Marconi100 Tier-0 Supercomputer](https://doi.org/10.1038/s41597-023-02174-3)

- SC'23 Workshops (ACM) · 2023 · 33 citations [PM100: A Job Power Consumption Dataset of a Large-Scale Production HPC System](https://doi.org/10.1145/3624062.3624263)

- Future Generation Computer Systems · 2024 · 23 citations [GRAAFE: GRaph Anomaly Anticipation Framework for Exascale HPC Systems](https://doi.org/10.1016/j.future.2024.06.032)

- Future Generation Computer Systems · 2026 · first author [Elevating Datacenter Resilience with ThermADNet: A Thermal Anomaly Detection System](https://doi.org/10.1016/j.future.2025.108311)

- DATE · 2021 · 9 citations [Prediction of Thermal Hazards in a Real Datacenter Room Using Temporal Convolutional Networks](https://doi.org/10.23919/date51398.2021.9474116)

[All 17 publications, with DOIs and BibTeX →](https://mskazemi.com/publications/)

### Program committee

PDP 2025 · PDP 2026 · AsHES 2026

### Reviewer

IEEE TCAD · FGCS · J. Grid Computing · SC · ACM CF · DATE · PDP · AsHES

### Supervision

2 PhD co-advisees · 5 MSc theses · Lab of Big Data Architectures, UniBo

// stack

## The toolchain behind the work.

### Agentic AI / ML

### MLOps & serving

### Cloud-native & infra

### Observability

### HPC

### Foundations

// hire me

## Freelance engagements — infrastructure you can trust.

Fixed-price starter audits to begin low-risk, or project work at a senior day rate. Remote, EU. I build systems your team can maintain after I'm gone — not black boxes.

### Kubernetes reliability & AIOps

Health-checks, observability, hardening, incident root-cause, and ops automation with human-approval gates.

### MLOps & ML in production

Get models out of the notebook: registry, serving, drift detection, governed retraining, monitoring — the stack I run in production on EuroHPC.

### Production LLM agents

Agents that act on real systems — tool-use, human-in-the-loop safety, tracing, and an audit trail you can defend.

Full details, how an engagement runs, and the questions people usually ask → [**mskazemi.com/hire**](https://mskazemi.com/hire/). Free 30-minute scoping call → [mohsen.seyedkazemi@gmail.com](mailto:mohsen.seyedkazemi@gmail.com?subject=Freelance%20enquiry).

// contact

## Let's build infrastructure that runs itself.

Open to research collaborations, open-source work, and industry partnerships in AI infrastructure, HPC, and autonomous operations.
