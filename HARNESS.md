# ArtifactWeaver Worker Harness

The worker harness keeps ArtifactWeaver safe for public open-source work. It protects the public rendering contract, bilingual docs, fake examples, and private-data boundary.

## Start Protocol

Before work starts, every worker must:

1. Read this file.
2. Read the current issue or task description.
3. Read the matching context pack.
4. Confirm allowed paths.
5. Confirm out-of-scope paths.
6. Run `git status --short --branch -uall`.
7. Confirm the current branch.
8. Add a start entry to the change log and decision log when the task requires it.
9. Avoid touching files outside the context pack unless the reason is recorded first.

## Done Protocol

Before handoff, every worker must:

1. Update English and Simplified Chinese documentation.
2. Update the change log.
3. Update the decision log for architecture choices.
4. Update quickstart or CLI reference when commands change.
5. Update schema docs when the manifest changes.
6. Run validation.
7. Output a handoff report.
8. Do not commit automatically.
9. Do not push automatically.

## M0 Boundary

M0 is Python-only. Do not introduce Node, Bun, Vite, React, Vue, Slidev, Playwright, PDF export, CI workflow, PyPI/npm publishing, Unity integration, Feishu integration, Jenkins integration, Steam integration, or a NoTimeToDie-specific adapter.

Examples must remain fake. Generated `dist/` output must stay out of Git.
