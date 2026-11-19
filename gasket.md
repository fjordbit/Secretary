# Gasket — U75 notes (12 Nov)

U75 builder (Opus): export increment for U70–U74 (8f97214..a3a633a, max/ subtree, first-parent) grafted on 025a0af,
Pages snapshot in publish/SWS on 2dc95f3, link proof on eight pages. Method as bobstay.md / scuttle.md / kai.md "## U69".
No identifier values, no personal names.

- 18:31 (machine clock) started; timebox 1 h.
- Start verified: monorepo main a3a633a = D:/git/prosjekter.git main; ls-remote fjordbit/max main 025a0af = export clone
  tip; publish/SWS 2dc95f3 = ls-remote origin and maxflow; first-parent 8f97214..a3a633a = 4. All as brief.
- Export: 4 trees <c>:max replayed with commit-tree onto 025a0af in work/ (tools/replay14.py; replay14, refs/mono/main14;
  author/committer/date and message byte-exact, checked per commit), fast-export --reference-excluded-parents
  out13..replay14, ref renamed byte-exact in python, rewrite 77 commands / 5 blobs / 0 messages (rw14.log), fast-import
  -> tip 71288f8 (FF of 025a0af; 4 over GitHub), worktree reset to main. verify_diff vs a3a633a:max: same 6 strategy
  paths as before (5 rewrite(original)==export, 1 pptx only-in-original).
- U74 squashed commits (5, from the branch reflog): 58 objects reachable from them and not from a3a633a (exact set
  difference; plain `rev-list --not` over-reports 80/22 because it marks only boundary trees). 0 of the 58 in the
  export clone.
- Scans: tip 845 files, 660 whole-word, per-file table identical to tip13. Increment 39 paths (27 A, 12 M, 0 D):
  whole blobs report.html, sws_data_sources.md, TASKS.md carry their old known hits; added lines 2 (owner-name entry),
  both re-rendered report.html lines, removed side the same 2. Messages, titles/alts/captions, rounds folder
  2026-11-12-sensor, sensor notes, placement note/script/json, figure: 0. Substring advisory new: 1 in sensor.html,
  base64 (b64ctx10). idscan 025a0af..71288f8: 0. No pdf in the increment; no file from secretary/ or max-private/
  (the folder name "agent-notes/kai.md" appears in unit reports/TASKS as before; the literature note cites EN 12927
  clause numbers with paraphrase and says the full text is held privately — no standard text file).
- Tests in tiptree14 (git archive of the tip; U41 venv): eight --check exit 0; nine SWS test files (p52 skipped)
  151 passed.
- Snapshot on 2dc95f3: 9 M, 20 A, 0 D; staged sws/ tree = export tip sws/ tree (e6ea499). unlink14 (= unlink8 + U17/U29
  reports): index 6, report 1, easy 2 (as before), procedures 2 NEW: tasks/reports/U29.md#L77 and U17.md#L20 (the drawn
  40 mm prototype citations) — tasks/ is not carried in the Pages repo; carrying would put a third folder in publish
  (brief D: only sws/ and docs/). href dropped, text kept, title gets the not-in-snapshot note. 0 double titles.
  Switch: eight entries on all eight pages, each target exists, current marked once. Root docs/index.html is a
  redirect to sws/, unchanged. Visible text procedures/sensor (visible14.py): 0 paths, 0 l.NNN, 0 snapshot notes,
  0 dates, 0 role words, 0 local paths. index.zip rebuilt (report.html + mp4, byte-checked), untracked; old at
  export-v3/index.zip.before-u75. Publish scan pubtree14 (+ _titles, _unzipped) 515 files, 397 hits, per-file table
  identical to pub13. Staged added lines: 2 owner-name hits, re-rendered report.html, removed side 2. Commit f51035e
  (tree = scanned staged tree b75b75c); idscan 2dc95f3..f51035e 0.
- Link proof tools/links14.py (= links13 + procedures, sensor; planted 3 breaks in a scratch copy, 3 caught), output
  export-v3/links14.txt (relative/own-repo/external, broken): index 384/0/0, report 491/63/39, easy 62/0/0, hardware
  42/303/0, software 19/310/0, housing 77/156/0, procedures 113/18/0, sensor 14/83/0; broken 0 on all eight.
- External: new pages have no external href. 36 distinct, all report.html, same list as U69; one HEAD each, no
  redirects followed (export-v3/ext14_status.txt): 200x13, 302x11, 301x5, 403x4, 000x2, 404x1.
  Not 200/3xx: 404 mennens.nl …/magnetic-rope-testing/en12927 ("EN 12927 Chapter 14 summary (Mennens)" under
  spec-2-applicable-standards; bare URL under ref-R10); 403 mans.io, bodycote.com, mdpi.com, precision-elec.com;
  000 (no answer in 20 s) iteh.es, farnell.com datasheet (200 in U69).
- Not verified: GitHub's blob view landing on #Lnn of .md files (as U63 caveat); nothing fetched from the project's
  own URLs.
- Outputs in export-v3: in14.raw.stream, in14/out14.stream, rw14.log, tiptree14/, addscan14/, scan_tip14, scan_added14,
  subscan_added14, pubtree14/, pubadd14/, scan_pub14, subscan_pubadd14, links14.txt, ext14_status.txt, visible14.txt,
  chk14_*; tools replay14, addscan14, links14, unlink14, switch14, visible14, linktext14. Nothing pushed.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 18:43 done.

— Gasket
