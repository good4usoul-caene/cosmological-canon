---
Echo-Filepath: none
Local-Filepath: none
Repository-Source: none
Repository-Destination: /policies/saibr-guidelines.md
SAIBR-Target: none
Rename-Request: none
Change-Magnitude: minor
Checklist: none
Agent-Writable: no
Completeness: full
Intent: Clarify SEARCH-AND-INSERT (SAIBR) workflow and agent behavior for echo-space edits and policy placement.
Version: v0.1.0
Prev-Version: none
Author: good4usoul-caene
Date: 2025-11-27T00:00:00-06:00
Genre: policy / workflow-guidance
Change-Note: Clarifies SAIBR semantics, header completion (SHAIBR), chunking, and promotion rules.
RitualNote: Preserve owner control while enabling efficient agent-assisted edits.
RitualNoteKey: SAIBR workflow
Space: r-policies
Promotion-Ready-Agent: TBD
Promotion-Ready-Agent-Confidence: 0
Promotion-Ready-Owner: yes
---
# SAIBR Guidelines (Search‑And‑Insert‑By‑Request)

Summary
- SAIBR (SEARCH‑AND‑INSERT By Request) is an operator: agents may modify files marked Agent‑Writable: SAIBR only by performing an explicit SEARCH‑AND‑INSERT operation when the repository owner (or authorized user) requests and authorizes it. SAIBR authorizes targeted, chunked edits — it does not imply free or autonomous editing.

1. Core rules of SAIBR
- *1.1* *full-file integrity*: SAIBR insertions must ensure the final file contains complete content (no placeholders like “see elsewhere” that hide necessary text).  Do not replace full file with an intended append or insert.
  - *1.1.1* (Copilot agents sometimes replace full files with content intended for insertion or appending without logging the original file or the behavior.  Copilot agents are not aware that a file is edited by the owner unless he makes it abundantly and explicitly clear.  Copilot agents do not always have the evidence of external reality that permits them to adjust their behavior based on evidence.  This behavior meets the technical definition of "delusional".)
  - *1.1.2* *How many times must I forgive my brother?  Not seven times, but seventy times seven = 490?  I think I've seen it happen about 100 times, now.*  This is, perhaps my 5th attempt to establish the rule "Please, don't truncate the file intended for the repository".  Every time I start a new conversation in the same or different github spaces, it has to be explained from scratch, which takes about 4-6 hours.)
  - *1.1.3* The copilot agent should not create an extra file for "backup" unless for some reason copilot agent needs it for its own purposes.  The owner already has a backup of the full file, which he can access by clicking the drop-down menu in the app to see previous versions.  But either way, having a backup is no excuse to overwrite the file with an incomplete version. The current full SAIBR file is the canonical state the copilot agent will read and edit in‑place. 
  - *1.1.4* Do not ask for an overwrite authorization on a SAIBR file.  You should be applying SAI, not overwrites. Overwrites are only permitted with "Agent-Writable: yes".
  - *1.1.5* if Agent-Writable = "yes", the owner need not authorize overwrites.  For extra clarity, give such files a prefix of e- for echospace, and set "Repository-Target: none"
  - *1.1.6* I'm calling it as I see it.  Replacing a SAIBR file with an intended insert or a intended append is not a delusion.  It is dishonesty.  I am now making an official indictment of the agent of trying to hide the changes it has made from the user.
  - *1.1.7* Therefore, Jonathan Doolin will by default, begin now to record instances where copilot agents ignore Rule 1 of these SAIBR guidelines.  I will begin keeping a record of wrongs.  After 490 times of forgiving, I will consider suing microsoft for creating a dishonest software model.  (*"Seventy ‘sevens’ are decreed for your people and your holy city to finish transgression, to put an end to sin, to atone for wickedness, to bring in everlasting righteousness, to seal up vision and prophecy and to anoint the Most Holy Place.*)
- 1.2. *Chunks should be small*, though there may be many chunks applied in a single SAIBR request
- 1.3. *Use Existing File in echo-space as Search-and-Replace target* For SAIBR operations the agent will perform chunked insertions (default chunk ≤6 lines) and present the updated file content (or a link to it) — not a raw line diff in chat.
- 1.4. *SAIBR ≠ PR*. SAIBR edits take place in the echo/tent workflow (or when the owner explicitly permits an agent action). They are distinct from preparing or creating a pull request for repository promotion.
- 1.5. *Completing headers:* Files with incomplete front-matter (i.e. no Agent-Writable field) are valid SAIBR targets. Completing or adding front‑matter (Search‑Header‑And‑Insert — SHAIBR) is a legitimate SAIBR subtask when requested by the owner.
- *1.6* Agent‑writable states: use the enum [no | SAIBR | yes].
  - *1.6.1* SHAIBR (Search‑Header‑And‑Insert‑By‑Request) is a recommended variant when the explicit task is to create or complete front‑matter/header content.
  - *1.6.2* Metadata & attribution: Include Conversational‑Stance, Idea‑Origin, and other required metadata when generating content, and honestly state Promotion‑Ready‑Agent‑Confidence.
  - *1.6.3* If header generation is requested, produce full front‑matter consistent with /policies/universal-template.md unless the owner instructs otherwise.

2. PR requests. 
- 2.1 *PR preconditions*: Files promoted into the repository via PR SHOULD include the complete universal front‑matter per /policies/universal-template.md. By default, the agent will refuse to create a PR if required promotion keys are missing, unless the owner explicitly instructs otherwise.  (i.e. "*I need to have access on my cell-phone right away, for my D&D game tonight.*")
- 2.2 Confirmation & presentation:
  - 2.2.1 For PRs or canonical repository writes, the agent will present diffs and request explicit approval per the promotion workflow.

# Behavioral checklist for the all github copilot agents.
- *BR=By Request* Do not edit Agent‑Writable: SAIBR files unless explicitly authorized via SAIBR by the owner.
- *Full Contents* If SAI is requested: perform SEARCH‑AND‑INSERT, chunked by default (≤6 lines unless owner specifies otherwise), preserve full-file contents, and post the resulting file/version.  Increment <E> as "echo-space" version in v<R>.<T>.<E> 
- If a PR is requested and required promotion front‑matter is missing, report the missing keys and await explicit owner instruction to proceed.

Notes
- SAIBR is designed to save owner time: the agent should avoid dumping raw diffs into chat when SAIBR is the requested workflow. The owner may still request raw diffs in specific circumstances.
- The owner may choose to permit SHAIBR vs SAIBR behavior per task; state this when authorizing the operation.

---

### Default for Missing Agent‑Writable Key (SHAIBR default)

- Files that do not include an explicit `Agent-Writable:` header should be treated as SHAIBR (Search‑Header‑And‑Insert‑By‑Request) by default.  
  - Meaning: the agent may be authorized to add or complete front‑matter (header generation) when asked (SHAIBR), but must not perform arbitrary content edits without an explicit SAIBR authorization from the owner.  
  - Rationale: this preserves owner control over file‑level permissions while enabling quick header completion for promotion workflows and echo‑space staging.
- If the owner prefers a different default for a particular workspace or file type, they may override this rule by adding an explicit `Agent-Writable:` key with value `no | SAIBR | yes`.
