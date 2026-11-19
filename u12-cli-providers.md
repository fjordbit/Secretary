# U12 cli-providers — Tether

## 2026-11-02 — started
- Unit / branch: U12 / u12-cli-providers (C:/Users/stian/Prosjekter-u12/max), at main 91897db
- Name: Tether
- Plan: ADR 0006, TASKS edit, claude_cli.py + codex_cli.py, backend switch, MCP bridge, tests, report.

— Tether

## 2026-11-02 — built, in QC
- ADR 0006, TASKS edit, claude_cli.py, codex_cli.py, _cli.py, mcp_bridge.py, tests done.
- 187 passed / 4 skipped (full suite); live_cli 4/4 passed on both subscriptions.
- base.py: only registry() body changed (the brief requires the switch there). Flagged in the report.
- qc-falsifier running. Not committed yet.

— Tether

## 2026-11-02 — committed
- Unit / branch: U12 / u12-cli-providers (C:/Users/stian/Prosjekter-u12/max)
- Commit: 6dce2a4 — U12 beta backend on subscription CLIs (ADR 0006)
- Tests: 192 passed, 4 skipped; live_cli 4/4 passed (Claude Code + Codex, subscription auth)
- qc-falsifier: pass 1 had 1 blocking (tools ran unlogged without a run log), fixed; pass 2 no blocking findings.
- Ready for Kai's check: yes
- Needs Stian: confirm ADR 0006 (incl. the base.py registry() edit and changed tool-use semantics);
  confirm "training on chats" is off on Claude and ChatGPT plans for all three users.
- Not pushed, not merged. Stopping.

— Tether
