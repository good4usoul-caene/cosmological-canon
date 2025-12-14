#!/usr/bin/env python3
"""
Format Rommel chapter files for readability and add navigation links.

- Processes all .md files in library/books/rommel/chapters
- Skips files starting with 'Links-'
- Prepends a navigation block linking to ./Links-Book-List.md and the book-specific Links-Bible-XX-Book.md if present
- Creates backups with .bak extension containing original contents
- Splits paragraphs into sentences / clause-phrases (sentence-ending punctuation, semicolons, em-dash) and places each on its own line
- Preserves fenced code blocks, headings, lists, and other Markdown structures
- If a file has complex constructs making safe processing ambiguous, readability reformatting is skipped and a comment added
"""
import os
import re
from pathlib import Path

BASE_DIR = Path("library/books/rommel/chapters")

# load links map from Links-Book-List.md
LINKS_FILE = BASE_DIR / "Links-Book-List.md"
links_map = {}
if LINKS_FILE.exists():
    txt = LINKS_FILE.read_text(encoding="utf-8")
    # match lines like: [Genesis](Links-Bible-01-Genesis.md)
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', txt):
        name = m.group(1).strip()
        file = m.group(2).strip()
        links_map[name.lower()] = file  # case-insensitive matching
else:
    print(f"Warning: {LINKS_FILE} not found. Only Links-Book-List link will be added to files.")

# helper to split paragraph into sentences/phrases and preserve punctuation
SPLIT_PATTERN = re.compile(
    r'''(.*?                # non-greedy up to
        (?:                 # non-capturing group for end punctuation
            [.!?]           # sentence end punctuation
            (?:["')\]\]])?  # optional trailing quote/bracket (non-capturing group)
            |;              # or semicolon
            |—              # or em dash
        )
    )(?:\s+|$)              # followed by whitespace or end
    ''', re.VERBOSE | re.DOTALL)

def split_sentences(text):
    text = text.strip()
    if not text:
        return []
    parts = []
    for m in SPLIT_PATTERN.finditer(text):
        part = m.group(1)
        if part:
            parts.append(part.strip())
    # leftover if nothing matched (e.g., no punctuation)
    if not parts:
        return [text]
    # if pattern missed trailing text, capture it
    used = ''.join(parts)
    if len(used) < len(text):
        tail = text[len(used):].strip()
        if tail:
            parts.append(tail)
    return parts

def is_fenced_start(line):
    return bool(re.match(r'^(?:```|~~~)', line))

def is_heading(line):
    return bool(re.match(r'^\s{0,3}#{1,6}\s', line))

def is_fenced_or_indented_code_block(paragraph_lines):
    # if paragraph starts with fenced code or with 4-space indent or tab, treat as code
    first = paragraph_lines[0]
    if re.match(r'^(?: {4}|\t)', first):
        return True
    if is_fenced_start(first):
        return True
    return False

def process_paragraph(par_lines):
    """
    Process a paragraph (list of lines), return processed lines.
    Preserve list markers and blockquote markers.
    """
    joined = "\n".join(par_lines).rstrip()
    # If it's a heading only (single line), keep as-is
    if len(par_lines) == 1 and is_heading(par_lines[0]):
        return [par_lines[0]]
    # If fenced/indented code block, return as-is
    if is_fenced_or_indented_code_block(par_lines):
        return par_lines

    # Detect list item marker prefix (e.g., "- ", "* ", "1. ", "  - ")
    list_prefix_match = re.match(r'^(\s*(?:\d+\.\s+|[-+*]\s+|>\s+))', par_lines[0])
    prefix = ""
    if list_prefix_match:
        prefix = list_prefix_match.group(1)
        # remove the prefix from the first line for processing
        content = [re.sub(r'^\s*(?:\d+\.\s+|[-+*]\s+|>\s+)', '', par_lines[0])]
        # rest lines keep their indentation trimmed to continue sentence
        content += [l.lstrip() for l in par_lines[1:]]
        text = " ".join([l for l in content]).strip()
    else:
        text = " ".join([l.strip() for l in par_lines]).strip()

    # Split into sentences/phrases
    pieces = split_sentences(text)
    out_lines = []
    for i, piece in enumerate(pieces):
        if prefix:
            # only prefix the first line; subsequent lines align under content with same indentation
            if i == 0:
                out_lines.append(f"{prefix}{piece}")
            else:
                # compute indentation equal to prefix spaces (but without list char)
                indent = re.match(r'^(\s*)', prefix).group(1)
                out_lines.append(f"{indent}{piece}")
        else:
            out_lines.append(piece)
    return out_lines

