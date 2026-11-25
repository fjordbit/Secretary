# jackline — U126 (firmware update and connection design note)

- Worktree C:/Users/stian/Prosjekter-u126, branch u126-update-and-connection from b5478a7 (main tip verified).
  Tip 6c85176. Adds only max/sws/transmitter/update_design/ (update_and_connection.md, update_calc.py, update_calc.json).
  No merge, push or export.
- C half built with GCC 16.2 (WinLibs path as in c_half/README.md): half_core.o text 3 068 B at -O2, 2 600 at -Os
  (README says 2 568 at -Os; flags differ). x86-64 core only; MCU image estimated 16/32/64 kB, marked ASSUMED.
- One web lookup, general terms (open-source MCU bootloader test/confirm/revert method); nothing about the project.
- Fresh falsifier: arithmetic clean; 12 wording/citation findings (byte-7 frame mix-up, "moving" detector placed
  at the box, "must" lines on top, rope-stopped contradiction, box-restart contradiction, given facts cited to spec,
  "element type"). All fixed before commit.
- Scans: scan_tree on the folder 0 (before commit); idscan b5478a7..HEAD 0 (run right after the commit, on the
  added lines).
- Not done: no MCU build (no cross compiler); flash erase/write times not counted; port rate limit not on record;
  nothing built in the simulator.

— jackline
