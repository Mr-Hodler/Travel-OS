# Travel OS

![version](https://img.shields.io/badge/version-1.5-blue)

Six skills that manage the Notion **Travels & City** database. The database already exists and is correct. Travel OS does not redesign it, it keeps it filled, current and usable.

## Why this exists

The Notion environment was built once, carefully: a Nations database for country-level rules, a City database for local detail, a Travel database for the operational itinerary, each with a complete default template. The templates were the good part. The failure mode was never the structure, it was filling it: sections left generic, tables half empty, placeholders shipped as if they were content, a single trip split across two pages because it crossed a border.

Travel OS closes that gap. Every skill that writes a page reads the same three shared standards, and every page goes through a verification pass before it is called finished. One skill writes no page: it owns the scheduled tasks that make the others run when they are supposed to. And since 1.3 the maintenance half is a pair rather than a single skill, because an audit that can only report is an audit whose findings accumulate: `travel-db-audit` finds the defects, `travel-db-repair` closes them.

## The catalog

| Skill | What it does |
| --- | --- |
| **nation-city-pages** | Fills Nations and City pages to the template, point by point. Researches first, writes second, and adds the things the template does not cover but the reader wants: history, the two food lists, concrete Do and Don't, verified politics, embassies, the Bitcoin business layer. |
| **trip-itinerary** | Builds the Travel page from real data harvested out of Spark, Gmail and Calendar. Flights with PNRs, accommodation with confirmation codes, side events, and a red callout at the top listing every agenda conflict and missing piece it found. |
| **travel-scheduler** | Owns the scheduled tasks behind the others: the two one-shot pre-departure runs per trip, the page refresh ten days out, the monthly audit. Creates them with the trigger tools that survive the end of a session, converts Lugano local time to UTC, names them so they can be found again, and removes them when the trip is over. |
| **pre-departure-check** | Forty-eight hours out, re-reads the itinerary, verifies live what may have changed since it was written, and hands back a short ordered list of what is still open. |
| **travel-db-audit** | Sweeps the whole database for incomplete pages, stale figures, broken relations and trips wrongly split across pages. Runs unattended and stays silent when there is nothing to report. |
| **travel-db-repair** | Closes what the audit found. Parks duplicates instead of deleting them, rewires relations read off the page rather than guessed, corrects data that is objectively false, strips fake sources and leaves the name where no official link exists, migrates pages written against an older spec after mapping them block by block. |

Run order: **nation-city-pages** builds the reference layer, **trip-itinerary** builds on it, **travel-scheduler** sets the reminders that trip needs, **pre-departure-check** closes the loop before departure, **travel-db-audit** keeps the whole thing honest over time, and **travel-db-repair** is what the audit hands its findings to.

## Shared standards

Three files in `knowledge/`, bundled into every package so a skill installed on its own still resolves them:

- **`notion-travel-db.md`** the map: data source ids, property schemas, the direction relations resolve, naming conventions, and the one-trip-one-page rule
- **`page-standard.md`** the fill contract: reproduce the template to the letter, fill every point, and the verification pass that decides whether a page is finished
- **`research-standard.md`** what must be checked live every time, what can be written from knowledge, and where trip data actually comes from

Beside them, `knowledge/templates/` holds the canonical specification of each of the three data sources: `nations-spec.md`, `city-spec.md` and `travel-spec.md`. Each one carries the whole structure of its template, section by section, table by table, toggle by toggle, plus the additions made in 1.2. **The specs are canonical and the default templates in Notion are aligned to them**, so where the two diverge the spec wins and the Notion template is what needs updating. `knowledge/template-sync.md` holds the direction of truth, how the Notion templates are brought into line, how to re-check that they still are, and the one limit that matters: a page created by clicking New page inside the database by hand starts from the Notion template, not from the spec, so the two have to be kept aligned anyway. The three `*-template.md` files beside the specs are historical snapshots of the templates as they stood on 2026-09-24, before the additions, kept for reference and not maintained.

## Install

```
/plugin marketplace add Mr-Hodler/Travel-OS
/plugin install travel-os
```

Needs the Notion connector. `trip-itinerary` and `pre-departure-check` also need Spark or Gmail, and Google Calendar. `travel-scheduler` needs the trigger tools of the `claude-code-remote` MCP server, and nothing else. `SETUP.md` has the whole matrix, the Drive folder convention, what to do on first use and how to verify that every connector actually responds.

## What's new in 1.5

**The character cap was the wrong metric.** A page was measured on the characters of its markdown, and
table markup is not read: the count measured the page against something no reader ever crosses. What is
measured now is the **visible text**.

**And the lever turned out not to be a shorter page. It is two levels in every heavy section:** the
operational essentials visible the moment the section opens, then one toggle `Dettaglio: <what it holds>`
carrying all the rest. **Nothing is deleted, it is moved one level down.** The caps, all on the visible
text: **900 characters for what an open section shows, 1,200 for `⚡ Scheda rapida`, 1,200 for the
`🔁 Da riverificare` toggle, 1,300 for the first level of the history toggle, 300 for a table cell,
4 lines for a callout, 3 consecutive lines of prose.** The `Dettaglio` toggles have no cap. One declared
exception: on a Nations page `Do`, `Don't` and the two food tables stay at the first level of section 7.

**Measured on the pilot, five pages, visible characters before and after:** Poland **83,139 to 15,059**,
Helsinki **80,208 to 10,628**, Warsaw to **10,713**, Kraków **44,822 to 17,465**, Finland **49,409 to
16,089**, with **zero facts lost**, verified by counting distinct numbers, links, proper names and
`da verificare` entries before and after.

**The page now opens on `⚡ Scheda rapida`**, the first block, outside every toggle, with
`🔁 Da riverificare prima di partire` second and as a toggle. The `🗓️ Ultimo aggiornamento`
block and every declaration of density are gone, replaced by one line: `Aggiornata il <data>. Fonti:
<elenco>.` **No enumeration is written as prose** any more, and every kind of list has mandatory columns.
New required entries: `Cibo da provare` and `Cibo strano` on a Nations page, and `Dove stare quartiere per
quartiere`, `Centri finanziari e business district`, `Come fare business in città`, `Cosa fare e cosa non
fare` and `Cibo strano` on a City page. **The flag lives in the page icon and never inside `Name`**, and a
City page carries the flag of its own nation.

`travel-db-audit` gained nine defect classes for all of this, and `travel-db-repair` gained the nine Notion
traps the pilot paid for, from a heading whose edited text makes Notion drop `{toggle="true"}` and the
children's indentation, to `update_content` in batch being atomic and silent.

## What's new in 1.4

**The pages were measured and given a density budget.** Fourteen live pages were fetched and counted on
2026-09-25. The median City page body was **84,569 characters**, and the three Chinese city pages held up
as the length reference measured **83,804**, so there was no short reference left in the database: it had
drifted as a whole. The reader's verdict was that half the text would have been more than enough, and the
caps are that halving made checkable: **42,000 characters for a City body, 32,000 for a Nations body,
4,500 for one numbered section, 3,500 for a history toggle, 300 for a table cell, and 3 consecutive lines
of prose before it has to become a table or a list.** Measured on the `<content>` block as `notion-fetch`
returns it, so two agents get the same number.

Beside the caps, `knowledge/page-standard.md` gains `How to write a line`, which is how the numbers are
reached: **a table beats a paragraph** whenever there are more than two comparable entries, one line one
fact, bold on the search key and not on a clause, the link on the name, no connective or editorial
sentences, no datum in two sections, a caution clause reduced to `da verificare`. And the rule that binds
all of them: **compressing is not cutting**, every fact, address, hour, link and `da verificare` entry
survives, only the words around them go.

**The history toggle moved inside section 1** on both page types, `travel-db-audit` gained a `page over the
density cap` defect class with the procedure to measure it, and `travel-db-repair` gained the compression
pass that closes it. The City spec gained the `Top quartieri dove stare` table that answers `dove dormo` in
one row, and `Centri finanziari e distretti business` plus `Come fare business qui` in section 10.

## What's new in 1.3

**Sixth skill: `travel-db-repair`.** It comes out of a maintenance pass over 81 pages of the database, run by
hand, and it exists because `travel-db-audit` was designed to find defects and route them and had nowhere to
route them to. Everything beyond three mechanical corrections was proposed, nobody was going to do it by hand
twice, and the findings accumulated. The repair skill is the write half of that pair.

It carries six repair classes **in order of return**, which is the part that cannot be guessed from the
outside. Duplicates first: not deleted, parked. The survivor is chosen by which page holds more real content,
what only the loser has is moved into it, the relations are repointed, and the loser goes with
`notion-move-pages` under a parking page outside the databases with a note saying why and what replaced it,
which the user deletes with one click. Relations second, because they are what makes the database unnavigable
and they are a property write with no content touched. Then data that is objectively false, then fake sources,
then generation migration, then cosmetics in bulk.

**Fake sources are the class worth naming on its own**, because they are invisible: the page looks filled,
reads as researched, and cannot be checked. Dozens of `Link` cells all pointing at the same generic portal,
generation residue like `utm_source=chatgpt.com` and `([turn0searchNN])` left in a URL. The rule is now written
into `knowledge/page-standard.md` as a **link contract**: look for the real official site, and if it is not
found remove the link and leave the name. Never swap a fake link for another generic one.

**The generation marker**, also in `page-standard.md`. Every page carries `Ultimo aggiornamento` with the date
**and the version of the spec it was written against**, so a future migration reads the footer and knows what
is behind without opening everything. A date alone does not say whether a page is a generation old.

**The operating rules the pass paid for**, now in the skill and in compact form in `CLAUDE.md`: parallelise by
group of pages and never by class of defect, because two agents on the same pages with `update_content`
overwrite each other silently; never `replace_content` on a page that has content, except a generation
migration and only after the block by block mapping; `notion-fetch` can return a stale snapshot, so force a
refresh before a structural edit; a placeholder is worse than a declared hole; re-fetch and verify after every
page, and the section count never decreases; the web search budget is shared and finite, and when it runs out
you write `da verificare` instead of reporting a figure you did not check, which is now the fallback in
`knowledge/research-standard.md`; and what comes out of a table moves rather than disappears.

**A factual error about the schema is corrected.** Two agents claimed the City data source has no `Maps`
property. It does: `Maps` is a url property on City, and `knowledge/notion-travel-db.md` now carries all three
schemas as complete tables with their types, plus the note that `Maps` is populated **at property level and not
as a row inside the page**, because a Google Maps link written into the page body leaves the property empty and
the link invisible to every query that lists the data source. `travel-db-audit` now detects an empty `Maps`, a
fake source, and generation drift between pages written against different specs. `nation-city-pages` carries
the link contract, the generation marker and the stale snapshot warning.

**`SETUP.md` and `CLAUDE.md`** are new at the repo root: the first says which connector each of the six skills
needs, what the `05_Viaggi` folder convention is, what to do on first use and how to verify that everything
responds; the second is what an agent reads before working in this repo.

Nothing was removed. The three `*-template.md` historical snapshots are untouched.

## What's new in 1.2

**The repo is now the source of truth for the three templates.** It was the other way round in 1.1: Notion held the master and the repo held a snapshot, which meant the repo could describe the templates but never improve them. The three `*-spec.md` files are now canonical, the three Notion default templates were brought up to them by addition, and `knowledge/template-sync.md` states the direction, the procedure and the limit.

Each spec also carries what the template was missing. Nations gained a `Storia del paese` toggle, the CH and IT consular emergency numbers as rows distinct from the embassy switchboard, a `Costi tipici nel paese` table in local currency and CHF, a `Fare business nel paese` block, explicit `Do` and `Don't` with a `Cosa non dire` line, `Chi governa oggi` with a verification date, and `Ultimo aggiornamento` with `Da riverificare prima di partire`. City gained a `Farmacia 24h` row, `Rischi stagionali` tied to the real travel window, explicit `Do` and `Don't` with `Cosa non dire`, an `Allenamento e wellness` table because the reader trains every day and needs a day pass near where he sleeps, the two dish tables `Da provare, buoni` and `Da provare, strani o divisivi`, `Chi accetta Bitcoin`, `Consolati e camere di commercio`, `Eventi tech ricorrenti`, and the same two closing blocks. Travel gained the red `DA RISOLVERE` callout at the top, `Transfer da e verso casa` because the home to airport leg is the one that is always missing, an `Impegni remoti e call` table separate from the tours, a `Conflitti di agenda` section, a cost summary split into `a carico azienda` and `a carico mio` with two totals, a `Modo semplificato` block so a short trip does not get a template built for a long one, a `Checklist finale` grouped by `Prima di partire` and then by city, and the `un viaggio una pagina` rule written on the page.

Nothing was removed anywhere. On Notion the Jarvis instruction callouts stay, because Notion is where they are read; the specs leave them out, because a specification does not need instructions on how to fill itself.

## What's new in 1.1

**`travel-scheduler`**, the fifth skill. `pre-departure-check` and `travel-db-audit` each declared the cadence they wanted and neither owned the mechanism, so the scheduling was improvised every time and mostly not done at all. It is now one skill: the two one-shot pre-departure runs per trip, a page refresh ten days out because the nation and city pages a trip is built on go stale while nobody is looking at them, and the monthly audit.

It exists mainly for one defect. A task created with the in-process cron tools is discarded when the session that created it ends: the call reports success, the user is told the reminder is set, and 48 hours before departure nothing fires and nothing reports the loss. `travel-scheduler` uses the `claude-code-remote` trigger tools only, writes each task prompt so it survives a cold start with no memory of the conversation, converts Europe/Zurich local time to UTC and reports both, and says whether the task is actually allowed to act when nobody is present to approve it.

Version 1.0 was the first release: four skills and three shared standards, extracted from the Helsinki and Warsaw trip of September 2026 after the same mistakes were made by hand and corrected.

---

See `HANDBOOK.md` for skill by skill usage. Proprietary and confidential, internal use only.
