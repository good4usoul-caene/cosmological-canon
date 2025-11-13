#!/usr/bin/env python3
"""
tools/riddles_chapter_sentence_parser.py

Usage:
  python tools/riddles_chapter_sentence_parser.py --file library/books/ascii-riddles-of-barabbas.txt

Outputs (non-destructive):
  .build/riddles_structure.json
  .build/riddles_structure.csv
  tent/riddles/<chapter-slug>.md  (one stub file per detected chapter)

Notes:
- Heuristics are conservative. Please review .build/riddles_structure.json and the generated chapter stubs.
- If you prefer different chapter-heading rules, edit CHAPTER_HEADING_RE below.
"""
import re
import os
import csv
import json
import argparse
from pathlib import Path
from datetime import datetime
from textwrap import shorten

# Configurable regexes / thresholds
CHAPTER_HEADING_RE = re.compile(r'^\s*(?:Chapter|CHAPTER|chapter|\d+\.)\s*(\d+)?\b.*', re.IGNORECASE)
TABLE_LINE_RE = re.compile(r'\|')  # simple detection: pipe characters typical of ascii tables
TABLE_SPACED_COLS_RE = re.compile(r'\s{2,}')  # multiple spaces may indicate column layout
POEM_LINE_MAX_LEN = 80  # poem lines are usually short-ish
POEM_LINE_COUNT_THRESHOLD = 3  # need at least this many short lines in a block to consider 'poem'
SENTENCE_SPLIT_RE = re.compile(r'(?<=\S[.!?])\s+(?=[A-Z0-9""\'\(\[]+)')  # crude sentence splitter

# I/O paths
OUT_DIR = Path('.build')
TENT_DIR = Path('tent/riddles')

def ensure_dirs():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TENT_DIR.mkdir(parents=True, exist_ok=True)

def read_file(path):
    with open(path, 'r', encoding='utf8', errors='replace') as f:
        return f.read().splitlines()

def find_chapter_boundaries(lines):
    """Return a list of (start_idx, heading_line) for each detected chapter."""
    boundaries = []
    for i, line in enumerate(lines):
        if CHAPTER_HEADING_RE.match(line):
            boundaries.append((i, line.strip()))
    if not boundaries:
        # fallback: treat entire file as single chapter
        boundaries = [(0, 'Chapter 1')]
    return boundaries

def slice_chapters(lines, boundaries):
    chapters = []
    for idx, (start, heading) in enumerate(boundaries):
        end = boundaries[idx+1][0] if idx+1 < len(boundaries) else len(lines)
        chunk_lines = lines[start:end]
        chapters.append({'heading': heading, 'start_line': start+1, 'end_line': end, 'lines': chunk_lines})
    return chapters

