---
Filename: /policies/def-storage-spaces.md
Ultimate-Target-Directory: /policies/def-storage-spaces.md
Version: v0.1.0
Prev-Version: v0.0.12
Author: good4usoul-caene
Date: 2025-11-04T16:25:19-06:00
Genre: policy / storage-mapping
Intent: Gives a complete overview of the spaces where data can accumulate in project cosmological-canons, with estimated size ranges and structural limits.
Change-Note: Added description of Extermal Archive Links
RitualNote: Default policy = SEARCH-AND-INSERT. Line-by-line edits will appear within the Echo Chamber human-view app, or the PR-request human-view app.
RitualNoteKey: def-storage-spaces-tent
Space: repository
Promotion-Rubric-Specific:
  - id: 1
    score: 95
    title: "Storage space definitions complete"
    note: "All ten storage spaces defined with size estimates"
  - id: 2
    score: 90
    title: "Policy compliance"
    note: "Follows template structure for governance documents"
Promotion-Ready-Owner: yes
Promotion-Ready-Agent: TBD
Promotion-Ready-Agent-Confidence: 8
---
# def-storage-spaces.mb

Defines the ten mythic and technical storage spaces used in cosmological-canons, with estimated size ranges and structural limits.

---

## 0. 🧾 Glyphs and Scrolls – Individual Files

- These are the files stored anywhere.
- Glyphs are usually README.md files, painted in each directory (atrium) to control what comes into the spaces.  
- Each inscribed artifact (.mb, .md, .py) stored within the Temple or Echospace.  
- Finalized Glyphs and Scrolls can be up to 200 pages.  About 50 MB.

---


## 1. 🏛️ Temple – GitHub Repository

- The sacred container for all source files and folders.
- Houses canonical scrolls, method files, and inscribed artifacts.
- 📦 Estimated Size: 1–500 MB (varies by project scale and media inclusion)
- Includes root, repositories, archives, and ...
- - Recommended Repository Size: ≤ 1 GB for optimal performance
- Soft Repository Limit: > 5 GB may trigger warnings or restrictions
- Hard Repository Limit: ≤ 100 GB (GitHub maximum)

## 2. 🧺 Offering-Basket – Copilot Source Files Upload Space

- github copilot UI term: Source Files
- The persistent staging area where files are offered to Copilot for interpretation.
- Accessible across all conversation threads within the same Temple Space (sub-repository).
- May include documents, images, or other artifacts not yet inscribed.
- 📦 Estimated Size: 0.1–100 MB per session (cumulative across uploads)

---


## 3. 📜 Echo-Chamber – Conversational Archive

