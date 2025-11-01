---
Filename: def-access.md
Ultimate-Target-Directory: /policies/
Version: tent
Prev-Version: none
Author: good4usoul-caene
Date: 2025-11-01T22:45:00Z
Genre: policy / access-control
Change-Note: Defines access and automation patterns for agents and bots to create PRs and perform repo automation.
RitualNote: Tent copy — owner-editable. Promotion to Temple requires SEARCH‑AND‑INSERT + explicit Owner confirmation.
---

# def-access.mb — Access & Automation Guidance

Purpose
- Describe who may grant programmatic access for agents/bots to create branches and open PRs, and offer recommended, secure patterns for enabling automation while protecting repository sovereignty.

Core guidance
1. Human-first control
   - The Repository Owner (good4usoul-caene) retains final authority to grant any programmatic permission.
   - Any one-time permissioning step must be performed by the Owner or an authorized GitHub organization admin.

2. Preferred patterns to enable automated PR creation
   - GitHub App installation (recommended)
     - Install a dedicated GitHub App (or the official Copilot App if available) to the repository or organization.
     - Grant the App minimal scopes required: "Contents: read & write", "Pull requests: write" (or equivalent granular permissions).
     - App-based tokens are scoped and auditable; they are preferred for long-lived automation.
   - Machine/bot user with Personal Access Token (PAT)
     - Create a GitHub machine user (bot) and issue a PAT with repo:contents & repo (pull_request) scopes.
     - Store the PAT in GitHub Secrets and use it from CI workflows.
     - PATs are convenient but require careful secret management.
   - GitHub Actions with workflow actor
     - Use the built-in GITHUB_TOKEN for actions in the repository (note: GITHUB_TOKEN is scoped to repo and can create PRs; ensure appropriate workflow permission settings).
     - For cross-repo PRs or organization-level automation, prefer App or PAT.

3. Minimum access required for creating PRs
   - repo:contents write (create branch, add/modify files)
   - pull_request write (create PRs and add PR metadata)
   - (Optional) workflow write if automation needs to run or re-run workflows

4. Audit & governance
   - All automated commits and PRs must include visible provenance in front-matter (Author: Copilot-Agent/<id> or Bot/<id>), Change-Note, and RitualNote.
   - CI should record the actor (App or bot login) and create an audit entry in /pasture/archive/ or /tent/errorstatus/ when automation creates PRs for the first time.
   - Require SEARCH‑AND‑INSERT + Owner confirmation for promotion to Temple/policies.

5. One-time Owner actions (how to enable)
   - Option A — Install App:
     1. Go to the App install URL (or Settings → Installed GitHub Apps).
     2. Install to repository or org and grant repo write permissions.
   - Option B — Create bot user & PAT:
     1. Create a GitHub user (e.g., caravan-bot).
     2. Generate a PAT with repo permissions.
     3. Add PAT to this repo’s Settings → Secrets → Actions (e.g., name: BOT_PAT).
   - Option C — Configure Actions:
     1. Enable workflows to use GITHUB_TOKEN and ensure workflow file allows write permissions for contents and pull_request if needed.

6. Example workflow invocation patterns
   - Use a GitHub Action that runs with BOT_PAT or App token and executes:
     - create a branch (git checkout -b feature/<desc>)
     - add/commit files
     - push to origin
     - create PR (gh pr create or API call)
   - Ensure PR body includes links to source echo/candidate files in /cache/ or /pasture/ and includes the structured next‑steps block.

7. Security notes
   - Never embed tokens in files. Use GitHub Secrets.
   - Limit token scope to the minimum required and rotate tokens periodically.
   - Log and notify Owner when automation first creates a PR.

8. Ritual note
- Programmatic actors may assist with preparing commit-ready blocks and PR drafts but must not be considered owners. Human confirmation (Owner "yes") is required for promotion to canonical/policy locations.

---