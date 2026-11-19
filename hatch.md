# hatch — U80 Vessel Library (16 Nov)

- Worktree C:/Users/stian/Prosjekter-u80, branch u80-vessel-library from 5f415b6.
- Read: the 5 Oct mail; agentic/00, 01, 04, 07; functional spec (grep for vessel/hosting/users/security);
  logging-maintenance/ and systems-integration/ notes; people/ramin.md, carl-herland.md; CAD memory; log 16 Nov.
- Record on company IT: only 3DEXPERIENCE on the Cloud (CATIA/PLM). Silent on: identity/SSO, file storage,
  backup, ERP/project-number system, M365/SharePoint, server/cloud subscription. Written as "not known".
- Functional spec: is a customer-site product spec; it has its own "vessel library" (Digital Twin Dashboard,
  6.4: mass, load curve, trim; 3 roles; audit log). Noted as "define values the same way".
- Price concept (agentic/04): per part / per project; does not lean on a vessel database.
- Mail vs brief: mail = knowledge library (docs, notes, history, roles); brief = sizing reference
  (docking/structural values, source+confidence, similarity search, export). Design takes mail scope + keeps
  source/confidence, docking values in starting set, range filter.
- Wrote: vessel-library/01_First_Design.md; draft reply in secretary/inbox/drafts/2026-11-16_ramin_vessel_library_reply.md.
- Recommendation A (own small web app), 11–21 person-weeks phase 1.
- Reviews running: naval architect cold reader; software architect.
- Reviews in. Engineer: "sound document library, weak engineering core" -> added docking record, LCG+ref,
  lightship, fore/aft drafts, keel/appendages, beam moulded vs over all, tonnes vs LT, condition on weights,
  dated owner/flag/class, load curve as document, CSV export, compare, class-group shared data.
  Architect: "sound honest first draft; fix value model, doc identity, purge, restriction" -> typed values with
  condition/time/preferred, unit table, Document+Revision, organisations, multi-links, purge with tombstone,
  restriction on notes/values/search/export, IMO unique among active, softened B/C, hybrid noted, run cost 2-4 pw/yr,
  estimate raised to 15-28 pw (~20), "same range as brief" claim corrected.
- Not taken: free-text notes instead of 6 categories (mail asks); drop checksum (cheap, gives no-overwrite);
  drop restricted mark (left as decision Q5); drop DWT (mail lists it); auto un-merge (manual via change log);
  low-code 4th option (no new info until IT names one).
- Design ~3800 words, table-heavy: roughly 6-7 A4, at or slightly over the limit.
- Committed d842901 on u80-vessel-library. No merge, no push. Draft outside repo.
