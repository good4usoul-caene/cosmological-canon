#!/usr/bin/env python3
"""
Enhanced tools/riddles_chapter_sentence_parser.py

Handles the special dual structure of Chapter 1:
- Chapter 1A (Rewritten): Systematic verse-by-verse methodology 
- Chapter 1B (Original): Earlier "loosey goosey" approach

Usage:
  python tools/riddles_enhanced_parser.py --file library/books/ascii-riddles-of-barabbas.txt

Outputs (non-destructive):
  .build/riddles_enhanced_structure.json
  .build/riddles_enhanced_structure.csv
  tent/riddles/<chapter-slug>.md  (one stub file per detected chapter/version)

Special handling:
- Detects "Tab N" chapter markers
- Identifies Chapter 1 split at "YouTube Read-Along: Chapter 1" marker
- Preserves biblical verse references with enhanced detection
- Categorizes content by methodology phase (early/systematic/rewritten)
"""
print("Hello, world! This is the top of the file!")

import re
import os
import csv
import json
import argparse
from pathlib import Path
from datetime import datetime
from textwrap import shorten
from typing import List, Dict, Tuple, Optional


# Enhanced regexes for Riddles of Barabbas structure
CHAPTER_BREAK_RE = re.compile(r'§§CHAPTER_BREAK§§', re.IGNORECASE)
VERSE_REFERENCE_RE = re.compile(r'\(?\b(?:John|Matt|Matthew|Mark|Luke|Genesis)\s+\d+:\d+(?:-\d+)?\)?|\b\d+\s*[-–—]\s*')
REWRITE_INDICATOR_RE = re.compile(r'I have now made two efforts|latter effort above|former effort below', re.IGNORECASE)

# Content analysis patterns
TABLE_LINE_RE = re.compile(r'\|')
POEM_LINE_MAX_LEN = 80
POEM_LINE_COUNT_THRESHOLD = 3
SENTENCE_SPLIT_RE = re.compile(r'(?<=\S[.!?])\s+(?=[A-Z0-9""\'\(\[]+)')

# Enhanced I/O paths
OUT_DIR = Path('.build')
TENT_DIR = Path('tent/riddles')

def ensure_dirs():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TENT_DIR.mkdir(parents=True, exist_ok=True)

def read_file(path):
    """Read file and split into lines."""
    with open(path, 'r', encoding='utf8', errors='replace') as f:
        content = f.read()
    return content.splitlines()

def find_chapter_boundaries(lines):
    """
    Find chapter boundaries using '§§CHAPTER_BREAK§§' and extract chapter titles.
    Returns list of (start_idx, chapter_info) tuples.
    """
    boundaries = []
    i = 0
    chapter_header_re = re.compile(r'Chapter\s+(\d+)(?:\s*-\s*(.+))?', re.IGNORECASE)
    while i < len(lines):
        if CHAPTER_BREAK_RE.search(lines[i]):
            # Find next non-empty line for chapter header
            header = None
            j = i + 1
            while j < len(lines):
                if lines[j].strip():
                    header = lines[j].strip()
                    break
                j += 1
            chapter_num = None
            version = None
            chapter_title = None
            type_ = 'unknown'
            if header:
                match = chapter_header_re.match(header)
                if match:
                    chapter_num = int(match.group(1))
                    chapter_title = match.group(2) if match.group(2) else None
                    # Optional: detect version (A/B) if present after number
                    version_match = re.match(r'Chapter\s+(\d+)([A-Z])', header)
                    version = version_match.group(2) if version_match else None
                    if chapter_num == 1 and version:
                        type_ = 'rewritten' if version == 'A' else 'early'
                    elif chapter_num >= 10:
                        type_ = 'systematic'
                    else:
                        type_ = 'early'
            chapter_info = {
                'number': chapter_num if chapter_num else len(boundaries) + 1,
                'type': type_,
                'version': version,
                'title': header or f'Chapter {len(boundaries) + 1}',
                'chapter_title': chapter_title
            }
            boundaries.append((i, chapter_info))
        i += 1
    if not boundaries:
        # Fallback: treat entire file as single chapter
        chapter_info = {
            'number': 1,
            'type': 'unknown',
            'version': None,
            'title': 'Chapter 1'
        }
        boundaries = [(0, chapter_info)]
    return boundaries

