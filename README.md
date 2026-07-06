<h1 align="center">Mohsen Seyedkazemi Ardebili</h1>

<p align="center">
  <b>Platform Engineer · AIOps · MLOps · LLM-Orchestrated Infrastructure</b><br/>
  Research Fellow, University of Bologna · Bologna, Italy
</p>

<p align="center">
  <a href="https://linkedin.com/in/mskazemi"><img src="https://img.shields.io/badge/LinkedIn-mskazemi-0A66C2?style=flat&logo=linkedin&logoColor=white" /></a>
  <a href="https://scholar.google.com/citations?user=xP64pZsAAAAJ"><img src="https://img.shields.io/badge/Scholar-179%20citations%20·%20h--index%207-4285F4?style=flat&logo=googlescholar&logoColor=white" /></a>
  <a href="https://orcid.org/0000-0002-1166-6559"><img src="https://img.shields.io/badge/ORCID-0000--0002--1166--6559-A6CE39?style=flat&logo=orcid&logoColor=white" /></a>
  <a href="https://kubeintellect.com"><img src="https://img.shields.io/badge/KubeIntellect-kubeintellect.com-3E0097?style=flat" /></a>
  <a href="https://arxiv.org/abs/2509.02449"><img src="https://img.shields.io/badge/arXiv-2509.02449-b31b1b?style=flat&logo=arxiv&logoColor=white" /></a>
</p>

---

I build autonomous AI systems for datacenter-scale infrastructure — LLM-orchestrated Kubernetes agents, deep learning anomaly detection on Tier-0 HPC clusters, and hybrid HPC/cloud orchestration pipelines. Seven years of hands-on ops in mission-critical industrial environments before a PhD in HPC systems at the University of Bologna gives me a different lens: I care about correctness, observability, and production trust, not just benchmark numbers.

---

## Featured Project

### [KubeIntellect](https://github.com/MSKazemi/kubeintellect) — Autonomous Kubernetes Operations

> LLM-orchestrated multi-agent framework for root cause analysis, diagnosis, and human-gated cluster operations across the full Kubernetes API surface.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://github.com/MSKazemi/kubeintellect)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat&logo=langchain&logoColor=white)](https://github.com/MSKazemi/kubeintellect)

**Architecture:**
- LangGraph FSM supervisor with PostgreSQL checkpoints and human-in-the-loop approval gates
- Dynamic Code-Generator agent: sandboxed tool synthesis and validation at runtime
- Modular domain agents: logs, metrics, RBAC, lifecycle, scheduling, exec, proxy
- OpenAI-compatible FastAPI backend + LibreChat UI

---

## Other Projects

| Project | Description | Key Metrics | Stack |
|---------|-------------|-------------|-------|
| [kube_q](https://github.com/MSKazemi/kube_q) | CLI + Python SDK for KubeIntellect | Streaming responses, Rich TUI | Python |
| [mcp-zenodo](https://github.com/MSKazemi/mcp-zenodo) | MCP server exposing Zenodo to LLM tool calls | MCP-compliant | Python, FastAPI |
| [AOBench](https://github.com/MSKazemi/aobench) | Agent Operations Benchmark — evaluates LLM agents on HPC operational tasks | 80 tasks · 26 snapshot envs · trace scoring | Python, FastAPI, MCP |
| [GRAAFE](https://github.com/MSKazemi/GRAAFE) | Graph anomaly anticipation for exascale HPC | AUC 0.91, 49 racks, ~1000 nodes | Python, GCN |
| [HazardNet](https://github.com/MSKazemi/HazardNet) | Thermal hazard prediction for datacenters | <100ms inference, <0.2% CPU | Python, TCN/LSTM |
| [AI4HPC](https://github.com/MSKazemi/AI4HPC) | AIOps pipeline: Prometheus → Kubeflow → MLflow | F1 0.99, ~87ms latency | Python, Kubeflow |

---

## Research

**PhD:** Design, Analysis, and Management of High-Performance Computing Systems · University of Bologna (2018–2022)

**Focus:** Autonomous infrastructure control · HPC/cloud convergence · LLM agents for ops · Datacenter anomaly detection

**EU Projects:** DECICE · Graph-Massivizer · EUROPEAN PILOT · REGALE · EPI SGA1 · SEANERGYS

**Scholar:**

| Citations | h-index | i10-index |
|-----------|---------|-----------|
| 179 (154 since 2021) | 7 | 6 |

### Selected Publications

| Title | Venue | Year | Citations |
|-------|-------|------|-----------|
| [KubeIntellect: A Modular LLM-Orchestrated Agent Framework for Kubernetes Management](https://arxiv.org/abs/2509.02449) | arXiv | 2025 | — |
| [M100 ExaData: A Data Collection Campaign on CINECA's Marconi100 Tier-0 Supercomputer](https://www.nature.com/articles/s41597-023-02174-3) | *Nature Scientific Data* | 2023 | 50 |
| PM100: A Job Power Consumption Dataset of a Large-Scale Production HPC System | SC'23 Workshops | 2023 | 21 |
| [GRAAFE: Graph Anomaly Anticipation Framework for Exascale HPC Systems](https://github.com/MSKazemi/GRAAFE) | *Future Generation Computer Systems* | 2024 | 17 |
| HazardNet: Thermal Hazard Prediction Framework for Datacenters | *FGCS* | 2024 | — |
| Multi-level Anomaly Prediction in Tier-0 Datacenter | *ACM Computing Frontiers* | 2022 | — |

[All publications →](https://scholar.google.com/citations?user=xP64pZsAAAAJ)

---

## Stack

**Platform & Infrastructure**

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat&logo=helm&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)

**AI / ML**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat&logo=langchain&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Kubeflow](https://img.shields.io/badge/Kubeflow-1570EF?style=flat)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)

**Observability**

![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=flat&logo=opentelemetry&logoColor=white)

---

## Academic Service

**PC Member:** PDP 2025 · PDP 2026 · AsHES 2026

**Reviewer:** IEEE TCAD · FGCS · Journal of Grid Computing · SC · ACM CF · DATE · PDP · AsHES

**Supervision:** 2 PhD co-advisees (ongoing) · 5 MSc theses completed · Lab of Big Data Architectures, UniBo (2020–2024)

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=MSKazemi&show_icons=true&hide_border=true&theme=default&count_private=true" height="130" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MSKazemi&layout=compact&hide_border=true&theme=default" height="130" />
</p>
