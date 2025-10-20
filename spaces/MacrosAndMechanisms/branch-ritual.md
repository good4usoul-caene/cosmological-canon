# Branch Ritual — Liminal Ritual (branch as event in time)

Technical title
- Branch Ritual (git branch as event)

Dual‑language headline
- Technical: branch — a pointer to a commit history  
- Mythic: branch ritual — an event in which a strand of knowledge is performed, practiced, and offered

Purpose
- Name the branch not merely as a place but as a ritual event: the act of change is temporal and intentional.
- Encourage contributors to document intent, provenance, and preservation when creating or closing a branch ritual.

Definition (concise)
- Technical: a branch is a named git ref that points to a sequence of commits.  
- Mythic: a branch ritual is the ceremony that records an enactment of change; committing is the placing of ritual steps into the strand.

Naming conventions (practical)
- Use `liminal/` or `ritual/` prefix for work framed as an event:
  - Examples: `liminal/add-pr-template`, `ritual/seed-macros`, `liminal/restore-spirits`
- Use `feat/`, `fix/`, `chore/` for routine, small, or maintenance changes.
- Prefer verb-first names (seed, add, restore) and keep names short and descriptive.

Commit & PR posture (ritual workflow)
- Branch‑level metadata:
  - Branch name, short intent sentence (in branch description / PR title), and a preservation note (if relevant).
- Commit message style:
  - Start with an intent prefix, e.g. `liminal: seed initial Temple scaffolding — authored by good4usoul-caene`
  - Include provenance where relevant (author, scripts used, notable SHAs).
- PR expectations:
  - Title: short intent (what the ritual does now).
  - Body: describe what’s already present in the branch, preservation notes, reviewer checklist, and planned follow‑ups.
  - Close the ritual explicitly in the PR by merging or archiving and documenting the result.

Reviewer guidance
- Primary reviewers: human agents (with automated checks as assistants).
- Concrete reviewer checklist:
  - [ ] Confirm preservation of eloquent artifacts (list SHAs / filenames).
  - [ ] Inspect provisioning scripts for destructive or secret behaviors.
  - [ ] Validate EOL and gitattributes for cross‑platform safety.
  - [ ] Confirm license and attribution entries are correct.

Windows / case sensitivity note
- When restoring files that differ only by case (e.g., `Spirits.md` vs `SPIRITS.md`), perform a safe two‑step rename to avoid Windows case conflicts:
  1. Temporarily rename the existing file (e.g., `git mv SPIRITS.md SPIRITS.md.temp`).
  2. Restore desired-case file, commit, then remove temp and commit again.

Ritual annotation (dual‑language example)
- At the top of key files, include both technical and mythic comments:
  ```
  % Technical: Declares canonical macro for typesetting matrices
  % Mythic: Inscribes the framed glyph for structural invocation
  % Author: good4usoul-caene
  ```

Attribution & provenance
- Record authorship and notable SHAs that introduced or preserved eloquent artifacts. This keeps evidence of intent and responsibility.

Next steps
- Add this note to `spaces/MacrosAndMechanisms/` and reference it in the PR template as an optional framing statement.