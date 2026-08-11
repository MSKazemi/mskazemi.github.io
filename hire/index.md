# Hire a Freelance AI SRE, MLOps &amp; Kubernetes Engineer (Remote, EU) — Mohsen Seyedkazemi Ardebili

> Freelance AI infrastructure consultant working remotely worldwide: Kubernetes reliability and AIOps, MLOps platforms, and production LLM agents.

Source: <https://mskazemi.com/hire/> · Author: Mohsen Seyedkazemi Ardebili · This is the Markdown twin of the HTML page; the HTML is canonical.

---

available · remote · EU

Freelance AI SRE, MLOps and Kubernetes engineering — remote, worldwide.

I help teams whose infrastructure has outgrown the people watching it: clusters that page at 3 a.m. for reasons nobody has time to chase, models that made it to production and then quietly stopped being right, and AI agents that are about to be given credentials nobody has thought hard enough about. Start with a **fixed-price audit** — you get a written answer either way, and neither of us has to guess whether we work well together.

- BASED Bologna, Italy (CET) · remote worldwide

- MODE Remote · CET · English

- START Fixed-price audit from €150 · projects €600–700/day

// why me

## I ran infrastructure before I researched it.

Seven years as the IT and network administrator of a combined-cycle power plant of more than 1,000 MW, where there is no staging environment and a bad change is measured in megawatts. Then a PhD in high-performance computing at the University of Bologna, and since then research and platform engineering on EuroHPC-funded projects — currently as architect and lead developer of the MLOps platform for **SEANERGYS**.

That combination is the actual offer. Plenty of people can build you an agent; fewer have been the person on call when an automated system did the wrong thing at scale. My work is consistently about the same thing — letting a machine take over more of the operator's judgement, while keeping a human at the gate and an audit trail behind it. It is also why [KubeIntellect](https://mskazemi.com/projects/kubeintellect/) pauses for approval before it touches anything it cannot undo, and why [NovaFabric](https://mskazemi.com/projects/novafabric/) exists at all.

I build systems your team can maintain after I am gone. No black boxes, no dependency on me for the next incident.

// engagements

## Start small and fixed-price. Scale only if it is working.

### Kubernetes reliability & AIOps

Health-checks, observability that answers questions instead of producing dashboards, hardening, incident root-cause analysis, and ops automation with human-approval gates. For teams running production Kubernetes without a dedicated SRE function.

### MLOps & ML in production

Getting models out of the notebook and keeping them honest: registry, serving, drift detection, governed retraining, monitoring. The same stack I run in production for a EuroHPC project, sized down to what your team can actually operate.

### Production LLM agents

Agents that act on real systems — tool boundaries, scoped RBAC, human-in-the-loop safety, tracing, and an audit trail you can put in front of a regulator or a customer's security team without flinching.

Rates are for direct clients. Longer engagements and retainers are negotiable; agencies and platforms are quoted separately.

// how it goes

## Four steps, no surprises.

### 1 · A free 30-minute call

You describe the problem. I tell you honestly whether it is one I can help with, and what I would do first. If it is not a fit, I will say so on the call.

### 2 · A fixed-price audit

Scoped in writing before it starts, delivered as a report you keep whatever happens next: findings, root causes, and a prioritised list of fixes with effort estimates.

### 3 · Implementation, if you want it

Day-rate project work against the priorities the audit found. Reviewable increments, your repo, your CI, your conventions.

### 4 · Handover

Documentation, runbooks, and a walkthrough with the people who will own it. The engagement ends when your team can run it without me.

// questions people actually ask

## Answers before you have to email for them.

### Can I hire a freelance MLOps engineer remotely?

Yes — that is exactly this. I work remotely with clients worldwide from **Bologna, Italy**, and invoice from Italy, so the contract stays straightforward with no extra administration on your side. CET is my base working day, and I overlap with other time zones by arrangement.

### What does an AI SRE actually do?

It applies machine learning and LLM agents to reliability work: correlating logs, metrics and cluster state to reach a root cause faster than a human paging through dashboards, then proposing — or, with approval, applying — the fix. The part that matters in production is the gate. A well-built AI SRE does not take a destructive action without a human approving it, and it leaves a trail showing what it did and on what evidence.

### How do you find the root cause of a failing Kubernetes pod?

Start from the object, not the dashboard: pod status and events, the container's exit code and last state, then the scheduling decision, resource limits and eviction pressure, then the logs of the failing container _and its neighbours_, and finally the metrics around the moment of failure. Most production pod failures resolve to a handful of causes — image or config errors, OOM kills, failing probes, resource starvation, or a dependency that was already down. The real engineering problem is not diagnosing one pod; it is making that path repeatable, so the third engineer to see the alert reaches the same answer as the first.

### Can an LLM agent safely run commands on a production cluster?

Only under constraints you can state and test: a scoped identity with real RBAC rather than cluster-admin; read and write paths separated so investigation never needs elevated rights; anything destructive stopping at an explicit human approval; and every action recorded with the evidence that motivated it, so it can be replayed afterwards. An agent that cannot be told _no_ by the permission system is not production-ready, whatever its benchmark scores say.

### Which languages and time zones?

CET, working in English. I also speak Persian, Azerbaijani and Turkish natively, and Italian at A2. I do _not_ speak German or French — German-language engagements are not a fit, and I would rather say that here than three emails in.

// contact

## Tell me what is breaking.

A free 30-minute scoping call, no deck. If I am not the right person, I will try to tell you who is.
