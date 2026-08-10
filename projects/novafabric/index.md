# NovaFabric — Replayable AI Infrastructure · Mohsen Seyedkazemi Ardebili

> NovaFabric turns any AI agent or model run into a portable, signed, replayable evidence capsule — captured with no code changes. Open-source, self-hosted.

Source: <https://mskazemi.com/projects/novafabric/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

open source · Apache-2.0 · self-hosted

Replayable AI infrastructure.

An open-source, self-hosted toolkit that turns any AI agent or model run into a **portable, signed, replayable evidence capsule** — captured with no code changes and owned entirely by you. Observability tells you _what happened_; NovaFabric answers the harder question — _what would happen if I ran this again, today?_

- INSTALL pip install novafabric

- RUNS laptop → Docker → K8s → SLURM

- OFFLINE no cloud · no account

// the problem

## When an AI run breaks, every layer is suspect.

A modern AI system isn't a single model — it's a drifting graph of prompts, models, tools (HTTP APIs, MCP servers, shell commands), memory/RAG context, datasets, environments, and execution targets (laptop, container, K8s pod, SLURM job). Each layer drifts at its own rate, and when something misbehaves you can't tell which layer moved.

The ecosystem has excellent telemetry for _what happened_ — and almost nothing for _what would happen if I ran this again, under the same conditions, today._ Reproducibility isn't a nice-to-have: it's the precondition for debugging, regression detection, governance, and trust.

// what it does

## Capture → Seal → Replay → Diff → Audit.

### Asset Registry

The identity layer — `name@version` for models, agents, prompts, tools, datasets, evals, and deployments.

### Run Capsule

A portable per-run snapshot — inputs, outputs, model calls, tool calls, a full environment lock, and the trace — written on success _and_ failure. A folder you own, not a row in someone's cloud.

### Replay Engine

Reconstruct a past run in four honest modes — `exact`, `mocked`, `semantic`, and `forensic` — each making a specific, falsifiable promise.

### Lineage Graph

Causation — which assets and prior runs contributed to this run, and what depends on it.

### Evidence Bundle

A signed, audit-ready export — capsule + lineage + attestations + redaction proof — that a third party can verify _without NovaFabric installed_.

### Zero-instrumentation capture

`nova capture python my_agent.py` — per-SDK hooks, wire-level hooks (httpx/requests/aiohttp/urllib3), and transparent HTTP/MCP proxies record any command. No application changes; all patches removed after the run.

// the honest contract

## Four replay modes — each a falsifiable promise.

### exact

Deterministic re-execution against the same local model, container, data, and environment — bit-identical where deterministic.

### mocked

Re-run the command with every model/tool call served from the capsule cache — no model called, no tool invoked, fully deterministic.

### semantic

Re-execute and compare _meaning_ (via a judge model), not tokens — for remote closed-weight LLMs whose weights and routing change without notice.

### forensic

Inspect the captured run without re-executing anything — read-only, no network, no side effects.

The taxonomy is deliberately honest: NovaFabric does **not** claim exact replay of remote closed-weight models — that's what `semantic` and `mocked` are for. Making the promise falsifiable is a feature.

// trust & governance

## Sealed so it can't be silently altered.

### NovaSeal — three independent proofs

Every sealed capsule binds a DSSE signature (ECDSA P-256 / Ed25519), an RFC 3161 trusted timestamp (eIDAS-qualified path for the EU), and an append-only Merkle log with inclusion proofs.

### Pluggable signing backends

Local keys, AWS KMS, Azure Key Vault, GCP KMS, or keyless Sigstore (Fulcio + Rekor). `nova verify` re-checks signature, timestamp, and log integrity.

### Policy & maker-checker

An OPA/Rego policy engine (allow / deny / require-human / require-batch) and dual-approval with cryptographic separation of duties — proposer ≠ approver, enforced by key fingerprint.

### Compliance exporters

WORM retention (S3 Object Lock, Azure immutable blob, GCS Bucket Lock) with legal holds, plus exporters for EU AI Act Annex IV, NIST AI RMF, GDPR RoPA, and CycloneDX AI-BOM.

// standards-based, not reinvented

## Adopts open standards; invents only two formats.

Only the Run Capsule and Evidence Bundle are new on-disk formats — everything else adopts an existing open standard, so NovaFabric feeds your observability stack rather than replacing it.

**Design slogan:** local-first now, distributed-ready always, cluster-scale later — a one-node run is the smallest case of a distributed run. Built in Python 3.12+ with a Go collector tier; server mode, collector, object store, and dashboard are marked _experimental_, and cross-cluster federation is design-intent, not shipped.

// more

## Explore the rest of the lab.
