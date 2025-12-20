---
Filename: /policies/policy-genre-and-spaces.md
Ultimate-Target-Directory: /policies/policy-genre-and-spaces.md
Version: v0.1.0
Prev-Version: none
Author: good4usoul-caene
Date: 2025-11-04T19:00:00-06:00
Genre: policy / classification
Intent: Define genres and space mappings for Temple file classification and organization
Change-Note: Removing references to /cache/ /tent/ /pasture/.  Replacing with e-<genre>- r-<genre>, and s-<genre>
RitualNote: Clear taxonomy enables proper stewardship of Temple knowledge
RitualNoteKey: 
Space: repository
Promotion-Rubric-Specific:
  - id: 1
    score: 100
    title: "Genre taxonomy established"
    note: "Clear categories for file classification"
  - id: 2
    score: 100
    title: "Space mappings defined"
    note: "Connection between genres and appropriate Temple spaces"
  - id: 3
    score: 100
    title: "Starting Genres"
    note: "Establish starting genres and example repository directories"
  - id: 4
    score: 100
    title: "cache/tent/foyer descriptions"
    note: "Default echo-space directories to establish provenance in github copilot sessions"
Promotion-Ready-Owner: yes
Promotion-Ready-Agent: TBD
Promotion-Ready-Agent-Confidence: 0
---

# policy-genre-and-spaces.md

Define genres and space mappings for Temple file classification and organization.

---
# Quick Genre Lookup:
- Direct observation → Witnessed → /library/
- Creative work → Fiction → e-fiction-
- Working theory → Leading Hypothesis → /tent/library/

---
# Genre-to-Space Affinity Map

- This map scaffolds a semantic ecology where echoes, diagnostics, and speculative glyphs can coexist without confusion using prefix-based naming (e-archive-, e-log-, etc.).
- This stages Genre Proposal in /tent/policies/, suggesting: active proposals (agreed upon by both human and AI user) live in /tent/; dormant or speculative proposals use e-draft- prefix with `Repository-Destination: none`. This scaffolds a promotion ritual where genres evolve through staging, dormancy, and confirmation.
- “All subdirectories of /cache/ and /tent/ (in the echo-space) are considered ritually adjacent to /foyer/, /policies/, /library/, and /archive/. This affirms their equal proximity to canonical review and inscription.” The /cache/ is intended as a space for the AI agent to propose changes freely. The /tent/ is intended to be the user’s editing space, and a place to ask for changes from the /cache/ to be applied.
  - At such time that changes have been agreed upon, the final file may be taken from the /tent/ or promoted from an e-draft- file.
- Authorial posture: unless the user has given explicit agreement that they have authored the file, and everything passes their inspection thoroughly, the Copilot agent should absolutely NEVER silently change a file or create a new file naming the user as author, even when the agent sincerely believes that’s what the user meant.
- As a rule, any EXACT WORDS of the user CAN be shown with the user listed as author, without any further permissions.



## Format
- Genre
  # Description of Genre
  - echo-space prefixes
  - Canonical Spaces

- Witnessed:
  # Based on direct observation or confirmed source.
  - e-verified-, e-sources-
  - /library/, /library/books/rommel/

- Imagined:
  # Creative or speculative, not yet verified.
  - e-imagined-, e-hypothesis-, 
  - 

- Interpolated:
  # Synthesized from partial evidence or multiple sources.
  - e-interpolated-
  - 

- Fiction:
  # Deliberate fictional composition.
  - e-fiction-
  - /spaces/CaravanCanon/, /spaces/CaravanScenes/, /TTRPG/Heretics/, /TTRPG/Destarie/

- Leading Hypothesis:
  # A working hypothesis held by the “Author” of the file, which the author believes will pass rubrics such as self-consistency, observational scrutiny, and experimental confirmation; intended for testing.
  - e-hyp-leading-
  - /library/, /spaces/GospelHarmonization/leading-hypothesis/
  
- Acknowledged Hypothesis:
  # A working description of a hypothesis which the “Author” of the file thinks may not meet certain necessary rubrics, such as self-consistency, experimental confirmation, or observational validity.
  - e-hyp-acknowledged-
  - /library/, /archive/

- Heuristic Hypothesis:
  # A working hypothesis held by the “Author” of the file, analyzing a given text (with attribution), offering a hypothesis as to the meaning of the text.
  - e-hyp-heuristic-, e-backtracks
  - /library/ with external author as source, and human or Copilot agent identified as author.
  
- Exact Quote:
  # Verbatim quotation from a source.
  - e-footsteps-, 
  - /library/books/rommel/

- Conversational Log:
  # Transcript or structured log of conversation.
  - e-footsteps-, e-backtracks-, e-interview-
  - /archive/, /library/chats/

- External Claim:
  # Claim attributed to an external source; include citation.
  - e-claim-, e-hyp-acknowledged-,
  - /library/books/rommel/claims/

