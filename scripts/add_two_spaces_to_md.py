import os
import re

# Directory containing the markdown chapter files
CHAPTERS_DIR = os.path.join('library', 'books', 'rommel', 'chapters')

# Exclude files starting with these prefixes (case-insensitive)
EXCLUDE_PREFIXES = ('README', 'LINKS')

# Only process .md files

def add_two_spaces_to_lineends(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Guarantee exactly two spaces before every newline for non-blank lines
    new_lines = []
    for line in lines:
        if line.strip() == '':
            new_lines.append('\n')
        else:
            # Remove trailing whitespace, then add exactly two spaces before the newline
            new_lines.append(re.sub(r'[ \t]+$', '', line) + '  \n')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    for fname in os.listdir(CHAPTERS_DIR):
        if not fname.lower().endswith('.md'):
            continue
        if fname.upper().startswith(EXCLUDE_PREFIXES):
            continue
        fpath = os.path.join(CHAPTERS_DIR, fname)
        if os.path.isfile(fpath):
            add_two_spaces_to_lineends(fpath)
    print('Done: Two spaces added to all .md files in', CHAPTERS_DIR)

if __name__ == '__main__':
    main()
