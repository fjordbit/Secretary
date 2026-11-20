# trunnel — U123 sensing-element round: two more answers (Fable 5.2 on the API key, GPT-5.6 Sol max) (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u122, branch u122-rerun-rounds, tip 7fdcfbf checked, tree clean. Start 13:35.
- Models offered (`agent models`, re-listed now): newest Sol is gpt-5.6-sol (only 5.6), levels none/low/medium/high/
  xhigh/max (+ -fast) -> `gpt-5.6-sol-max`. Fable: `claude-fable-5-2` through model_round.py's claude backend
  (Claude Code `claude -p --model claude-fable-5-2`). The tool passes no effort flag for Claude (Claude Code has
  `--effort`, the tool does not use it; it also strips CLAUDE_EFFORT), so Fable ran at the Claude Code default.
- Round folder C:/Users/stian/element_round_2026-11-20_u123/ (brief.md copied from the 19 Nov as-sent copy, SHA-256
  A2FC2942... equal; models.yaml names both exactly). scan_tree 0 before sending.
- Key: loaded as ANTHROPIC_API_KEY inside one Bash command for the claude child only (`tr -d '\r\n' < key file`),
  no echo, no set -x. `--list` under the key: "claude-fable-5-2 ready, uses ANTHROPIC_API_KEY"; run without
  --claude-login, so the tool ran on the key. round.json model_used (from Claude Code's modelUsage) =
  claude-fable-5-2; no fallback flag passed.
- Runs: Fable ok 232 s; Sol ok 270 s; both input_sha256 f6d1d639... = 19 Nov. The two runs started in the same second
  and shared one temp work base (separate work folders inside); both answered, no effect.
- Front matter: home written as ~, no user name, account id or key fragment. scan_tree 0 on both answer folders
  before copying. Key fragment (first 12 chars) count in round folder + model-round/rounds: 0.
- Sheets (fresh sheet-reading subagent, part numbers only, PDFs read via fitz and deleted): key finds — TMAG5253
  (Fable's radial baseline, "in plane, fairly sure") senses perpendicular to the package top: a direction error;
  ALT025-10E (Sol) in plane, ±10 mT linear (Sol ±15); TAS2143-AAAB (Sol, unsure) no sheet found; A1393 3.0 V,
  50 mV/mT, 3.2 mA, DFN not SOT-23W, direction/range not on sheet; MLX91208/91216 in plane, 5 V, 12 mA;
  HMC1021 ±0.6 mT (now read: Opus +1 -> 18/2). Tallies: Fable 19/2 after falsifier fixes (1 direction), Sol 11/4 (+1 part not found).
- Five-way: 5 mm 5/5; pairing 5/5 by kind; Hall 3 (Opus, Fable, Sol) vs TMR 2 (Grok, Codex), all on the strong-field
  test; drift: no sheet figure in any; liner stainless Opus+Fable, polymer Grok+Sol, Codex either. New: sensing layer
  ~1 mm off mid-plane / board offset; coverage between elements; keeper bar.
- parts.yaml L01 line+value now name which answers propose stainless (+ ref to note l.335); E10, A03 unchanged.
  render --check 153 rows 0 problems; parts table, parts.html, results.html rebuilt; results --check ok;
  test_sws_results 26 passed (solver venv). results.html line "All three outside answers put ... 5 mm" (builder
  text) now understates (five of five): listed, builder not changed.
- Commit 18d8776. idscan (staged vs 7fdcfbf) 0 on 826 added lines; scan_tree 0; key fragment 0 in worktree,
  round folder, model-round, branch history.
- Falsifier (fresh, files only): brief byte-identical, counts reproduce, nothing picked, no key-looking string.
  1 blocking fixed: Sol never called eddy currents negligible -> 4 of 5 (Sol a crude estimate it doubts). Minor
  fixed: Fable tally 19/2 (TMAG5170 Z noise judged as Opus'; "any axis" and HMC family not counted); Opus range 5;
  Fable's tilt figure moved off the TMR row; TMR2501/2505 worded; pass-table title; Hall reason not put on Sol;
  "as it says" removed; "three of five" -> all five give a per-table pass figure. L01 ref line 337.
- Tip eb0e658. idscan 7fdcfbf..HEAD 0 (832 added lines); scan_tree 0; render --check 0 problems; results --check ok;
  test_sws_results 26 passed. Key fragment count 0 (branch history, notes, repo sws, round folder, model-round).
- Not done: results.html builder text "All three outside answers ... 5 mm" not changed (outside the brief; now five
  of five). No merge, push or export. End ~15:20. -- trunnel
