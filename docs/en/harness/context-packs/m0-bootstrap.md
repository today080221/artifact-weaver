# Context Pack: M0 Bootstrap

## Goal

Create the initial Python-only ArtifactWeaver repository, CLI, manifest contract, HTML report renderer, bilingual documentation, and worker harness.

## Allowed Paths

- `LICENSE`
- `NOTICE`
- `README.md`
- `README.zh-CN.md`
- `HARNESS.md`
- `HARNESS.zh-CN.md`
- `CONTRIBUTING.md`
- `CONTRIBUTING.zh-CN.md`
- `pyproject.toml`
- `.gitignore`
- `.gitattributes`
- `.githooks/**`
- `.github/**`
- `src/artifact_weaver/**`
- `schemas/**`
- `examples/**`
- `docs/**`
- `tools/**`

## Forbidden Paths And Data

- Any private downstream repository path.
- Any Unity project path.
- Any real screenshot path.
- Any real QA report path.
- Any company path.
- Any file outside this repository.
- Actual Steam AppID or DepotID values.
- Actual Jenkins internal URLs.
- Actual skill IDs or synergy IDs.

## Validation

Run `python tools/validate_repo.py` and the final M0 command list before handoff.
