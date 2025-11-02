#!/usr/bin/env bash
set -euo pipefail

# Usage: run from the directory where you want the repo structure created,
# or from your repository root. This will create the files and then zip them.

ROOT_DIR="${PWD}"
echo "Creating files under ${ROOT_DIR} ..."

# create directories
mkdir -p .github/workflows scripts policies pasture/archive

# stage-echo-to-foyer.yml
cat > .github/workflows/stage-echo-to-foyer.yml <<'YML'
name: Stage echo (cache|tent) → /foyer/ for review

on:
  workflow_dispatch:
    inputs:
      echo_source:
        description: "Echo source to stage (echo/cache or echo/tent)"
        required: true
        default: "echo/cache"
      file_pattern:
        description: "Optional glob (relative to echo source) to select files (default: all)"
        required: false
        default: "**/*"

jobs:
  stage-echo-to-foyer:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Checkout repository (no persisted credentials)
        uses: actions/checkout@v4
        with:
          persist-credentials: false
          fetch-depth: 0

      - name: Configure git user
        run: |
          git config user.name "caravan-bot"
          git config user.email "caravan-bot@example.com"

      - name: Resolve inputs
        id: inputs
        run: |
          echo "source=${{ github.event.inputs.echo_source }}" >> $GITHUB_OUTPUT
          echo "pattern=${{ github.event.inputs.file_pattern }}" >> $GITHUB_OUTPUT

      - name: Stage matching echo files into /foyer/
        id: copy
        run: |
          SRC="${{ steps.inputs.outputs.source }}"
          PATTERN="${{ steps.inputs.outputs.pattern }}"
          echo "Source: $SRC"
          echo "Pattern: $PATTERN"

          mkdir -p foyer
          if [ -d "$SRC" ]; then
            if command -v rsync >/dev/null 2>&1; then
              if [ "$PATTERN" = "**/*" ] || [ -z "$PATTERN" ]; then
                rsync -a "$SRC"/ foyer/ || true
              else
                (cd "$SRC" && eval "shopt -s globstar; for f in $PATTERN; do [ -f \"$f\" ] && rsync -R \"\$f\" ../foyer/ || true; done") || true
              fi
            else
              cp -a "$SRC"/. foyer/ || true
            fi
          else
            echo "Source directory '$SRC' not present; nothing to stage."
          fi

          git add foyer || true
          if git diff --staged --quiet; then
            echo "no_changes=true" >> $GITHUB_OUTPUT
          else
            echo "no_changes=false" >> $GITHUB_OUTPUT
          fi

      - name: Commit staged foyer files
        if: steps.copy.outputs.no_changes == 'false'
        run: |
          git commit -m "Bot: stage echo → /foyer/ for human review (run ${{ github.run_id }})" || true

      - name: Create PR for foyer staging
        if: steps.copy.outputs.no_changes == 'false'
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.BOT_PAT }}
          commit-message: "Bot: stage echo → /foyer/ for review"
          branch: "bot/stage-foyer-${{ github.run_id }}"
          title: "Stage echo artifacts to /foyer/ for review"
          body: |
            This PR stages artifacts from ${{ github.event.inputs.echo_source }} into /foyer/ for human review.
            Do NOT promote to /policies/ or to repository root without SEARCH‑AND‑INSERT + explicit Owner confirmation.
          labels: "auto-stage, needs-review"

      - name: Report nothing staged
        if: steps.copy.outputs.no_changes == 'true'
        run: echo "No artifacts staged; no PR created."
YML

# stage-echo-to-echo-policies.yml
cat > .github/workflows/stage-echo-to-echo-policies.yml <<'YML'
name: Stage echo (cache|tent) → /echo/policies/ for policy preview

on:
  workflow_dispatch:
    inputs:
      echo_source:
        description: "Echo source to stage (echo/cache or echo/tent)"
        required: true
        default: "echo/cache"
      file_pattern:
        description: "Optional glob (relative to echo source) to select files (default: all)"
        required: false
        default: "**/*"

