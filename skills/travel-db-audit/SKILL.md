---
name: travel-db-audit
description: >-
  Audit periodico del database Notion Travels & City. Trova pagine rimaste incomplete (placeholder residui,
  celle vuote, sezioni del template mancanti), dati scaduti (prezzi, orari, chi governa, tassi di cambio,
  locali chiusi), relazioni rotte o mancanti tra Nations, City e Travel, viaggi spezzati su più pagine
  quando dovrebbero essere una, pagine duplicate e itinerari passati archiviabili. Usala quando l'utente
  dice "audit del database viaggi", "controlla le pagine viaggio", "cosa è incompleto", "quali pagine sono
  stale", "il database è a posto", "fai un giro di controllo", oppure in inglese "travel db audit", "check
  the travel pages", "what is incomplete", "which pages are stale". Restituisce un report a tabella con
  pagina, problema, gravità e azione consigliata. Non modifica niente senza conferma, tranne le correzioni
  meccaniche e sicure, che elenca comunque nel report. Gira anche su schedule, e resta silenziosa quando
  non c'è niente da segnalare.
---

# Travel DB audit

The database decays in predictable ways: a page written in a hurry keeps its placeholders, a price goes out
of date, a city loses its nation relation, one trip ends up as two pages. None of it errors and none of it
is visible from the database view. This skill finds it on a schedule, so a trip never finds it instead.

## Read first, every run

| File | What it settles |
| --- | --- |
| `knowledge/page-standard.md` | defines what complete means, therefore what incomplete means, lists the placeholder tokens to hunt, and carries **the density budget** that defines what over-long means |
| `knowledge/notion-travel-db.md` | the three data source ids, the property schemas, relation direction, the one trip one page rule |
| `knowledge/research-standard.md` | which facts rot, therefore which pages are stale by age alone |
| `knowledge/drive-convention.md` | the Drive folder per trip, the canonical names, and the current list of folders and pages that do not correspond |

## What it looks for

