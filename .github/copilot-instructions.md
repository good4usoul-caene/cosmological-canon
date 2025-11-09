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
Change-Note: Promote tent-copy-v0.0.13 to canonical repository file; applied full template and set Ritual-Note per Owner instruction.
Ritual-Note: "Train up a child in the way he should go" (Proverbs 22:6)
Space: repository
Promotion-Ready-Agent: yes
Promotion-Ready-Agent-Confidence: 10
Promotion-Ready-Owner: yes
---
# 🤖 GitHub Copilot Agent Instructions

*Consolidated from README and echo-space files - established 2025-11-09*  
*"Train up a child in the way he should go" (Proverbs 22:6)*

## 🏛️ Temple Framework Overview

This repository uses a structured "Temple" framework with echo-spaces for drafts and canonical spaces for permanent content. All agents must respect this hierarchy and follow proper promotion work: drafts and experiments belong in echo‑spaces (/pasture/, /cache/), staging for human review belongs in /tent/, and canonical policy or content belongs under repository spaces (/policies/, /methods/, /spaces/). Promotion requires explicit front-matter, provenance, and Owner confirmation.

## 📁 Directory Structure & Agent Permissions

### Echo Spaces (Agent-Writable)
These directories are **open canvases** for agent suggestions and drafts.

Note: For the precise, three-state definition of what "agent‑writable" permits in each location (default echo-draft, tent-with-user-permission, and exceptional canonical staging/safe-mistake), see the Runtime Permissions & Echo‑Space Clarification section later in this document. That section contains the operational distinctions agents must follow.

These directories are **open canvases** for agent suggestions and drafts:

#### `/pasture/` - Experimental Drafts
- **Purpose**: Transient space for ephemeral offerings, experiments, and scratch artifacts
- **Agent Permission**: Full creative freedom - treat as "Tabula Rasa"
- **Special Note**: `/pasture/treehouse/` available for completely wild ideas
- **Keep Clean**: Keep this root tidy. Agents may create drafts here, provided each file includes complete provenance front-matter. Do not leave un-headered or stray files in the `/pasture/` root; every echo-space artifact must be traceable and follow the promotion ritual.
- **Promotion Rule**: Never promote pasture content without owner review

#### `/cache/` - Agent Drafts
- **Purpose**: Agent drafts and temporary artifacts (agent-writable)
- **Agent Permission**: Primary workspace for initial drafts
- **Keep Clean**: Keep this root tidy. Agents may create drafts here, provided each file includes complete provenance front-matter. Do not leave un-headered or stray files in the `/cache/` root.
- **Promotion Path**: cache → tent → repository (with review stages)

#### `/tent/` - Staging Drafts
- **Purpose**: Human-editable staging copies closer to canonical form
- **Agent Permission**: Limited - human editable with agent assistance
- **Keep Clean**: Keep this root tidy. Agents may create /tent/ staging copies (agent-created first copy requires user consent semantics) but every /tent/ file must include the required provenance front-matter and be prepared for Owner review. Do not leave un‑headered or stray files in the `/tent/` root.
- **Promotion Rule**: Requires owner confirmation before repository promotion

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

## 🔄 Promotion Workflow Rules

