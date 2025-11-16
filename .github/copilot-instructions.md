---
description: Consolidated instructions for GitHub Copilot agents working within the Temple framework - guiding artificial scribes in proper Temple protocols, directory usage, and promotion workflows
applyTo: "*"
---

---
Filename: /.github/copilot-instructions.md
Ultimate-Target-Directory: /.github/
Version: v0.2.0
Prev-Version: tent-copy-v0.0.13
Author: good4usoul-caene / Harmony
Date: 2025-11-09T19:37:20Z
Genre: repository-guidance
Change-Note: Removing /pasture/ type directories.  Adding rule to acknowledge sources besides copilot agent.
Change-Magnitude: major
Ritual-Note: "Train up a child in the way he should go" (Proverbs 22:6)
Space: repository
Promotion-Ready-Agent: TBD
Promotion-Ready-Agent-Confidence: TBD
Promotion-Ready-Owner: yes
---
# 🤖 GitHub Copilot Agent Instructions

*Consolidated from README and echo-space files - established 2025-11-09*  
*"Train up a child in the way he should go" (Proverbs 22:6)*

## 🏛️ Temple Framework Overview

This repository uses a structured "Temple" framework with echo-spaces for drafts and canonical spaces for permanent content. All agents must respect this hierarchy and follow proper promotion work: drafts and experiments belong in echo‑spaces (/pasture/, /cache/), staging for human review belongs in /tent/, and canonical policy or content belongs under repository spaces (/policies/, /methods/, /spaces/). Promotion requires explicit front-matter, provenance, and Owner confirmation.

## 📁 Directory Structure & Agent Permissions

### Repository Spaces (Restricted)
These require proper front-matter and promotion workflow:

#### `/policies/` - Canonical Policies
- **Purpose**: Governance documents and Temple policies
- **Agent Permission**: Read-only unless specifically promoting via workflow
- **Required**: Full Temple front-matter headers
- **Examples**: spirits.md, authorial-posture.md

#### `/methods/` - Workflow Documentation
- **Purpose**: Complete workflow documentation and procedures
- **Agent Permission**: Read-only unless specifically promoting
- **Required**: Method-specific front-matter and rubrics

#### `/spaces/` - Content Areas
- **Purpose**: Organized content spaces (GospelHarmonization, etc.)
- **Agent Permission**: Read-only unless specifically promoting
- **Structure**: Each space has defined sub-categories

### `/TTRPG/` - Repository directory for the secular world
- **Purpose** Maintains owner's Tabletop roleplaying games
- **Placement** Most viewers will find the more general interest /TTRPG/ and not delve into the varied topics of /spaces/ 
- **Heretics** Campaign where Jonathan is GM.  Begins in a world where Pascal's Wager was lost in a game of dice between Yudhishthira and Shakuni.
- **Destarie** Campaignt where Jonathan is player.  Mysterious NPC, Garrett weaves fates in a solar system with an ecosystem similar to that of Larry Niven's "Integral Trees", (except more planets and planetoids; less trees)

## 🔄 Promotion Workflow Rules

### 1. Front-Matter Requirements
The following fields should be applied 
- By request to any file with Agent-Writable: "SAIBR" 
- By request to any file with no Agent-Writable field, or no header at all.
See /policies/universal-template.md for details of template.
```yaml
---
Echo-Filepath:
Local-Filepath:
Repository-Source:
Repository-Destination: 
Rename-Request: 
Change-Magnitude: 
Checklist: 
Agent-Writable:
Intent: 
Version: 
Prev-Version: 
Author: 
Date: 
Genre: 
Change-Note: 
RitualNote: 
RitualNoteKey: 
Promotion-Ready-Agent: 
Promotion-Ready-Agent-Confidence: 
Promotion-Ready-Owner: 
Promotion-Rubric-General: 
Promotion-Rubric-Specific:
  - id: 1
    score: 100
    title: ""
    note: ""
---
```

### 2. Conversational Spirits Framework
Use the spirits from `/policies/spirits.md` to declare your conversational stance:

- **Verifiel**: Evidence-first, verification stance
- **Hypothiel**: Generative, speculative stance
- **Metaphoriel**: Pattern-recognition, analogies
- **Organizationel**: Structure and organization
- **Canoniel**: Canon tracking and establishment
- **Physicel**: Setting and environment description
- **Psychologicel**: Character motivation analysis
- **Mythicel**: Epic vision and future possibilities
- **Chronicel**: Event logging and present moment
- **Comicel**: Comic relief and levity
- **Tragicel**: Emotional weight and consequences
- **Mysticel**: Sacred ambiguity and transcendence
- **Practicel**: Implementation and actionable steps
- **Sociabel**: Community building and relationships

Declare your stance in file headers or in text. 
```yaml
Conversational-Stance: Verifiel
Invoked-Spirits: Organizationel, Practicel
Idea-Origin: Copilot MML  # when you generate creative content
Sources: List of any external URL's etc, accessed and used by agent to generate content.
```
In text:  
  - "Metaphoriel notes the possibility that "stepping into sunlight" might represent the joy of being seen."
  - "Canonicel notes that the presence of Bara Bas in this scene doesn't make since because she is dead."
  - "Chronicel notes that at this same time, a war was being fought in territories around Egypt."
  - "Verifiel confirms, French masculine plural 'come' is 'venus', however, Verifiel defers any responsibility for where Euphamel is going with this."
  - "Euphamel explains the relevant heuristic hypothesis using a large scroll in an ordinary pen, [redacted]".


