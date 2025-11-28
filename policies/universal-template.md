---
Echo-Filepath: none #
Local-Filepath: /policies/universal-template.md
Repository-Source: /templates/front-matter-template.md
Repository-Destination:  /policies/universal-template.md
SAIBR-Target: none
Rename-Request: none  
SAIBR-Target: none
Change-Magnitude:  huge #none|minor|major|huge
Checklist: /policies/Checklist-2025-11-15.md
Agent-Writable: no #no|SAIBR|yes Determines whether copilot agent may Search And Insert (without truncation) By Request.  "none" means no changes are allowed.  "any" means the file may be changed at will by the copilot agent.
Intent: Establish owner authority over file-naming and file-promotion by use of the Agent-Writable tag.  Establish clarity of naming and storage in echo-space, local-space, and repository space, based on observed default behavior of agents.
Version: v0.2.1
Prev-Version: front-matter-template.md v0.1.16
Author: good4usoul-caene
Date: 2025-11-04 19:16:00 CST
Genre: Confirmed Rule
Change-Note: Added `SAIBR-Target` field.  Changed "Space" field.
RitualNote: God grant me the serenity to accept the things I cannot change, Courage to change the things I can, And wisdom to know the difference.
RitualNoteKey: Reinhold Niebuhr: Serenety Prayer - Alcoholics Anonymous
Space: staged # This was an Agent-requested field, and I believe it is redundant - Jonathan
Promotion-Ready-Agent: TBD
Promotion-Ready-Agent-Confidence: 6
Promotion-Ready-Owner: yes
Promotion-Rubric-General: File To Be Determined
Promotion-Rubric-Specific:
  - id: 1
    score: 
    title: "Establish as many filename tags as necessary"
    note: "(1) Echo and (2)Local filenames, Repository (3) Source and Repository (4) Destination, (5) Rename Request seem a minimum, but there might be others."
  - id: 2
    score: 100
    title: "Yes:  Maintain Promotion Ready Ternary; Two fields for owner and agent."
    note: "TBD|yes|no"
  - id: 3
    score: 100
    title: "File references for Genre & authorial posture"
    note: "**Author**: required. See file /policies/authorial-posture.md **Genre**: required, see /policies/policy-genre-and-spaces.md"
  - id: 4
    score: 50
    title: "Space entry redundancy check"
    note: "With the five different listed file name paths, Space may be redundant. "
  - id: 5
    score: 0
    title: "Separation of header vs sample header"
    note: "No files yet created with new header"
  - id: 6
    score: 80
    title: "SEARCH-AND-INSERT as UTD"
    note: "Reducing confusion by using Agent-Writable field"
  - id: 7
    score: N/A
    title: "Add /templates/ to repository directory list"
    note: "Renaming file to /policies/universal-template.md"
  - id: 7
    score: N/A
    title: "Delete only file in /templates/ and place under /policies/ or /methods/"
    note: "Files in echo-spaces cannot be deleted."
  - id: 8
    score: 0
    title: "promotion-rubric-template.md header validated"
    note: "No general promotion rubric.md has been promoted to repository"
  - id: 9
    score: 90
    title: "promotion-ritual.md vs front_matter_example.md"
    note: "To be resolved later"
  - id: 10
    score: 0
    title: "Consider binaries for Promotion-Rubric-General"
    note: "General Promotion-Rubrics are explicit enough for binary decisions"
  - id: 11
    score: 20
    title: "SAIB clarifications"
    note: "We need to establish granularity (line, or fine?) and other parameters (max yadda yadda 6)  Instructions (tentative) on this are in /.github/copilot-instructions.md.  It might also help if I could see the documentation for SEARCH-AND-INSERT, so I could update my priors on what the parameters actully do."
  - id: 12
    score: 
    title: ""
    note: ""
---
# Body begins here

Definitions
- **Full Path** Includes both path and filename.
- **Agent-Writable**  Set to "yes", "no" "SAIBR", "SHAIBR" or "PR" determines whether and how an agent may apply changes to a file. 
  - **SAIBR** Search-And-Insert-By-Request:  When SAIBR is allowed, Copilot agent may apply changes to the body and/or header of the SAIBR-marked-file via a SEARCH-AND-INSERT.  
  - **SHAIBR** Search-Header-and-Insert-By-Request:  When SHAIBR is allowed, Copilot agent may apply changes to the headers of the file, but must keep the body.
  - As of Thanksgiving, 11/27/2025.  Jonathan has begun recording instances where agents improperly remove information from files in the echo-space marked SAIBR or SHAIBR.  See \policies\saibr-guidelines.md (Rule 1.1.6-1.1.7)
  - **PR** If Agent-Writable is set to PR, no further edits are allowed in the echo-space, but Agent may "write" the file to the repository.  
  - **no** If Agent-Writable is set to "no", the agent must not edit the echo-space file at all.  
  - **yes** If Agent-Writable is set to "yes", the agent may freely insert, append, or overwrite the echo-space file with or without request from the human user/owner.  In such a case, consider the following rules as guidelines (not strict limits)  Repository-Target should generally be set to no, and the filename should generally have prefix "e-" for echospace.


