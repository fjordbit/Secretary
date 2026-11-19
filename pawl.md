# pawl — U112 notes (the half in C)

- Worktree C:/Users/stian/Prosjekter-u112, branch u112-half-in-c from d8a0cf4 (verified = tip of u110-line-beta).
  Adds only max/sws/line_beta/c_half/ and tests/test_c_half.py. Beta venv made inside line_beta (.venv, ignored).
- Core: half_core.h/.c, C11, integer only, no heap, one caller-owned struct, double frame buffer. hal.h is
  declarations only. host_main.c reads a binary table written by c_half/table_to_bin.py (no CSV/decimal parsing in
  C; temperature to 0.01 degC and the 1 Hz edge made integer once in Python by the beta's own expressions).
  Settings reach the core via half_config_t, computed with the beta's own functions and carried in the bin header.
- Proof: 19 tests, frames + COBS stream identical byte for byte in every case (both filters; 100/250/500 per s;
  converter 1000; fault+drift+hum table; full scale; restart mid-frame; example CSV via CLI; odd Python chunking).
  Mutation check (C truncating division in place of floor) makes the full-scale case fail: the test sees it.
- Found: the three-stage correction overshoots (4.0 % of a single step; 1.158 x 2^23 in the test's repeated
  full-range steps; 1.017 x 2^23 for a channel held at +full from boot). Past the 24-bit field both sides wrap to
  the other sign. Python not changed, so C not either; for the owner (clamp before packing is the usual answer).
- Python half floats: none in the signal path; temperature int(round(t*100)), samples-per-frame at set-up,
  sample_centre_offset_s (logger only).
- Measured (PC): C core 35 ns per set (both halves), ~7000x real time; Python half ~370x; C ~19x faster. Core text
  3068 B (-O2) / 2568 B (-Os), x86-64. RAM per half 3424 / 5824 / 10624 B for 25 / 50 / 100 samples per frame.
  Ops ESTIMATE (model in measure.py): 4000/s, 250/s three-stage: mean 511 ops per set (2.0 M ops/s), worst set
  9862 (frame end, CRC).
- Field to counts: statement "core does not change with element type" true with three limits: counts_per_uT
  formula hard-wires the bridge form (Hall needs a formula change, not only constants); 16 channels fixed by the
  frame; digital-output parts change the meaning of the rate code and the edge latch.
- Full beta suite after the add: 72 passed (53 + 19), 3 slow deselected.
- Scans: idscan d8a0cf4..HEAD 0; scan_tree on committed files (git archive) 0. (scan_tree on the working folder
  hits a __pycache__ .pyc with the absolute path; ignored, never committed.)
- Reviewer (fresh agent, built from git archive in an empty folder): no blocking. Clean at strict flags, -O0..-O3,
  -fanalyzer, -m32; UBSan runtime not in this toolchain, trap mode used, no trap. 11 injected faults: 8 caught,
  2 missed (temperature field order, overflow bit), now covered by test_core.c. Minors documented (24-bit input
  precondition, edge must be handled before its push, buffers reused after restart, size wording).
- Tip f86978a. 20 tests in test_c_half.py pass. Scans 0 (idscan d8a0cf4..HEAD; scan_tree on git archive).
- Follow-up (owner's ruling, clamp at full scale): half.py and half_core.c clamp to -2^23..2^23-1 before packing;
  no health bit (link note gives all 16 bits a meaning; RAILED is an input level, not used) -> open point.
  Full suite incl. slow: 76 passed, 1 failed (test_position_within_10_mm_after_registration, the known 27.3 mm
  position FAIL). 77 = 56 base + 21 new; Kai's 55+1 is the base suite; my earlier 72 was "not slow" only.
