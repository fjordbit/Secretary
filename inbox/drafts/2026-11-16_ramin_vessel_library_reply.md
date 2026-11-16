# DRAFT — reply to Ramin: Vessel Library requirements

**Not sent.** For Stian to review, edit and send himself. English. Reply to his mail of 5 Oct.

---

**Subject:** RE: Vessel Library System / Vessel Database – Initial Requirements for Review

Hi Ramin,

Sorry this took a while. Short version: yes to starting simple — your list is a good base, and I've written a first
design from it (attached).

**Missing, and matters for version 1:**
1. **Where it runs and how people log in.** Ideally company accounts / single sign-on, on the company network, so we need IT early.
2. **Where the files live, how big, and backup.** CAD files and large PDFs decide storage. CAD models already in 3DEXPERIENCE should be linked, not copied.
3. **One source for project number and customer.** If a system already owns them, we link to it rather than type them twice.
4. **The values we size with, and our own dockings.** Docking weight with its condition, LCG, keel and appendage data — each with its source and whether it is measured or estimated — plus a simple record of each docking we did with the measured weight. Cheap now, hard to add later.
5. **Who may see customer documents.** Some are under NDA; three roles let every viewer see everything.

**More complicated than it looks:**
- **Configurable properties.** I'd keep it to a fixed starting list plus admin-added properties of four simple types, with units. No formulas.
- **Duplicate vessels** (renamed, no IMO, sister ships). IMO unique when given, a "did you mean" check, and an admin merge. Sister ships stay separate.
- **The vessel sites you listed.** Fine as examples. If we ever want to copy data from them, we should check their terms first — I don't know what they allow.

**Decisions I need from you before development:**
1. Who uses it in version 1, and who owns the data (one named person).
2. Do customer documents need restricted access, per customer or per project?
3. Are you OK with a small web application of our own, or do you want it on something we already have (e.g. 3DEXPERIENCE)? I lean to our own; the reasons are in the design.

**Next step:** I'm travelling this week. When I'm back, a short session with you, Esten, Rolf-Atle and Carl to settle
the above, and engineering picks 10 real vessels as test data. Then a first skeleton to click through in 1–2 weeks.
The full first version is a few months of work (my first estimate is about 20 person-weeks; the range and what
drives it are in the design), and how fast IT can answer will probably set the calendar.

Best,
Stian

---

## For Stian only (not part of the mail)

**Assumed:** the design goes along as an attachment (`Prosjekter/vessel-library/01_First_Design.md`, on branch
u80-vessel-library — convert to PDF or paste as you like). Ramin's role per the mail signature: CPO. Esten, Rolf-Atle
and Carl named as in his mail; their roles are not known.

**Left out, and why:**
- Full-text search inside PDFs: his own list already limits search to titles and notes; it is in the design as later.
- The size estimate: now named in the mail in one sentence (about 20 person-weeks; range 15–28 in the design), on Stian's word 16 Nov.
- Import of what exists today: one of the design's open questions; too early to ask him where it all is.
- Our older brief's similarity search and export to calculations: not phase 1; a range filter is kept.
- The link to the customer-side "vessel library" in our functional spec: in the design only.
- No mention of agents or the multi-agent flow.
