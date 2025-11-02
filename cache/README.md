---
Filename: cache/README.md
Ultimate-Target-Directory: /cache/
Version: v0.1
Prev-Version: ""
Author: good4usoul-caene
Date: 2025-11-02T16:48:00Z
Genre: meta
Change-Note: Draft README for /cache/ (local copy)
RitualNote: Cache holds early-stage workflow drafts and support files for Owner review. Do not merge without SEARCH‑AND‑INSERT confirmation.
Space: cache
Promotion-Ready: cache-draft
---

Purpose
The /cache/ directory contains draft workflows, tooling proposals, and other support artifacts prepared by the Caretaker. Items here are intended for review and revision before being promoted to canonical repository locations.

Principles
- Keep the /cache/ repository directory PERFECTLY CLEAN except for THIS README.md file.
- Everything in /cache/ is a draft. Inspect and approve before merging.
- Workflows and tooling drafts in /cache/ should include a front matter header (Filename, Ultimate-Target-Directory, Author, Date, Change-Note, RitualNote, Promotion-Ready) so validation tooling can read provenance.
- Keep sensitive details (secrets, tokens) out of cached drafts; use placeholders and documentation only.
- Use the SEARCH‑AND‑INSERT method to propose exact insertion points for any artifact that will be promoted to /workflows/ or other guarded directories.

Promotion path (echo → repository)
- Promotion path is: /cache/ <-> (tent or pasture optional) -> Ultimate-Target-Directory (echo-space) -> Ultimate-Target-Directory (repository space)

Process
- When ready to promote a cached workflow, prepare a PR that:
  - Adds front matter with Promotion-Ready: owner-approved (set by the Owner only).
  - Includes a test checklist and a manual run plan for a safe staging run (workflow_dispatch).
  - Mentions reviewers listed in CODEOWNERS for /workflows/.
- Do not promote cache content directly into /policies/ or /methods/ without Owner review and the required front-matter.
