# garboard — U101 section E (desk study)

Started. Worktree C:/Users/stian/Prosjekter-u101e, branch u101e-falsify at c19d94c.

- Section E of U101 (desk study, no solver). Worktree C:/Users/stian/Prosjekter-u101e, branch u101e-falsify from c19d94c (verified = u100-h52-sweep tip).
- Read the five notes, their JSON (spot checks recomputed: kernel gain/residual, bracket nulls, H52 map steel-left max-mean, H52 run drift-null radii and slopes at the zero), five builder notes, three outside answers (opinions, anonymised as 1-3), spec rev130 render, REDLINE, register rows, sensor notes.
- Main finds: H52 drift null 3.7-5.9 mm inside the zero at the magnet as modelled (run.json), crosses the element only in a narrow induction band (~0.85 mm per 0.01 T); slope at the zero 3.0-5.3 mT/mm (not the 2 mT/mm in section D's brief); bracket nulls interpolated in k 1.0-1.3 where the level changes 60 %; kernel max misfit 6.2 % (5.4 % is the gain); ring-vs-wire Limits sentence in four notes contradicts axial_liftoff; F2 "4-6x" is 3.7-7.3x; groove at same magnet costs 4-14 % of short fault.
- Unrechecked falsifier fixes listed with lines (U95, U96, U97 - result not recorded in stemson's note -, U98, U100 pass 2). U100 pass-2 fixes re-checked against JSON: hold.
- Consequences (largest): magnet size/sizing rule (groove pushes the 1.92 T-sized head below the floor; 2.00 T needs ~24 mm N52 vs 15.8); spec "cut-out not adopted"; axial part position and range rule; shared/universal head; FAT LMA +-0.5 %.
- Commit ad85858 (one file, sws/3d/falsify/e_documents.md). scan_tree 0, idscan 0 (133 added lines). build.py --check: 1 problem, report.html stale (as base). pytest not reproducible: no venv on the machine has both markdown and jsonschema; solver venv minus 3 jsonschema modules: test_sws_report fails as base + 72 env failures.
- garboard
