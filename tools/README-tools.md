# Tools — scan-markup & chunker

Purpose
- Non-destructive tooling to help extract typographic gospel-markup and to chunk long books by chapter headings.

Installation
1. Place the `tools/` files in the repo.
2. From repo root:
   ```
   npm install
   ```

Scan markup (detect bold/underline/italics/red)
- Example:
  ```
  npm run scan-markup
  # or (more explicit)
  node tools/scan-markup.js --dir library/books --out .build/markup_scan_results.csv
  ```
- Output: .build/markup_scan_results.csv
- Notes:
  - .md/.markdown/.txt -> converted to HTML via markdown-it; then parsed to find <strong>/<em>/<u>/<ins>/<span style="color:red"> and <font color="red">.
  - .docx files are converted to HTML via mammoth and then parsed.
  - Output CSV columns: file, paragraph_index, match_text, format, gospel, excerpt

Chunk a book into chapters
- Example:
  ```
  npm run chunk-queen
  # or
  node tools/chunker.js --file library/books/queen-of-the-south.md --out .build/queen
  ```
- Output: .build/queen/*.md and .build/queen/index.json
- Heuristics: lines starting with "Chapter" or markdown headings.

Safety and non-destructive policy
- These tools do not modify repository source files. They create outputs under .build/ or .build/markup_scan_results.csv.
- If you want different output locations, pass --out.

Notes for JS Code copilot
- You can refine heading regex, or adjust format-to-gospel mapping as needed.
- If many .docx files are present and mammoth is slow, consider converting docx to md/docx-to-md separately and then scanning.