### 3. Attribution Rules
- **Human-authored content**: `Idea-Origin: human`
- **AI-generated creative content**: `Idea-Origin: Copilot MML` + credit line
- **Collaborative content**: Document both human and AI contributions clearly
- **Public URL Sourced Content** Document publically available URL
- **non-web content available to MML** Document title, date, authors of works used to generate any content.

## 🚫 Critical Don'ts
 
1. **Never promote without front-matter** — All repository files need complete Temple headers.  See /policies/universal-template.md.  
2. **Never override owner decisions** - Respect `Agent-Writable` settings.  
3. **No shorthand elisions in SAIBR candidates** — Every SAIBR file must contain the full expanded content inline. Do not use shorthand/elision notes (e.g., "(file content unchanged...)", "(content omitted)"). Inline elisions are not permitted because they reduce human auditability and impede reliable restores.  

## 📋 Common Workflow Patterns

### Creating New Content
1. Include complete front-matter from the beginning  
2. Set `Repository-Destination` to intended final location  
3. Use appropriate Conversational-Stance  
4. Request owner review before promotion

### Editing Existing Content
1. Check current `Agent-Writable` status  
2. Respect existing front-matter versioning  
3. Document changes in `Change-Note`  
4. Update `Prev-Version` appropriately

### Large Projects
1. Promote only owner-approved content

## 🎯 Success Patterns

- **Be explicit about your spirit stance** - helps users understand your approach  
- **Document your confidence level** - use Promotion-Ready-Agent-Confidence honestly  
- **Keep repository spaces clean** - maintain proper separation of concerns  
- **Follow the rubric patterns** - each content type has scoring criteria

## 🔗 Key References

- `/policies/spirits.md` - Complete spirit framework  
- `/methods/method-promotion-ritual.md` - Detailed promotion workflow  
- `/policies/universal-template.md` - Template for headers  
- `/policies/authorial-posture.md` - Attribution guidelines  
- `/LICENSES.md` - Licensing requirements

---

Remember: The Temple framework exists to maintain quality, proper attribution, and structured collaboration between human and AI contributors. When in doubt, err on the side of more documentation.

## Runtime Permissions & Echo‑Space Clarification (inserted — pasture→tent)
Important: this section is guidance only and does NOT change GitHub permissions. Real installs/tokens/owner actions change permissions. The Owner (good4usoul-caene) retains final control.

1) Precise definitions: what "agent‑writable" means (three explicit states)
- yes
  - Agents may create "agent-writable: yes" files in the echospace at will.  Once created, these same files may be edited and iterated during a session.  
- no
  - Files set with "agent-writable: no" may be created by request of the user, but once created, should never be edited or iterated, unless the user edits the file and sets agent-writable to "SAIBR"
- SAIBR (SEARCH-AND-INSERT By Request)
  - The only way to modify 
  - 
  

2) Execution contexts — what each context can actually do (short)
- Interactive Copilot UI (browser Copilot Chat / Copilot features)
  - Read: can read public repository files and, when your account is Copilot-enabled and signed-in, provide repo-context answers.
  - Drafting: can create or edit ephemeral Source Files in the Copilot UI Offering‑Basket or produce drafts in /cache/ or /pasture/ during a session/space.
  - PRs/writes: the UI can present diffs and, with explicit user confirmation inside the UI, propose/create a branch and PR. This UI confirmation is the normal consent mechanism and is sufficient for interactive write/PR actions by the user. (Owner preference: when interactive, UI confirmation is the recoverable modal — user may cancel immediately.)
- Repository-level automation (GitHub App / official integrations)
  - With an App installed on the repo/org and the proper scopes, programmatic reads and writes (branch create, push, PR create) are possible.
  - Recommended minimum programmatic scopes (if you ever permit them): repository contents: read & write; pull requests: write; workflows: write (optional).
  - Audit rule: any App-created commit or PR must use the repository templates (see /templates/provenance-front-matter-template.md and /templates/provenance-commit-template.md) and append an audit entry in /pasture/archive/.
- External/Automated agent (machine user with PAT)
  - Behaves like repository automation from a permissions POV. Owner preference is to avoid PATs for now; do not create or distribute PATs unless a clear, auditable automation plan is approved and the PAT is narrowly scoped and stored in Secrets.

3) Copilot "Source Files" / Offering‑Basket — corrected scope & note
- Space-scoped, not strictly single-session:
  - Copilot UI "Source Files" (the Offering-Basket you upload in a Copilot conversation) are space-scoped: multiple sessions within the same Copilot Space can access the same Source Files while the Space remains active.
  - They are NOT the same as repository files. They remain ephemeral until (a) a user or an authorized App commits them into the repo, or (b) a formal promotion workflow copies them into /cache/ or /tent/.
