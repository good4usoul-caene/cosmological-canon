

# Template for ALL created files:
 - https://github.com/good4usoul-caene/cosmological-canon/blob/main/templates/front-matter-template.md

# Promotion Ritual (/cache/, /pasture/, /tent/, staged, repository)
 - https://github.com/good4usoul-caene/cosmological-canon/blob/main/methods/method-promotion-ritual.md

# Authorial Posture: (How to attribute files.  Credit user only with work explicitly approved)
  - https://github.com/good4usoul-caene/cosmological-canon/blob/main/policies/authorial-posture.md

# Pasture Ecology: (Use of /pasture/ for logging, free play, unsafe, and promotion)
  - https://github.com/good4usoul-caene/cosmological-canon/blob/main/policies/pasture-ecology.md

# Conversational Logging: (general logging guidelines -- Keep exact words from user prompt)
 - https://github.com/good4usoul-caene/cosmological-canon/blob/main/methods/method-log-conversation.md

# Conversational Spirits:  (Copilot agent stances, and narrative protocols)
 - https://github.com/good4usoul-caene/cosmological-canon/blob/main/policies/spirits.md
 

# Policies & Promotion Rituals (brief)

This README documents the canonical promotion ritual and the echo → foyer → promotion pipeline used in this repository.

Key directories
- echo/cache/         — Agent drafts and temporary artifacts (agent-writable).
- echo/tent/          — Human-editable staging copies (editable by humans and agents with limits).
- echo/foyer/         — Handoff staging area for human review (promote only after SEARCH‑AND‑INSERT).
- echo/policies/      — Policy-focused preview staging area.
- foyer/              — Repository staging area for items prepared for promotion.
- policies/           — Canonical policy files (Temple). Promotion target.
- pasture/archive/    — Audit and Promotion Record storage.

Promotion flow (summary)
1. Agent writes draft to echo/cache/ or echo/tent/.
2. Run stage-echo-to-foyer.yml (manual) to copy selected artifacts into echo/foyer/ (PR created for review).
3. Reviewer performs SEARCH‑AND‑INSERT and sets `Promotion-Ready: owner-approved` in front-matter of files when ready.
4. Owner triggers promote-foyer-to-policies.yml or promote-foyer-to-root.yml (Owner-only workflows).
5. Promotion workflow validates `Promotion-Ready: owner-approved`, writes a Promotion Record to pasture/archive/, and creates a PR for human merge.

Owner responsibilities
- Confirm SEARCH‑AND‑INSERT edits before running promotion workflows.
- Maintain branch-protection rules requiring human reviewers for merges to main or /policies/.
- Add a repository secret `ALL_SOULS_TOKEN` (or install a GitHub App) to enable workflows to push PR branches. Rotate/revoke secrets after testing.

Notes
- Do NOT bypass foyer or echo/policies staging when promoting policy files.
- All promoted files must include provenance front-matter (Author, Date, Change-Note, RitualNote, Ultimate-Target-Directory) and `Promotion-Ready: owner-approved` when promoted.
