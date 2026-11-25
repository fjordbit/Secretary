# gammon — U130 builder notes

## 2026-11-25 — started
- Unit / branch: U130 / u130-prototype-data-fable (C:/Users/stian/Prosjekter-u130), from b5478a7 (main tip verified b5478a7).
- Work folder: C:/Users/stian/prototype_data_round_fable_2026-11-25/

## 2026-11-25 14:47 — run started
- Data copied to work folder; 31 files, sha256 of copy = original (all match).
- venv in work folder (numpy 2.5.5, scipy 1.18.1, pandas 3.1.1, matplotlib 3.11.2) made from Prosjekter-u05 max/.venv python.
- Work folder mapped to V: with subst (user name kept out of the model's paths and the brief); removed after the run.
- Limits: project settings V:/.claude/settings.json (defaultMode dontAsk; deny Read/Edit on max-private, secretary, agent-notes, Prosjekter*, prototype_data_round_2026-11-25; deny WebFetch, WebSearch, Agent; bypass disabled). Program run with --bare (auth strictly the API key, no CLAUDE.md/hooks/memory), --setting-sources project, --tools Read,Edit,Bash, --allowedTools Bash Read(./**) Edit(./**) (the settings file's allow list is ignored because the folder is not trusted; I did not touch user-level config to trust it), --permission-mode dontAsk, --effort max, --max-budget-usd 100, --no-session-persistence, env -i with a short whitelist plus ANTHROPIC_API_KEY.
- Probes (3 runs, model claude-fable-5-2, apiKeySource ANTHROPIC_API_KEY): Read denied in all five denied folders incl. an existing file; Read outside cwd (Downloads) denied; Edit outside denied; Edit/Bash inside work; WebFetch/Glob/Grep/Write not present in the tool set. Shell commands are NOT confined by the deny rules.
- Brief sha256 7e958e9b...56d88, scan_tree 0 (brief + notes.txt).
