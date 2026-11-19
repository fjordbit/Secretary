# Becket — U59 notes (10 Nov)

U59 builder (Opus): export increment for U58 (db05b45..ff08f9f, max/ subtree, first-parent) grafted on 9d9a329, then
the Pages snapshot in publish/SWS on top of 40f186a. Method as stanchion.md / kai.md "## U57", "## U38" B(1)-(4).
Export and publish only; no content change (rule 10: the record this rests on is the U38 export method). No
identifier values in these notes.

- Start: ls-remote fjordbit/max main = 9d9a329 = export clone tip; monorepo main ff08f9f, first-parent range 1 commit.
  publish/SWS at 40f186a (origin and maxflow, ls-remote), only index.zip untracked.
- Export: ff08f9f:max replayed with commit-tree onto 9d9a329 in work/ (replay11; author/committer/date from the
  original, exported env), fast-export --reference-excluded-parents, ref line renamed to refs/heads/main, rewrite
  (34 commands, 5 blobs, 0 messages), fast-import into export/, worktree reset -> tip da77fe4 (parent 9d9a329).
  verify_diff vs ff08f9f:max: the same 6 strategy paths, rewrite(original)==export.
- Scans (scan_tree, whole-word): tip 784 files, 660 hits, per-file table identical to tip10 (persons/drawings 0;
  customer #5 1 = the known U13 png). Increment added lines + message + titles: 0 (whole blobs of report.html and
  TASKS.md carry their old known hits). Rounds folder: 17 files, 0. Substring advisories: one person entry, 9 in
  added lines, all inside longer words in five round files (tools/b64ctx10.py, counts only).
- At tip: four --check ok; 61 passed (five SWS test files, U41 venv, in tiptree11).
- Snapshot: 4 M, 19 A (build_hardware.py, hardware.html, rounds/ 17 files). unlink8: 6/1/2/0, 0 double titles.
  Links: 0 unresolved, 0 missing fragments on all four pages; hardware.html 142 repo links all carried, no #Lnn past
  file end (tools/repolinks11.py). Switch: four entries on all four pages, each target exists. Visible text
  index/easy/hardware: 0 paths, 0 l.NNN, 0 snapshot notes (report.html as every earlier snapshot). Publish root
  docs/index.html not changed: it is a redirect with one link to sws/, it does not list the pages.
- index.zip rebuilt (report.html + mp4), untracked; old at export-v3/index.zip.before-u59. Publish scan 466 files,
  397 whole-word, per-file table identical to pub10; persons/drawings/customer 0. Snapshot added lines: 0 whole-word.
  Commit c81b11f on 40f186a. Nothing pushed.
- Outputs in export-v3: scan_tip11.txt, scan_added11.txt, subscan_added11.txt, scan_rounds11.txt, scan_pub11.txt,
  subscan_pub11.txt, addscan11/, pubadd11/, pubtree11/, pubtitles11/, tools/links11.py, tools/repolinks11.py.

— Becket
