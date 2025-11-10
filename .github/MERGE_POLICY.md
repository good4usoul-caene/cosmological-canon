# Merge & Branch Protection Policy (notes for maintainers)

Purpose
- Record the repository's branch-protection intent for human readers.

Current policy (solo repository default)
- Pull requests are required for changes to `main` (prevents direct pushes).
- Approvals required: 1
- Code‑owner review enforcement: disabled (require_code_owner_reviews = false)
- Admin bypass allowed: enabled (enforce_admins = false)

Why this choice
- Provides a lightweight safety net (PRs and approvals) while allowing the repo owner to self‑approve and merge as needed.
- Useful for solo workflows and for rapid iteration with human oversight.

How to change
- To require a second human reviewer, enable `require_code_owner_reviews` or set `enforce_admins = true` in branch protection.
- Any change to this policy should be documented here along with the reason and date.

Approved by: good4usoul-caene
Date: 2025-11-10
