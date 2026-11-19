# Stanchion — U57 notes (10 Nov)

U57 builder (Opus): export increment for U56 (224704b..db05b45, max/ subtree, first-parent) grafted on 9f3beec, then
the Pages snapshot in publish/SWS on top of ed8274c. Method as kai.md "## U38" B(1)-(4), "## U51", "## U53", "## U55",
bulwark.md, ratline.md, kedge.md. Export and publish only; no content change (rule 10: the record this rests on is the
U38 export method). No identifier values in these notes.

- Start: ls-remote fjordbit/max main = 9f3beec = export clone tip; monorepo main db05b45, first-parent range 1 commit.
  publish/SWS at ed8274c (both remotes, ls-remote), only index.zip untracked.
- Export: db05b45:max replayed with commit-tree onto refs/exp/tip10 in work/ (replay10, author/committer/date from the
  original), fast-export --reference-excluded-parents, ref line renamed to refs/heads/main, rewrite (27 commands,
  5 blobs, 0 messages), fast-import into export/, worktree reset to main -> tip 9d9a329 (parent 9f3beec).
  verify_diff vs db05b45:max: the same 6 strategy paths, rewrite(original)==export.
- Scans: tip (763 files) persons/drawings/customer-name 0 whole-word; new: U56.md owner's name 1. Increment (20 blobs,
  added lines, message, 563 titles/alts/labels + 53 captions) 0/0. Substring advisories: all inside base64 image data
  or inside longer words (tools/b64ctx10.py, counts only), as before. 3 --check ok; 37 passed (four SWS test files,
  U41 venv, run in the archived tip tree).
- Snapshot: 13 files M, 2 A (working_area.png + its script). unlink8: 6/1/2, 0 double titles; links 0 unresolved,
  0 missing fragments. Visible text index/easy: 0 paths, 0 l.NNN, 0 snapshot notes (report.html carries file paths
  and l.NNN in visible text as in every earlier snapshot). Images: 5/68/4, all PNG data URIs. working_area.png is
  embedded on index and report (byte-identical to the carried file); easy.html does NOT embed it — it links to
  index.html#what-is-decided where it is (U56 allowed "the plot or a link to it"). Video resolves on report and easy.
  LD/LMA defined once on the short page with the LF note. Short page and easy read: no "reading is open"; the full
  report still says the B_rope definition is open in about 30 places inside rendered source documents (rerun note,
  verification, rope range, geometry, reconciliation, spec rev130, redline, U08 report). Not changed (content).
- index.zip rebuilt (report.html + mp4), untracked; old at export-v3/index.zip.before-u57. Publish scan (446 files incl.
  zip contents and titles) persons/drawings/customer 0; table = U55's minus four owner's-name hits.
  Commit 40f186a on ed8274c. Nothing pushed.
- Outputs in export-v3: scan_tip10.txt, scan_added10.txt, subscan_added10.txt, scan_pub10.txt, subscan_pub10.txt,
  addscan10/, pubtree10/, pubtitles10/, tools/b64ctx10.py.

— Stanchion