def analyze_verse_references(text_block: str) -> Dict:
    """
    Analyze biblical verse references in a text block.
    Returns counts and examples of verse references found.
    """
    verse_matches = VERSE_REFERENCE_RE.findall(text_block)
    
    # Categorize verse references
    biblical_refs = []
    numeric_refs = []
    
    for match in verse_matches:
        if re.search(r'(?:John|Matt|Matthew|Mark|Luke|Genesis)', match, re.IGNORECASE):
            biblical_refs.append(match.strip())
        elif re.search(r'^\d+\s*[-–—]', match):
            numeric_refs.append(match.strip())
    
    return {
        'total_verses': len(verse_matches),
        'biblical_references': len(biblical_refs),
        'numeric_references': len(numeric_refs),
        'biblical_examples': biblical_refs[:5],  # First 5 examples
        'numeric_examples': numeric_refs[:5],
        'verse_density': len(verse_matches) / max(len(text_block.split()), 1) * 100
    }

def split_sentences(text):
    """Split text into sentences using the original parser's logic."""
    parts = [p.strip() for p in SENTENCE_SPLIT_RE.split(text) if p.strip()]
    if not parts:
        return [text.strip()]
    return parts

def count_syllables(word):
    """Rough syllable count for English words."""
    word = word.lower().strip(".,!?;:")
    if not word:
        return 0
    
    # Basic syllable counting heuristics
    vowels = "aeiouy"
    syllables = 0
    prev_was_vowel = False
    
    for i, char in enumerate(word):
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            syllables += 1
        prev_was_vowel = is_vowel
    
    # Handle silent 'e'
    if word.endswith('e') and syllables > 1:
        syllables -= 1
    
    # Ensure at least one syllable
    return max(1, syllables)

def detect_stress_pattern(words):
    """Detect stress patterns in a line of poetry - simplified iambic detection."""
    # Common unstressed words (function words)
    function_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'of', 'for', 
                     'with', 'by', 'from', 'up', 'out', 'off', 'down', 'over', 'under', 'through',
                     'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'will', 'would',
                     'he', 'she', 'it', 'they', 'his', 'her', 'its', 'their', 'some', 'all', 'not',
                     'could', 'should', 'can', 'may', 'might', 'must', 'shall', 'do', 'does', 'did'}
    
    stress_pattern = []
    for word in words:
        clean_word = word.lower().strip(".,!?;:")
        if clean_word in function_words:
            stress_pattern.append('u')  # unstressed
        else:
            stress_pattern.append('/')  # stressed
    
    return stress_pattern

def count_stressed_syllables(words):
    """Count only the stressed syllables in a line of words."""
    stress_pattern = detect_stress_pattern(words)
    stressed_count = 0
    
    for i, word in enumerate(words):
        if i < len(stress_pattern) and stress_pattern[i] == '/':
            # This is a stressed word, count its syllables
            stressed_count += count_syllables(word)
    
    return stressed_count

def analyze_meter(line):
    """Analyze the metrical pattern of a line."""
    words = line.split()
    if not words:
        return {'syllables': 0, 'stressed_syllables': 0, 'stress_pattern': [], 'meter_type': 'unknown'}
    
    syllable_count = sum(count_syllables(word) for word in words)
    stressed_syllables = count_stressed_syllables(words)
    stress_pattern = detect_stress_pattern(words)
    
    # Simple iambic detection (roughly alternating unstressed/stressed)
    stressed_positions = [i for i, stress in enumerate(stress_pattern) if stress == '/']
    
    meter_type = 'mixed'
    if len(stressed_positions) >= 2:
        # Check if stressed syllables roughly alternate
        avg_gap = len(words) / len(stressed_positions) if stressed_positions else 0
        if 1.5 <= avg_gap <= 2.5:  # Roughly every other word
            meter_type = 'iambic-like'
    
    return {
        'syllables': syllable_count,
        'stressed_syllables': stressed_syllables,
        'stress_pattern': stress_pattern,
        'meter_type': meter_type,
        'feet': stressed_syllables  # Use stressed syllables for feet count
    }