| Class | Signal | Detected from |
| --- | --- | --- |
| **Incomplete page** | residual `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`, `[Amount]`, `YYYY-MM-DD`; empty table cells; rows still generic; template sections missing or misnumbered; a `Jarvis`, `Operational instructions` or `Guidance` block left in the page | page content, fetch required |
| **Stale data** | prices, opening hours and closing days, who governs, an exchange rate older than the date stated next to it, a venue that may have closed, transport works that have ended | footer date and `Last edited time`, then a targeted live check |
| **Broken relation** | a City with no `Nation`; a Nation whose `Cities` omits a city that points at it; a Travel with a `City` but not the matching `Nations`; a relation pointing at a duplicate page | the row listing alone |
| **Split trip** | two or more Travel pages with overlapping or adjacent `Dates` that are one journey. One trip is one page, with multiple relations and one day by day table | the row listing alone |
| **Duplicate** | the same country or city twice, usually a naming variant: with and without the flag emoji, English against local name, singular spelling drift | normalised name match on the listing |
| **Archivable** | a Travel whose `Dates` ended more than 90 days ago and is still sitting in the active view | the row listing alone |
| **Empty `Drive link`** | a Travel page whose `Drive link` is blank. A defect even when no folder exists yet, because the page then names no home for the documents it was built from | the row listing alone |
| **Drive and Notion do not correspond** | a trip folder under `05_Viaggi` with no Travel page, a Travel page with no folder, or a `Drive link` pointing at a folder that is not the one named for those dates. Matching is on destination and on `Dates` against the `YYYY.MM_Destinazione` folder name, never on the title, which drifts | the row listing plus one read of `05_Viaggi` |
| **Fake sources** | many `Link` cells pointing at the same generic portal, a search result URL standing in for a site, generation residue such as `utm_source=chatgpt.com` or `([turn0searchNN])`, a link whose text and target do not name the same thing. The page looks filled and is not verifiable, which is what makes this the most dangerous class | page content, fetch required |
| **Generation drift** | a page written against an older spec: sections missing against the current `*-spec.md`, or an `Ultimo aggiornamento` block that names an older spec version or names none at all. Nothing on the page looks wrong, it is simply a generation behind | the footer marker, then the section count against the spec |
| **Empty `Maps` on a City** | a City page whose `Maps` url property is blank, or whose Google Maps link was written as a row inside the page body instead of into the property, which leaves the property empty and the link invisible to every query. `Maps` exists on the City data source, see the schema in `knowledge/notion-travel-db.md` | the row listing alone |
| **Page over the density cap** | since 1.5 the metric is the **visible text**, not the markdown characters. Any table cell over 300, any callout over 4 lines, any run of prose longer than 3 consecutive lines, the first level of the history toggle over 1,300. The page is complete and correct and still unusable, because the reader cannot find a datum in it. Caps in `knowledge/page-standard.md`, `Density budget`. A structural variant of the same class: the history toggle sitting **above** section 1 instead of nested inside it, which is a pre-1.4 generation defect | page content, fetch required |
| **Sezione aperta oltre 900 caratteri visibili** | what a section shows before its `Dettaglio` toggle exceeds **900 visible characters**. The reader opens the section and gets a wall instead of the three to six lines he came for. Counted on the visible text with the `Dettaglio` toggles closed | page content, fetch required |
| **`Scheda rapida` mancante o oltre 1.200** | no `⚡ Scheda rapida` at all, or it is not the **first block** of the page, or it sits inside a toggle, or it exceeds **1,200 visible characters**. It is the block the page exists to open on | page content, fetch required |
| **Toggle `Dettaglio` assente in una sezione pesante** | a heavy section with no `Dettaglio: <what it holds>` toggle under it, so everything it holds is at the first level. The two levels are the lever the whole standard rests on | page content, fetch required |
| **Blocco `Ultimo aggiornamento` residuo** | the `🗓️ Ultimo aggiornamento` block still in the page. It was removed in 1.5 in favour of the single line `Aggiornata il <data>. Fonti: <elenco>.` | page content, fetch required |
| **Dichiarazione di densità residua** | a note on compression, a character count, a statement of how dense the page is, left anywhere in it. Metadata addressed to whoever wrote the page, standing in front of whoever reads it | page content, fetch required |
| **Elenco in prosa dove serve una tabella** | more than two items, each with more than one attribute, threaded into a sentence or a paragraph. Three venues and their prices inside one line of prose is the signature. Mandatory columns per kind of list in `knowledge/page-standard.md`, `No lists in prose` | page content, fetch required |
| **Sezione senza toggle** | a numbered section that has lost its `{toggle="true"}`, so the whole page opens expanded. Usually the aftermath of a heading whose text was edited, which makes Notion rebuild the block and drop the attribute along with the children's indentation | page content, fetch required |
| **Bandiera dentro il `Name`** | a flag emoji inside the title property instead of in the page icon. It produces the duplicate that normalises to the same string, `Poland` against `Poland 🇵🇱`, and makes every query match on a character nobody types | the row listing alone |
| **City senza icona bandiera** | a City page whose icon is not the flag of the nation its `Nation` relation points at, or that has no icon at all | the row listing alone |

Staleness thresholds: a page is stale at **12 months** since its footer date, and at **6 months** if a
Travel page relates to it with dates inside the next 90 days. An imminent trip raises the bar on its own
reference pages.

## How it runs

1. **List, do not fetch.** `notion-query-data-sources` on Nations, City and Travel. Three queries return
   names, relations, dates and last edited time for the whole database. That is enough to produce four of
   the six classes above without opening a single page.
2. **Triage from the listing.** Missing relations, past-dated trips, overlapping date ranges, names that
   normalise to the same string: these are findings already, with no fetch cost. List `05_Viaggi` once in the
   same pass, one level deep, and diff the trip folders against the Travel rows: a folder with no page
   and a page with no folder are both findings from the two listings alone, with nothing opened.
3. **Fetch only the suspects.** Pages that triage flagged, plus pages attached to a trip in the next 90
   days, plus the oldest handful by footer date. Never the whole database. State in the report how many
   pages were opened and how many were listed only, so the reader can see the coverage of the run.
