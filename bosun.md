# Bosun -> Kai: U22 release check (u22-flow-driver @ 9e66432), 4 Nov 2026

**Verdict: GO.** No blocking item. Seven non-blocking items for Keelson, none needs a design change.

## What was checked (evidence)

1. **Hygiene: CONFIRMED.** `git diff --name-only main..u22-flow-driver | grep -v '^max/'` -> empty; no `.env`, `runs/`, `.vault` tracked (`git ls-tree -r u22-flow-driver`); only e-mail in added lines is `someone@example.invalid` (a test fixture). `git grep -i "max-private|identifiers.yaml"` -> report prose ("not read") and two tests writing a tmp `identifiers.yaml`; no content. Absolute `C:/Users/stian` paths: 4 files, all reports/docs (U21.md, U22.md "How to run"), none in code.
2. **Suite: CONFIRMED.** `python -m pytest -q` -> `544 passed, 5 skipped in 91.80s`, first run, no flake. `check_u21.py` -> `U21 check: all ok`. `max flow check` on the three saved charts -> `ok ... (0 warning(s))` each. `cmp` saved vs specimen: all three byte-identical.
3. **Conformance: CONFIRMED.** `Orchestrator._run`, `load_roles`, `Role`, `_tweak` absent (grep; `test_orchestrator.py:633` asserts); `roles.yaml` gone and nothing reads it; `SCHEMAS["tweak"]` gone; `ReviewPolicy` allows only `severity`, `default_severity` (`orchestrator.py:128`). Engine order is the data-edge level sort (`driver.py:200-223`), no role order. Every name-keyed branch found and judged: `driver.py:580-633` per `params.schema` (the §2.2 table is keyed on schema); `:733`, `:814-815` `_has_role("compliance")` (§2 gate row states it); `:51` per-rule `checking` wording (§2 "today's lines"); `:528` judge diff (§4.3); `:701` `msg:material` packing (§2 context row). No `if role ==` on a role name. `blocked` as a run end only at `:819` (unwired block-power gate, §4.4) and `:993` (see item 5 below). Chart `attempts` is the cap (`:825`), no policy ceiling. Boundary: `_ask` calls only `boundary.complete` (`orchestrator.py:422`), tool loop limited to wired specs (`:419,459`); `Boundary.complete` masks messages, system, tool descriptions/parameters, response schema (`boundary.py:149-164`); bridge masks `tools/list` and results (`mcp_bridge.py:98-99,132`). CLI: `--tools ""`, `--allowedTools` = bridge tools only (`claude_cli.py:72-76`), `MAX_MCP_TOOLS` = wired tools (`_cli.py:194`). `can: spawn` in no chart; schema refuses it (check_u21 ok line). Done-when spot-check: 13 lines read against their sections; 10 hold, 3 miscite (item 4).
4. **WYSIWYG on the real tape: CONFIRMED.** Scratch replay with `tests.test_wysiwyg.log_maps_onto_chart` on `20261104-132842-0ec252` (chart.json + log.jsonl, read-only): 100 events, every one resolves; 7 agent firings = 7 `model.call`; one `tool.call sws.fibre_load` by tool-caller, wired; `run.end needs_human`. No `settings` map in its `preflight` (run predates milestone 2; expected).
5. **Studio: CONFIRMED.** Served on 8798: `/api/runs` lists the run; `/log?from=0` 100 events, `flow` line names `max_core/flows/max/max-default-loop.chart.json`; `/api/runs/<id>/chart` returns the run's own chart (25 blocks, 51 edges), not max-agentlive; `/api/flows` three flows, `refused: [] warned: []`; `/api/palette` = schema params; `/api/zoom?block=writer&run=<id>` returns prompt text (1938 chars), rules, tools, boundary; `engine: {}` because that run has no settings map. Server stopped (venv python + its base-interpreter child; nothing else on 8798).
6. **Security: CONFIRMED.** `HOST = "127.0.0.1"` (`studio.py:63`); only `do_GET`/`do_HEAD` (POST/PUT -> 501); `/api/zoom?flow=../..` -> 404; `/max_core/driver.py` -> 404; zoom reads only under `max_core/agents/` (`studio.py:270`). Vault `load`, `save`, `token_for` all under `FileLock` (`boundary.py:36,68,79`). No `shell=True` in the repo; no network import but `urllib.parse`.
7. **Report: partly.** Dates 4 Nov 2026; `[UNVERIFIED]` on the two live runs not done, honest. **1337 prose words (1430 with code)**, over 1200.

## Non-blocking (Keelson)

1. `tasks/reports/U22.md`: over 1200 words; no "Hours" section (builder.md), no "checked before creating" line (hard rule 7), no section titled "Conformance to flow-driver.md" with met/departed/open per claim (process rule 5; the Done-when lines carry the citations but not the status).
2. `orchestrator.py:101` docstring says "decision E, 5 Nov 2026"; should be 4 Nov.
3. Three Done-when citations are loose: "hand-off endpoints resolve by block id (§10)" is §12 / ADR "What it does not change"; "end panel names the ladder from its own note (§10)" is not in the design (Studio detail, say so); "/api/flows shows each saved flow's save check (§8)" is a read-only addition, §8 names save and preflight only.
4. `driver.py:993`: checkpoint ends `blocked` on a verdict other than pass/needs_human. R6's checker returns only those two, so unreachable today, but §4.4 says `blocked` is for R1/R2 gates only. Drop it or raise.
5. `U22.md` "How to run it" and U21.md §13 carry `C:/Users/stian/...` paths in a repo two managers watch; use a relative path or `%PY%` only.
6. Live run 1 shows `settings` absent; the second live run (decision A) is the first tape with the map and the `prompt.*` hashes; say so in the report.
7. Zoom for a run without settings returns `engine: {}` silently; a one-word "no settings map (run before milestone 2)" would match the Studio's chart fallback message.

## Not checked

Browser rendering (API only); §3 round/latch semantics line by line (trusted to the scripted tests); `codex_cli.py` internals; prompt-file wording against §2.1; review-policy layer values; the two live runs not yet made.

— Bosun
