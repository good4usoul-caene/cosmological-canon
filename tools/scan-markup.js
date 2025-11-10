#!/usr/bin/env node
/**
 * tools/scan-markup.js
 *
 * Usage:
 *   node tools/scan-markup.js --dir library/books --out .build/markup_scan_results.csv
 *
 * Scans markdown/html/txt/docx files under a directory and writes a CSV with columns:
 * file, paragraph_index, match_text, format, gospel, excerpt
 *
 * Dependencies: markdown-it, jsdom, mammoth, glob, csv-writer, yargs
 */
const fs = require('fs');
const path = require('path');
const glob = require('glob');
const MarkdownIt = require('markdown-it');
const { JSDOM } = require('jsdom');
const mammoth = require('mammoth');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');

const argv = yargs(hideBin(process.argv))
  .option('dir', { type: 'string', demandOption: true })
  .option('out', { type: 'string', default: '.build/markup_scan_results.csv' })
  .argv;

const md = new MarkdownIt({ html: true, linkify: true });

function ensureDir(p) {
  const d = path.dirname(p);
  if (!fs.existsSync(d)) fs.mkdirSync(d, { recursive: true });
}

function findMatchesInDom(dom, file) {
  const doc = dom.window.document;
  const results = [];

  // bold -> <strong> or <b> => Matthew
  doc.querySelectorAll('strong, b').forEach((el, idx) => {
    results.push({
      file,
      para_index: idx + 1,
      match_text: el.textContent.trim(),
      format: 'bold',
      gospel: 'Matthew',
      excerpt: el.parentElement ? el.parentElement.textContent.trim().slice(0, 300) : el.textContent.trim().slice(0, 300)
    });
  });

  // italics -> <em>i> => Luke
  doc.querySelectorAll('em, i').forEach((el, idx) => {
    results.push({
      file,
      para_index: idx + 1,
      match_text: el.textContent.trim(),
      format: 'italics',
      gospel: 'Luke',
      excerpt: el.parentElement ? el.parentElement.textContent.trim().slice(0, 300) : el.textContent.trim().slice(0, 300)
    });
  });

  // underline -> <u> or <ins> => Mark
  doc.querySelectorAll('u, ins').forEach((el, idx) => {
    results.push({
      file,
      para_index: idx + 1,
      match_text: el.textContent.trim(),
      format: 'underline',
      gospel: 'Mark',
      excerpt: el.parentElement ? el.parentElement.textContent.trim().slice(0, 300) : el.textContent.trim().slice(0, 300)
    });
  });

  // red -> <span style="color:red"> or <font color="red"> or inline style => John
  doc.querySelectorAll('span, font, *').forEach((el) => {
    const style = el.getAttribute && (el.getAttribute('style') || el.getAttribute('color') || '');
    if (style && /red/i.test(style)) {
      results.push({
        file,
        para_index: 0,
        match_text: el.textContent.trim(),
        format: 'red',
        gospel: 'John',
        excerpt: el.parentElement ? el.parentElement.textContent.trim().slice(0, 300) : el.textContent.trim().slice(0, 300)
      });
    }
  });

  return results;
}

async function processDocx(file) {
  try {
    const buffer = fs.readFileSync(file);
    const res = await mammoth.convertToHtml({ buffer });
    const html = res.value;
    const dom = new JSDOM(html);
    return findMatchesInDom(dom, file);
  } catch (e) {
    console.error('docx read error', file, e.message);
    return [];
  }
}

function processHtmlLike(text, file) {
  const dom = new JSDOM(text);
  return findMatchesInDom(dom, file);
}

async function scan() {
  const pattern = path.join(argv.dir, '**/*.{md,markdown,html,htm,txt,docx}');
  const files = glob.sync(pattern, { nodir: true, dot: true });
  const out = [];
  for (const file of files) {
    const ext = path.extname(file).toLowerCase();
    try {
      if (ext === '.docx') {
        const matches = await processDocx(file);
        out.push(...matches);
      } else {
        const content = fs.readFileSync(file, 'utf8');
        let html = content;
        if (ext === '.md' || ext === '.markdown' || ext === '.txt') {
          html = md.render(content);
        }
        const matches = processHtmlLike(html, file);
        out.push(...matches);
      }
    } catch (e) {
      console.error('skip', file, e.message);
    }
  }

  ensureDir(argv.out);
  const csvWriter = createCsvWriter({
    path: argv.out,
    header: [
      { id: 'file', title: 'file' },
      { id: 'para_index', title: 'paragraph_index' },
      { id: 'match_text', title: 'match_text' },
      { id: 'format', title: 'format' },
      { id: 'gospel', title: 'gospel' },
      { id: 'excerpt', title: 'excerpt' },
    ]
  });
  await csvWriter.writeRecords(out);
  console.log('Scan complete. Results written to', argv.out);
}

scan().catch(e => {
  console.error(e);
  process.exit(1);
});
