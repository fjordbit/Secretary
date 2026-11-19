# Buoy — U20 preflight / max doctor / Studio lamps

- 22:13 start. Worktree C:/Users/stian/Prosjekter-u20 on u20-preflight from eabaa39. Timebox 3.5 h (to ~01:45).

— Buoy

- 22:30 Stages 1-3 built (max_core/preflight.py, `max run` preflight + --skip-preflight, `max doctor`, ADR 0010 for the new `preflight` event, TRY_IT Tier 3). Kai's scope addition in: MAX_CLAUDE_CONFIG_DIR -> CLAUDE_CONFIG_DIR, MAX_CODEX_HOME -> CODEX_HOME (both verified on this machine: an empty folder makes both status commands say not logged in). pytest 455 passed / 5 skipped (was 426/5). Real `max doctor`: both GREEN. Account e-mail shown by doctor, kept out of log.jsonl. QC next, then Studio lamps.

— Buoy

- 22:45 Stages 1-3 committed: d327d0c (preflight + account dirs), 685ef68 (max run preflight, ADR 0010), 08c7dbe (max doctor, TRY_IT Tier 3, TASKS U20). QC on 1-3: no blocking; 3 non-blocking fixed before commit.
- Stage 4 (Studio lamps, Play gate, Re-check, scripted in --demo/--rehearse) built and tested: 468 passed / 5 skipped. Real-server headless check: both green on this machine; Codex amber + Play off with MAX_CODEX_HOME on an empty folder. Report tasks/reports/U20.md written. Final QC (fable) running.

— Buoy

- 22:48 Done. 4518cb5 (Studio lamps), bad2570 (report). Final QC (fable): no blocking; non-blocking handled. Not pushed, not merged. Worktree clean. Open questions are in tasks/reports/U20.md.

— Buoy

- 23:00 Kai's final-QC fixes landed (Claude api_key login AMBER, finished-run replay ungated, .env.example, report). 472 passed / 5 skipped. qc-falsifier: no blocking. Not pushed, not merged.

— Buoy
