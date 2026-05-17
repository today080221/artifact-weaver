# ADR 0001: Python-First Render Core

## Status

Accepted for M0.

## Decision

M0 uses a Python-only, standard-library-first render core. It does not introduce Node, Bun, Vite, React, Vue, Slidev, or Playwright.

## Context

M0 needs to stabilize the artifact contract, CLI, manifest, HTML report renderer, documentation guardrails, and worker harness before introducing frontend engineering.

## Consequences

The Python core must not depend on Unity, Node, external services, or private downstream projects. Future optional renderer backends can be added behind a backend boundary without changing the core contract.
