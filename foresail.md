# foresail — U108 notes (data path, blind round, traffic)

- Worktree C:/Users/stian/Prosjekter-u108, branch u108-data-path from 1bd304c (= main, verified); merged
  u106-groove-plots (d112319) cleanly as b2889f4. Commit 8c3218c adds only max/sws/data-path/ (21 files).
- Three blind agents (opus) got the brief text only; answers saved unchanged as answers/answer_1..3.md (they
  arrived as hand-back text; written out de-indented, signatures kept).
- Kai's mid-run correction applied: two converters per half (owner), digital temperature; traffic.py has 16
  signal channels only, temperatures as header values read once a second; comparison table has the
  "converters per half" row with the specification marked out of date; note says once the brief said three.
- traffic.py: standard library, named constants; batched 100 ms frames (23 B header from the link note, CRC-32,
  COBS, 8N1), per-sample framing as the link note's case, polled 2-wire RS-485 for shared lines, MQTT/TCP and UDP
  Ethernet overhead with segmentation, storage as raw frames and as 4-byte values.
- Answer 1 error: "13 000 channels, 3.3 M samples/s" for B (64 ch x 204); right is 3 264 / 816 000.
- Figures: plotstandard/figkit imported from ../3d/groove_plots unchanged; all checks pass. T1 slide cut at
  350 S/s so figkit's band labels clear the curves. figkit places hspan labels just under the band (cannot move
  without changing figkit). T3 1 Gbit/s not drawable on a linear axis with the data visible: stated in the note.
- Falsifier (opus): arithmetic holds; one blocking (agent name in a table header) and 17 minor; all fixed except
  slide label position (figkit) and the spec filename date (a path). No second pass (blocking fix trivial).
- Scans: idscan 1bd304c..HEAD 0 hits; scan_tree on data-path 0. No push, no merge, no export.
- Not verified: the cable rule (from memory), converter native lowest rate, logger format.
