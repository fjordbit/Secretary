# Windlass — export of Prosjekter main 8d7ac15 to the cleaned repo (7 Nov 2026)

Status: STOPPED at step 6 (scan). Nothing pushed anywhere, D:/git/max-export.git untouched.

- Split tip a69c990 (tree = Prosjekter main:max, verified). Old split = 20817cc (matches 51c9bc1).
- 6 new first-parent split commits, all linear (subtree split folded the three merges away; merge trees equal their side tips).
- Cherry-picks clean, no conflicts. Rewrite: 0 blobs, 0 messages changed. Rewritten main = e73673b (identical objects, since nothing changed).
- Whole-tree scan: one entry of kind "project" with a placeholder appears 16x as a whole word in 5 sws/ files that are already on GitHub since 4 Nov and not touched by this export. rewrite_names.py does not replace it (that entry has no `match` field; dry run over whole tree and full history: 0 changes). Could not tell from here whether it is meant to stay. Kai/Stian to decide.
- Three "site" entries (with a `policy` field, no placeholder) appear in sws/ too; presumably allowed by policy.
- Secrets: only fake test keys, empty .env.example, .invalid test e-mails, fixture NOK amounts, public component BOM estimates in EUR in the SWS spec.
- Work dirs: scratchpad 2a40536beb49695d/.../scratchpad/max-clean (main = e73673b), max-export (cherry-picks).

— Windlass

## v2 full-history rewrite (7 Nov, second task)
- D:/git/max-export-v2.git created (new bare, HEAD -> main). D:/git/max-export.git untouched. Nothing pushed.
- 101 commits in, 101 out; 15 branches, 0 tags; rewrite: 9 blobs changed, 0 messages.
- main v2 = f0c85fd: the project entry has 0 hits; the diff against e73673b touches 5 sws files, 16 lines, all name → placeholder only.
- SWS branches: 17 lowercase occurrences of the project name remain in 4 twin/ files (code-like `name.x9` tokens), not covered by the exact/upper rules. A project number (another project entry) appears 3 times as a whole word in twin/ files, and a person entry appears once, lowercase, in a path in sws/3d/rope3d.py (u16, u19). All of these were there before the rewrite. Not clean yet: Kai to decide.
- sws-report `build.py --check`: ok on u08, u16, u17, u19 (v2). main has no workflows.
- The u17 branch name contains a person's first name (not on the identifier list).

— Windlass

## v2 rebuilt with Kai's three extra rules (7 Nov, third task)
- D:/git/max-export-v2.git deleted and rebuilt. 101/101 commits, 13 blobs and 0 messages changed. v2 main = ff533da.
- Project entries (all cases), the project number and the person: 0 real hits on main, u08, u16, u17, u19. What is left is sites (allowed) and false positives (floats, base64, inside words, PNG bytes).
- Every diff edit, old tip → v2, is a plain identifier → placeholder swap (main: 5 files/16 lines; u19: 7 files/24 lines).
- build.py --check ok and test_sws_report passes on all four SWS branches. Nothing pushed.

— Windlass
