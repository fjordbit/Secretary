# wildcat — U115 H40 head on 38-40 mm rope (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u115, branch u115-h40-on-38 from 1735f4b (verified = tip of main).
- Adds only max/sws/3d/h40_on_38/. g_lib.py etc. imported unchanged; plotstandard.py + figkit.py copied unchanged
  from u106-groove-plots d112319 (not on main).
- Grades by remanence swap at H40 size (as groove_plots/run_missing.py), not the trade-off run's thicker magnet.
- Temperature: the trade-off run was 25 C only; used the tool's rule Br(T) = Br25 (1 - 0.0012 (T - 25)) for both
  grades. Rope/steel curves temperature-free in the tool.
- 378 solves (depth 58, standing 240, signals 80), all converged, 8-10 workers, ~20 s each. Logs in the scratchpad.
- Off-centre rope and one broken wire: stand-ins only (local-gap reading; ring of one wire's area). No 3D.
- Peak rope induction sits at z 45 mm (inside the magnet's inner edge), 0.28-0.33 T above the mid-plane: passes
  2.3 T for N52 high curve and in the cold; mid-plane never (1.865-2.067 T).
- Falsifier (fresh subagent, files only): reran 2 cases from scratch, rope induction identical; zero / B_z match
  with the notes' 1 mm read stencil, but a 0.05 mm stencil moves standing B_z by up to ~1.8 mT and the zero 0.3 mm
  (now stated in section 1). 3 blocking (peak-minus-mid range 0.23-0.36 T; "stiff/soft" curve words; easy-read 6
  firmer than section 3) and 8 minor - all fixed. No second pass.
- Commit 83e7977 (18 files, adds only h40_on_38/). idscan 1735f4b..HEAD 0; scan_tree 0. stand.json 1.6 MB (profiles).
