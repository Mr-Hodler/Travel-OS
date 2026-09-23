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
| `knowledge/page-standard.md` | defines what complete means, therefore what incomplete means, and lists the placeholder tokens to hunt |
| `knowledge/notion-travel-db.md` | the three data source ids, the property schemas, relation direction, the one trip one page rule |
| `knowledge/research-standard.md` | which facts rot, therefore which pages are stale by age alone |

## What it looks for

| Class | Signal | Detected from |
| --- | --- | --- |
| **Incomplete page** | residual `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`, `[Amount]`, `YYYY-MM-DD`; empty table cells; rows still generic; template sections missing or misnumbered; a `Jarvis`, `Operational instructions` or `Guidance` block left in the page | page content, fetch required |
| **Stale data** | prices, opening hours and closing days, who governs, an exchange rate older than the date stated next to it, a venue that may have closed, transport works that have ended | footer date and `Last edited time`, then a targeted live check |
| **Broken relation** | a City with no `Nation`; a Nation whose `Cities` omits a city that points at it; a Travel with a `City` but not the matching `Nations`; a relation pointing at a duplicate page | the row listing alone |
| **Split trip** | two or more Travel pages with overlapping or adjacent `Dates` that are one journey. One trip is one page, with multiple relations and one day by day table | the row listing alone |
| **Duplicate** | the same country or city twice, usually a naming variant: with and without the flag emoji, English against local name, singular spelling drift | normalised name match on the listing |
| **Archivable** | a Travel whose `Dates` ended more than 90 days ago and is still sitting in the active view | the row listing alone |

Staleness thresholds: a page is stale at **12 months** since its footer date, and at **6 months** if a
Travel page relates to it with dates inside the next 90 days. An imminent trip raises the bar on its own
reference pages.

## How it runs

1. **List, do not fetch.** `notion-query-data-sources` on Nations, City and Travel. Three queries return
   names, relations, dates and last edited time for the whole database. That is enough to produce four of
   the six classes above without opening a single page.
2. **Triage from the listing.** Missing relations, past-dated trips, overlapping date ranges, names that
   normalise to the same string: these are findings already, with no fetch cost.
3. **Fetch only the suspects.** Pages that triage flagged, plus pages attached to a trip in the next 90
   days, plus the oldest handful by footer date. Never the whole database. State in the report how many
   pages were opened and how many were listed only, so the reader can see the coverage of the run.
4. **Verify the rot, do not assume it.** Age is a suspicion, not a finding. Run the live check where it is
   cheap and high value, so who governs and the exchange rate. Where a live check is not worth it in this
   run, the finding is recorded as `da verificare` with the age that raised it, never as a corrected value.
5. **Write the report.** Shape in `references/report-template.md`.

## Output

A table, ordered by severity and then by the imminence of the trip that depends on the page.

| Column | Contents |
| --- | --- |
| Pagina | name and link |
| Tipo | Nation, City or Travel |
| Problema | the specific defect, with the token or the empty field named. "Incompleta" is not a finding |
| Gravità | Alta, Media, Bassa |
| Azione consigliata | one imperative line, with the skill that does it |

Severity, fixed so two runs agree: **Alta** is anything that will mislead on a trip inside the next 90 days,
or a broken relation that hides a page from the trip that needs it. **Media** is incomplete or stale with
nothing imminent depending on it. **Bassa** is cosmetic, naming, and archiving.

Findings route out: incomplete or stale Nation and City pages go to `nation-city-pages` in enrichment mode,
split trips and thin itineraries to `trip-itinerary`.

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
- Never report a page as incomplete without naming the field or the token that made it fail. A finding that
  cannot be acted on in one step is not a finding.
- Report in Italian. No em dashes and no en dashes.