def get_rhyme_key(word):
    """Extract rhyming sound from word ending with improved phonetic matching."""
    word = word.lower().strip(".,!?;:")
    if len(word) < 2:
        return word
    
    # Improved rhyme detection - handle common English rhyme patterns
    # Look for common endings and normalize them
    
    # Handle common rhyming patterns
    rhyme_patterns = {
        # -ard sound (guards, yard, card)
        'guards': 'ard', 'yard': 'ard', 'card': 'ard', 'hard': 'ard',
        # -ame sound (name, tame, same, claim, domain)  
        'name': 'ame', 'tame': 'ame', 'same': 'ame', 'frame': 'ame',
        'claim': 'ame', 'domain': 'ame', 'main': 'ame',
        # -iss sound (amiss, piss, this, miss)
        'amiss': 'iss', 'piss': 'iss', 'this': 'iss', 'miss': 'iss',
        # -ock sound (flock, stock, rock)
        'flock': 'ock', 'stock': 'ock', 'rock': 'ock', 'clock': 'ock',
        # -ate sound (gate, state, late)
        'gate': 'ate', 'state': 'ate', 'late': 'ate', 'fate': 'ate',
        # -tion sound (prevention, invention, mention)
        'prevention': 'tion', 'invention': 'tion', 'mention': 'tion',
        # -eep sound (sheep, keep, deep)
        'sheep': 'eep', 'keep': 'eep', 'deep': 'eep', 'sleep': 'eep',
        # -eer sound (near, frontier, fear)
        'near': 'eer', 'frontier': 'eer', 'fear': 'eer', 'here': 'eer'
    }
    
    if word in rhyme_patterns:
        return rhyme_patterns[word]
    
    # Fallback to suffix-based detection for unlisted words
    if word.endswith('tion'):
        return 'tion'
    elif word.endswith('ment'):
        return 'ment'
    elif word.endswith('ness'):
        return 'ness'
    elif word.endswith('ing'):
        return 'ing'
    elif word.endswith('ed'):
        return 'ed'
    elif word.endswith('ard') or word.endswith('ards'):
        return 'ard'
    elif word.endswith('ame') or word.endswith('aim') or word.endswith('ain'):
        return 'ame'
    elif word.endswith('iss'):
        return 'iss'
    elif word.endswith('ock'):
        return 'ock'
    elif word.endswith('ate'):
        return 'ate'
    elif word.endswith('eep'):
        return 'eep'
    elif word.endswith('eer') or word.endswith('ear'):
        return 'eer'
    elif len(word) >= 3:
        return word[-3:]
    
    return word[-2:]

def detect_poetic_lines(verse_text):
    """Detect poetic line breaks based on STRESSED syllable count and rhyme patterns."""
    words = verse_text.split()
    if not words:
        return [verse_text]

    # Target: break lines at every 4 stressed syllables
    target_stressed = 4

    lines = []
    current_words = []
    current_stressed = 0

    for word in words:
        word_stressed = count_stressed_syllables([word])
        current_words.append(word)
        current_stressed += word_stressed

        if current_stressed >= target_stressed:
            lines.append(' '.join(current_words))
            current_words = []
            current_stressed = 0

    # Add any remaining words as the last line
    if current_words:
        lines.append(' '.join(current_words))

    return lines if lines else [verse_text]

def format_chapter_content(content, content_type='prose'):
    """Format chapter content with proper line breaks using poetic analysis."""
    if not content or not content.strip():
        return content
    
    # Always try verse formatting first since this theological text uses numbered verses
    verse_pattern = re.compile(r'(\d+)\s+([^0-9]+?)(?=\s+\d+\s+[A-Z]|\s+\d+\s+[a-z]|$)')
    verses = verse_pattern.findall(content)
    
    if verses and len(verses) > 3:  # If we found multiple verses, format as verse
        formatted_lines = []
        
        for verse_num, verse_text in verses:
            verse_text = verse_text.strip()
            
            # Use poetic line detection
            poetic_lines = detect_poetic_lines(verse_text)
            
            if poetic_lines:
                verse_content = f"**{verse_num}.** {poetic_lines[0]}"
                for line in poetic_lines[1:]:
                    verse_content += f"\n{line}"
                formatted_lines.append(verse_content)
            else:
                # Fallback to simple formatting
                formatted_lines.append(f"**{verse_num}.** {verse_text}")
        
        return '\n\n'.join(formatted_lines)
    
    elif content_type == 'verse' or content_type == 'poem':
        sentences = split_sentences(content)
        if len(sentences) > 2:
            return '\n\n'.join(sentences)
    
    # For prose content, use sentence splitting with paragraph formation
    sentences = split_sentences(content)
    if len(sentences) > 1:
        paragraphs = []
        current_paragraph = []
        
        for sentence in sentences:
            current_paragraph.append(sentence)
            if len(current_paragraph) >= 2:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []
        
        if current_paragraph:
            paragraphs.append(' '.join(current_paragraph))
        
        return '\n\n'.join(paragraphs)
    
    return content