jobs:
  stage-echo-policies:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          persist-credentials: false
          fetch-depth: 0

      - name: Configure git user
        run: |
          git config user.name "caravan-bot"
          git config user.email "caravan-bot@example.com"

      - name: Resolve inputs
        id: inputs
        run: |
          echo "source=${{ github.event.inputs.echo_source }}" >> $GITHUB_OUTPUT
          echo "pattern=${{ github.event.inputs.file_pattern }}" >> $GITHUB_OUTPUT

      - name: Stage matching echo files into /echo/policies/
        id: copy
        run: |
          SRC="${{ steps.inputs.outputs.source }}"
          PATTERN="${{ steps.inputs.outputs.pattern }}"
          echo "Source: $SRC"
          echo "Pattern: $PATTERN"

          mkdir -p echo/policies
          if [ -d "$SRC" ]; then
            if command -v rsync >/dev/null 2>&1; then
              if [ "$PATTERN" = "**/*" ] || [ -z "$PATTERN" ]; then
                rsync -a "$SRC"/ echo/policies/ || true
              else
                (cd "$SRC" && eval "shopt -s globstar; for f in $PATTERN; do [ -f \"$f\" ] && rsync -R \"\$f\" ../echo/policies/ || true; done") || true
              fi
            else
              cp -a "$SRC"/. echo/policies/ || true
            fi
          else
            echo "Source directory '$SRC' not present; nothing to stage."
          fi

          git add echo/policies || true
          if git diff --staged --quiet; then
            echo "no_changes=true" >> $GITHUB_OUTPUT
          else
            echo "no_changes=false" >> $GITHUB_OUTPUT
          fi

      - name: Commit echo/policies staging
        if: steps.copy.outputs.no_changes == 'false'
        run: |
          git commit -m "Bot: stage echo → /echo/policies/ for policy preview (run ${{ github.run_id }})" || true

      - name: Create PR for echo/policies staging
        if: steps.copy.outputs.no_changes == 'false'
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.BOT_PAT }}
          commit-message: "Bot: stage echo → /echo/policies/ for preview"
          branch: "bot/stage-echo-policies-${{ github.run_id }}"
          title: "Stage echo artifacts to /echo/policies/ for policy preview"
          body: |
            This PR stages artifacts from ${{ github.event.inputs.echo_source }} into /echo/policies/ for human review and SEARCH‑AND‑INSERT preparation.
            Do NOT promote to /policies/ without explicit Owner confirmation.
          labels: "auto-stage, needs-policy-review"

      - name: Report nothing staged
        if: steps.copy.outputs.no_changes == 'true'
        run: echo "No artifacts staged; no PR created."
YML

# promote-foyer-to-root.yml
cat > .github/workflows/promote-foyer-to-root.yml <<'YML'
name: Promote /foyer/ → repository root (Owner-only)

on:
  workflow_dispatch:
    inputs:
      source_branch:
        description: "Source branch containing reviewed /foyer/ changes (optional: leave blank to use latest bot staging branch)"
        required: false
        default: ""
      promotion_note:
        description: "Short owner promotion note"
        required: false
        default: "Owner-approved promotion to root"

jobs:
  promote-to-root:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Ensure caller is Repository Owner
        run: |
          echo "Triggered by: $GITHUB_ACTOR"
          if [ "${GITHUB_ACTOR}" != "good4usoul-caene" ]; then
            echo "Only the Repository Owner (good4usoul-caene) may run this promotion workflow."
            exit 1
          fi

      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          persist-credentials: false
          fetch-depth: 0

      - name: Determine source branch
        id: src
        run: |
          if [ -n "${{ github.event.inputs.source_branch }}" ]; then
            echo "source_branch=${{ github.event.inputs.source_branch }}" >> $GITHUB_OUTPUT
          else
            branch=$(git ls-remote --heads origin 'bot/stage-foyer-*' | awk '{print $2}' | sed 's|refs/heads/||' | sort -r | head -n1)
            if [ -z "$branch" ]; then
              branch="main"
            fi
            echo "source_branch=$branch" >> $GITHUB_OUTPUT
          fi
          echo "Using source branch: ${{ steps.src.outputs.source_branch }}"

      - name: Fetch and checkout source branch
        run: |
          git fetch origin ${{ steps.src.outputs.source_branch }}:refs/remotes/origin/${{ steps.src.outputs.source_branch }} || true
          git checkout -b promote-from-${{ steps.src.outputs.source_branch }} origin/${{ steps.src.outputs.source_branch }} || git checkout -b promote-from-${{ steps.src.outputs.source_branch }}

      - name: Validate Promotion-Ready front-matter in foyer files
        id: validate
        run: |
          missing=""
          if [ -d "foyer" ]; then
            while IFS= read -r -d '' file; do
              if ! grep -qE '^Promotion-Ready:[[:space:]]*owner-approved' "$file"; then
                missing="${missing}\n${file}"
              fi
            done < <(find foyer -type f -print0)
          else
            echo "No /foyer/ directory present. Nothing to promote."
            exit 1
          fi

          if [ -n "$missing" ]; then
            echo "The following foyer files are missing 'Promotion-Ready: owner-approved' in front-matter:"
            echo -e "$missing"
            exit 2
          else
            echo "All foyer files have Promotion-Ready: owner-approved"
          fi

      - name: Copy foyer files into repository root respecting Ultimate-Target-Directory
        id: copy
        run: |
          ts=$(date -u +"%Y%m%dT%H%M%SZ")
          promoted_list=""
          while IFS= read -r -d '' file; do
            filename="$(basename "$file")"
            target=$(grep -m1 '^Ultimate-Target-Directory:' "$file" | sed -E 's/^Ultimate-Target-Directory:[[:space:]]*//')
            target="${target#/}"
            if [ -z "$target" ]; then
              target="."
            fi
            mkdir -p "$target"
            cp "$file" "$target/$filename"
            promoted_list="${promoted_list}\n${file} -> ${target}/${filename}"
          done < <(find foyer -type f -print0)

          echo -e "Promoted files:${promoted_list}"
          echo "promoted_list<<EOF" >> $GITHUB_OUTPUT
          echo -e "${promoted_list}" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

          git add . || true

      - name: Create Promotion Record
        if: steps.copy.outputs.promoted_list != ''
        run: |
          timestamp=$(date -u +"%Y%m%dT%H%M%SZ")
          record="pasture/archive/promotion-record-${timestamp}.md"
          mkdir -p pasture/archive
          cat > "${record}" <<EOF
