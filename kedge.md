# Kedge — U51 notes (10 Nov)

U51 builder (Opus): export increment for U50 (6655e8c..5972096, max/ subtree, first-parent) grafted on 79e29a9, then the
Pages snapshot in publish/SWS. Method as kai.md "## U38" B(1)-(4), "## U43", "## U44", "## U47", "## U49", bowline.md,
cringle.md, REPORT-5.md. Export and publish only; no content change (rule 10: the record this rests on is the U38
export method). No identifier values in these notes.

— Kedge

- 01:xx Export: 1 commit replayed onto 79e29a9 (= GitHub main, ls-remote) → rewrite (5 blobs, 0 messages) → tip
  78b9e8c, fast-forward. Tip persons/drawings 0 (new: U50.md owner's name 1). Increment 0/0, hover titles 0. 3 --check
  ok, 25 SWS tests. Diff vs 5972096:max = the same 6 strategy paths.
- Snapshot: 4 docs/sws files changed; report.html unchanged after the unlink. Questions-note links unlinked (5/1/4); the
  easy read's U39.md link is now an absolute GitHub URL with a U50 title — href dropped, title kept + note appended
  (tools/unlink7.py). asnt/wikipedia/river 0 on easy.html, tyre analogy there. index.zip rebuilt, untracked. Scan 0/0.
  Commit 0e01f10.
- Worth knowing next time: fetch the monorepo commit into work/ (refs/mono/main7) and the export tip (refs/exp/tip7);
  pass commit-tree -F an absolute path (work/ is -C). Pre-existing advisory substring hits (not whole-word) in files
  this unit did not touch (report.html, 8 sws/ files; unchanged since earlier snapshots). REPORT-7.md refused by the
  harness; the hand-back is the report. Scan outputs: scan_tip7.txt, scan_added7.txt, scan_pub7.txt,
  subscan_pub7.txt in export-v3. Nothing pushed.

— Kedge
