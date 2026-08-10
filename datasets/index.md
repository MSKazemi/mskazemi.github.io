# Open HPC datasets — Marconi100 telemetry, job power, thermal hazards

> Three open, CC-BY-4.0 datasets from CINECA's Marconi100 and Marconi A2 Tier-0 supercomputers: 24.8 GB of node telemetry for anomaly detection, 287 MB of per-job power consumption, and 1 GB of thermal-hazard sensor data from 3,312 nodes. Co-authored by Mohsen Seyedkazemi Ardebili. DOIs, scale, licence and citation for each.

Source: <https://mskazemi.com/datasets/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

open data · CC BY 4.0

Roughly 26 GB of real telemetry, free to download and free to use.

Most research on datacenter anomaly detection and power modelling is done on synthetic traces, because production supercomputer telemetry is almost never released. These three datasets are the exception: operational data from **CINECA's Marconi100 and Marconi A2** Tier-0 systems, published openly under CC BY 4.0. I am a co-author on all three and the first author of one.

## What open datasets exist for HPC anomaly detection?

Three, and they cover different questions. **M100 ExaData** is the one to start with for anomaly detection and predictive maintenance; **PM100** is the one for job power prediction and power-aware scheduling; the **HazardNet dataset** is the one for thermal-hazard and cooling research. All three are on Zenodo, all three are CC BY 4.0, and none requires an application or an account.

| Dataset | What it contains | Scale | Period | Licence | DOI |
| --- | --- | --- | --- | --- | --- |
| M100 ExaData | Node power, temperature, CPU frequency, workload and job-scheduler telemetry from Marconi100, via the ExaMon monitoring system | 24.78 GB · 50 files | Mar 2020 – Sep 2022 | CC BY 4.0 | [10.5281/zenodo.7541722](https://doi.org/10.5281/zenodo.7541722) |
| PM100 | Per-job power-consumption records from the same production system, for power-aware scheduling and job power prediction | 287 MB | Marconi100 production | CC BY 4.0 | [10.5281/zenodo.10127767](https://doi.org/10.5281/zenodo.10127767) |
| HazardNet dataset | Inlet and outlet temperature plus power readings from 3,312 compute nodes of Marconi A2, for thermal-hazard prediction | 1.02 GB · 3 files | 14 Jan – 31 Dec 2019 | CC BY 4.0 | [10.5281/zenodo.10050368](https://doi.org/10.5281/zenodo.10050368) |

## What is M100 ExaData?

M100 ExaData is a data-collection campaign on CINECA's Marconi100 Tier-0 supercomputer, described in _Nature Portfolio's Scientific Data_ in 2023. It captures what the machine was actually doing — per-node power draw, temperatures, CPU frequency, workload and job-scheduler state — across roughly two and a half years of production operation, so that anomaly-detection and predictive-maintenance methods can be compared on the same real data instead of on simulations. It is the most-cited paper I have contributed to.

Paper: [Borghesi et al., _Scientific Data_ 10:288 (2023)](https://doi.org/10.1038/s41597-023-02174-3).

## What is PM100 for?

PM100 answers a narrower question: _how much power does a given job actually draw?_ It pairs job records with measured power consumption on a large production system, which is what you need to train a model that predicts a job's power before it runs — the basis for power-aware scheduling, energy budgeting and carbon-aware placement.

Paper: [Antici, Seyedkazemi Ardebili, Bartolini & Kiziltan, SC'23 Workshops (2023)](https://doi.org/10.1145/3624062.3624263).

## What is in the thermal-hazard dataset?

Inlet and outlet temperature and power readings from **3,312 compute nodes** of Marconi A2, covering 14 January to 31 December 2019 — a full year of a Tier-0 machine's thermal behaviour, including the periods where cooling and heat generation fell out of balance. It was released alongside HazardNet, a framework that predicts a forthcoming thermal hazard from a rolling window of those sensors, on a six-hour horizon chosen with the facility manager rather than by grid search.

Paper: [Seyedkazemi Ardebili, Acquaviva, Benini & Bartolini, _Future Generation Computer Systems_ 155:340–353 (2024)](https://doi.org/10.1016/j.future.2024.01.031).

## Are these datasets free to use commercially?

Yes. All three are **CC BY 4.0**, which permits commercial use, redistribution and derivative works as long as the dataset and its paper are credited. There is no application form, no data-use agreement and no account — the files are on Zenodo and download directly. The [AOBench](https://mskazemi.com/projects/aobench/) benchmark built partly on this data is Apache-2.0 and archived at [10.5281/zenodo.21854863](https://doi.org/10.5281/zenodo.21854863).

## How do I cite them?

Cite the Zenodo record _and_ the paper that describes it.

```

@dataset{borghesi2023m100,
  author    = {Borghesi, Andrea and Di Santi, Carmine and Molan, Martin and
               Seyedkazemi Ardebili, Mohsen and Mauri, Alessio and Guarrasi, Massimiliano
               and Galetti, Daniela and Bartolini, Andrea},
  title     = {M100 dataset: time-aggregated data for anomaly detection},
  year      = {2023},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.7541722},
}

@article{borghesi2023exadata,
  author  = {Borghesi, Andrea and Di Santi, Carmine and Molan, Martin and
             Seyedkazemi Ardebili, Mohsen and others},
  title   = {M100 ExaData: a data collection campaign on the CINECA's
             Marconi100 Tier-0 supercomputer},
  journal = {Scientific Data},
  volume  = {10}, number = {1}, pages = {288}, year = {2023},
  doi     = {10.1038/s41597-023-02174-3},
}

@inproceedings{antici2023pm100,
  author    = {Antici, Francesco and Seyedkazemi Ardebili, Mohsen and
               Bartolini, Andrea and Kiziltan, Zeynep},
  title     = {PM100: A Job Power Consumption Dataset of a Large-scale
               Production HPC System},
  booktitle = {Proceedings of the SC'23 Workshops},
  pages     = {1812--1819}, year = {2023},
  doi       = {10.1145/3624062.3624263},
}

@article{ardebili2024hazardnet,
  author  = {Seyedkazemi Ardebili, Mohsen and Acquaviva, Andrea and
             Benini, Luca and Bartolini, Andrea},
  title   = {HazardNet: A thermal hazard prediction framework for datacenters},
  journal = {Future Generation Computer Systems},
  volume  = {155}, pages = {340--353}, year = {2024},
  doi     = {10.1016/j.future.2024.01.031},
}

```

## What has been built on this data?

Peer-reviewed work using these datasets includes [GRAAFE](https://doi.org/10.1016/j.future.2024.06.032), a graph neural network that anticipates node anomalies and is served online through a Kubeflow pipeline; [HazardNet](https://doi.org/10.1016/j.future.2024.01.031), the thermal-hazard predictor above; [ThermADNet](https://doi.org/10.1016/j.future.2025.108311), a thermal anomaly detection system; and [AOBench](https://mskazemi.com/projects/aobench/), a benchmark for LLM agents operating HPC systems whose environments are partly reconstructed from this telemetry. The [full publication list](https://mskazemi.com/publications/) has DOIs and BibTeX for all of them.

Dataset sizes, licences and publication dates verified against the Zenodo API on 2026-08-10. Paper identifiers resolved through Crossref. If you use these datasets and hit a problem with them, [tell me](https://mskazemi.com/#contact) — I would rather fix the record than have it quietly mis-cited.

// more

## The work built on this data.