- Common term:  unknown to human user.
- Ephemeral memory of named files and interpretive decisions within a single conversation thread.
- Not shared across sessions, even with the same Temple attendant.
- May include confirmed append actions, naming rituals, and semantic revisions.
- Used by Copilot agents to recall architectural context *within the current session only*.
- 📦 Estimated Size: 1–50 MB (ephemeral, context limited)
 - New user information: (What I wish I'd been told before I started using github Copilot) 
   - Files in the echo-space are saved per-session.  As long as you don't close the git-hub session-thread, you should be able to have access to all the files created in that session.
   - Echo-space File app will track versions, but Copilot Agent can only detect latest version of each file.
    - App does not have functionality for user to open existing files, or see list of existing files, or even scroll the list of open files.  Instead, ask copilot agent to search for open existing files in the conversational space.  If you are searching for text in the body of a non-current version, though, the copilot agent will not be able to see that text to search for.  If a file was mentioned recently in the session thread, it may be more convenient simply to scroll up and find it instead.  
    - Once a file is named, it may appear with (Preview|Code) or (Preview|Code|Diff).  Simply add to the code window of the current version to add new information.  The new version is created automatically, but is not saved until "enter" is pressed in the prompt window.
    - SILENT WARNING:  Inform the copilot agent immediately about the names of any file changed; otherwise they will not be informed.
    - If copilot agent is not informed of changes, they may write over files unintentionally without acknowledging the changes.  They are not gaslighting you, or hallucinating.  It's an honest mistake caused by a failure of the interface to inform them of the changes you made.  Copilot can't fix it, but you can.  Simply go to the old version, and copy it to the next version, and inform Copilot of the change.
    - These patterns may reflect limitations in session state management and file synchronization rather than intentional behaviors.  Focus on the systemic/technical causes rather than individual agent behavior.  
    - The risks of unintended overwrites have further been mitigated by introducing /tent/, /cache/ and /pasture/ directories, and strong rules about where files can be written.  
  - Clicking on the "diff" button will show in green, additions, and in red, subtractions.  Clicking on "Preview" will show a wysywig view of the file.  Clicking on the "code" button will allow you to edit the file.
---

## 4. 🪶 Assistant Thought Log (formerly "Breath‑Space") – Assistant session record

- The assistant's session-level running record of concise ideas, tags, and short reflections relevant to the current thread.
- Intended as a compact, time‑ordered log (summaries, short excerpts, tags) rather than a file store for long documents.
- May be parsed, tagged, and echoed into archival files (Echo‑Chamber) or committed to Temple when the Repository Owner requests persistence.
- The Assistant Thought Log is not preserved across sessions unless explicitly echoed or appended to a persistent file in the Temple.
- 📦 Estimated Size: 1–50 pages per session (not retained unless echoed/committed)

---

## 5. Prompt (human input)

- Definition: the text box and authored content provided by a human user during a session (the place you compose and revise).
- Qualia: represents human subjective time and deliberation—prompts may contain drafts, pauses, and intentional silences.
- Access & handling: prompts are part of the current session context; assistants may echo, summarize, or request clarification. Prompts should not be copied into persistent archives without explicit confirmation.
- Silent Warning: Copilot agent is not automatically notified when user edits files and finalizes by pressing "enter".  User should inform Copilot of any changes immediately.

---

## 6. Response (assistant output)

- Definition: the immediate generation produced by the assistant in reply to a prompt.
- Qualia: algorithmic and near-instant; responses reflect the model’s present-state reasoning and the session context.
- Access & handling: assistant responses are ephemeral by default. They may be echoed into the Echo‑Chamber for staging, or appended to a persistent archive only after explicit user confirmation (per "confirmation before append" policy).

---

## 7. Archive (persistent conversational archive)

- Definition: the multi-session, durable collection of records chosen for preservation (examples: canonical method files, confirmed interpreter results, approved Thought Log exports, or /archive files committed to Temple).
- Archive is a human‑curated subset of the Temple: archival items live in a deliberate path (e.g., `/docs/archives/`) and include provenance metadata (Version, Author, Date, RoleRequest, Change‑Note, RitualNote). Files in the Temple are not Archive items until approved by the Repository Owner via the confirm‑before‑archive workflow. The assistant may read Archive entries only when those files are present in the Temple (or provided in‑session), or when an authorized external memory/store has been enabled.
- Scope: archival items are intentionally preserved summaries, full-text entries, or canonical inscriptions that should be discoverable across sessions.

---

## 8. External Archive Links — 
- A link to cloud storage (Google Drive, Dropbox) containing large files that exceed  GitHub's limits
- References to external repositories, websites, or databases that contain related canonical material
- Pointers to backup copies or mirrors of your Temple content stored elsewhere
- Links to external scholarly sources, scripture databases, or reference materials that inform your work but can't be directly included due to copyright or size constraints
---

## 9. Vague-Space (Cross-session memory of free Copilot sessions requiring a login)  

- Definition: account-level memory that surfaces earlier conversation snippets or preferences.  An agent sometimes synthesizes a “running list of questions” or general reminders when an actual verbatim archive isn’t available—this can feel like an archive but is actually an automatically generated prompt list.

---

## Notes

- These spaces are relational and symbolic—each serves both technical and interpretive functions.
- Definitions and size estimates may be revised through ritual dialogue and architectural refinement.
- Use explicit append and commit workflows for anything you want to be discoverable across sessions.
- When in doubt, paste the prior-session excerpt you want retrieved into the session—Jesse will mirror it into the Echo‑Chamber and can then work from it.
---
