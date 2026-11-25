# gunport — U125 (prototype recording, newest Codex): STOPPED at item 2

Main tip verified b5478a7 (from Prosjekter-u05). No worktree made, no branch, no commit, nothing sent.

Item 1 (checks before sending):
- notes.txt read in full; scan_tree on a copy: 0 hits. No personal, customer or site name in it.
- Brief (brief.md) not written yet, so not scanned (item 3 comes after the stop).
- Headers: 30 files, two header variants only (one per logger), identical across all 15 folders. They carry:
  file type TOA5, station name "VOLT 100", model "VOLT 116", serial 6111 or 7686, OS "VOLT100.Std.06.01" /
  "...06.03", empty program name and signature, table "data"; then channel names brfull1-6, 9-14, units mV/V.
  Nothing beyond logger model, serial, OS and channel names.

Item 2 (how files reach the model) — the STOP:
- model_round.py puts the brief and --files into ONE text prompt (input.md). Default limits 200 KB per file,
  400 KB total; non-text or over-limit files are listed as "not sent".
- Cursor backend (where Codex is offered): `--mode ask` (read-only, no commands), workspace = an empty folder
  holding only input.md; the preamble tells the model "do not run commands ... work from this text only".
- Codex CLI backend: `-s read-only`, shell_tool and unified_exec disabled. Also no code execution.
- So the model cannot be given a data folder and cannot compute. Text in the prompt only.
- The data: 30 files, 1.16 MB to 87.8 MB each, 229 MB total. Every single file is over the 200 KB file limit;
  at default limits only the brief would go. Raising the limits does not help: 229 MB cannot sit in one prompt
  and the model still runs no code.

Model that would have run: gpt-5.3-codex-xhigh (Cursor `agent models` today; newest Codex listed is 5.3,
highest level "Extra High"; "-fast" excluded).

What could be sent instead (options for Kai / the owner; I chose none):
 a) notes.txt + headers + per-file summary statistics computed locally (means, rms per band, etc.) — but then
    the figures are ours, and Codex only reads them; not an independent analysis of the raw data.
 b) Decimated / excerpted raw text: e.g. short windows of each run and steady file (steady1 runs 8.65 MB in about
    540 s = about 16 kB per second per logger), within 400 KB total that is 400 / 16 = about 25 s of data
    overall across all 30 files: far too little for steady2 noise bands down to 0.01 Hz.
 c) A change to the round tool (or a separate route) that lets Codex run code in a folder with a copy of the
    data (workspace-write sandbox, shell on, no network). Not allowed for me: outside models go only through
    the tool as it stands.

No API key read. No background work running. Scratch copy of notes.txt in the session scratchpad only.

— gunport