Required Fields:
- **Rename-Request**: Type:  Full Path.  Relevance: If the file's intent is inconsistent with the filename, 
  - this field serves as a request to create a copy of the file with a new name, and 
  - a reminder of what the file was called, should this file be opened later.  
  - This entry comes first, because if the file has been renamed, any study of the obsolete file is wasted time.
- (1A) **Echo-Filepath** Type:  Full Path.  Relevance: github copilots accessed through "Spaces" on website.  What is the full path of the file in this echo-space? (or none)
- (1B) **Local-Filepath**  Type:  Full Path.   Relevance: github copilot accessed through VS Code on user's computer.  What is full path of the file called on user's computer? (or none)
  - Either 1A or 1B is required.  If both are included, the irrelevant one should be "none"
**Repository-Source**  Required.  Type:  Full Path.  Relevance: Is there an existing file in the repository, which this file is emulating or copied from?  Give the full path of that file. (or none)
**Repository-Destination** Required.  Type:  Full Path.  Relevance:  If this file is intended for promotion to the repository, enter it's full path here.  
  - Usually Repository-Destination and Repository-Source will be the same.)
**SAIBR-Target**:  Type: Full Path.  Relevance:  If the file's intent or Change-note is about performing a SEARCH-AND-INSERT from this source file to another file in the echo-space or local-space, this entry gives a clear reference to that target. 
**Change-Magnitude**:  Type: enum.  Relevance: Compared to the last version, if any, does this new document make any change?  "none"-trivial changes.  "minor" - a change that makes a significant clarification.  "major" - a change that represents a "change-of-mind", e.g. a correction.  "huge" - a change that will require further changes in one or many other files.
**Checklist**: Type:  Text or Full Path.  Give text or a link to a file containing a checklist of other updates that need to be made, relevant to this file.  
**Agent-Writable**: no #no|PR|SAIBR|SHAIBR|yes Determines whether copilot agent may Search And Insert (without truncation) By Request.  "SHAIBR" = "Search Headers and Insert by request", "no" means no changes are allowed.  "yes" means the file may be changed at will by the copilot agent, "PR" means the file is ready to be put in the repository by Pull Request.  PR means no further changes are permitted in the echo-space file before commit to repository.
- **Completeness** Type: enum:  Values |full| contains full current draft, |insert| Contains candidates for SAIBR for full draft.  |thought| contains agent-created material not intended for SAIBR |snippet| is for anything that doesn't fit full, insert, or thought.
- **Intent**: Type: Text - Required — The Intent of the file that will be placed at the Ultimate-Target-Directory. Do not put Change-Notes here.
- **Version**: Type: dotted list with a v at the beginning? - required: v<R>.<T>.<E>.  E=Echo-space version.  T = Temple Space version, R represents a major revision.
- **Prev-Version**: Type: same as version - required (can be "none")
- **Author**: Type: Text - required. See file /policies/authorial-posture.md 
- **Date**: Type: ISO 8601: - required — include explicit timezone offset (ISO 8601). Example (CST): 2025-11-04T19:16:00-06:00.
- **Genre**: Type: enum - required, see /policies/policy-genre-and-spaces.md
- **Change-Note**: Type: Text - required (short): one-line human-readable explanation of the most recent change. For SEARCH-AND-INSERT proposals include the intended insertion target/path here.
- **RitualNote**: Type: Text - required: any scriptural or philosophical support for the Intent of the file.
- **RitualNoteKey**: Type: Text - required. Leave space for a reference to any scripture or philosophical writing.
- **Space**: Type: Text Regexp Pattern "^(s|e|r)-([a-z]+)-?$" Enum: [s]ource, [e]cho, [r]epository.  String genre/file-type prefix.  Optional field intended only for "Agent-Writable: yes" echo-space files, marking intended space the agent would like the file to go.  e= stay in echo-space.  r=put in repository.  s=put in offering basket (source files)
- **Promotion-Rubric-General** Type: filepath Relevance: We might have a universal rubric, and/or rubrics that apply to certain types of files.  If this field is empty, assume only default promotion requirements.
- **Promotion-Rubric-Specific** Type: yaml list; required: A structured list of specific requirements (id/score/title/note) that together determine Promotion-Ready status.  If no rubrics have been determined, include a placeholder:
  - id: 1
    score: 100
    title: ""
    note: ""
- **Promotion-Ready-Owner**: Type: enum - required — yes|no|TBD
- **Promotion-Ready-Agent**: Type: enum - required — yes|no|TBD
- **Promotion-Ready-Agent-Confidence**: Type: Numeric - Copilot-determined value between 0–10 based on the agreed rubrics and other concerns.

Notes on promotion enforcement (brief)
- Dates: include explicit timezone offset (ISO 8601). Example (CST): 2025-11-04T19:16:00-06:00.
---