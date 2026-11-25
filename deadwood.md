# deadwood (U133) — temperature in the twin

- Worktree C:/Users/stian/Prosjekter-u133, branch u133-dt-temperature from b5478a7 (main tip verified from u05).
  Venv inside max/sws/line_beta/.venv (Python312 base, requirements.txt), not committed.
- New: linebeta/thermal.py (5-node lumped day model, sun-study formulas re-implemented), linebeta/thermal_twin.py
  (magnet factor at T_magnet; per-grade record table option from 3d/falsify/b_tolerances.md; element offset/TCS
  vs board temperature; two sensor readings per half), thermal_days/ (4 ASSUMED profiles + make_days.py),
  thermal_runs.py, thermal_out/, figures/temperature/ T1-T5, tests/test_thermal.py, note
  temperature_in_the_twin.md.
- Shared-file blocks (marked U133): settings.toml [thermal] after [temperature]; rope_sim.py wrapper at the end
  (HeadSim.generate -> thermal_twin.generate only when thermal.enabled); half.py 3 lines (temps (k,) or (k,2));
  README.md 6 lines after the settings paragraph.
- Second sensor: the two existing i16 fields (upper / lower). Not built: aux slot, frame change. Left for a C/Python
  byte test in that mode: host input row (table_to_bin ROW_DT, host_main {t,t}).
- Record sources: sun study (due-diligence/sws_sun_exposure*.{py,md}; contains a place name - not repeated),
  b_tolerances.md s.2, d_measurement_chain.md, sws_sensor_candidates.md s.2.2 (TMR2151S / TMR2584; the 0.5 mV
  offset unit ambiguity left open), spec rev131 render l.36, l.346, l.367; register l.330, l.423-424.
- Web: one general query (humid subtropical climate, coastal summer day) - only textbook climate-type text.

— deadwood
