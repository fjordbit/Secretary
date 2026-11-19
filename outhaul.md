## 2026-11-11 13:3x (machine clock) - started
- Unit / branch: U64 / u64-price-complexity from f73fb3e (C:/Users/stian/Prosjekter-u64/max)
- Job: prices looked up (part numbers only), per-half cost, complexity counts, one figure, section on hardware.html via build_hardware.py, note sws_price_complexity.md.
- Timebox 2 h, ends ~15:30 machine clock.
— Outhaul

## 2026-11-11 13:5x (machine clock) - committed, done
- Unit / branch: U64 / u64-price-complexity, tip 8f24500 (C:/Users/stian/Prosjekter-u64/max). No merge, no push, no export.
- Earlier graph: not found as a figure; spec §7 has a masked "Cost vs complexity" table, its columns followed.
- Prices: 15 parts from DigiKey (part numbers only in queries); not found: TI 1 ku, a second distributor, the oscillator.
- Result: no "cheaper = more complex"; A has the lowest chain BOM and the fewest tasks, D (most complex) is not cheaper; the assembled overlap comes from the estimates. Temperature priced apart.
- Five --check ok; 89 tests; 5 / 6 A4; scans 0 / 0. Falsifier and cold reader PASS WITH FIXES, fixes applied, neither re-run.
- Section a little over ½ A4 (prints in 135–150 mm).
— Outhaul
