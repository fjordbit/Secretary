# winch — U82 notes (model-round: way of working with sub-agents)

Started 16 Nov. Repo C:/Users/stian/model-round, main, local commits only (author model-round <model-round@localhost>). Not pushed.

## Docs checked (code.claude.com, 16 Nov)
- "Create custom subagents": `.claude/agents/*.md`, YAML frontmatter + body = system prompt; required `name`, `description`;
  `tools` comma string or YAML list (omitted = inherits all); `model` sonnet/opus/haiku/fable/full id/inherit (omitted = main
  model); delegation automatic by description, by name in natural language, or `@agent-<name>`; subagents may nest unless
  `Agent` is left out of tools; new `agents` dir needs a session restart.
- "Extend Claude with skills": `.claude/skills/<name>/SKILL.md`; fields name, description, argument-hint, allowed-tools
  (space/comma string or list), disable-model-invocation (recommended true for side-effect workflows), $ARGUMENTS.

## Built
- .claude/agents: builder (Read Glob Grep Write Edit Bash, no Agent), cold-reader, falsifier, domain-reviewer (Read Glob Grep).
- templates/brief.md, templates/handback.md; .claude/skills/brief-task/SKILL.md (disable-model-invocation: true);
  briefs/ in .gitignore; CLAUDE.md second part (55 lines total); README section; examples/sensor-comparison (brief + facts).

## Proof
- pytest 15 passed.
- Clean clone, `claude -p` on login (apiKeySource none): init lists agents builder, cold-reader, domain-reviewer, falsifier;
  skills brief-task, synthesize-round. cold-reader invoked on facts.md -> MOSTLY CLEAR; fixed wiring + divider resistor.
- Worked example end to end in clean clone: builder wrote comparison.md; falsifier FAIL (37 claims, 26 OK, 1 WRONG,
  5 NO SOURCE, 5 CANNOT CHECK because it was not given the brief) -> example now gives falsifier the brief too.
- scan_tree on git archive of HEAD: 19 files, 0 hits. On the full clone: hits only in clone's .git (local origin path,
  made by cloning; not in commits). git grep names/paths: 0. Commit authors/messages clean.
- /brief-task in `claude -p` (clean clone): skill loads and asks question 1 of 3 first, writes nothing before answers.
- Cold start (fresh sub-agent, README + CLAUDE.md only): got the steps right; gaps fixed in bc6c4cd (where results go,
  yes before builder, which reviewer when, fix loop, tests). Not re-read after the fix. Tip bc6c4cd, CLAUDE.md 63 lines.
- Not verified: /brief-task run interactively (disable-model-invocation; needs a human to answer); domain-reviewer and
  builder in a real non-example task; example re-run after the brief fix.
