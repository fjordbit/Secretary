#!/usr/bin/env bash
# Live run of the U22 default loop, recorded and guarded.
# Recording: console.log (timestamped stdout+stderr) + MAx's own runs/<id>/log.jsonl (the replayable tape).
# Guard: 30 min wall clock (timeout) and a watcher that kills the run past 40 model.call events.
set -u
OUT="C:/Users/stian/AppData/Local/Temp/claude/C--Users-stian-secretary/f9fb39d7-f149-451c-adb1-e423fb8c9455/scratchpad/live_run_1"
MAX="C:/Users/stian/Prosjekter-u22/max"
PY="C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python"
CAP_CALLS=40
CAP_SECS=1800
cd "$MAX" || exit 2
ls runs > "$OUT/runs_before.txt"
date +"%F %T start" > "$OUT/watch.log"

( timeout $CAP_SECS "$PY" -u -m max_core.cli run \
    "Can SWS share the PROFINET fibre on [PROJECT] side A without breaking the FMECA?" \
    --flow max-default-loop --docs tests/fixtures/fibre-demo --fmeca-scope "SWS network" 2>&1 \
  | while IFS= read -r line; do printf '%s %s\n' "$(date +%T)" "$line"; done > "$OUT/console.log"
  echo "exit=${PIPESTATUS[0]}" > "$OUT/exit.txt" ) &
RUNNER=$!

# watcher: newest run dir that is not in runs_before
while kill -0 $RUNNER 2>/dev/null; do
  sleep 20
  newdir=""
  for d in runs/*/; do
    d=${d%/}; n=${d#runs/}
    grep -qx "$n" "$OUT/runs_before.txt" || newdir="$d"
  done
  if [ -n "$newdir" ] && [ -f "$newdir/log.jsonl" ]; then
    calls=$(grep -c '"model.call"' "$newdir/log.jsonl")
    tools=$(grep -c '"tool.call"' "$newdir/log.jsonl")
    lines=$(wc -l < "$newdir/log.jsonl")
    echo "$(date +%T) run=$newdir events=$lines model.call=$calls tool.call=$tools" >> "$OUT/watch.log"
    echo "$newdir" > "$OUT/run_dir.txt"
    if [ "$calls" -gt "$CAP_CALLS" ]; then
      echo "$(date +%T) CAP HIT ($calls > $CAP_CALLS): killing python" >> "$OUT/watch.log"
      powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { \$_.CommandLine -like '*max_core.cli run*' -or \$_.CommandLine -like '*max-exchange*' } | ForEach-Object { Stop-Process -Id \$_.ProcessId -Force }" >/dev/null 2>&1
      echo "exit=killed-by-cap" > "$OUT/exit.txt"
      break
    fi
  else
    echo "$(date +%T) no run dir yet" >> "$OUT/watch.log"
  fi
done
wait $RUNNER 2>/dev/null
date +"%F %T end" >> "$OUT/watch.log"
cat "$OUT/exit.txt" 2>/dev/null
