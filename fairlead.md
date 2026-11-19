# Fairlead — U38 notes (9 Nov)

U38 builder (Opus). Scratch: C:/Users/stian/export-v3/. No identifier values in these notes.

- 02:1x Read brief (kai.md U38), secretary log 2026-11-04 l.5-8, l.62; 2026-11-07 l.83-110.
- Method: replayed `<commit>:max` trees (brief's alternative to subtree split) for the 34 first-parent
  commits 4730e63..2e8ebf9 onto 51c9bc1 with commit-tree in work/ (clone of D:/git/max-export.git, monorepo
  main fetched in as refs/mono/main); author and committer name/email/date copied from each original.
  No empty commits. Then fast-export --reference-excluded-parents (refspec replay -> main) -> rewrite_names.py
  (34 blobs changed, 0 messages) -> fast-import into a fresh clone export/ -> main = 97bd8ce, parent of first
  new commit = 51c9bc1, fast-forward confirmed. Push URLs of both clones set to DISABLED.
- rewrite_names.py's drop rule removed the strategy pptx again (it is in 4730e63:max and 2e8ebf9:max, not in
  51c9bc1) — consistent with v1.
- diff tip vs 2e8ebf9:max: 6 paths; 5 text files where rewrite(original)==export byte-for-byte (verify_diff.py),
  plus the dropped pptx. Read three: only placeholders on the export side.
- Scan tip tree: identifiers.yaml persons 7-10 = 0, drawings 11-12 = 0; project #0 16 -> 0 vs 51c9bc1;
  #6 = 2 (the two known float false positives); customer #5 = 1 (U13 png); sites #2-4 (allowed-private).
  Mask-map only: owner's name and user_path (not in identifiers.yaml) — reported to Kai.
- Tests at tip (max venv, py 3.12.10, markdown 3.7, pytest 9.1.1): build.py --check ok; 2 passed.
- No rule added to rewrite_names.py (no person/drawing hit).
- Patch scan (added lines, 618 new blobs, messages): persons/drawings 0; project #6 only in the two float json blobs.
- Report: C:/Users/stian/export-v3/REPORT.md. Tip 97bd8ce. Nothing pushed. Push is Kai's.
- Open for Kai: user_path (map-only) grew 1 -> 14 in the tip; owner's name map-only; neither in identifiers.yaml.

— Fairlead

## U40 (9 Nov ~03:5x)
- Export: 1 commit (U39 merge) onto 97bd8ce → tip 54afb64; scans persons/drawings 0; 4 checks ok (6 tests). Diff vs 2c94172:max = U38's 6 paths.
- Snapshot in publish/SWS: commit 3d29a1c (only sws/, docs/sws/; 173 A, 35 M, 0 D). Kept the two docx the last snapshot had,
  did not add rev128-130 docx (brief said no docx; asked Kai to decide). index.zip was untracked before me; left alone.
  Unlinked 4 links to the questions note (not carried). Publish-tree scan persons/drawings 0.
- Report C:/Users/stian/export-v3/REPORT-2.md. Nothing pushed.

— Fairlead
- Kai's decision: rev128-130 docx scanned (persons/drawings/customer 0) and added as second commit f545164. — Fairlead
