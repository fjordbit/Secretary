# crowsnest

## 2026-11-20 — started
- Unit / branch: U118 / u118-hmi-round (C:/Users/stian/Prosjekter-u118), base 5a8dcc6 (tip of main, verified)
- Round folder: C:/Users/stian/hmi_round_2026-11-20/ (brief.md, models.yaml); brief scan_tree 0 hits before sending
- Models: Opus, Grok 4.5 high, GPT-5.3 Codex high (Cursor), GPT-5.6 Sol high (Cursor)

## 2026-11-20 — committed
- Commit: b528d89 on u118-hmi-round — max/sws/hmi/round_1/ (brief, 4 answers, 4 clean mock-ups, PNGs, hmi_round_1.md); files added only
- Checks: scan_tree 0 (brief before sending, answers before copying, folder before commit); idscan 5a8dcc6..HEAD 0; checker pass after fixes (second pass)
- Ready for Kai's check: yes. No merge, push or export.

## 2026-11-20 — follow-up: Grok slot rerun (owner: 4.5 is old)
- Cause: pick "grok" took the first listed name with the word, cursor-grok-4.5-high.
- Listed through model_round.cursor_models (`agent models`), Grok names: cursor-grok-4.5-low, -low-fast, -medium, -medium-fast, -high, -high-fast; cursor-grok-4.6-low, -low-fast, -medium, -medium-fast, -high, -high-fast, -xhigh, -xhigh-fast; grok-4.7-low, -low-fast, -medium, -medium-fast, -high, -high-fast, -xhigh, -xhigh-fast.
- Codex names: gpt-5.3-codex-low, -low-fast, gpt-5.3-codex, -fast, -high, -high-fast, -xhigh, -xhigh-fast. No newer Codex than 5.3.
- Sol names: gpt-5.6-sol-none, -low, -medium, -high, -xhigh, -max (each with -fast). 5.6 is the only Sol; -xhigh and -max are higher reasoning levels than the -high that answered.
- Taken: grok-4.7-xhigh (newest version, highest level, not fast), pinned with model: in models_grok.yaml.
