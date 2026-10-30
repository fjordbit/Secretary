# Open items

Standing list. The daily files in `log/` record what happened; this is what has
not happened yet. Reviewed at 08:00 with the daily entry.

Last reviewed: 2026-09-09.

---

## Before Friday — the in-person window closes

Stian travels back to Bergen on **Friday 11 September**. Anything that needs
people in the same building has three days, and Wednesday is already gone.

- [ ] **Spare-parts / after-sales conversation.** Did not happen Wednesday.
      **Preferably Thursday.** Questions ready at
      `Prosjekter/systems-integration/01_Spare_Parts_API_Questions.md`. Ask for a
      sample export and any API documentation in advance.
      *Timebox note below.*
- [ ] **Send the mail to Ramin.** Drafted at
      `inbox/drafts/2026-09-09_ramin_platform_questions.md`. He is back from
      Switzerland Thursday.
- [ ] **Twenty minutes with Ramin** to finish what Monday's meeting cut short —
      still not captured anywhere what was left open.
- [ ] **AI policy review.** Due this week. **Blocked:** the document is not on
      this machine and nobody has sent it. Chase whoever owns the draft.

## Logging → Maintenance

New strand, from the meeting of 10 September. Notes at
`Prosjekter/logging-maintenance/01_Concept_and_Open_Questions.md`.

- [ ] **Find the "Tosibox on steroids" product.** Name was not caught in the
      meeting. Needed: name, link, price. Ask whoever mentioned it — faster than
      guessing from the market.
- [ ] **Get the address-standardisation document** (PLC IO ↔ maintenance
      objects, POS numbering) and the copy held in the management system. Not on
      this machine.
- [ ] **Ramin's wire rope / fleet angle calculations** — where they live, what
      form.
- [ ] **Confirm EG Maintenance's ingestion interface.** API, file drop, database,
      agent. If there is no external ingestion path, the cloud half of the
      pipeline does not exist.
- [ ] **Measure the filter ratio.** Capture one real docking raw at 100 Hz,
      apply candidate deadbands offline, count what survives. Everything about
      transport and storage depends on this number and nobody has it.
- [ ] **Overload data** — currently a want, not a source. Establish whether the
      PLCs already record it.

## Waiting on someone else

- [ ] AI policy document — from whoever is drafting it.
- [ ] Ramin's answers: tenant AI features, hosting region, FEM package, 3ds Max,
      SD/SSD, where the VB app runs.
- [ ] Decks V1–V3, if they exist at all. Only V4 is known to.
- [ ] Meeting details: who, when, what is being decided.

## Build work — for a separate session, not for me

- [ ] **Revision viewer.** Spec complete at
      `Prosjekter/agentic/06_Revision_Tracking_Spec.md`.
- [ ] **Steel price feed.** Not yet specified. Small: fetch a current price from
      a public source, nothing more.

## MAx — show-and-tell, then API

Decided 2026-10-29 (see that day's log).

- [ ] **ADR: CLI providers on subscriptions for the demo phase.** Write it into
      `max/docs/decisions/` once U0 has landed. U0 may take number 0005.
- [ ] **Mail to Syncrolift: prepaid API accounts** (Anthropic + OpenAI), paid by
      the company, not reimbursed. Send it on the visit the week before
      20 November, after the demo. Draft it to `inbox/drafts/` before the visit.
- [ ] **Demo on that visit:** main GUI, the idea, the workspace. What has to
      work by then follows from that (U0 → U1-CLI → U4 → U5).
- [ ] **One home for the repos.** Today there are five copies: `fjordbit/max`, `fjordbit/SWS`,
      `MAx-Flow/SWS-Documentation`, local `D:/git/prosjekter.git`, and `publish/SWS`. Move to
      the MAx-Flow org, archive the fjordbit copies, and make publishing one automatic push
      (scan → push) instead of Kai pushing to two remotes. Raised 2026-10-30, not urgent.
- [ ] **Hosting** (separate task, later): run MAx locally on the tower, reach
      it from the phone. Not started; nobody has a plan yet.

## Paper

- [ ] Apply the section 5 rewording (`05_Section5_Cloud_Rewording.md`) and cut
      **rev5**. Relabel the front page as part of cutting it.
- [ ] Decide which HTML variant is canonical — styled or plain. The tracker
      needs one answer before it is built.
- [ ] Fill the placeholders before circulation: author, date, budget figures,
      allocation in days per week, gate thresholds N and X %.
- [ ] Decide item 16 of the assumptions review — whether to replace the customer
      name in the example prompt.

## Later — raised, not scheduled

- [ ] **Mail access for Kai.** Stian has approved mail to
      stian.krogstad@syncrolift.com; there is no mail tool yet.
- [ ] **Calendar access for Kai.** Nothing exists yet, so "keep the calendar
      clean" is currently advice rather than a service.
- [ ] The 08:00 daily entry does not happen on its own. It needs a scheduled
      job; none has been set up.

## Decided, so it stops being asked

- **Drafts and notes are in English.** Asked three times without an answer, so
  taken as settled: everything written so far — the paper, the briefs, the
  reviews — is English. Say the word and it changes.

---

## Timebox on the spare-parts job

Stian's read: probably not prioritised by them, but possibly straightforward,
maybe half a day, and worth it for the goodwill.

That judgement is reasonable and there is a real argument for it beyond
goodwill — he is new, and the people who own those systems are the same people
whose process documentation weeks 1–6 of project 02 depends on. Half a day spent
solving their problem buys standing with exactly the group he will need.

The risk is that **"half a day" is an estimate made before seeing the systems**,
and integration between two unknown systems is where that estimate usually
breaks. So, applying his own rule from CLAUDE.md:

**Gate:** have the conversation first. If afterwards it is not *clearly* half a
day, it becomes a written recommendation handed to whoever owns it — not his
build. Deciding that after the conversation is prudent; deciding it after three
days of work is not.

## Logging → Maintenance, settle in this order

From `Prosjekter/logging-maintenance/03_Logging_Rate_and_Storage.md`. The first
question governs all the others; answering them out of order wastes the work.

- [ ] **What is the fastest event we must not miss?** Not "how fast can we log".
      10 Hz is generous for running hours and load cycles; it may miss a snatch
      load entirely. Different answers buy very different systems.
- [ ] **How does data reach SQL today** — WinCC Tag Logging on an HMI, or
      something else? Currently unknown.
- [ ] **Count the tags per hoist**, then check what PowerTag and archive-tag
      licences the sites already hold. Small job, prices the whole approach.
- [ ] **How long must data be kept?** Months or decades. Decides SQL Server
      versus a time-series store, and that choice is cheap now, expensive later.
