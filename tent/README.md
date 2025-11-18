---
Echo-Filepath: none
Local-Filepath: /tent/README.md
Repository-Source: none
Repository-Destination: none
Rename-Request: none
Change-Magnitude: major
Checklist: /policies/Checklist-2025-11-15.md
Agent-Writable: yes
Completeness: full
Intent: Explain the purpose and rules of the /tent/ staging area for review and human editing before repository promotion.
Version: v0.1.0
Prev-Version: none
Author: good4usoul-caene
Date: 2025-11-17T00:00:00-06:00
Genre: Staging Policy
Change-Note: Recreated /tent/ folder and README.md with universal-template header and clear staging instructions.
RitualNote: "Let every file in the tent be reviewed before promotion."
RitualNoteKey: Numbers 9:15-23 (Israel camped at the tent of meeting until the cloud lifted)
Space: tent
Promotion-Rubric-General: none
Promotion-Rubric-Specific:
  - id: 1
    score: 100
    title: "Tent staging rules explained"
    note: "README.md provides clear instructions for review and promotion workflow."
Promotion-Ready-Owner: yes
Promotion-Ready-Agent: yes
Promotion-Ready-Agent-Confidence: 10
---

# /tent/ Staging Area README

**Purpose:**
- Use /tent/ as a staging area for review and human editing before any file is promoted via SAIBR to a local copy of the same file.

**Rules:**
1. Do not promote files from /tent/ directly to the repository unless explicitly approved.  No repository /tent/ directory should ever appear.
2. All files in /tent/ should be marked with `Repository-Destination: none` 
3. Usually, files in /tent/ should have `Agent-Writable: yes`. 
4. Often, files in /tent/ should have optional field `SAIBR-Target` set to another local file intended for promotion to the repository.
3. Use this space for review, staging, and collaborative editing only.

**Workflow:**
- Drafts and candidate files are placed here for human review.
- Only after explicit user approval and proper front-matter should files be promoted to canonical repository spaces.

---
