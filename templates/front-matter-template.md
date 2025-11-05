---
Filename: /templates/front-matter-template.md
Temporary-Target-Directory: /templates/front_matter_template.md
Ultimate-Target-Directory: /templates/front-matter-template.md
Intent: Describe the purpose of each header entry.
Version: v0.1.16
Prev-Version: v0.1.15
Author: good4usoul-caene
Date: 2025-11-04T19:16:00-06:00
Genre: Tentative Rule
Change-Note: Bumped to v0.1.16; minor editorial fixes.
RitualNote: Clarify before Commit
RitualNoteKey: Excerpt Matthew 13:15 "they would see with their eyes, hear with their ears, and understand with their hearts."
Space: staged
Promotion-Ready-Agent: TBD
Promotion-Ready-Agent-Confidence: 6
Promotion-Ready-Owner: yes
Promotion-Rubric-General: templates/promotion-rubrics/front-matter-draft-rubric.md
Promotion-Rubric-Specific:
  - id: 1
    score: 95
    title: "Discuss Promotion-Rubric fields"
    note: "Using a General Promotion-Rubric for all files, and a Specific Rubric for an individual file"
  - id: 2
    score: 100
    title: "Discuss Promotion-Ready ternary"
    note: "Allows Promotion-Ready-Agent to be set to TBD (requires owner approval)"
  - id: 3
    score: 90
    title: "File references for Genre & authorial posture"
    note: "Have authorial posture; may need to extrapolate enumerated genres from policy-genre-and-spaces.md"
  - id: 4
    score: 90
    title: "Space entry redundancy check"
    note: "Making Space an entry primarily used in Agent drafts"
  - id: 5
    score: 80
    title: "Separation of header vs sample header"
    note: "Sample headers belong in example files"
  - id: 6
    score: 80
    title: "SEARCH-AND-INSERT as UTD"
    note: "Require target filename in Change-Note when UTD=SEARCH-AND-INSERT"
  - id: 7
    score: 80
    title: "Add /templates/ to repository directory list"
    note: "Include /templates/ in root README and def-storage-spaces.md"
  - id: 8
    score: 100
    title: "promotion-rubric-template.md header validated"
    note: "Header fields present and parseable"
  - id: 9
    score: 90
    title: "promotion-ritual.md vs front_matter_example.md"
    note: "To be resolved later"
  - id: 10
    score: 90
    title: "Consider binaries for Promotion-Rubric-General"
    note: "General Promotion-Rubrics are explicit enough for binary decisions"
---
# Body begins here

Required Fields:
- **Filename**: Required — final repo path (include filename if different)
- **Temporary-Target-Directory**: optional — used when a local or echo-space copy of the file has an incorrect filename or placement (e.g., an underscore vs hyphen mismatch). Record the local filename here when it differs from Ultimate-Target-Directory.
- **Ultimate-Target-Directory**: required for promotion — allowed examples: /policies/, /methods/, /foyer/, /, NONE, SEARCH-AND-INSERT. For SEARCH-AND-INSERT, provide the final insertion filename/path in Temporary-Target-Directory and document the insertion proposal in Promotion-Rubric or Change-Note. For echo-space drafts (Space: tent/cache/pasture) UTD may be omitted; promotion will require it.
- **Intent**: Required — The Intent of the file that will be placed at the Ultimate-Target-Directory. Do not put Change-Notes here.
- **Version**: required: v<R>.<T>.<E>, tent, pasture, cache
- **Prev-Version**: required (can be "none")
- **Author**: required. See file /policies/authorial-posture.md 
- **Date**: required — include explicit timezone offset (ISO 8601). Example (CST): 2025-11-04T19:16:00-06:00.
- **Genre**: required, see /policies/policy-genre-and-spaces.md
- **Change-Note**: required (short): one-line human-readable explanation of the most recent change. For SEARCH-AND-INSERT proposals include the intended insertion target/path here.
- **RitualNote**: required: any scriptural or philosophical support for the Intent of the file.
- **RitualNoteKey**: required. Leave space for a reference to any scripture or philosophical writing.
- **Space**: optional: declarative convenience field for echo-space artifacts (cache/tent/pasture/staged/repository). Make it required only for echo-space drafts, optional for final/canonical files.
- **Promotion-Rubric-General** optional. See templates/promotion-rubrics/front-matter-draft-rubric.md for general promotion-rubric information that applies to all.
- **Promotion-Rubric-Specific** required: A structured list of specific requirements (id/score/title/note) that together determine Promotion-Ready status.
- **Promotion-Ready-Owner**: required — yes|no|TBD
- **Promotion-Ready-Agent**: required — yes|no|TBD
- **Promotion-Ready-Agent-Confidence**: Copilot-determined value between 0–10 based on the agreed rubrics and other concerns.

Notes on promotion enforcement (brief)
- Drafts (Space: tent/cache/pasture): UTD may be omitted; validator: warn only.
- Staged (Space: staged): UTD strongly recommended; validator: warn if absent.
- Promotion (Promotion-Ready-Owner == owner-approved): validator: block promotion if UTD is empty or equals SEARCH-AND-INSERT without an explicit insertion target recorded in Temporary-Target-Directory and Promotion-Rubric/Change-Note.
- Dates: include explicit timezone offset (ISO 8601). Example (CST): 2025-11-04T19:16:00-06:00.
---