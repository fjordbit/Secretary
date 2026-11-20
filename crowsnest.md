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
- Grok rerun: grok-4.7-xhigh answered (1478 s); scan_tree 0; mock-up clean; committed ed8ac2a (4.5 files git rm'd, note rewritten, bending-cycles line corrected per owner: shared server). Checker: 1 blocking (a "Grok alone" item Opus also had), fixed; 2 minor fixed.
- Codex: 5.3 is the newest Codex offered; kept. Full list: agent-notes/models_offered_2026-11-20.md.

## 2026-11-20 — round 2 (Opus, OpenBridge, permanent findings)
- OpenBridge read from its public repo (github.com/Ocean-Industries-Concept-Lab/openbridge-webcomponents, develop): LICENSE.txt = AGPL-3.0-only for 180 days per version, then also Apache-2.0; commercial licence for JIP members before that. Tokens from packages/openbridge-webcomponents/src/palettes/variables.css (day/dusk/night/bright), Noto Sans, type scale from IMPLEMENTATION_GUIDELINES.md.
- Brief: C:/Users/stian/hmi_round2_2026-11-20/brief.md; no cut-off option (owner's correction applied before sending); owner's two dismissal examples in; bending cycles via shared server. Sent to claude-opus-5-5 with round-1 answer + mock-up.
- Round 2 committed c1629d4 (max/sws/hmi/round_2/). Opus answered; scan_tree 0; mock-up clean; all 64 colour values match the verified tokens. Checker: pass, 6 minor fixed (incl. licence sentence reworded as my reading, not legal advice). Opus raised re-termination as an owner decision: marked not applicable in the note. idscan 5a8dcc6..HEAD 0. No merge, push or export.
