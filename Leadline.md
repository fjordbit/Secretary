# Leadline — U101 section D (measurement chain, desk study)

Worktree C:/Users/stian/Prosjekter-u101d, branch u101d-falsify from c19d94c (verified = u100-h52-sweep tip).
Tip 5aa981b. Added only: max/sws/3d/falsify/d_measurement_chain.md, d_chain.py, d_chain.json. No solver run.

Findings (details in the note):
- F2 not broken: groove level divides every sensor zero error by 4.4–5.6x. Wording weak: magnet over 65 K = 3.5 % of metal at k 1, uncompensated.
- F1 input "about 2 mT/mm" is the no-groove value; grooved zero gradient 3.0 (k1) / 5.3 (2.00 T) / 9.3 (2.10 T) mT/mm.
- ±20 mT window at 16 mm: 16.9 mT at 2.00 T only with depth ±0.1, element ±0.5, zero trimmed on real rope; 26 mT at 2.10 T; ~32 mT untrimmed.
- F5 not broken, reinforced: 1 % metal = 410–960 µT long-term zero stability needed.
- F6 weakened: LMA rests on DC offset stability no TMR sheet states; radial cross field 31 -> 107 mT (1.90 -> 2.10 T) vs signal x1.7.
- Most serious: TMR2584 offset tempco "0.5 mV max" — total = 0.1–0.2 % of metal, per K = 7–16 %. Decides the weaker link.

Checks: build.py --check 1 problem (stale report.html) only. pytest: neither venv collects the full suite (jsonschema missing in Prosjekter venv,
markdown missing in u05 venv); with 3 modules ignored 72 failed / 637 passed, identical with and without the added files. idscan 0, scan_tree 0.
One general web query (TMR class offset drift): strong-field exposure -> irreversible offset shift (maker app note).
— Leadline