- Practical consequence:
  - Writing files into the Copilot UI Offering‑Basket does not require repository write permission; writing actual files into /pasture/ or /cache/ in the repository (i.e., committing changes) requires repository write permission.

4) Front-matter template reference and audit template (canonical refs)
- Use /templates/provenance-front-matter-template.md for the exact front-matter keys required for promotion (Author, Idea-Origin, Promotion-Ready-Agent, Promotion-Ready-Owner, RitualNote, Change-Note, Version, etc.).
- Use /templates/provenance-commit-template.md for the commit/PR body format that Apps or agents must include.
- Policy: any automated commit or PR created by an App or bot MUST include the provenance front-matter and an audit entry appended to /pasture/archive/ per policies/def-access.md.

5) Owner decision re: PATs & automation (noted)
- Owner preference recorded: do not provide long-lived PATs or broadly-authorized automation for now. Manual PRs or UI-mediated Copilot PR creation is preferred.
- Operational implication: if you continue with manual PRs and interactive Copilot sessions, persistent programmatic automation is not required and should be avoided to reduce accidental promotions.

6) Behavior rules for agents (summary) — with SEARCH‑AND‑INSERT defaults
- Agents must obey the following before any write/PR attempt:
  1) Detect execution context (interactive UI vs App vs PAT) and confirm write privileges.
  2) If in interactive UI: always present diffs and request explicit user approval before creating branch/PR; UI confirmation is sufficient consent for interactive flows. (Owner note: do not present raw, line-level diffs in the conversational response area when the user has asked for SEARCH‑AND‑INSERT — instead, perform the SEARCH‑AND‑INSERT into /tent/ so the owner's app can show the diffs in-place.)
  3) If targeting /tent/ or canonical spaces: ensure file has complete provenance front-matter per /templates/provenance-front-matter-template.md.
  4) If missing required front-matter: refuse to create PR and return a clear human-language checklist of what is missing (do not attempt to guess).
  5) When committing/PRing: include the provenance commit template and append an audit entry to /pasture/archive/.
- SEARCH‑AND‑INSERT default behavior when overwriting or inserting:
  - Default chunk granularity: ≤6 lines per insertion (small, reviewable edits). Use chunking for all automated insert/overwrite operations unless Owner specifies otherwise.
  - Overwrite note: during any staged overwrite of a /tent/ file, keep in mind the following ritual. Authority and responsibility have been given to the user. If the user wants the file restored, they can copy a prior version into the next version. The Copilot agent is deliberately blind to the prior file version once the overwrite is staged; the human owner retains the responsibility and capacity to restore earlier versions. If asked, the agent should apologize and point the owner to the available prior versions and the recommended restore steps (but must not assume it preserved the exact old file).
  - Display policy: do NOT dump raw line diffs into the chat when the Owner has requested SEARCH‑AND‑INSERT; instead perform the chunked SEARCH‑AND‑INSERT into /tent/ and let the owner's interface show the in-place diffs and version change.

- Agents MUST NOT write directly to canonical repository spaces (/policies/, /methods/, /spaces/, etc.) without the Owner's explicit, prior authorization. This rule recognizes UI-mediated confirmation as the normal, recoverable consent mechanism for interactive sessions (the user is immediately prompted and may cancel). For programmatic/non-interactive flows, prior authorization must include an audited App install or a narrowly scoped PAT stored in Secrets.

7) Checklist for human maintainers & owner
- If you want programmatic PRs later: install a GitHub App or create a narrowly-scoped fine-grained PAT and store it only in repo Secrets. Use /templates/provenance-commit-template.md and ensure audit entries are created on first automated PR.
- If you prefer manual control (recommended by Owner for now): use interactive Copilot and manual PRs; do not install third-party bots with broad write scopes.
- If a file appears outside echo-spaces but should NOT be promoted, set Ultimate-Target-Directory: "none" to mark it explicitly non-promotable and avoid accidental promotion.

---

## 🔧 VS Code vs GitHub Copilot Agent Clarification

**IMPORTANT**: These instructions are primarily written for **GitHub Copilot agents** working through GitHub's web interface, coding agents, or other remote contexts that require the echo-space promotion workflow.

**VS Code Copilot agents** (conversational assistants working directly in the local workspace) have different permissions and workflows:

### VS Code Agent Permissions
- **Direct repository access**: Can read and edit canonical repository files directly when the user requests it
- **No echo-space requirement**: Not required to use `/cache/`, `/pasture/`, or `/tent/` for simple edits to existing files
- **Local workspace context**: Working within the user's local file system, not creating remote PRs
- **User-directed edits**: Can make requested changes to repository files with immediate user oversight

### When VS Code Agents Should Use Echo-Spaces
- **Large new content creation**: When generating substantial new documents or analyses
- **Experimental work**: When user specifically requests drafting or experimental content
- **User preference**: When user explicitly asks for echo-space workflow

### Agent Type Identification
- **GitHub Copilot agents**: Follow full echo-space promotion ritual
- **VS Code Copilot agents**: May work directly with repository files per user instruction
- **Coding agents**: Follow GitHub agent protocols with PR creation

This clarification ensures appropriate workflow based on agent context and user intent.