---
Promoted-By: $GITHUB_ACTOR
Promotion-Time: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
Source-Branch: ${{ steps.src.outputs.source_branch }}
Note: ${{ github.event.inputs.promotion_note }}
Files-Promoted:
${{ steps.copy.outputs.promoted_list }}
---
This promotion record documents the Owner-authorized promotion from /foyer/ to repository root.
EOF
          git add "${record}"

      - name: Commit promotion changes
        run: |
          if git diff --staged --quiet; then
            echo "No staged changes to commit."
            exit 1
          else
            git commit -m "Bot: promote /foyer/ → repository root (run ${{ github.run_id }})" || true
          fi

      - name: Create Promotion PR
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.BOT_PAT }}
          commit-message: "Bot: promote /foyer/ → repository root (run ${{ github.run_id }})"
          branch: "bot/promote-foyer-root-${{ github.run_id }}"
          title: "Promote /foyer/ artifacts to repository root (owner confirmed)"
          body: |
            Owner-triggered promotion of foyer artifacts to repository root.
            Promotion Record (created in this PR): pasture/archive/promotion-record-<timestamp>.md
            Note: merges to main must follow branch-protection and human-review requirements.
          labels: "auto-promote, needs-review"
YML

# promote-foyer-to-policies.yml
cat > .github/workflows/promote-foyer-to-policies.yml <<'YML'
name: Promote /foyer/ (or /echo/policies/) → /policies/ (Owner-only)

on:
  workflow_dispatch:
    inputs:
      source_branch:
        description: "Source branch containing reviewed foyer/echo/policies changes (optional)"
        required: false
        default: ""
      promotion_note:
        description: "Short owner promotion note"
        required: false
        default: "Owner-approved promotion to /policies/"

