#!/usr/bin/env node
/**
 * tools/chunker.js
 *
 * Usage:
 *   node tools/chunker.js --file library/books/queen-of-the-south.md --out .build/queen
 *
 * Splits a Markdown/text file into chapter files based on heading patterns.
 * Non-destructive: writes outputs under the provided --out directory.
 *
 * Heuristic chapter heading patterns:
 *  - Lines starting with "Chapter" (case-insensitive), e.g., "Chapter 1", "CHAPTER I"
 *  - Markdown headings: "# Chapter 1", "## Chapter 2"
 */
const fs = require('fs');
const path = require('path');
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');

const argv = yargs(hideBin(process.argv))
  .option('file', { type: 'string', demandOption: true })
  .option('out', { type: 'string', default: '.build/chapters' })
  .argv;

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

function splitByHeadings(text) {
  const lines = text.split(/\r?\n/);
  const chapters = [];
  let current = { title: 'frontmatter', lines: [] };
  const headingRe = /^\s*(?:#\s*)?(Chapter|CHAPTER|chapter)\b.*$/i;
  for (const line of lines) {
    if (headingRe.test(line) || /^#{1,3}\s*chapter\b/i.test(line)) {
      // start new chapter block
      chapters.push(current);
      current = { title: line.trim(), lines: [] };
    } else {
      current.lines.push(line);
    }
  }
  chapters.push(current);
  // drop initial empty frontmatter if empty
  return chapters.filter(ch => ch.lines.join('').trim() !== '');
}

function sanitizeFileName(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function main() {
  const input = argv.file;
  const outdir = argv.out;
  ensureDir(outdir);
  const text = fs.readFileSync(input, 'utf8');
  const chapters = splitByHeadings(text);
  const index = [];
  chapters.forEach((ch, i) => {
    const title = ch.title || `chapter-${i+1}`;
    const fname = `${sanitizeFileName(path.basename(input, path.extname(input)))}-ch${String(i+1).padStart(2,'0')}.md`;
    const fpath = path.join(outdir, fname);
    const full = (title ? `# ${title}\n\n` : '') + ch.lines.join('\n');
    fs.writeFileSync(fpath, full, 'utf8');
    index.push({ file: fpath, chapter: title, chapter_index: i+1 });
  });
  const indexPath = path.join(outdir, 'index.json');
  fs.writeFileSync(indexPath, JSON.stringify(index, null, 2), 'utf8');
  console.log('Chunking complete. Chapters written to', outdir, 'index at', indexPath);
}

main();
