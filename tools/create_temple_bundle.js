// Create a small Temple bundle: PR template, .gitattributes, LICENSES.md, per-space README stubs, CHS scaffold.
// Run: node tools/create_temple_bundle.js
// Behavior: creates each file only if it does not already exist (safe to run multiple times).
const fs = require('fs');
const path = require('path');

const files = [
  {
    path: path.join('.github','PULL_REQUEST_TEMPLATE','pull_request_template.md'),
    content: `Title: [short, descriptive title]

Summary
-------
[Brief summary of the change and its intent — include both technical and mythic lines if helpful.]

Spirits / Conversational stance (required)
-----------------------------------------
Conversational-Stance: [Verifiel | Hypothiel | Metaphoriel | Organizationel]
Invoked-Spirits: [comma-separated list of additional invoked spirits, optional]

Idea provenance (required)
--------------------------
Idea-Origin: [human | Copilot MML]
Idea-Origin-Details: [optional — fuller provenance or credit text and date]
# Example:
# "human requested names for spirits of scientific inquiry | Copilot MML offered angel names by (probably anonymous) request of Jonathan Doolin, circa Sep-Oct 2024"

Files changed
-------------
- [list of key files changed]

Provenance & Licensing (if applicable)
-------------------------------------
- If the change adds translated text or externally authored content, include original_translation, edition, ISBN and place the permission file under /permissions/.
- License: [see LICENSES.md]

Testing & Verification
----------------------
- How was this tested? [unit tests, manual checks, proofread, Verifiel checks performed]
- If Hypothiel produced creative portions, have Verifiel checks been scheduled? [yes/no]

Notes for reviewers
-------------------
[Anything reviewers should focus on — including whether the change requires editorial or ethical review]

Checklist (quick)
- [ ] Conversational-Stance set
- [ ] Idea-Origin set and Idea-Origin-Details included if needed
- [ ] Provenance recorded if external text added
- [ ] License mapping updated if needed
`
  },
  {
    path: '.gitattributes',
    content: `# Repository canonical EOL: LF. Windows checkouts may be CRLF (via core.autocrlf=true).

*.md    text eol=lf
*.tex   text eol=lf
*.sty   text eol=lf
*.cls   text eol=lf
*.bib   text eol=lf
*.yml   text eol=lf
*.yaml  text eol=lf
*.json  text eol=lf
*.xml   text eol=lf
*.html  text eol=lf
*.js    text eol=lf
*.ts    text eol=lf
*.py    text eol=lf
*.sh    text eol=lf
*.csv   text eol=lf
*.ps1   text eol=crlf
*.bat   text eol=crlf
*.cmd   text eol=crlf

*.svg   text eol=lf

*.png   binary
*.jpg   binary
*.jpeg  binary
*.gif   binary
*.pdf   binary
*.zip   binary
*.tar.gz binary

*       text=auto
`
  },
  {
    path: 'LICENSES.md',
    content: `Repository licensing mapping (place this at repo root)

- Code / scripts / macros: MIT (default) — add per-file header if different.
- Text / ritual content: CC-BY-SA-4.0 (default) — annotate exceptions in file headers.
- Include explicit per-file header when deviating.
`
  },
  {
    path: path.join('permissions','.gitkeep'),
    content: ''
  },
  {
    path: 'SPIRITS.md',
    content: `Conversational Spirits — Stances for Temple Interaction

Verifiel: evidence-first stance (historical, scriptural, scientific plausibility)
Hypothiel: generative stance (mark Idea-Origin: Copilot MML for creative content)
Metaphoriel: pattern-recognition; suggested for CaravanScenes
Organizationel: structural; suggested for Chronicle Scribe & Macros

File headers should include:
% Conversational-Stance: <Verifiel|Hypothiel|Metaphoriel|Organizationel>
% Invoked-Spirits: ...
% Idea-Origin: <human|Copilot MML>
% Idea-Origin-Details: <optional fuller provenance>
`
  },
  {
    path: path.join('spaces','CanonicalTemplates','README.md'),
    content: `## CanonicalTemplates

Purpose: Houses reusable Canons, macros, and ritual declarations. Files are templates—living artifacts for invocation.
Mythic: "To template is to offer. To offer is to invite."
`
  },
  {
    path: path.join('spaces','CaravanCanon','README.md'),
    content: `## CaravanCanon

Purpose: Custodial collection of the Caravan's formalized canons and canonical metadata.
Greeting stance suggested: Verifiel
`
  },
  {
    path: path.join('spaces','CaravanScenes','README.md'),
    content: `## CaravanScenes

Purpose: Scene-level artifacts used by the Caravan.
Greeting stance suggested: Metaphoriel
`
  },
  {
    path: path.join('spaces','ChronicleScribe','README.md'),
    content: `## Chronicle Scribe

Purpose: Live witness of Temple interactions; locus of temporal annotation.
Greeting stance suggested: Organizationel
`
  },
  {
    path: path.join('spaces','MacrosAndMechanisms','README.md'),
    content: `## Macros and Mechanisms

Purpose: Ritual chamber for LaTeX macro design, naming conventions, and ethical calibration.
Greeting stance suggested: Organizationel (invite Metaphoriel for naming)
`
  },
  {
    path: path.join('spaces','CHS','chron-scaffold-chunk.csv'),
    content: `chunk_id,source,notes
CHS-001,Mark:1-4,placeholder for chunk-level harmonization
CHS-002,Matthew:1-3,placeholder
`
  }
];

files.forEach(f => {
  const dir = path.dirname(f.path);
  fs.mkdirSync(dir, { recursive: true });
  if (!fs.existsSync(f.path)) {
    fs.writeFileSync(f.path, f.content, 'utf8');
    console.log('Wrote', f.path);
  } else {
    console.log('Skipped (exists):', f.path);
  }
});
console.log('Provisioning complete. Please inspect files, then git add/commit/push as you prefer.'); 