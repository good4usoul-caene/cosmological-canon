---
Filename: pasture/README.md
Ultimate-Target-Directory: /pasture/
Version: v0.1
Prev-Version: ""
Author: good4usoul-caene
Date: 2025-11-02T16:35:41Z
Genre: meta
Change-Note: Added canonical front-matter and clarified definitions/principles
RitualNote: Pasture is a low-trust, transient space. Do not promote without review.
Space: pasture
Promotion-Ready: pasture-draft
---

Purpose
The pasture is a transient space for ephemeral offerings, experiments, and scratch artifacts. It is not part of the canonical Temple and is intended for short‑lived drafts or experiments.

Definitions:
 - repository files and directories:  Files and directories that actually exist on the github
 - echo files and directories: files and directories that exist in individual copilot sessions, (conversation spaces) but have not necessarily been uploaded to the repository
 - Echo files:  /tent/, /cache/, /pasture/:  Temporary echo-only workspaces, containing files that may or may not be destined for promotion to the repository.
   - Context 1: echo files in the echo space.
   - Context 2: the single README.md file (this file) in the repository directory, /pasture/README.md
 - Staged Files:  Context Sensitive Definition:  /foyer/, /policies/, /methods/, /workflows/, /scripts/, /library/, /archive/ (and any other directory that does not start with /tent/, /cache/, or /pasture/)
   - Context 1:  May be talking about files in the echo-space that are not yet ready for a PR request.
   - Context 2:  May be talking about files that are already in the repository.
   - Context 3: May be talking about files that are in the echo space and either have already been promoted via PR request, or that have all fields ready for promotion to the repository.
 - Ultimate-Target-Directory (UTD):  This is the repository directory where the file is meant to be stored.  If the ultimate filename is different from the actual filename, this UTD should include the final filename, as well.

Principles
- Keep the /pasture/ repository directory PERFECTLY CLEAN except for THIS README file.  Same goes with /tent/ and /cache/, with similar readme files.  There're no cows in the Temple pasture, not even sacred ones.
- Echo Files: /cache/ and /pasture/ (Context 1) and subdirectories should be treated by Copilot agents as open canvasses--Tabula Rasa to make any suggestion needed.  /pasture/treehouse/ is available for completely wild ideas.
- Echo Files (Context 1:) in /tent/ files and subdirectories should only be created or modified with the express request of the user.
- Any file in the echo space should have version "pasture", "tent" or "cache" and Ultimate-Target-Directory, according to it's recommended placement amongst the repository directories, for example: NONE (no promotion recommended), SEARCH-AND-INSERT-<filename>, (for partial files intended for inclusion in more complete drafts), /foyer/ (for repository root), /policies/, /methods/, /library/caravan-canon/, /library/interp-scripture/, /archives/, etc (for repository subdirectories)
- Do not promote pasture content into /tent/ or Staged files without Owner review and the required front-matter (see templates/front_matter_template.md).
- Use pasture for early-stage ideas, snippets, and throwaway experiments only.

Process
- If an item in pasture should become canonical, prepare a tent or cache draft with proper front matter, run SEARCH‑AND‑INSERT to identify the target location, and request Owner confirmation before promotion.
- Do not place secrets, credentials, or sensitive data in pasture.

Local notes
- This file is a local draft. If you want it added to the repository, I can produce the git/gh commands to create a branch and open a PR.
