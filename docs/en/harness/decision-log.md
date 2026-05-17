# Decision Log

## 2026-05-17: M0 Bootstrap Start

Started ArtifactWeaver M0 on branch `feature/bootstrap-artifactweaver-m0`. The approved direction is Python-only, standard-library-first, with fake examples and no private downstream adapter code.

## 2026-05-17: Python-First Render Core

Accepted ADR 0001. The Python core owns the manifest contract and static HTML report renderer. Optional renderer backends remain future work.