jobs:
  promote-to-policies:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Ensure caller is Repository Owner
        run: |
          echo "Triggered by: $GITHUB_ACTOR"
          if [ "${GITHUB_ACTOR}" != "good4usoul-caene" ]; then
            echo "Only the Repository Owner (good4usoul-caene) may run this promotion workflow."
            exit 1
          fi

      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          persist-credentials: false
          fetch-depth: 0

      - name: Determine source branch
        id: src
        run: |
          if [ -n "${{ github.event.inputs.source_branch }}" ]; then
            echo "source_branch=${{ github.event.inputs.source_branch }}" >> $GITHUB_OUTPUT
          else
            branch=$(git ls-remote --heads origin 'bot/stage-foyer-*' | awk '{print $2}' | sed 's|refs/heads/||' | sort -r | head -n1)
            if [ -z "$branch" ]; then
              branch="main"
            fi
            echo "source_branch=$branch" >> $GITHUB_OUTPUT
          fi
          echo "Using source branch: ${{ steps.src.outputs.source_branch }}"

      - name: Fetch and checkout source branch
        run: |
          git fetch origin ${{ steps.src.outputs.source_branch }}:refs/remotes/origin/${{ steps.src.outputs.source_branch }} || true
          git checkout -b promote-from-${{ steps.src.outputs.source_branch }} origin/${{ steps.src.outputs.source_branch }} || git checkout -b promote-from-${{ steps.src.outputs.source_branch }}

      - name: Validate Promotion-Ready front-matter in foyer or echo/policies files
        id: validate
        run: |
          missing=""
          for DIR in foyer echo/policies; do
            if [ -d "$DIR" ]; then
              while IFS= read -r -d '' file; do
                if ! grep -qE '^Promotion-Ready:[[:space:]]*owner-approved' "$file"; then
                  missing="${missing}\n${file}"
                fi
              done < <(find "$DIR" -type f -print0)
            fi
          done

          if [ -n "$missing" ]; then
            echo "The following files lack 'Promotion-Ready: owner-approved' in front-matter:"
            echo -e "$missing"
            exit 2
          else
            echo "All candidate files have Promotion-Ready: owner-approved"
          fi

      - name: Copy foyer / echo/policies files into /policies/
        id: copy
        run: |
          promoted=""
          mkdir -p policies
          for DIR in foyer echo/policies; do
            if [ -d "$DIR" ]; then
              while IFS= read -r -d '' file; do
                filename="$(basename "$file")"
                cp "$file" "policies/$filename"
                promoted="${promoted}\n${file} -> policies/${filename}"
              done < <(find "$DIR" -type f -print0)
            fi
          done
          echo -e "promoted_list:${promoted}"
          echo "promoted_list<<EOF" >> $GITHUB_OUTPUT
          echo -e "${promoted}" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

          git add policies || true

      - name: Create Promotion Record
        if: steps.copy.outputs.promoted_list != ''
        run: |
          timestamp=$(date -u +"%Y%m%dT%H%M%SZ")
          record="pasture/archive/promotion-record-${timestamp}.md"
          mkdir -p pasture/archive
          cat > "${record}" <<EOF
---
Promoted-By: $GITHUB_ACTOR
Promotion-Time: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
Source-Branch: ${{ steps.src.outputs.source_branch }}
Note: ${{ github.event.inputs.promotion_note }}
Files-Promoted:
${{ steps.copy.outputs.promoted_list }}
---
Owner-authorized promotion record for /policies/.
EOF
          git add "${record}"

      - name: Commit promotion changes
        run: |
          if git diff --staged --quiet; then
            echo "No staged changes to commit."
            exit 1
          else
            git commit -m "Bot: promote → /policies/ (run ${{ github.run_id }})" || true
          fi

      - name: Create Promotion PR
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.BOT_PAT }}
          commit-message: "Bot: promote → /policies/ (run ${{ github.run_id }})"
          branch: "bot/promote-policies-${{ github.run_id }}"
          title: "Promote /foyer/ artifacts to /policies/ (owner confirmed)"
          body: |
            Owner-triggered promotion of foyer/echo/policies artifacts to /policies/.
            Promotion Record: pasture/archive/promotion-record-<timestamp>.md
            NOTE: This PR must be reviewed and merged per branch protection rules. Do not merge without SEARCH‑AND‑INSERT confirmation.
          labels: "auto-promote, needs-review"
YML

# upload-file.js
cat > scripts/upload-file.js <<'JS'
/**
 * Ad-hoc script to create or update a file in a GitHub repo using a PAT.
 *
 * Usage (locally):
 *   export GITHUB_TOKEN=ghp_xxx   # or set in environment
 *   node scripts/upload-file.js --owner good4usoul-caene --repo myrepo --path policies/def-access.md --message "Add def-access" --file ./local/def-access.md
 *
 * Note: Install @octokit/rest and minimist first:
 *   npm install @octokit/rest minimist
 */

const fs = require('fs');
const path = require('path');
const { Octokit } = require('@octokit/rest');
const argv = require('minimist')(process.argv.slice(2));

