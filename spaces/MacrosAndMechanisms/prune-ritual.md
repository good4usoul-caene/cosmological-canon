# Prune Ritual — Closing a Branch Ritual

Technical title
- Prune Ritual (branch cleanup and archival)

Dual‑language headline
- Technical: pruning — safely remove stale branch refs and archive history  
- Mythic: pruning — a closing rite that honors completed enactments and clears space for new growth

When to prune
- After a branch has been successfully merged and is no longer needed.
- When a branch is intentionally abandoned and you’ve recorded why (tag/archive).
- Never prune without ensuring provenance is preserved (tags, backups, or a clear commit message).

Safe workflow
1. Tag the branch to preserve the tip:
   git checkout branch-name
   git tag archive/branch-name-YYYYMMDD
   git push origin --tags

2. Delete remote branch:
   git push origin --delete branch-name

3. Delete local branch:
   git branch -d branch-name
   # use -D only when you intentionally force-delete

4. Recovery (if accidental):
   git reflog                # find commit SHA
   git checkout -b branch-name <commit-sha>
   git push --set-upstream origin branch-name

Etiquette & metadata
- Add a short note where the branch was closed (PR comment or issue) recording:
  - Why it was pruned
  - Any archived tag name and SHA
  - Who performed the prune and when

Windows / case-sensitivity note
- When cleanup involves files that differ only by case, prefer archiving and restoring on a case‑sensitive environment or use a temp rename workflow to avoid filesystem conflicts.

Ritual posture
- Pruning is not erasure; it is respectful closure. Archive before deletion, document intent, and preserve provenance so future seekers can trace the lineage of ideas.