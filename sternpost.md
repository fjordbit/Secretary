# sternpost — U78 notes (model round as a standalone repo)

Started 16 Nov. Repo: C:/Users/stian/model-round (local only, branch main, no remote).
Commit identity in the new repo: neutral (`model-round <model-round@localhost>`), so no account name rides in.

## Built
- model_round.py (single script, PyYAML only), models.yaml (claude default; cursor pick "gpt high",
  "gemini high"; codex off), examples/weather-station/brief.md, .claude/skills/synthesize-round/SKILL.md,
  CLAUDE.md, README.md, tests/ (15, CLIs faked), requirements*.txt, .gitignore (rounds/, .venv).
- Carried over: empty folder per backend with input.md only, git-tree refusal, Claude flags/env (no tools,
  --restricted, no CLAUDE.md/memory/session/skills), Cursor ask mode + --workspace, Codex read-only flag set,
  child env stripped of API routing vars, ~ for home in records, header block + round.json, --list/--dry-run/--only.
- Dropped: masking + private tools, pack globs/NOT_SENT list, default paths, preambles, tier notes, xAI and
  Anthropic-SDK paths (Claude goes through Claude Code only; key passes through unless --claude-login).
- New: --files with per-file/total limits, sent / not_sent (with reason) in each header; key_rejected status with
  --claude-login fix; not_installed / not_logged_in reported with the one fix command; redaction of key values;
  pick: = all words must match, -fast skipped.

## Proof
- pytest 15 passed. --list and --dry-run real here (Cursor CLI + Claude Code login): 3/3 DRY-RUN-OK.
- Without --claude-login, the env key is rejected -> status key_rejected with the flag named (2 s).
- Real run of the example brief (--claude-login): 3/3 ok; /synthesize-round run from PowerShell wrote
  synthesis.md (19 unsourced claims, 8 disagreements). From Git Bash the skill fails because Git Bash rewrites
  the leading "/" into a path. The README now says to use PowerShell or CMD.
- Cold start (fresh subagent, fresh clone, new venv, README only): reached the dry run; Cursor 2/2 ok; Claude
  key_rejected until it applied the README's --claude-login fix. Fixed in dc3f4c3 and b1325d1 the places where
  it had to guess: --list "ready" does not test the key; --claude-login up front; re-running one backend; the -2
  folder suffix; the byte gap.
- Not verified: the Python winget ID on a clean machine; the Codex install command on Windows (row off by
  default); the execution-policy row; a machine without the CLIs (faked in tests only).
- Tip b1325d1. No remote. Prosjekter-u05 untouched. rounds/ (gitignored) scans 0.
- scan_tree on a clean clone: 0 hits (the working folder's .venv/__pycache__ have hits; gitignored, not in repo).
