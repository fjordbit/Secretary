# DRAFT (longer version) — reply to Ramin: Vessel Library requirements

**Not sent.** For Stian to review, edit and send himself. English. Reply to his mail of 5 Oct.

---

**Subject:** RE: Vessel Library System / Vessel Database – Initial Requirements for Review

Hi Ramin,

Sorry this took a while. Yes to starting simple; your list is a good base. My first design is attached.

**What it is for.** One place to see everything we know about a vessel. For sales, project and basic-design
engineers, and site and service people who bring back photos, load readings and lessons.

**Version 1 lets a user:**
- Search by name, old name, IMO, project number or name, document title or note text.
- Filter by type and ranges (e.g. beam 20–25 m), compare 3–5 vessels, export to Excel/CSV.
- Add values with unit, condition and source, and record dockings with measured weight, LCG and drafts.
- Upload documents and photos with revisions, linked to vessels, a sister class or a project.
- Write notes in your six categories. Archive, never delete; every change is logged.

**Later, on purpose:** search inside PDFs, PDF reading, outside-site import, a project-system link, an API.
The data model keeps the door open.

**Not in your list yet, and matters for version 1:**
1. **Where it runs and how people log in.** Company accounts (single sign-on if we have it), company network only. IT's answers will likely set the calendar.
2. **Where the files live, how big, and backup.** Sizes drive cost. Ideally files go in a store IT already backs up, and CAD models in 3DEXPERIENCE are linked, not copied.
3. **One source for project number and customer.** Typed once now; linked later if a system owns them.
4. **The values we size with, and our own dockings.** Measured docking data is the most valuable thing we hold. Each value keeps its source and whether it is measured, declared or estimated; weights and drafts need a condition (lightship, as docked, full load). Long tons read as tonnes is a 1.6 % error on the weight we size against. Cheap now, hard to add later.
5. **Who may see customer documents.** Some may be under NDA, but three roles let every viewer see everything. I propose a "restricted" mark for a group (e.g. the project team), also in search and export. Plus one logged exception to "never delete": what an NDA or privacy law says must be destroyed.

**More complicated than it looks:**
- **Configurable properties.** A starting list plus admin-added properties of four types (number, text, date, choice), with units. No formulas.
- **Duplicates** IMO unique when given, a "did you mean" check, a logged admin merge. Sister ships stay separate, grouped in a class.
- **The vessel sites you listed.** Fine as examples; check their terms before copying data.

**Where to build it.** Options: (A) a small web application of our own, (B) 3DEXPERIENCE, (C) a configured
document-library product (SharePoint-type). I recommend A (not yet a decision), provided IT can give it
company login and backed-up file storage. The core is vessel values with unit, condition and source; C is weakest there.
Running A takes a small server, about 2–4 person-weeks a year of upkeep, and a named owner. C is the fallback; B needs the licence question below.

**The plan:**
- **First a skeleton to click through, 1–2 weeks of work after we meet:** login, search, vessel page, new/edit vessel, document upload, change history, with 10 real vessels picked by engineering.
- **Full first version:** 15–28 person-weeks of build (not calendar time; IT and engineering time not counted), about 20 most likely. Drivers: importing today's material (largest unknown), restricted access, login, a project-system link, file sizes.

**From IT:** login, file storage and backup, a place to run it, a security review. Who should I ask?

**From engineering:** which values sizing needs, in which units and conditions; the 10 test vessels. From Esten,
Rolf-Atle and Carl, and the sales side: where vessel information lives today.

**Decisions I need from you before development:**
1. Who uses it in version 1, and who owns the data (one named person).
2. Do customer documents need restricted access? If yes, per customer or per project?
3. OK with option A? If you prefer 3DEXPERIENCE: does our licence give viewers to non-CAD users?
4. Does a system already own project numbers and customers? Which?

**Next step:** I'm travelling this week. When I'm back, a short session with you, Esten, Rolf-Atle and Carl to settle
this. Then the skeleton.

Best,
Stian

---

## For Stian only (not part of the mail)

**Added compared with the short version:** purpose and users; five lines on what version 1 does, and what is left
for later; a "why" and a proposal on each missing point (incl. the 1.6 % long-ton/tonne error, and purge as the one
exception to "never delete"); the three architecture options with the recommendation, its reason, running cost and
the need for a named owner; the skeleton's screens and data; 15–28 (about 20) person-weeks with what drives it; asks
to IT and engineering; decision 4 (project-number system, Q4). CAD as reference (Q10) stays a proposal in point 2,
not a fifth decision. Body is about 700 words, a little over the 650 aim, after a fact-check asked for more precise
wording.

**Left out, and why:** the data model and per-part estimate table (in the design); IT lead times, licence prices,
user numbers (design: "not known"); AI search and calculations from the later-list (no AI mention; calculations are
simply out of scope); logging who reads what (Q5 detail, for the session); the older-brief comparison; the
customer-side "vessel library"; agents. "A few months of work" from the short draft replaced by the figure, to avoid
a calendar promise.

**Unsure:** "1–2 weeks of work after we meet": the design gives the skeleton's effort, not a start. Esten, Rolf-Atle
and Carl: roles not known; the mail asks them, with sales, where vessel information lives today. "Who should I ask?"
(IT contact) assumes Ramin knows. "Fine as examples" about the vessel sites is your opinion, as in the short draft.