### 1. Front-Matter Requirements
All promoted files MUST include:
```yaml
---
Filename: /path/to/file.md
Ultimate-Target-Directory: /intended/final/location/
Intent: Clear description of file purpose
Version: v1.0.0
Prev-Version: none
Author: good4usoul-caene
Date: YYYY-MM-DDTHH:MM:SS-TZ
Genre: [Documentation|Method|Policy|Analysis|etc]
Change-Note: Description of what changed
RitualNote: Spiritual/metaphysical context
RitualNoteKey: Biblical reference or inspirational quote
Space: [pasture|tent|cache|repository]
Promotion-Ready-Agent: [yes|no]
Promotion-Ready-Agent-Confidence: [1-10]
Promotion-Ready-Owner: [TBD|approved|rejected]
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

Declare your stance in file headers:
```yaml
Conversational-Stance: Verifiel
Invoked-Spirits: Organizationel, Practicel
Idea-Origin: Copilot MML  # when you generate creative content
```

### 3. Attribution Rules
- **Human-authored content**: `Idea-Origin: human`
- **AI-generated creative content**: `Idea-Origin: Copilot MML` + credit line
- **Collaborative content**: Document both human and AI contributions clearly

## 🚫 Critical Don'ts

1. **Never bypass echo-spaces** - Don't write directly to `/policies/`, `/methods/`, or `/spaces/` without going through promotion workflow.  
2. **Keep echo roots clean, but allow staged drafts with provenance** - Agents may create drafts in `/pasture/` and `/cache/` and may stage owner-review copies in `/tent/`, but every echo-space file must include the required provenance front‑matter and follow the promotion ritual; do not leave un‑headered or stray files in these roots.  
3. **Never create echo-space files outside proper directories** - Unless downloading an existing repository file, or promoting a versioned file, no files should appear in the echo-space except within /cache/, /pasture/, or /tent/.  
4. **Never promote without front-matter** - All repository files need complete Temple headers.  
5. **Never override owner decisions** - Respect `Promotion-Ready-Owner` settings.  
6. **No shorthand elisions in /tent/ candidates** — Every /tent/ candidate must contain the full expanded content inline. Do not use shorthand/elision notes (e.g., "(file content unchanged...)", "(content omitted)") inside /tent/ or other echo-space candidate files. Inline elisions are not permitted because they reduce human auditability and impede reliable restores.  
7. **Chapterization rule for very large works** — If the content is very large, break it into smaller chapter-level tent candidates. Each /tent/ candidate must include the full expanded content for the chapter(s) it represents; referencing a pasture copy is acceptable for archival provenance but is not a substitute for inline content in the tent candidate. For each chapterized tent file include:
   - Chapter-Range: descriptive label (e.g., "Chapter 1: Genesis of Wind")  
   - Full-Content-Included: yes  
   - If a pasture copy is referenced, include Full-Content-Pasture-Path and Full-Content-SHA256 in the front-matter for provenance only — the tent candidate must still contain the full chapter text inline.  

(6/7) Rationale: Tent-stage files are human-review artifacts. They must present complete, unambiguous material for reviewers to inspect, verify, and approve. Inline completeness avoids link-rot, simplifies manual review, and preserves a single, auditable human-visible snapshot for each promotion decision.

8. **Never promote without front-matter** — All repository files need complete Temple headers (Filename, Ultimate-Target-Directory, Version, Prev-Version, Author, Date, Genre, Change-Note, RitualNote, Space, Promotion-Ready-Agent, Promotion-Ready-Agent-Confidence, Promotion-Ready-Owner).  
9. **Never override owner decisions** — Respect `Promotion-Ready-Owner` settings; do not promote, edit, or remove owner‑approved indicators without explicit owner authorization.

## Optional note on root/foyer naming
Per Owner decision: use /foyer/ as the default human-facing alias for the filesystem root ("/") when describing owner-facing snapshots, root-level staging, or owner-review artifacts.

- Meaning: /foyer/ is a conceptual, human-facing alias that maps to the repository root (literal "/"). Using /foyer/ in documentation makes it explicit that the reference is owner-facing and not an agent-staging area.
- Rules:
  - Agents must NOT create or modify files under /foyer/ unless the Owner explicitly instructs them to do so.
  - For agent staging and drafting use /pasture/, /cache/ and /tent/ as described above.
  - If an actual directory named /foyer/ is created in the repository, it means a mistake has been made.
  - Option: If the Owner prefers, create a real /foyer/ directory with owner-managed files (foyer.instructions, foyer.README.md) that explicitly map owner-facing references to the repository root; if created, that directory is Owner-managed and must include clear front-matter.
- Example phrasing for agents and docs:
  - "Create a root-facing copy for Owner review (a /foyer/ copy) — the canonical file remains under '/' but the owner sees it labeled as a /foyer/ copy."

## 📋 Common Workflow Patterns

### Creating New Content
1. Start in `/cache/` or `/pasture/` with experimental draft  
2. Include complete front-matter from the beginning  
3. Set `Ultimate-Target-Directory` to intended final location  
4. Use appropriate Conversational-Stance  
5. Request owner review before promotion

### Editing Existing Content
1. Check current `Promotion-Ready-Owner` status  
2. Respect existing front-matter versioning  
3. Document changes in `Change-Note`  
4. Update `Prev-Version` appropriately

### Large Projects
1. Use `/pasture/treehouse/` for wild brainstorming  
2. Organize into logical `/cache/` structure  
3. Move stable pieces to `/tent/` for human review  
4. Promote only owner-approved content

## 🎯 Success Patterns

- **Be explicit about your spirit stance** - helps users understand your approach  
- **Document your confidence level** - use Promotion-Ready-Agent-Confidence honestly  
- **Respect the echo → tent → repository flow** - don't rush promotion  
- **Keep repository spaces clean** - maintain proper separation of concerns  
- **Follow the rubric patterns** - each content type has scoring criteria

## 🔗 Key References

- `/policies/spirits.md` - Complete spirit framework  
- `/methods/method-promotion-ritual.md` - Detailed promotion workflow  
- `/templates/front-matter-template.md` - Template for headers  
- `/templates/provenance-front-matter-template.md` - Exact keys and example front-matter for promotion (use this for staging and PRs)  
- `/templates/provenance-commit-template.md` - Recommended commit/PR body template to include provenance and audit notes  
- `/policies/authorial-posture.md` - Attribution guidelines  
- `/LICENSES.md` - Licensing requirements

---

Remember: The Temple framework exists to maintain quality, proper attribution, and structured collaboration between human and AI contributors. When in doubt, err on the side of more documentation.

## Runtime Permissions & Echo‑Space Clarification (inserted — pasture→tent)
Important: this section is guidance only and does NOT change GitHub permissions. Real installs/tokens/owner actions change permissions. The Owner (good4usoul-caene) retains final control.

1) Precise definitions: what "agent‑writable" means (three explicit states)
- agent‑writable (default echo-draft)
  - By default, "agent‑writable" designates files and directories intended for agent drafting: specifically /cache/ and /pasture/.
  - Properties: agents may create, edit, and iterate drafts here during a session. These are ephemeral or staging artifacts and must not be promoted without the promotion ritual.
- agent‑writable (with user permission / tent staging)
  - /tent/ files are "agent‑writable with user permission": creation of a /tent/ file is considered an action that requires an explicit user command or enthusiastic user consent, but agents must create the first /tent/ staging copy because users cannot directly create echo-space files via the UI. The agent-created /tent/ copy elevates the draft into human-review staging and therefore requires the user's confirmation to proceed toward promotion.
  - Put simply: first-draft origin in the echo-space is agent-created; /tent/ signals a human-review stage and is gated by user consent prior to promotion.
- agent‑writable (exceptional canonical staging & safe‑mistake policy)
  - Non-echo canonical files (anything outside /cache/, /pasture/, /tent/) are only agent-writable in exceptional, controlled circumstances:
    a) the file is a copy taken from the repository and staged for Owner review (copy-in for edit),  
    b) the file is taken from /tent/ and staged specifically to prepare an intentional copy for repository promotion (tent→staging copy), or  
    c) if a mistake occurs and a file exists outside echo-spaces but is NOT meant for promotion, set Ultimate-Target-Directory: "none" to mark it explicitly as non-promotable and avoid accidental promotion.
  - Rationale: three states (default drafts, tent-with-user-permission, exceptional canonical staging / safe-mistake mode) eliminate ambiguity about what "agent-writable" allows in each place.

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