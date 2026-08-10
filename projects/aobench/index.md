# AOBench — Agent Operations Benchmark for HPC · Mohsen Seyedkazemi Ardebili

> AOBench is a trace-driven, role-aware, RBAC-enforced benchmark for evaluating LLM agents on realistic HPC operations tasks. By Mohsen Seyedkazemi Ardebili.

Source: <https://mskazemi.com/projects/aobench/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

benchmark · research in preparation

Agent Operations Benchmark for HPC.

A **trace-driven, role-aware, RBAC-enforced** benchmark for LLM agents in HPC facilities. It asks a blunt question — _can an autonomous agent actually be trusted to operate a supercomputer?_ — and answers it against real operational traces, real operator roles, and hard policy constraints.

- SCOPE 88 tasks · 29 environments · 16 systems

- DESIGN 5 roles × 10 categories · 12 scorers

- STACK Python · MCP · SLURM

// why it exists

## "Helpful in a chat" is not "safe on a cluster."

General LLM-agent benchmarks reward answering questions. Running an HPC facility is a different job: the same action is correct for one operator role and a policy violation for another, and a single unauthorised command can take down a shared national resource. Evaluating agents for that world needs realistic traces, explicit roles, and a scorer that treats a policy breach as a hard failure — not a rounding error on an accuracy score.

AOBench is built to measure **operational trustworthiness**, not conversational fluency — so a facility can reason about whether an agent is anywhere near deployment-ready before it ever touches production.

// what it measures

## Trace-driven, role-aware, policy-scored.

### Realistic task matrix

88 tasks across ten question categories and five operator roles, drawn from real HPC operational scenarios rather than synthetic puzzles.

### Completion-under-Policy scorer

A task only counts if it's completed _within the operator's authority_ — any RBAC violation is a hard fail, no matter how "correct" the answer looks.

### CLEAR scorecard

12 scorers over six evaluation dimensions, aggregated into five reported axes — **C**ost · **L**atency · **E**fficacy · **A**ssurance · **R**eliability — so trade-offs stay visible instead of collapsing into one number.

### Snapshot environments

29 deterministic environment bundles reconstruct real cluster state — 23 synthetic and 6 built from real Marconi100 ExaData telemetry — so every agent meets identical conditions.

// the scale of it

## Built so the answer is reproducible.

16 model systems — 2 hosted through the OpenAI API, 13 local models through Ollama, and a tool-free baseline — were run over the 59-task development split, with a frozen run ID behind every headline number so any result can be traced back to the exact run that produced it. Six of the 29 environments are reconstructed from real Marconi100 telemetry, which is what separates this from a synthetic puzzle set.

**Status.** AOBench is an active research project; the associated paper is _submitted, not accepted_, and per-model results are not published here — they belong in the paper, with their methodology attached. The code is open (Apache 2.0, v0.4.0) and archived with a DOI at [10.5281/zenodo.21854863](https://doi.org/10.5281/zenodo.21854863).

// more

## Explore the rest of the lab.
