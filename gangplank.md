# gangplank — U116 notes (principle drawings of the line and its timing)

- Worktree C:/Users/stian/Prosjekter-u116, branch u116-line-drawings from aa1eae5 (verified = tip of
  u109-transmitter-line). Adds only max/sws/transmitter/drawings/.
- Round folder C:/Users/stian/line_drawings_round_2026-11-20 (brief.md, models.yaml: cursor gpt-5.6-sol-xhigh only,
  the Sol pick used in earlier rounds). scan_tree on the folder 0 before sending. Run with --claude-login.
- Own arithmetic: drawings/line_drawings_check.py -> .json (stdlib). VF 0.60/0.66/0.78 assumed (record: ~0.66).
- Round 1: gpt-5.6-sol-xhigh answered (138 s); 6 SVGs; A drew Half 2B on 2A's cable -> corrected copy. Numbers all
  agree with own arithmetic. PNGs via headless Chrome (scratchpad topng.sh).
- Kai's extension (data flow, levels 0-4): round 2 with gpt-5.6-sol-max (newest/highest Sol in `agent models`),
  answered in 303 s; 11 SVGs + 6 pseudocode blocks. Corrected/readable copies: l0 (labels overlapped), l3a (edge
  latched at frame completion in half_core.c, not per line sample). Notes under pseudocode: wrong type -> wrong_half;
  logger smooths with mains-period mean. Found in code/settings: 125/s alternative does not fit 100 ms frame
  (settings.samples_per_frame raises); 4096 MB cap = 23 h for 4 halves at 178 MB/h.
- Existing pages not changed (adds only); counts made explicit in dataflow.md.
