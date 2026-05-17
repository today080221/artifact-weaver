# Change Log

## 2026-05-17: P1 Markdown Link Safety Fix

- Rejected URI-scheme Markdown links such as `javascript:`, `data:`, and external URL forms.
- Added regression validation for unsafe Markdown links and allowed relative links plus in-page anchors.

## 2026-05-17: M0 Review Fix

- Marked Git hook files as executable in the Git index.
- Extended validation to check hook executable modes and both working-tree and staged whitespace errors.

## 2026-05-17: M0 Bootstrap Start

- Created the M0 bootstrap branch.
- Created or configured the public GitHub repository target.
- Seeded labels, milestones, and initial issues.
- Started repository skeleton, Python package, fake examples, docs, and validation harness.