async function main() {
  const token = process.env.GITHUB_TOKEN || process.env.BOT_PAT;
  if (!token) {
    console.error('Set GITHUB_TOKEN or BOT_PAT in env to a PAT with repo scopes.');
    process.exit(1);
  }

  const owner = argv.owner;
  const repo = argv.repo;
  const filePath = argv.path; // repo path to create/update
  const message = argv.message || `Add/update ${filePath}`;
  const localFile = argv.file;

  if (!owner || !repo || !filePath || !localFile) {
    console.error('Usage: node upload-file.js --owner <owner> --repo <repo> --path <repo/path> --file <localfile> [--message "commit message"]');
    process.exit(1);
  }

  const octokit = new Octokit({ auth: token });

  const content = fs.readFileSync(path.resolve(localFile), { encoding: 'utf8' });
  const b64 = Buffer.from(content, 'utf8').toString('base64');

  try {
    let sha;
    try {
      const get = await octokit.repos.getContent({
        owner,
        repo,
        path: filePath,
      });
      if (Array.isArray(get.data)) {
        throw new Error('Expected file but found directory');
      }
      sha = get.data.sha;
    } catch (err) {
      if (err.status && err.status === 404) {
        sha = undefined;
      } else if (err.message && err.message.includes('Expected file')) {
        console.error('Destination path is a directory in the repo. Choose a file path.');
        process.exit(1);
      } else {
        sha = undefined;
      }
    }

    const params = {
      owner,
      repo,
      path: filePath,
      message,
      content: b64,
      committer: {
        name: 'caravan-bot',
        email: 'caravan-bot@example.com',
      },
      author: {
        name: 'caravan-bot',
        email: 'caravan-bot@example.com',
      },
    };
    if (sha) params.sha = sha;

    const res = await octokit.repos.createOrUpdateFileContents(params);
    console.log('File created/updated:', res.data.content.html_url);
  } catch (err) {
    console.error('Error creating/updating file:', err);
    process.exit(1);
  }
}

main();
JS

# policies/README.md
cat > policies/README.md <<'MD'
# Policies & Promotion Rituals (brief)

This README documents the canonical promotion ritual and the echo → foyer → promotion pipeline used in this repository.

Key directories
- echo/cache/         — Agent drafts and temporary artifacts (agent-writable).
- echo/tent/          — Human-editable staging copies (editable by humans and agents with limits).
- echo/foyer/         — Handoff staging area for human review (promote only after SEARCH‑AND‑INSERT).
- echo/policies/      — Policy-focused preview staging area.
- foyer/              — Repository staging area for items prepared for promotion.
- policies/           — Canonical policy files (Temple). Promotion target.
- pasture/archive/    — Audit and Promotion Record storage.

Promotion flow (summary)
1. Agent writes draft to echo/cache/ or echo/tent/.
2. Run stage-echo-to-foyer.yml (manual) to copy selected artifacts into echo/foyer/ (PR created for review).
3. Reviewer performs SEARCH‑AND‑INSERT and sets `Promotion-Ready: owner-approved` in front-matter of files when ready.
4. Owner triggers promote-foyer-to-policies.yml or promote-foyer-to-root.yml (Owner-only workflows).
5. Promotion workflow validates `Promotion-Ready: owner-approved`, writes a Promotion Record to pasture/archive/, and creates a PR for human merge.

Owner responsibilities
- Confirm SEARCH‑AND‑INSERT edits before running promotion workflows.
- Maintain branch-protection rules requiring human reviewers for merges to main or /policies/.
- Add a repository secret `BOT_PAT` (or install a GitHub App) to enable workflows to push PR branches. Rotate/revoke secrets after testing.

Notes
- Do NOT bypass foyer or echo/policies staging when promoting policy files.
- All promoted files must include provenance front-matter (Author, Date, Change-Note, RitualNote, Ultimate-Target-Directory) and `Promotion-Ready: owner-approved` when promoted.
MD

# create zip
ZIP_NAME="promotion-workflows.zip"
if command -v zip >/dev/null 2>&1; then
  zip -r "${ZIP_NAME}" .github workflows scripts policies pasture -x "*/.git/*"
  echo "Created ${ZIP_NAME} in ${ROOT_DIR}"
else
  # fallback: use python to create zip
  python3 - <<PY
import zipfile, os
zf = zipfile.ZipFile("${ZIP_NAME}", "w", zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk("."):
    if ".git" in root.split(os.sep): 
        continue
    for f in files:
        if root.startswith("./.git"):
            continue
        # include only our target dirs
        if root.startswith("./.github") or root.startswith("./scripts") or root.startswith("./policies") or root.startswith("./pasture"):
            zf.write(os.path.join(root, f), arcname=os.path.join(root, f).lstrip("./"))
zf.close()
print("Created ${ZIP_NAME}")
PY
fi

echo "Done. Open ${ZIP_NAME} or unzip to inspect files."