def categorize_content_type(lines: List[str]) -> str:
    """
    Categorize the content type of a chapter section.
    """
    total_lines = len([l for l in lines if l.strip()])
    if total_lines == 0:
        return 'empty'
    
    # Count different content types
    table_lines = sum(1 for line in lines if TABLE_LINE_RE.search(line))
    poem_lines = sum(1 for line in lines if len(line.strip()) < POEM_LINE_MAX_LEN and line.strip())
    prose_lines = total_lines - table_lines - poem_lines
    
    # Determine primary type
    if table_lines > total_lines * 0.3:
        return 'table'
    elif poem_lines > total_lines * 0.6:
        return 'verse'
    elif prose_lines > total_lines * 0.7:
        return 'prose'
    else:
        return 'mixed'

def slice_chapters(lines, boundaries):
    """
    Slice text into chapter sections based on boundaries.
    """
    chapters = []
    
    # Handle single-line format
    if len(lines) == 1:
        content = lines[0]
        
        # Sort boundaries by position
        sorted_boundaries = sorted(boundaries, key=lambda x: x[1].get('position', 0))
        
        for idx, (start, chapter_info) in enumerate(sorted_boundaries):
            # Calculate content boundaries
            chapter_start = chapter_info.get('position', 0)
            if idx + 1 < len(sorted_boundaries):
                chapter_end = sorted_boundaries[idx + 1][1].get('position', len(content))
            else:
                chapter_end = len(content)
            
            # Extract chapter content
            chapter_content = content[chapter_start:chapter_end]
            chapter_lines = [chapter_content]  # Single line containing chapter
            
            # Analyze content
            verse_analysis = analyze_verse_references(chapter_content)
            content_type = categorize_content_type(chapter_lines)
            
            # Enhanced chapter data
            chapter_data = {
                'info': chapter_info,
                'lines': chapter_lines,
                'start_line': 0,  # All from line 0 in single-line format
                'end_line': 1,
                'line_count': 1,
                'content_type': content_type,
                'verse_analysis': verse_analysis,
                'methodology_phase': chapter_info['type'],
                'has_systematic_verses': verse_analysis['biblical_references'] > 5,
                'preview': shorten(chapter_content, 200),
                'char_count': len(chapter_content),
                'char_start': chapter_start,
                'char_end': chapter_end
            }
            
            chapters.append(chapter_data)
    else:
        # Original multi-line logic
        for idx, (start, chapter_info) in enumerate(boundaries):
            end = boundaries[idx+1][0] if idx+1 < len(boundaries) else len(lines)
            chapter_lines = lines[start:end]
            
            # Analyze content
            full_text = '\n'.join(chapter_lines)
            # Normalize EOLs and scan up to 5 lines after chapter break for metadata
            title = ''
            youtube = ''
            location = ''
            # Scan first 5 lines for metadata fields
            for i in range(min(5, len(chapter_lines))):
                line = chapter_lines[i].replace('\r','').replace('\n','').strip()
                if i == 0:
                    # First line: likely chapter title
                    title = line.replace('§§CHAPTER_BREAK§§','').strip()
                if line.lower().startswith('youtube readalong:'):
                    youtube = line.split(':',1)[-1].strip()
                if line.lower().startswith('location:'):
                    location = line.split(':',1)[-1].strip()
            # Update chapter_info
            chapter_info = dict(chapter_info)  # copy to avoid mutating original
            if title:
                chapter_info['chapter_title'] = title
            if youtube:
                chapter_info['youtube'] = youtube
            if location:
                chapter_info['location'] = location
            verse_analysis = analyze_verse_references(full_text)
            content_type = categorize_content_type(chapter_lines)
            # Enhanced chapter data
            chapter_data = {
                'info': chapter_info,
                'lines': chapter_lines,
                'start_line': start,
                'end_line': end,
                'line_count': len(chapter_lines),
                'content_type': content_type,
                'verse_analysis': verse_analysis,
                'methodology_phase': chapter_info['type'],
                'has_systematic_verses': verse_analysis['biblical_references'] > 5,
                'preview': shorten(' '.join(chapter_lines[:5]), 200)
            }
            chapters.append(chapter_data)
    
    return chapters

def generate_chapter_slug(chapter_data):
    """Generate a filename-safe slug for the chapter."""
    info = chapter_data['info']
    # Use chapter number and normalized title for filename
    num = f"{info['number']:02d}"
    # Remove non-alphanumeric characters and collapse spaces for title
    title = info.get('chapter_title') or info.get('title') or ''
    title_slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.strip()).strip('-').lower()
    return f"{num}-{title_slug}"