def process_file(path: Path):
    text = path.read_text(encoding="utf-8")
    original = text
    # Create backup
    bak_path = path.with_suffix(path.suffix + ".bak")
    bak_path.write_text(original, encoding="utf-8")

    lines = text.splitlines()
    out_lines = []
    in_fence = False
    fence_delim = None

    # We'll build paragraphs outside fenced blocks.
    i = 0
    paragraphs = []
    cur_para = []
    # We'll track if we enter a fenced code block so we don't process until it ends.
    while i < len(lines):
        line = lines[i]
        if not in_fence and is_fenced_start(line):
            in_fence = True
            fence_delim = line.strip()[:3]
            # flush current paragraph
            if cur_para:
                paragraphs.append(("para", cur_para))
                cur_para = []
            # collect fence block
            fence_block = [line]
            i += 1
            while i < len(lines):
                fence_block.append(lines[i])
                if lines[i].strip().startswith(fence_delim):
                    break
                i += 1
            paragraphs.append(("fence", fence_block))
            i += 1
            continue

        if in_fence:
            # shouldn't be here because we handled fence above, but as safe fallback:
            out_lines.append(line)
            i += 1
            continue

        # blank lines separate paragraphs
        if line.strip() == "":
            if cur_para:
                paragraphs.append(("para", cur_para))
                cur_para = []
            paragraphs.append(("blank", [""]))
        else:
            cur_para.append(line)
        i += 1

    if cur_para:
        paragraphs.append(("para", cur_para))

    # Now process paragraphs
    for ptype, block in paragraphs:
        if ptype == "blank":
            out_lines.append("")
        elif ptype == "fence":
            out_lines.extend(block)
        elif ptype == "para":
            try:
                processed = process_paragraph(block)
                out_lines.extend(processed)
            except Exception as e:
                # On error, mark skip and return original plus skip comment
                comment = f"<!-- Readability reformatting skipped for {path.name} due to error: {e} -->"
                return False, comment + "\n" + original

    # Prepend navigation block
    # Determine book name from filename (text before first '-'), e.g., Genesis-1.md -> Genesis
    book_name = path.name.split('-', 1)[0]
    book_key = book_name.strip().lower()
    nav_lines = ["<!-- navigation start -->",
                 f"[Links-Book-List](./Links-Book-List.md)"]
    if book_key in links_map:
        nav_lines.append(f"[{book_name}]({os.path.join('./', links_map[book_key])})")
    else:
        nav_lines.append(f"<!-- Book-specific links file not found for {book_name} -->")
    nav_lines.append("<!-- navigation end -->")
    nav_block = "\n".join(nav_lines) + "\n\n"

    final_text = nav_block + "\n".join(out_lines).rstrip() + "\n"
    path.write_text(final_text, encoding="utf-8")
    return True, str(bak_path)

def main():
    if not BASE_DIR.exists():
        print(f"Error: directory {BASE_DIR} not found.")
        return
    md_files = []
    for p in BASE_DIR.glob("*.md"):
        name_upper = p.name.upper()
        # Exclude files starting with README or LINKS (case-insensitive)
        if name_upper.startswith("README") or name_upper.startswith("LINKS"):
            continue
        # Exclude if .bak file already exists
        bak_path = p.with_suffix(p.suffix + ".bak")
        if bak_path.exists():
            continue
        md_files.append(p)
    modified = []
    skipped = []
    for md in md_files:
        print(f"Processing: {md}")
        ok, info = process_file(md)
        if ok:
            modified.append((str(md), info))
            print(f"  Modified. Backup: {info}")
        else:
            skipped.append((str(md), info))
            # If skipped, still prepend navigation block but do not alter content - info contains comment+source
            # Write the file as-is with navigation block and the comment produced
            with md.open("r", encoding="utf-8") as f:
                original = f.read()
            nav_block = ("<!-- navigation start -->\n"
                         "[Links-Book-List](./Links-Book-List.md)\n"
                         f"<!-- Book-specific links file not found for {md.name.split('-',1)[0]} -->\n"
                         "<!-- navigation end -->\n\n")
            md.write_text(nav_block + info, encoding="utf-8")

    print("\nSummary:")
    print(f"  Files processed: {len(md_files)}")
    print(f"  Modified: {len(modified)}")
    print(f"  Skipped due to errors: {len(skipped)}")
    if modified:
        print("\nModified files and backups:")
        for m, bak in modified:
            print(f" - {m} (backup at {bak})")
    if skipped:
        print("\nSkipped files (info):")
        for s, info in skipped:
            print(f" - {s}: {info[:80]}...")

if __name__ == '__main__':
    main()