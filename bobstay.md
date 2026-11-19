# Bobstay — U69 notes (11 Nov)

U69 builder (Opus): export increment for U64–U68 (f73fb3e..8f97214, max/ subtree, first-parent) grafted on 1e215a2,
then the Pages snapshot in publish/SWS on 832e98f, link proof on six pages. Method as scuttle.md / kai.md "## U63".
No identifier values, no personal names.

- 15:10 (machine clock) started; timebox 1 h, ends ~16:10.
- Start verified: monorepo main 8f97214 = D:/git/prosjekter.git main; ls-remote fjordbit/max main 1e215a2 = export
  clone tip; publish/SWS 832e98f = ls-remote origin and maxflow; first-parent f73fb3e..8f97214 = 5. All as brief.
- Export: 5 trees <c>:max replayed with commit-tree onto 1e215a2 in work/ (replay13, refs/mono/main13; author/committer/
  date and message byte-exact from the original — checked per commit), fast-export --reference-excluded-parents, ref
  renamed byte-exact in python, rewrite 69 commands / 5 blobs / 0 messages, fast-import -> tip 025a0af (FF of 1e215a2;
  5 over GitHub). verify_diff vs 8f97214:max: same 6 strategy paths, rewrite(original)==export.
  Aside: U63's 1e215a2 message has one trailing newline more than f73fb3e's (git log %B); mine are exact. Not changed.
- Scans: tip 818 files, 660 whole-word, per-file table identical to tip12. Increment 36 paths (25 A, 11 M), blobs +
  added lines + messages + 1043 titles/alts/captions: whole blobs report.html, sws_data_sources.md, TASKS.md carry their
  old known hits (tip table unchanged); added lines 2 (owner-name entry) both in re-rendered report.html lines, removed
  side carries the same 2 (perfile add/del scan). Messages, titles 0. Rounds folder and price data file: 0. Substring
  advisories: all b64 or in-word (b64ctx10). idscan 1e215a2..025a0af: 0.
- Tests at tip (U41 venv, tiptree13): six --check ok (build, short, easy, hardware, software, housing); seven SWS test
  files (p52 skipped) 113 passed.
- Snapshot on 832e98f: 8 M, 19 A, 0 D (housing.html, build_housing.py, rounds/2026-11-11 12 files, price files, two pngs).
  unlink8: 6/1/2/0/0/0 (index/report/easy/hardware/software/housing), 0 double titles. Switch: six entries on all six
  pages, each target exists. Visible text hardware/software/housing (and index/easy): 0 paths, 0 l.NNN, 0 snapshot
  notes. Root docs/index.html is a redirect, unchanged. index.zip rebuilt (report.html + mp4, byte-checked), untracked;
  old at export-v3/index.zip.before-u69. Publish scan pubtree13 491 files, per-file table identical to pub12. Staged
  added lines: 2 owner-name hits, both re-rendered report.html lines, removed side the same 2. Commit 2dc95f3; idscan 0.
- Link proof export-v3/tools/links13.py (= links12 + housing.html; planted 3 breaks in a scratch copy, 3 caught),
  output export-v3/links13.txt: index 382/0/0, report 487/63/39, easy 60/0/0, hardware 39/297/0, software 17/310/0,
  housing 75/156/0 (relative/own-repo/external); broken 0 on all six. Nothing unlinked beyond unlink8's usual 9.
- External: the three newer pages have NO external href; their datasheet and distributor URLs sit in carried files
  (price data json, housing/price md, round files: 51 distinct), reached via own-repo links. Not fetched (not on a page).
  36 distinct external URLs, all on report.html; one HEAD each, no redirects followed, statuses below
  (export-v3/ext13_status.txt). The U63 404: "EN 12927 Chapter 14 summary (Mennens)" and "ISO 4309 and MRT (Mennens)"
  under spec-2-applicable-standards, plus the bare URL under register-references, all the same mennens.nl URL.
    200 https://arxiv.org/pdf/2201.03302
    302 https://docs.iba-ag.com
    403 https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/s1-understanding_ntp
    200 https://docu.ngsolve.org/latest/
    302 https://doi.org/10.1002/nme.2579
    302 https://doi.org/10.1007/BF01396415
    302 https://doi.org/10.1007/s007910050004
    302 https://doi.org/10.1016/j.softx.2020.100466
    302 https://doi.org/10.1109/20.717799
    302 https://doi.org/10.1109/TMAG.1983.1062812
    302 https://doi.org/10.13272/j.issn.1671-251x.2022090059
    302 https://doi.org/10.3390/nano12010023
    302 https://doi.org/10.3390/s19173763
    200 https://getdp.info
    200 https://gmsh.info
    301 https://goudsmitmagnetics.com/uploads/pdf/neodymium_grades_available_at_goudsmit_20230310_1547.pdf
    200 https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4827215
    000 https://iteh.es/catalog/standards/sist/8c7a9d01-9d03-4ff9-8fd7-834c56432e42/sist-en-12927-2019
    302 https://magpylib.readthedocs.io
    403 https://mans.io/files/viewer/1268719/427
    301 https://mennens.nl/en/services/magnetic-rope-testing/rope-inspection-safety-and-the-iso4309-regulation
    200 https://store.astm.org/e1571-21.html
    301 https://webstore.iec.ch/publication/2073
    200 https://www.allianceorg.com/pdfs/PhysicalPropertiesofMagnets.pdf
    200 https://www.australwright.com.au/technical-data/alloys/stainless-steel/stainless-steel-nitronic-60-uns-s21800/
    403 https://www.bodycote.com/?p=79093
    200 https://www.casar.de/Portals/0/L1_WIRE-220376-03_Katalog_CASAR_1122.pdf
    200 https://www.craneropesaustralia.com.au/product/casar-powerplast/
    200 https://www.farnell.com/datasheets/2860342.pdf
    403 https://www.mdpi.com/2079-4991/12/1/23
    404 https://www.mennens.nl/en/services/maintenance-and-inspection/test-and-repair/magnetic-rope-testing/en12927
    403 https://www.precision-elec.com/wp-content/uploads/2025/09/ABB-ACS880-Variable-Frequency-Drives-VFDs.pdf
    200 https://www.stanfordmagnets.com/coating.html
    000 https://www.technickenormy.cz/en/astm-e1571-25-standard-practice-for-electromagnetic-examination-of-ferromagnetic-steel-wire-rope
    200 https://www.ti.com/document-viewer/lit/html/SDAA451
    301 https://www.unirope.com/?p=2008
- Outputs in export-v3: in13/out13.stream, rw13.log, tiptree13/, addscan13/ (incl. perfile/), scan_tip13, scan_added13,
  subscan_added13, pubtree13/, pubadd13/, scan_pub13, links13.txt, ext13*.txt, tools/links13.py. Nothing pushed.
- 15:2x done.

— Bobstay
