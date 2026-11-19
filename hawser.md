# Hawser — U26 (Studio: auto-arrange the lines)

## 2026-11-07 start
Worktree C:/Users/stian/Prosjekter-u26, branch u26-studio-arrange from 4730e63. Reading the brief's READ list first.
— Hawser

## 2026-11-07 — before numbers (main 4730e63, measured from the drawn SVG, all levels)
- default loop: 105 line–block intersections, 85 crossings, 11/11 backward lines through the row band
- writer flow: 28 intersections, 11 crossings, 6/6 backward lines through the band
- Both saved flows are 0.2-draft with frames, so they draw through hier.js (each level auto-laid out; chart `view` x/y is not used there today).
- Assumption (not stopping): "saved view wins" = chart `view` in flat 0.1 charts (as today) + a per-level saved position store in hier levels (`K.arrange.save`), which arrange never overrides. No block-drag UI exists today, so nothing writes that store yet.
— Hawser

## 2026-11-07 — built, qc running
- After: default loop 0 intersections / 30 crossings (from 105/85); writer flow 0 / 6 (from 28/11); backward lines in band 0 (from 11 and 6).
- 116 Studio tests pass (new + existing). Report tasks/reports/U26.md. qc-falsifier running; commit after it.
- Side fix: hier.js now draws a block's own delay edge (ladder count); it was silently dropped at every level.
— Hawser

## 2026-11-07 — committed
- Unit / branch: U26 / u26-studio-arrange (C:/Users/stian/Prosjekter-u26)
- Commit: df48bbf. Studio auto-arrange: 0 line–block intersections on both saved flows; crossings 85→30 and 11→6.
- qc-falsifier: no blocking findings. It found four non-blocking points: one is fixed (the 0.5 px rounding), three are open and listed in report §6.
- Ready for Kai's check: yes. Not pushed, not merged.
- Needs Stian: see the report §4 (what "saved view" means in nested levels) and the open points in §6.
— Hawser

## 2026-11-07 — rebased onto main ce08340 (U23 merged), per Kai
- Commit: 121dc52 (was df48bbf). The only conflict was tasks/TASKS.md: kept both entries, U23 then U26. Main at ce08340 has no section titled "Landed on main"; U23's text there is its TASKS entry, and that is kept unchanged.
- Re-run from Prosjekter-u26/max (max_core resolves to u26): 116 passed in 105.83s (0:01:45).
- Not pushed, not merged.
— Hawser
