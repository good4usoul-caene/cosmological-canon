import os
import re
import urllib.parse

# Directory containing the .md files
CHAPTERS_DIR = os.path.join('library', 'books', 'rommel', 'chapters')
# Directory containing the backup .txt files
BACKUP_DIR = os.path.join(CHAPTERS_DIR, 'The-Most-Holy-Bible-text-files')

# Exclude patterns
EXCLUDE_PREFIXES = ('README', 'LINKS')
EXCLUDE_SUFFIXES = ('.md.bak',)

# Regex to find the navigation end block
NAV_END_RE = re.compile(r'<!-- navigation end -->', re.IGNORECASE)

def md_to_txt_filename(md_filename):
    base = os.path.splitext(md_filename)[0]
    txt_name = base.replace('-', ' ') + '.txt'
    return txt_name

def insert_backup_link(md_path, backup_rel_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find where to insert: after the <!-- navigation end --> block
    match = NAV_END_RE.search(content)
    if not match:
        print(f"No navigation end block found in {md_path}, skipping.")
        return False
    insert_pos = match.end()
    # Prepare the link line (encode spaces as %20)
    encoded_path = urllib.parse.quote(backup_rel_path)
    link_line = f"\n[Backup text file in The-Most-Holy-Bible-text-files]({encoded_path})\n"
    # Insert the link
    new_content = content[:insert_pos] + link_line + content[insert_pos:]
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Inserted backup link in {md_path}")
    return True

def main():
    for fname in os.listdir(CHAPTERS_DIR):
        if not fname.endswith('.md'):
            continue
        if any(fname.startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        if any(fname.endswith(s) for s in EXCLUDE_SUFFIXES):
            continue
        md_path = os.path.join(CHAPTERS_DIR, fname)
        txt_name = md_to_txt_filename(fname)
        backup_path = os.path.join(BACKUP_DIR, txt_name)
        if not os.path.exists(backup_path):
            print(f"Backup file missing for {fname}: {txt_name}")
            continue
        # Relative path for markdown link
        backup_rel_path = os.path.relpath(backup_path, CHAPTERS_DIR)
        insert_backup_link(md_path, backup_rel_path)

if __name__ == '__main__':
    main()