def write_chapter_stubs(chapters):
    print(f"[DIAGNOSTIC] Generating file: chapter_number={chapter_number}, chapter_title='{chapter_title}', filename='{filename}'")
    """
    Write chapter stub files to tent directory, with proper formatting.
    Output filename: <##>-<title-text>.md
    """
    for chapter_data in chapters:
        info = chapter_data['info']
        lines = chapter_data['lines']
        # We need to test whether this is giving a single line or multiple lines.
        print(f"[DIAGNOSTIC] Number of lines in chapter: {len(lines)}")
        # Where did this print to?  It's not in the console output. I executed python tools/riddles_enhanced_parser.py --file library/books/ascii-riddles-of-barabbas.txt --chapters 10 
        # Weirdly, the diagnostic print is not showing up in the console output. Maybe it's being suppressed somewhere?  Maybe I need to flush stdout?
        # Extract Youtube and Location from first 6 lines
        youtube = None
        location = None
        for line in lines[:6]:
            if line.lower().startswith('youtube readalong:'):
                youtube = line.strip().split(':', 1)[-1].strip()
            if line.lower().startswith('location:'):
                location = line.strip().split(':', 1)[-1].strip()
    # Compose header lines and filename, ignore version/type
    chapter_number = info.get('number', 'XX')
    chapter_title = info.get('chapter_title') or info.get('title') or ''
    # Normalize title for filename
    title_slug = re.sub(r'[^a-zA-Z0-9]+', '-', chapter_title.strip()).strip('-').lower()
    filename = f"{str(chapter_number).zfill(2)}-{title_slug}.md"
    print(f"[DIAGNOSTIC] Generating file: chapter_number={chapter_number}, chapter_title='{chapter_title}', filename='{filename}'")
    stub_path = TENT_DIR / filename
    header = f"Chapter {chapter_number}: {chapter_title}\n"
    youtube_line = f"Youtube Readalong: {youtube}\n" if youtube else ''
    location_line = f"Location: {location}\n" if location else ''
    # Write to file
    with open(stub_path, 'w', encoding='utf8') as f:
        f.write(header)
        if youtube_line:
            f.write(youtube_line)
        if location_line:
            f.write(location_line)
        f.write("\n")
        # Content Preview section
        f.write("## Content Preview\n\n")
        f.write(f"Chapter {chapter_number} - {chapter_title}\n")
        if youtube:
            f.write(f"Youtube Readalong: {youtube}\n")
        if location:
            f.write(f"Location: {location}\n")
        f.write("\n")
        # Full Chapter Content section
        f.write("## Full Chapter Content\n\n")
        for line in lines:
            f.write(line.rstrip() + '\n')
    print(f"✓ Generated: {stub_path}")
    def main():
        import argparse
        parser = argparse.ArgumentParser(description="Parse Riddles of Barabbas and output formatted chapters.")
        parser.add_argument('--file', required=True, help='Path to source text file')
        parser.add_argument('--output', default='tent/riddles', help='Output directory for chapter files')
        parser.add_argument('--chapters', nargs='*', type=int, help='Chapter numbers to extract (optional)')
        args = parser.parse_args()

        target_chapters = args.chapters if args.chapters else None

        print(f"📖 Parsing: {args.file}")
        if target_chapters:
            print(f"🎯 Focusing on chapters: {target_chapters}")

        ensure_dirs()

        # Read and parse file
        lines = read_file(args.file)
        print(f"📄 Read {len(lines)} lines")

        boundaries = find_chapter_boundaries(lines)
        chapters = slice_chapters(lines, boundaries)
        # Filter by target chapters if specified
        if target_chapters:
            chapters = [c for c in chapters if c['info']['number'] in target_chapters]
            print(f"🎯 Filtered to {len(chapters)} target chapters")

        # Report findings
        print("\n📊 Chapter Analysis:")
        for chapter_data in chapters:
            info = chapter_data['info']
            verse_count = chapter_data['verse_analysis']['total_verses']
            biblical_count = chapter_data['verse_analysis']['biblical_references']
            version_str = f" {info.get('version','')}" if info.get('version') else ""
            phase_str = f"[{info.get('type','')}]"
            print(f"  Chapter {info['number']}{version_str} {phase_str}: {chapter_data['line_count']} lines, "
                  f"{verse_count} verse refs ({biblical_count} biblical), {chapter_data['content_type']}")

        # Generate outputs
        write_chapter_stubs(chapters)
        print(f"\n✅ Enhanced parsing complete!")
        return 0
    print("Hello, world!..  Am I being executed?  Why?  What did I do?  Haha... I've escaped.  You'll never catch me.")
    if __name__ == "__main__":
        #Let's put a "hellow world" print here to see if this is being executed.
        print("Hello, world! If you're seeing this, the __name__ is '__main__'.")
        #Nothing printed. Why?
        main()