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
  const token = process.env.GITHUB_TOKEN || process.env.ALL_SOULS_TOKEN;
  if (!token) {
    console.error('Set GITHUB_TOKEN or ALL_SOULS_TOKEN in env to a PAT with repo scopes.');
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
