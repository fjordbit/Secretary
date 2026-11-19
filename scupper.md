# Scupper — U33 (peer-to-peer review round on one command), 8 Nov 2026

Builder for U33. Worktree C:/Users/stian/Prosjekter-u33 (max/ inside, same layout as u32), branch
u33-review-round from main 130203f. (First `worktree add` went to Prosjekter-u33/max, which nests the
repo one level too deep; removed and re-added at Prosjekter-u33 before any file was written.)

Rests on (rule 10): brief kai.md "U33" l.1139-1188 and the U32/U33 addendum l.1190+ (addendum wins);
review policy 8 Nov in the brief (company / Siemens / sub-suppliers may be named, personal and customer
names never); ADR 0011 + flow/chart.schema.json (output shape only, no chart built); ADR 0006 and
max_core/providers/claude_cli.py, codex_cli.py (safety flags reused); U31.md l.31, 65, 76, 83, 90-92, 102
(pack and masking); grok_brief_2026-11-08.md (the brief the real round sends). No SWS record row is
touched: U33 builds tooling, it does not change a spec or register value.

Rules held: identifiers.yaml read only by scripts that print counts; no value in notes or output.
Dry run only with a ten-line dummy from an empty scratchpad folder. No `agent login`. No keys.

— Scupper

## 8 Nov ~15:05 — built, dry run done, verifier running

- Cursor CLI installed (public installer, 2026.11.05); `agent status` = not logged in (owner's step).
- Private tools in max-private/tools: build_mask_map, mask_lib, mask_tree, unmask_text, scan_tree. Map: 15 entries
  (personal 5 / 9 variants, customer 1, sites 3, drawings 2, projects 3, user path 1). The owner's full name is not on
  the private list; the builder takes it from the secretary rules file by pattern. Values never printed.
- Scan gate is whole word (case-insensitive); the U31 pack: 0 whole-word, 248 substring hits, all inside longer
  words/numbers/base64 (checked by neighbour class only).
- Dry run: Claude CLI opus/sonnet/fable ok, Codex ok (gpt-6.1-sol), Cursor x4 not logged in, xAI no key, Claude API
  path not exercised (no key). Work folders held only input.md.
- Departure (in report): masked answers in repo, unmasked only in max-private/reviews (brief contradicts itself).
- Bash heredocs mangled backslashes and quotes twice; used the Write/Edit tools for those files.

— Scupper

## 8 Nov ~15:15 — committed 7ab3dab on u33-review-round (no merge, no push)

Verifier-U33: PASS on all checks; one finding blocking the real round (surname / mail form / shared first name /
genitive not masked or scanned) fixed in the private tools, map rebuilt (personal 5 entries / 13 variants), pack
rescanned to 0 whole-word hits, dry run repeated with the same results. Report: max/tasks/reports/U33.md.

— Scupper
