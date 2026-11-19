# Gybe — U79 notes (16 Nov)

U79 builder (Opus): export increment for U76 + U77 (a3a633a..5f415b6, max/ subtree, first-parent) grafted on 71288f8,
Pages snapshot in publish/SWS on f51035e, link proof on nine pages. Method as gasket.md / kai.md "## U75".
No identifier values, no personal names.

- 13:28 (machine clock) started; timebox 1 h.
- Start verified: Prosjekter-u05 main 5f415b6 = D:/git/prosjekter.git main; ls-remote fjordbit/max main 71288f8 =
  export clone tip; publish/SWS f51035e = ls-remote origin and maxflow. first-parent a3a633a..5f415b6 = 2 (U76, U77
  merges). Increment touches only max/. All as brief.
- Export: work/ fetched local main as refs/mono/main15; tools/replay15.py (= replay14, new range/base) -> replay15
  4fa2bb1, both commits "exact" (author/committer/dates/message). fast-export --reference-excluded-parents
  refs/exp/out14..replay15, ref renamed byte-exact in python (2 commit lines, 0 other), rewrite_names: 31 commands /
  5 blobs / 0 messages (rw15.log), fast-import into export/ -> main 0f7b145 (parent 452d853, parent 71288f8; FF of
  71288f8; 2 over GitHub), worktree reset to main, clean. verify_diff vs 5f415b6:max: the same 6 strategy paths
  (5 rewrite(original)==export, 1 pptx only-in-original). refs/exp/out15 = 0f7b145 in work/.
- Scans (u05 venv): tip tiptree15 853 files, 660 whole-word; per-file table identical to tip14 (BOM only).
  Increment addscan15: 18 paths (8 A, 10 M, 0 D). Whole blobs report.html 86, sws_data_sources.md 23, TASKS.md 7 =
  same old known hits as U75. Added lines: 2 (owner-name entry), both on the re-rendered report.html lines; removed
  side the same 2. New chapter, figure + script (sws/figures/sensor/), rig_sheet.html + builder, sws/procedures/
  AI guide, register rows, messages: 0 whole-word. Substring advisory new: 1 in tasks/reports/U76.md, inside an
  ordinary English word (ctx8, masked); sensor.html 1 = the known base64 one. idscan 71288f8..0f7b145: 0.
  No pdf in the increment; no file from secretary/ or max-private/ (agent-notes/kai.md named as brief source in
  TASKS/U76/U77 as before; no local paths in added lines).
- Tests in testtree15 (git archive of the tip, separate from the scanned tree; u41 venv): nine --check exit 0
  (build, easy, hardware, housing, procedures, rig_sheet, sensor, short, software); ten SWS test files (p52 skipped)
  180 passed.
- Snapshot on f51035e: 8 M, 5 A, 0 D; staged sws/ tree = export tip sws/ tree (07c0860). unlink15 (= unlink14) on
  nine pages: index 6, report 1, easy 2, procedures 2 (as before), rig_sheet 1 NEW: tasks/reports/U17.md#L20 (the
  drawn 40 mm prototype citation; tasks/ not carried). href dropped, text kept, title note; 0 double titles.
  Switch: eight entries on the eight menu pages, each target exists, current marked once; rig_sheet.html has no
  switch and is not on the menu. It opens from procedures.html, link "rig sheet" in #st-proto; its "Back to the
  procedures page" -> procedures.html#st-proto (2 links), anchor exists.
- AI guide link (procedures #st-proto and rig sheet): https://github.com/MAx-Flow/SWS-Documentation/blob/main/
  sws/procedures/prototype_test_ai_guide.md — GitHub blob view of the Pages repo, the same absolute URL in the
  snapshot and in the code repo's copy of the pages. Target exists in the snapshot (committed) and also at
  sws/procedures/prototype_test_ai_guide.md in the export tip. The guide holds no links of its own.
- Visible text sensor / rig_sheet / procedures / housing (visible14 -> visible15.txt): 0 on every pattern
  (paths, l.NNN, snapshot notes, dates, role words, local paths).
- Rig sheet print: headless Edge from the snapshot copy -> export-v3/rig15.pdf, A4 MediaBox, 4 pages. Not looked at
  as images (no PDF renderer here).
- index.zip rebuilt (report.html from the snapshot + mp4 from the old zip, both byte-checked), untracked; old at
  export-v3/index.zip.before-u79. Publish scan pubtree15 (+ _titles, _unzipped) 520 files, 397 hits, per-file table
  identical to pub14; _titles alone 0. Staged added lines: 2 owner-name hits in re-rendered report.html, removed
  side 2. Commit 1a58533 (tree 0a3c369 = scanned staged tree); idscan f51035e..1a58533 0.
- Link proof tools/links15.py (= links14 + rig_sheet.html), output export-v3/links15.txt (relative/own-repo/external,
  broken): index 384/0/0, report 493/63/39, easy 62/0/0, hardware 42/303/0, software 19/310/0, housing 79/156/0,
  procedures 115/19/0, sensor 45/85/2, rig_sheet 17/4/0; broken 0 on all nine.
- External: 38 distinct; 2 new (sensor.html, general physics on Wikipedia: Faraday's law of induction, interface
  conditions for EM fields), one HEAD each, no redirects followed (export-v3/ext15_status.txt): 200, 200. The other
  36 not re-checked (statuses in ext14_status.txt).
- Not verified: GitHub's blob view landing on #Lnn of .md files; nothing fetched from the project's own URLs. The
  code repo's copy of rig_sheet.html / procedures.html keeps the U17/U29 hrefs to the Pages repo's tasks/ (not
  carried) — same as procedures.html since U75.
- Outputs in export-v3: in15.raw.stream, in15/out15.stream, rw15.log, tiptree15/, testtree15/, addscan15/,
  scan_tip15, scan_added15, subscan_added15, pubtree15/, pubadd15/, scan_pub15, scan_pubadd15, subscan_pubadd15,
  links15.txt, ext15.txt, ext15_status.txt, visible15.txt, rig15.pdf, chk15_*, msg15.txt; tools replay15, addscan15,
  links15, unlink15. Nothing pushed.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 13:38 done.

— Gybe
