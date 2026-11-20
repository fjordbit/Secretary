# grapnel — U122 rerun of the 19 Nov data-line and sensing-element rounds (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u122, branch u122-rerun-rounds from b5478a7 (checked: tip of main). Start 12:05.
- Models offered: agent-notes/models_offered_2026-11-20.md (Cursor list). Newest Grok: grok-4.7 (4.7 > 4.6 > 4.5);
  highest level not -fast: `grok-4.7-xhigh`. Newest Codex: only gpt-5.3-codex-* offered (and the Codex CLI is not
  installed), the same version that answered on 19 Nov (gpt-5.3-codex-high) -> Codex NOT rerun, per the brief.
- Briefs: copied from C:/Users/stian/<round>_2026-11-19/brief.md, SHA-256 equal to the 19 Nov "as sent" copy
  (data line DBF9989C..., elements A2FC2942...). scan_tree on both new folders 0 before sending.
- Runs: C:/Users/stian/data_path_round_2026-11-20/ and C:/Users/stian/element_round_2026-11-20/ (models.yaml names
  grok-4.7-xhigh exactly; --list: ready). Both ok; round.json input_sha256 equal to 19 Nov (ae3461e1... data line,
  f6d1d639... elements); scan_tree 0 on both answer folders before copying.
- Sheets (general queries, part numbers only; PDFs read via fitz in the solver venv, not copied): A1324-5-6 (Allegro):
  A1326 2.375-2.625 mV/G, 4.5-5.5 V, 6.9 typ / 9 max mA, 1.3 mG/rtHz, QVO drift +-10 G. MLX90395 rev 006: IMC
  (concentrator). TMR2503: maker's current list lacks it; LCSC page quotes "perpendicular to the surface of the sensor
  package" (sheet itself did not open). AAT001-10E: NVE page, angle sensor, 3-20 mT, sine/cosine.
- Key finds: element round TMR vs Hall flips to 2 TMR (Grok, Codex) : 1 Hall (Opus); Grok's eddy arithmetic now right
  (3 of 3); CT100 hunted error falls; Grok's first radial part TMR2503 is a Z-axis part (conditional). Data line: Grok
  now 4000/s, 40 Hz FIR, 3-byte values (frame 1236 B), index + us from edge (no clock time): its old exceptions fall.
- parts.yaml unchanged (rows cite notes on their own branches via git show; changing line refs broke --check, reverted).
  results.html rebuilt: only the #L12 -> #L14 anchor to the 5 mm line. Checks: render --check 0 problems; results
  --check ok; test_sws_results 26 passed (solver venv).
- Commit 055dee5. idscan b5478a7..HEAD 0 (688 added lines); scan_tree 0 on both folders.
- Falsifier (fresh, files only): 0 blocking, 9 minor. Fixed: Grok tally 5/3 under the note's own rule; TMR2102-04 source row back; Grok tags; effort per slot named (Codex ran high, xhigh offered); Grok's 40 Hz low-pass not counted as proper filter; r_arith labels; an empty r_arith.py I had left in secretary/ by a failed command, deleted. Not fixed (outside item 4): parts.yaml L01 'outside answers' plural (only Opus; predates rerun); 14 rows cite merged branches u109/u113 whose copies still hold the withdrawn Grok text. Tip 7fdcfbf; idscan 0 (696 lines); scan_tree 0; checks ok. End ~13:10. -- grapnel
