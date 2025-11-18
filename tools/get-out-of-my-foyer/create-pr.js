/**
 * Create GitHub PR for library files using the Temple promotion workflow
 * 
 * Usage: node create-pr.js --title "PR Title" --body "PR Body"
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

  const owner = 'good4usoul-caene';
  const repo = 'cosmological-canon';
  const title = argv.title || 'Upload library files';
  const body = argv.body || 'Automated library upload';

  const octokit = new Octokit({ auth: token });

  console.log('Creating branch and PR for library uploads...');

  // Get main branch SHA
  const { data: mainBranch } = await octokit.repos.getBranch({
    owner,
    repo,
    branch: 'main'
  });

  const branchName = `library-upload-${Date.now()}`;
  
  // Create new branch
  await octokit.git.createRef({
    owner,
    repo,
    ref: `refs/heads/${branchName}`,
    sha: mainBranch.commit.sha
  });

  console.log(`Created branch: ${branchName}`);

  // Upload Queen of the South
  const queenContent = fs.readFileSync('tent/queen-of-the-south-full.md', 'utf8');
  await octokit.repos.createOrUpdateFileContents({
    owner,
    repo,
    path: 'library/books/queen-of-the-south-full.md',
    message: 'Add Queen of the South eschatological analysis',
    content: Buffer.from(queenContent).toString('base64'),
    branch: branchName
  });

  // Upload Riddles of Barabbas
  const riddlesContent = fs.readFileSync('tent/riddles-of-barabbas-full.txt', 'utf8');
  await octokit.repos.createOrUpdateFileContents({
    owner,
    repo,
    path: 'library/books/riddles-of-barabbas-full.txt',
    message: 'Add Riddles of Barabbas rhyming Gospel commentary',
    content: Buffer.from(riddlesContent).toString('base64'),
    branch: branchName
  });

  console.log('Files uploaded to branch');

  // Create PR
  const { data: pr } = await octokit.pulls.create({
    owner,
    repo,
    title: title,
    body: body,
    head: branchName,
    base: 'main'
  });

  console.log(`✅ PR created: ${pr.html_url}`);
  console.log(`📋 PR #${pr.number}: ${title}`);

  // Add audit entry
  const auditEntry = `
## Audit Entry - Library Upload
- **Date**: ${new Date().toISOString()}
- **Agent**: GitHub Copilot (Harmony)
- **Action**: Automated PR creation for library file uploads
- **Branch**: ${branchName}
- **PR**: #${pr.number}
- **Files**: queen-of-the-south-full.md, riddles-of-barabbas-full.txt
- **Author**: Jonathan Doolin (human-authored content)
`;

  // Append audit entry
  let pasturePath = 'pasture/archive/audit-log.md';
  try {
    const { data: existingAudit } = await octokit.repos.getContent({
      owner,
      repo,
      path: pasturePath,
      ref: branchName
    });
    
    const existingContent = Buffer.from(existingAudit.content, 'base64').toString('utf8');
    const updatedContent = existingContent + auditEntry;
    
    await octokit.repos.createOrUpdateFileContents({
      owner,
      repo,
      path: pasturePath,
      message: 'Add audit entry for library upload PR',
      content: Buffer.from(updatedContent).toString('base64'),
      sha: existingAudit.sha,
      branch: branchName
    });
  } catch (error) {
    // Create new audit log if it doesn't exist
    await octokit.repos.createOrUpdateFileContents({
      owner,
      repo,
      path: pasturePath,
      message: 'Create audit log for library upload PR',
      content: Buffer.from(`# Audit Log\n${auditEntry}`).toString('base64'),
      branch: branchName
    });
  }

  console.log('✅ Audit entry added');
}

main().catch(console.error);