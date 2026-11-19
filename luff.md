# luff — U109 notes (the transmitter line)

- Worktree C:/Users/stian/Prosjekter-u109, branch u109-transmitter-line from 8c3218c (verified = tip of
  u108-data-path). Adds only max/sws/transmitter/ (note, line_calc.py + json, make_figures.py, 7 figures + 3 slides,
  source.md, terms.md, answers/ with the three outside answers unchanged).
- Sheets read from ti.com into the scratchpad (not in the repo): ADS131M08 SBAS950B, ADS131E08 SBAS561C. E08 Table 1
  text is column-shifted in the extraction (dB of row k next to ENOB of row k+1; ENOB = dB/6.02 confirms the
  mapping); its Eq. 2 root-two factor not legible, taken as in the M08 sheet (marked).
- Found: the M08 has a built-in high-pass (DC block, Table 8-4), off by default; rule 2 says keep it off.
- Kai's mid-run addition (Nyquist, aliasing table, A1, filter responsibilities, box per SWS, 100 m case) done in
  part 3 / part 5 and the easy-read sentences (twelve instead of ten because of it).
- Answers read only after parts 1-5 were written; scan_tree on them 0 before copying; cmp identical.
- P1 is simulated (no ripple trace in the repo; ripple size from u19_summary.json stranded 3D model).
- figkit limit: S2 has 6 curves, so the 99 % aim is in the note, not as a band.
- Falsifier: see the hand-back.
- Falsifier (fresh agent, files only): 2 blocking (Codex position row misread; interpolation vs rule 1 contradiction)
  and 15 minor. All fixed: rule 1 now gives both readings (samples as they fall 80/125/250; logger interpolating
  40/50/100 three-stage, 50/80/160 block); tone table includes the correction gain; DC block 9.7 mHz-181 Hz, 8.3.8;
  radial drift and E08 drift added; radial element noise caution (~7 uT if voltage noise is what is fixed); ripple
  ratio from the axial 0.21 mT only (~0.015); slides relabelled and cut. No second pass (fixes were edits, not new
  method). Not fixed: "the owner" kept where it names who decides.
- Commit aa1eae5 on u109-transmitter-line (26 files, adds only max/sws/transmitter/). idscan 8c3218c..HEAD 0;
  scan_tree 0. Answers byte-identical before commit; git normalises their CRLF to LF on commit.
