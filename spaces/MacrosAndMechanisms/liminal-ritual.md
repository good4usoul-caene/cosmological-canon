# Liminal Ritual — Branch as Event

Technical title
- Liminal ritual (git branch as event in time)

Dual‑language headline
- Technical: branch — a pointer to a commit history  
- Mythic: liminal ritual — an event in which a strand of knowledge is rehearsed and extended

Purpose
- Preserve interpretive humility by naming the branch not only as a place but as an event: the act of change is the ritual.
- Make it explicit in documentation and PRs that work on a branch is a bounded rehearsal with intent, provenance, and an invitation to reviewers.

Definition (concise)
- Technical: A liminal ritual is a named git ref that points to a series of commits. It marks the chronological arc of a focused change.  
- Mythic: A liminal ritual is the ceremony in which an idea is enacted, iterated, and offered to the Canon.

Naming conventions (practical)
- Use `liminal/` prefix for branches that are conceptual events rather than tiny fixes:
  - Examples: `liminal/add-pr-template`, `liminal/seed-macros`, `liminal/restore-spirits`
- Use other conventional prefixes for short changes:
  - `feat/`, `fix/`, `chore/` remain valid for typical development tasks.
- Short guidance: prefer descriptive verbs (seed, add, restore) and keep names < 4 slash components.

Commit & PR posture (ritualized workflow)
- Commit messages should include intent line and provenance:
  - Example: `liminal: seed initial Temple scaffolding — authored by good4usoul-caene`
- PR title/body should include:
  - Short description (what is already present)
  - Preservation notes (what must not be overwritten)
  - Review checklist (concrete reviewer actions)
  - Mythic note (one or two lines framing intent; optional)
- Suggested PR body snippet (copy/paste-ready):
  - Title: Initial Temple scaffolding  
  - Body (short): "Seed the Temple: add PR template, .gitattributes, LICENSES, and scaffolding. Preservation: do not overwrite Spirits.md (commit 2d78a61). Reviewer checklist: confirm preservation, inspect tooling, verify license."

Reviewer guidance
- Human reviewers are primary; automated checks may assist.  
- Reviewer checklist example:
  - [ ] Confirm preservation of eloquent artifacts (Spirits.md / commit SHA).
  - [ ] Inspect provisioning scripts for unsafe operations.
  - [ ] Validate .gitattributes and LICENSES.

Windows / case‑sensitivity note
- When restoring files whose names differ only by case (e.g., `Spirits.md` vs `SPIRITS.md`) use a safe rename sequence to avoid Windows case conflicts:
  - Temporarily rename the existing file, restore the committed-case file, then remove the temp and commit.

Ritual annotation (dual‑language example)
- Add a small header comment at the top of important macros or README fragments that includes both technical and mythic phrasing:
  - Example:
    ```
    % Technical: Declares canonical macro for typesetting matrices
    % Mythic: Inscribes the framed glyph for structural invocation
    % Author: good4usoul-caene
    ```
- This lets future contributors read both the operational instruction and the ritual context.

Attribution & provenance
- Record authorship and the commit SHAs that introduced eloquent artifacts when those artifacts are preserved or restored. This maintains evidence of intent and responsibility.

Next steps (options)
- Add this file to `spaces/MacrosAndMechanisms/` in the repo and open a PR describing the change.  
- Or keep it as a local guideline and reference it in the PR template.

— end of liminal ritual note —