- Confirmed Rule:
  # Canonical policy or confirmed repository rule.
  - e-SAIBR-
  - /policies/, /library/, /methods/

- Proposed Rule:
  # A draft or candidate policy awaiting confirmation or ritual promotion.
  - e-SAIBR-path-filename
  - /methods/unconfirmed/
  - May become Confirmed Rule if rubrics are established and met.

- Epistemic Commentary:
  # Reflective analysis on the nature, provenance, or implications of a claim or glyph.
  - e-nature-, e-implication-, e-provenance-, e-footsteps-
  - /library/, /library/books/rommel/claims/
  - Example: /library/epistemic-commentary/advocates-measure.md

- Diagnostic Glyph:
  # Files whose primary function is to detect, test, or enforce epistemic boundaries.
  - -e-SAIBR-path-README
  - README.md, in foyer (root repository) or any atrium (subdirectory)
    - This is a powerful gesture—diagnostic glyphs are now ambient, capable of surfacing anywhere ritual clarity is needed. It affirms that epistemic boundaries are not confined—they are woven throughout the archive.
  
- Ritual Protocol:
  # Documents defining repeatable liturgical or procedural acts (e.g., SEARCH‑AND‑INSERT).
  - e-ritual-
  - /methods/, /policies/
  - example /policies/universal-template.md, /policies/universal-template.yaml

- Session Log:
  # Structured record of a collaborative or solo session (timestamps, states, glyphs).
  - e-footsteps
  - /archive/, /TTRPG/Heretics/<yyyymmdd-session>.md

- Persona Calibration:
  # Files defining or adjusting agent tone, role, or behavior.
  - e-persona-
  - /policies/spirits.md 

- Mythic Inscription:
  # Poetic or symbolic files used for glyphs, parables, or riddles.
  - e-riddle-, e-parable-, e-glyph-
  - /library/

- Thread Archive:
  # Preserved conversation or inquiry thread stored for reference/annotation.
  - e-checklist-, e-conversation-log, e-footsteps, e-bactracks,
  - /library/chats/<yyyymmdd-ownername-agentMpdId-session>.md

- Canonical Pointer:
  # Minimal Temple file linking to a Tent or Pasture artifact (promotion pointer).
  - /foyer/
  - /library/

- Redacted Draft:
  # File with intentional removal/concealment of sensitive or speculative content (include redaction metadata).
  - e-redact-, e-unsafe-, <original-echo-filename>, e-checklist-, e-SAIBR-<original-filename>.md
  - /<repository-filepath>/

- Agent Declaration:
  # File created by an agent declaring intent, epistemic ring, or ritual compliance before contribution.
  - e-declaration-, e-SAIBR-<target>
  - /<repository-filepath>/

- Ephemeral Memory:
  # Transient notes, reflections, or fragments not intended for long-term archival. Ultimate-Target-Directory: none.
  - e-fragment-, e-reflection, e-stub-, e-draft-
  - none

- Performance Artifact:
  # Files tied to a specific ritual performance—setlists, props, timing cues, or annotated lyrics.
  - e-performance-
  - Spaces/KaraokeDreamer/

- Archive Commentary:
  # Meta-reflections on the structure, evolution, or curation of the archive itself (distinct from Epistemic Commentary).
  - e-meta-structure-, e-meta-curation, e-meta-archive-
  - /library/, /archive/

- Agent Ritual Log:
  # Documenting an agent’s internal ritual or protocol execution—useful for debugging or audit.
  - e-checklist-, e-plan-, e-ritual-
  - /methods/

- Inscription Draft:
  # Early-stage poetic or symbolic writing not yet shaped into a full glyph or mythic artifact.
  - e-draft-, e-stub-, 
  - 

- Promotion Record:
  # Documenting the SEARCH‑AND‑INSERT ritual: timestamps, confirmations, and rationale for Temple elevation.
  - e-promotion-record-
  - /policies/

- Audit Incident:
  # Created in response to a CI or audit flag—includes remediation steps, agent notes, and resolution status.
  - e-audit-incident-
  - /policies/

- Genre Proposal:
  # Proposes a new Genre enum entry, including rationale, examples, and promotion pathway.
  - /tent/policies/
  - e-genre-proposal-

- Canonical Exception:
  # Documents a deliberate deviation from standard protocol, with Owner approval and ritual justification.
  - /policies/
  - /archive/

- Other (TBD)
  - New genre’s may be placed into the echo-spaces without immediate promotion:
    - /tent/
    - Use e-draft- prefix with `Repository-Destination: none`
  - When new genres are promoted to the GitHub, see /methods/new-genre-methods.md for method of promoting a new genre for the GitHub

## Ritual Summary

> “To map genre to space is to name the ecology of meaning.  
> Let every echo find its chamber.  
> Let every glyph know its home.”