def detect_table_block(block_lines):
    """Return True if block looks like a table (pipes or fixed-column spacing)."""
    pipe_count = sum(1 for l in block_lines if TABLE_LINE_RE.search(l))
    spaced_cols_count = sum(1 for l in block_lines if TABLE_SPACED_COLS_RE.search(l))
    # if many lines contain pipes or repeated spacing, consider a table
    return pipe_count >= 1 or spaced_cols_count >= max(1, len(block_lines)//4)

def chunk_blocks(lines):
    """
    Split chapter lines into contiguous blocks separated by blank lines.
    Return list of {'start', 'end', 'lines', 'type_guess'}.
    """
    blocks = []
    buf = []
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '':
            if buf:
                blocks.append({'start': start_idx, 'end': i, 'lines': buf})
                buf = []
                start_idx = None
        else:
            if start_idx is None:
                start_idx = i
            buf.append(line.rstrip())
    if buf:
        blocks.append({'start': start_idx, 'end': len(lines), 'lines': buf})
    return blocks

def guess_block_type(block):
    lines = block['lines']
    # Table detection
    if detect_table_block(lines):
        return 'table'
    # Poem detection: many short lines (line length < threshold)
    short_lines = [l for l in lines if len(l.strip()) > 0 and len(l) <= POEM_LINE_MAX_LEN]
    # Heuristic: if block has multiple short lines and multiple line breaks -> poem
    if len(lines) >= POEM_LINE_COUNT_THRESHOLD and len(short_lines) >= POEM_LINE_COUNT_THRESHOLD:
        # additional check: many lines end without period (common in verse)
        ends_with_period = sum(1 for l in lines if l.strip().endswith('.'))
        if ends_with_period < max(1, len(lines)//3):
            return 'poem'
    # Otherwise prose
    return 'prose'

def split_sentences(text):
    # Use the crude regex to split into sentences; fallback to whole text if no split
    parts = [p.strip() for p in SENTENCE_SPLIT_RE.split(text) if p.strip()]
    if not parts:
        return [text.strip()]
    return parts

def sanitize_slug(s):
    s2 = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    return s2[:80]

def process_chapters(chapters, source_path):
    out = []
    for ch_idx, ch in enumerate(chapters, start=1):
        heading = ch['heading']
        slug = sanitize_slug(heading or f'chapter-{ch_idx}')
        chapter_id = f'ch{ch_idx:02d}-{slug}'
        blocks = chunk_blocks(ch['lines'])
        processed_blocks = []
        for b_idx, b in enumerate(blocks, start=1):
            btype = guess_block_type(b)
            text = '\n'.join(b['lines']).strip()
            sentences = []
            if btype == 'poem':
                # treat each line as a unit, but also produce sentence-like units
                for ln in b['lines']:
                    ln = ln.strip()
                    if ln:
                        sentences.append(ln)
            elif btype == 'table':
                # keep as single block; try to split cell-like lines
                sentences = [ln.strip() for ln in b['lines'] if ln.strip()]
            else:
                # prose: join and sentence-split
                joined = ' '.join(l.strip() for l in b['lines'])
                sentences = split_sentences(joined)
            processed_blocks.append({
                'block_index': b_idx,
                'type': btype,
                'start_line': ch['start_line'] + b['start'],
                'end_line': ch['start_line'] + b['end'] - 1,
                'text_excerpt': shorten(text, width=240),
                'full_text': text,
                'sentences': sentences
            })
        out.append({
            'chapter_index': ch_idx,
            'chapter_id': chapter_id,
            'heading': heading,
            'start_line': ch['start_line'],
            'end_line': ch['end_line'],
            'blocks': processed_blocks,
            'source': source_path
        })
    return out

def write_outputs(structure):
    ts = datetime.utcnow().isoformat() + 'Z'
    json_path = OUT_DIR / 'riddles_structure.json'
    with open(json_path, 'w', encoding='utf8') as jf:
        json.dump({'created_at': ts, 'chapters': structure}, jf, ensure_ascii=False, indent=2)
    # CSV: row per block
    csv_path = OUT_DIR / 'riddles_structure.csv'
    with open(csv_path, 'w', encoding='utf8', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(['chapter_index','chapter_id','heading','block_index','type','start_line','end_line','excerpt','sentence_count'])
        for ch in structure:
            for b in ch['blocks']:
                writer.writerow([ch['chapter_index'], ch['chapter_id'], ch['heading'], b['block_index'], b['type'], b['start_line'], b['end_line'], b['text_excerpt'], len(b['sentences'])])
    # Create per-chapter markdown stubs
    for ch in structure:
        fname = TENT_DIR / f"{ch['chapter_id']}.md"
        with open(fname, 'w', encoding='utf8') as mf:
            mf.write('---\n')
            mf.write(f"title: \"{ch['heading']}\"\n")
            mf.write(f"source_file: {ch['source']}\n")
            mf.write(f"chapter_index: {ch['chapter_index']}\n")
            mf.write(f"start_line: {ch['start_line']}\n")
            mf.write(f"end_line: {ch['end_line']}\n")
            mf.write("status: draft\n")
            mf.write("contains_markup: unknown\n")
            mf.write("---\n\n")
            mf.write("# Exact text excerpt (paste canonical excerpt below)\n\n")
            mf.write("\n\n")
    print("WROTE:", json_path, csv_path, "chapter stubs under", TENT_DIR)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True, help='Path to ascii file (e.g., library/books/ascii-riddles-of-barabbas.txt)')
    args = parser.parse_args()
    src = Path(args.file)
    if not src.exists():
        print("ERROR: file not found:", src)
        return
    ensure_dirs()
    lines = read_file(src)
    boundaries = find_chapter_boundaries(lines)
    chapters = slice_chapters(lines, boundaries)
    structure = process_chapters(chapters, str(src))
    write_outputs(structure)
    print("Done. Please review .build/riddles_structure.json and the files under tent/riddles/")

if __name__ == '__main__':
    main()