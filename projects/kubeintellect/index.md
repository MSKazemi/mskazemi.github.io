# KubeIntellect — Human-Governed AI SRE for Kubernetes · Mohsen Seyedkazemi Ardebili

> KubeIntellect is a human-governed AI SRE for Kubernetes: an LLM-orchestrated operator that investigates the live cluster with real tools, explains what it found, and — with your approval — fixes it. By Mohsen Seyedkazemi Ardebili.

Source: <https://mskazemi.com/projects/kubeintellect/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

flagship · Journal of Grid Computing 2026

A human-governed AI SRE for Kubernetes.

You ask a question in plain English; it investigates your cluster with real tools — `kubectl`, Prometheus, Loki — explains what it found, and, _with your approval_, fixes it. It **acts on the cluster, not just talks about it** — and every mutating action pauses for explicit human sign-off before anything runs.

- LANG Python · LangGraph · FastAPI

- LICENSE AGPL-3.0 or commercial

- PYPI kubeintellect · kube-q

// the problem

## An assistant is not an operator.

Running Kubernetes at scale is a continuous operational burden. Failures are diverse — crash loops, OOM kills, image-pull errors, pending pods, missing endpoints, admission rejections — and the knowledge to resolve them is spread across the cluster API, metrics, and logs. On call at 2 a.m., an engineer bridges those tools by hand, correlates in their head under pressure, and hopes the fix works. Nothing is remembered, so the same fault pages someone else next week.

First-generation LLM ops assistants share three structural weaknesses:

### The assistant today

**Reactive.** It does nothing until a human notices a problem and types a question — a slow-burn failure at 3 a.m. is invisible until someone looks.

**Uniformly expensive.** It calls one large model on every turn, even for trivial "is this even a problem?" triage a compiled rule could answer for free.

**Unauditable.** When an agent touches a cluster, a chat transcript is not an audit log — you can't prove the record wasn't altered after the fact.

### KubeIntellect

**Continuous perception.** Zero-token detectors watch the event stream and recognise known failures at no LLM cost — catching problems _before_ they page anyone.

**Cost-aware reasoning.** A tiered "Cortex" reserves the most capable model for final synthesis and uses lighter compiled steps for triage.

**Provably auditable.** A hash-chained, tamper-evident flight recorder makes every decision deterministically replayable, with rollback points on any change.

// what it is

## It figures out where to look.

KubeIntellect inverts conventional Kubernetes tooling: instead of you knowing what to look for and the tool fetching it, **you describe what's wrong and it figures out where to look** — correlating logs, metrics, events, and configuration across many signals in parallel. Operators don't need to know `kubectl` syntax, PromQL, or LogQL.

For a simple question, you get a direct plain-English answer. For a genuine outage it runs a **root-cause analysis**: it fans out specialist agents — one each for the pod, its events, its logs, and its metrics — and synthesises their findings into one structured root cause, with supporting _and_ conflicting evidence, and a recommended change shown as a dry-run diff you approve before it applies.

// architecture

## What I built.

### Coordinator + parallel investigation

A planner/router decides, per query, whether to answer directly, run a targeted single-resource deep dive, or fan out a full root-cause investigation across concurrent domain specialists.

### Human-in-the-loop gate

Destructive operations pause mid-execution for explicit approve/deny. Cascading-blast actions (delete namespace/PV/CRD, drain, resource changes) always require confirmation — even in auto-approve mode.

### Four-tier RBAC

`readonly → operator → admin → superadmin`, enforced at the tool layer with namespace guardrails. It won't read Secrets or ServiceAccounts, so the agent cannot exfiltrate credentials.

### Hash-chained flight recorder

A tamper-evident, deterministically replayable audit log; mutations arm rollback points and produce grounded, source-cited incident postmortems.

### Dynamic tool synthesis

Generates new Python tools at runtime, validates them with AST safety checks, tests them, and can graduate a proven tool into the codebase via an automated pull request — no redeploy. Generated tools execute in-process behind AST validation; they are not sandboxed.

### MAPE-K perception loop

Compiled, zero-LLM-cost detectors watch streaming events; a graduated autonomy ladder lets it open investigations unprompted, strictly within human-set per-namespace bounds and allowlists.

// evaluation

## Measured, with the receipts.

Validated on a live cluster against a controlled, reproducible fault-injection corpus — each scenario ships an injection manifest, a gold expected diagnosis, and a recovery-verification script — scored by an independent judge model and fully regenerable from the released harness. KubeIntellect is **open source** and pre-commercial; every number is reproducible.

// white paper

## Read the technical decision paper.

A decision paper for platform, SRE, DevOps, and cloud-native decision-makers — continuous perception, tiered reasoning, and auditable autonomy for LLM-driven Kubernetes operations.

// stack & deployment

## The toolchain.

Multi-provider LLM support and ready-made overlays for Kind, EKS, GKE, AKS, and ACK. Packaged on PyPI as `kubeintellect` and `kube-q`; deployable via a guided init wizard, Docker Compose, or a Helm chart to any cluster on any cloud.

// more

## Explore the rest of the lab.
