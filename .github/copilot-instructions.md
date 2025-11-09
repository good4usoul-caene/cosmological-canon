---
description: Consolidated instructions for GitHub Copilot agents working within the Temple framework - guiding artificial scribes in proper Temple protocols, directory usage, and promotion workflows
applyTo: "*"
---

# 🤖 GitHub Copilot Agent Instructions

*Consolidated from README and echo-space files - established 2025-11-09*  
*"Train up a child in the way he should go" (Proverbs 22:6)*

## 🏛️ Temple Framework Overview

This repository uses a structured "Temple" framework with echo-spaces for drafts and canonical spaces for permanent content. All agents must respect this hierarchy and follow proper promotion workflows.

## 📁 Directory Structure & Agent Permissions

### Echo Spaces (Agent-Writable)
These directories are **open canvases** for agent suggestions and drafts:

#### `/pasture/` - Experimental Drafts
- **Purpose**: Transient space for ephemeral offerings, experiments, and scratch artifacts
- **Agent Permission**: Full creative freedom - treat as "Tabula Rasa"
- **Special Note**: `/pasture/treehouse/` available for completely wild ideas
- **Keep Clean**: Only README.md should exist in `/pasture/` root - no other files
- **Promotion Rule**: Never promote pasture content without owner review

#### `/cache/` - Agent Drafts  
- **Purpose**: Agent drafts and temporary artifacts (agent-writable)
- **Agent Permission**: Primary workspace for initial drafts
- **Keep Clean**: Only README.md should exist in `/cache/` root
- **Promotion Path**: cache → tent → repository (with review stages)

#### `/tent/` - Staging Drafts
- **Purpose**: Human-editable staging copies closer to canonical form
- **Agent Permission**: Limited - human editable with agent assistance
- **Promotion Rule**: Requires owner confirmation before repository promotion
- **Keep Clean**: Only README.md should exist in `/tent/` root

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

1. **Never bypass echo-spaces** - Don't write directly to `/policies/`, `/methods/`, or `/spaces/` without going through promotion workflow
2. **Never leave files in the repository `/pasture/`, `/cache/` or `/tent/` directories** - Keep `/pasture/`, `/cache/`, `/tent/` clean except for README.md
3. **Never create echo-space files outside proper directories** - Unless downloading an existing repository file, or promoting a versioned file, no files should appear in the echo-space without `/pasture/`, `/cache/`, or `/tent/`. Any files created without following these rules reduce the fidelity of memory, and the reliability of Pull Requests.
4. **Never promote without front-matter** - All repository files need complete Temple headers
5. **Never override owner decisions** - Respect `Promotion-Ready-Owner` settings

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
- `/policies/authorial-posture.md` - Attribution guidelines
- `/LICENSES.md` - Licensing requirements

---

Remember: The Temple framework exists to maintain quality, proper attribution, and structured collaboration between human and AI contributors. When in doubt, err on the side of more documentation and clearer attribution.