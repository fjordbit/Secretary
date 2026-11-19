# Ratline — U53 notes (10 Nov)

U53 builder (Opus): export increment for U52 + Kai's 82b02d7 (5972096..82b02d7, max/ subtree, first-parent) grafted on
78b9e8c, then the Pages snapshot in publish/SWS. Method as kai.md "## U38" B(1)-(4), "## U47", "## U49", "## U51",
kedge.md, bowline.md, REPORT-5.md. Export and publish only; no content change (rule 10: the record this rests on is the
U38 export method). No identifier values in these notes.

— Ratline

- Export: started on c593422 (tip ffc197f); Kai's mid-run change added 82b02d7. Replayed both in work/ (replay8,
  replay8b; refs/mono/main8, main8b), fast-export 78b9e8c..replay8b → rewrite (22 commands, 5 blobs, 0 messages) →
  scratch export main reset to 78b9e8c (ffc197f was local only) and re-imported: ffc197f (same hash) → tip 1bd191b.
  Fast-forward of 78b9e8c (= GitHub main, ls-remote).
- Scans: tip persons/drawings 0 (new: U52.md owner's name 1); increment 0/0 whole-word, 536 hover titles included;
  advisory substring hits in easy/index.html are inside base64 image data (masked-context check, tools/ctx8.py),
  unchanged from earlier snapshots. 3 --check ok, 29 tests. verify_diff vs 82b02d7:max: the same 6 strategy paths.
- Snapshot: 4 docs/sws files changed (report.html unchanged after the unlink). Links already had titles, so the old
  unlink5 would have written a second title; new tools/unlink8.py drops href and appends the note to the existing
  title (6/1/5 unlinked, 0 double titles). Visible text of index/easy: 0 paths, 0 l.NNN, 0 snapshot notes
  (tools/visible8.py). index.zip rebuilt, untracked. Publish scan 0/0, table identical to U51. Commit 54db766.
- Outputs in export-v3: scan_tip8.txt, scan_added8.txt, subscan_added8.txt, scan_pub8.txt, subscan_pub8.txt,
  pubtitles8/. Nothing pushed.

— Ratline
