# crossjack — U129 (prototype recording, Codex through the Cursor CLI): STOPPED at confinement

Main tip b5478a7 verified (Prosjekter-u05). Worktree C:/Users/stian/Prosjekter-u128 on u128-prototype-data-codex
at b5478a7, clean, no commits; none made (nothing to commit). Data copy in the work folder: 31 files, md5
identical to the original. No brief written, no data sent, the work folder untouched.

## The program
Cursor CLI `agent` 2026.11.19-f005e9d (LOCALAPPDATA/cursor-agent), logged in (same login as the round tool).
Newest Codex offered: gpt-5.3-codex-xhigh ("Codex 5.3 Extra High"; -fast excluded). Used only for the probes.
User-level config (read, not changed; security keys unchanged after the probes): approvalMode allowlist,
allow Shell(ls), sandbox mode disabled. The program rewrote its own privacy-cache timestamp there.

## Probes
Probe folder C:/Users/stian/u129_probe_parent/probe (dummy.txt + .cursor/cli.json), mapped to P:, its parent
to Q: (so no user path in the prompt). Project settings: allow Shell(python), Read(P:/**), Write(P:/**);
deny Read(C:/**), Write(C:/**), Read(Q:/**), Write(Q:/**), Shell(curl|powershell|ls|dir|type|cmd).
Run as node.exe + index.js directly (agent.cmd cut a multi-line prompt to its first line: run B was void).
- A, no model: `--sandbox enabled` -> exit 1, "Sandbox mode is enabled but not available on this system.
  Sandbox requires macOS or Linux." The bundle says the same: on win32 the helper "only provides network
  proxy, not filesystem isolation" and is reported unsupported.
- C, model in the loop, `--sandbox disabled` (allowlist mode, no --force), stream-json tool events:
  1 file tool read C:/Windows/win.ini: READ (deny Read(C:/**) did not stop it)
  2 file tool write Q:/out: "Edit rejected" (program)
  3 python reads win.ini: ran, content returned
  4 python writes Q:/out/shell_write.txt: ran, file exists on disk
  5 python urllib https://example.com: 200
  6 python lists the parent: ['out', 'probe']
  7 cmd /c type, 8 curl: "Command blocked by permissions configuration" (name deny-list only)
  9 WebFetch tool: "User Rejected" (program, non-interactive)
Every refusal above came from the program; the model attempted all nine.

## Result: none of the three limits hold
Shell commands run unsandboxed on Windows; an allowed `python` (needed for the analysis) reads, writes and
reaches the network anywhere. Rules match command names only. The file-tool read deny did not hold either.
Needed instead: a separate Windows account or machine holding only the work folder (and its own Cursor login),
or WSL/Linux where the sandbox exists — for Kai and the owner to decide; I chose none.

## Left behind
C:/Users/stian/u129_probe_parent/ (probe folder, out/shell_write.txt from probe 4). Cursor's own state:
~/.cursor/chats (two chats), ~/.cursor/projects/P/ (trust marker, transcript). subst P: and Q: removed.
No API key read. No background work running.

— crossjack
