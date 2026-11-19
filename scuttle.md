# Scuttle — U63 notes (11 Nov)

U63 builder (Opus): export increment for U60–U62 grafted on da77fe4, Pages snapshot on c81b11f, link proof.
Method as stanchion.md, becket.md, kai.md "## U57", "## U59". No identifier values, no personal names.

- 13:2x (machine clock) started; timebox 1 h, ends ~14:20.
- Start: ls-remote fjordbit/max main 9d9a329; fjordbit/SWS and MAx-Flow/SWS-Documentation main 40f186a; export clone
  da77fe4 on 9d9a329; publish/SWS c81b11f on 40f186a; monorepo main f73fb3e; first-parent ff08f9f..f73fb3e = 3. All as brief.
- Export: 3 trees <c>:max replayed with commit-tree onto da77fe4 in work/ (replay12, refs/mono/main12, refs/exp/tip12),
  fast-export --reference-excluded-parents, ref renamed byte-exact in python (sed broke the stream once; redone), rewrite
  37 commands / 5 blobs / 0 messages, fast-import -> tip 1e215a2 (FF of da77fe4; 4 over GitHub). verify_diff vs
  f73fb3e:max: same 6 strategy paths.
- Scans: tip 793 files, per-file table identical to tip11 (persons/drawings 0, customer #5 1 = known png). Increment
  (19 blobs, added lines, messages, titles): whole blobs report.html/TASKS.md carry old known hits as in U59; added lines,
  messages, titles 0; substring advisories all in-word or base64 (b64ctx10). idscan da77fe4..main 0.
- Tests at tip (U41 venv, tiptree12): five --check ok; six SWS files 84 passed.
- Snapshot: 7 M, 5 A. unlink8: 6/1/2/0/0. Switch 5 entries on 5 pages. Root docs/index.html is a redirect, unchanged.
  Visible text hardware/software/index/easy: 0 paths, 0 l.NNN, 0 snapshot notes. index.zip rebuilt (old:
  export-v3/index.zip.before-u63). Publish scan 472 files, table identical to pub11. Commit 832e98f; idscan 0.
- Link proof export-v3/tools/links12.py (negative-tested with 6 planted breaks, all caught): 0 broken on all five pages.
  Caveat: the 553 own-repo links on hardware/software go to .md files with #Lnn in GitHub's blob view, which renders
  markdown; whether GitHub lands on the line without ?plain=1 was not verified (no project URL fetched).
- External: 36 distinct, all on report.html; one HEAD each: 13x200, 16x3xx, 5x403, 1x404, 1 no answer. Per-URL
  statuses were not saved and not re-fetched (one HEAD rule), so the 404 is not identified.
- Outputs in export-v3: scan_tip12, scan_added12, subscan_added12, scan_pub12, addscan12/, pubtree12/, tiptree12/,
  tools/links12.py. Nothing pushed.
- 13:28 done.

— Scuttle