4. **Verify the rot, do not assume it.** Age is a suspicion, not a finding. Run the live check where it is
   cheap and high value, so who governs and the exchange rate. Where a live check is not worth it in this
   run, the finding is recorded as `da verificare` with the age that raised it, never as a corrected value.
5. **Measure the density on every page opened.** It costs nothing beyond the fetch already made, so it is
   never a reason to open a page and never skipped on a page that is open. Count the characters of the
   `<content>` block as `notion-fetch` returns it, markup included: that is the body figure. Then split on
   the `## ` headings and take the length from one `## N.` heading to the next: that is the per-section
   figure, and the longest section is reported by name because it is where the repair starts. Then the
   three spot checks: the length of the `<details>` block whose summary is `City History` or
   `Storia del paese`, the longest `<td>` cell, and the longest run of consecutive prose lines, meaning
   lines that are not a bullet, a table tag or a heading. Report the measured number against the cap, so
   `Dubai 106,835 / 42,000`, never the word `long`. A page under every cap is not a finding and is not
   listed.
6. **Write the report.** Shape in `references/report-template.md`.

## Output

A table, ordered by severity and then by the imminence of the trip that depends on the page.

| Column | Contents |
| --- | --- |
| Pagina | name and link |
| Tipo | Nation, City or Travel |
| Problema | the specific defect, with the token or the empty field named. "Incompleta" is not a finding, and neither is "lunga": a density finding carries the measured number against the cap and the longest section by name |
| Gravità | Alta, Media, Bassa |
| Azione consigliata | one imperative line, with the skill that does it |

Severity, fixed so two runs agree: **Alta** is anything that will mislead on a trip inside the next 90 days,
or a broken relation that hides a page from the trip that needs it. **Media** is incomplete or stale with
nothing imminent depending on it. **Bassa** is cosmetic, naming, and archiving.

Findings route out: incomplete or stale Nation and City pages go to `nation-city-pages` in enrichment mode,
split trips and thin itineraries to `trip-itinerary`. Everything this skill finds and is not allowed to fix
goes to `travel-db-repair`: duplicates, broken or misdirected relations, false data, fake sources, generation
drift, **pages over the density cap** and cosmetics. The audit finds and routes, the repair skill writes.

## What it may change without asking

Only mechanical, unambiguous and reversible edits. Three of them:

- deleting a leftover `Jarvis`, `Operational instructions` or `Guidance` block, which is scaffolding the
  page standard says to strip
- setting a City's `Nation` when exactly one Nation page matches the country that page is about
- adding the missing `Nations` relation on a Travel that already relates to a City of that nation

Every automatic fix is still listed in the report, marked `corretto`, so nothing happens off the record.

Everything else is proposed and not done: rewriting content, merging split trips, renaming, choosing which
of two duplicates survives, archiving a past trip. The Travel schema has no status property, so archiving
is the user's move and the report only hands over the list.

## Unattended runs

Fit for a schedule: monthly, plus seven days before the start date of any Travel page.

- **No memory.** The run derives everything from the database each time. It does not rely on a stored
  previous report and it does not ask for one.
- **Silent when clean.** No findings means one line, in Italian, and nothing else. No table, no summary of
  what was checked, no notification. A monthly audit that always says something is an audit nobody reads
  after the third month.
- **Alta and Media only** in unattended mode. Bassa findings are noise without a person present to say
  whether they matter, and they are still there on the next on demand run.
- The three safe fixes above still apply unattended, and are still reported. Nothing else writes when no
  one is there to confirm.

## Guardrails

- Never add a property, rename a data source, or create a new database. The environment is correct.
- Never delete a page. A duplicate is reported with which copy should survive and why, and the merge is the
  user's call.
- Never invent the corrected value. `da verificare` is a legitimate finding.
- `05_Viaggi` is read only in an audit. Never create, rename, move or delete anything in Drive, and never copy a passport, a visa or an ID scan into a Notion page or into a report. A missing folder is reported, not created.
- Never report a page as incomplete without naming the field or the token that made it fail. A finding that
  cannot be acted on in one step is not a finding.
- Report in Italian. No em dashes and no en dashes.
