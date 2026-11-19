# cathead — U81 notes (16 Nov 2026)

Unit: U81, Oracle ↔ maintenance system API map and estimate skeleton. Brief: kai.md "## U81".

- Worktree C:/Users/stian/Prosjekter-u81, branch u81-oracle-integration from 5f415b6.
- Sources read: first mail in inbox/GMail/mails_as_text.txt; both swagger files parsed by script only;
  systems-integration/01; logging-maintenance/01–03 (skimmed for the maintenance product).
- API not called. No web lookups made (Oracle tool names written from general knowledge: OIC, FBDI,
  EBS interface tables / SOA gateway, JDE Orchestrator/AIS).
- Script kept in the worktree for re-running the appendix counts: systems-integration/02_api_map_counts.py.
- Main findings: polling only; changed-since only on articles (LastModifiedDate) and stock transactions
  (FromDate + "Transferred" flag); none on work orders/assets/counters/hours; shared external keys only
  on customers/suppliers, invoices, messages; auth = username/password → bearer + tenant header, v2 refresh.
- Open: vendor not named in files; URL is a dev host "mm-mobile-api-dev"; relation to "EG Maintenance"
  in our notes not known; customer production version/edition not known.
- Draft note: secretary/inbox/drafts/2026-11-16_sondre_oracle_integration_status.md (not sent).
- Reviews: architect + falsifier subagents; results and fixes below.
- Review results: architect "defensible with fixes" (A too low; missing PM/contingency/security/initial
  load/hypercare; purchase flow; Oracle module names; Transferred-flag idempotency) — all applied, ranges
  raised to all-in. Falsifier: ~115 claims, 1 wrong (invoice create), 9 imprecise — all fixed.
- Committed 6a106bc on u81-oracle-integration. No merge, no push. ~4 400 words: at or slightly over 6 A4.
- Draft note figures updated to the all-in ranges.
