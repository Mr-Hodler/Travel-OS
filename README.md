# Travel OS

![version](https://img.shields.io/badge/version-1.2-blue)

Five skills that manage the Notion **Travels & City** database. The database already exists and is correct. Travel OS does not redesign it, it keeps it filled, current and usable.

## Why this exists

The Notion environment was built once, carefully: a Nations database for country-level rules, a City database for local detail, a Travel database for the operational itinerary, each with a complete default template. The templates were the good part. The failure mode was never the structure, it was filling it: sections left generic, tables half empty, placeholders shipped as if they were content, a single trip split across two pages because it crossed a border.

Travel OS closes that gap. Every skill that writes a page reads the same three shared standards, and every page goes through a verification pass before it is called finished. The fifth skill writes no page: it owns the scheduled tasks that make the other four run when they are supposed to.

## The catalog

| Skill | What it does |
| --- | --- |
| **nation-city-pages** | Fills Nations and City pages to the template, point by point. Researches first, writes second, and adds the things the template does not cover but the reader wants: history, the two food lists, concrete Do and Don't, verified politics, embassies, the Bitcoin business layer. |
| **trip-itinerary** | Builds the Travel page from real data harvested out of Spark, Gmail and Calendar. Flights with PNRs, accommodation with confirmation codes, side events, and a red callout at the top listing every agenda conflict and missing piece it found. |
| **travel-scheduler** | Owns the scheduled tasks behind the others: the two one-shot pre-departure runs per trip, the page refresh ten days out, the monthly audit. Creates them with the trigger tools that survive the end of a session, converts Lugano local time to UTC, names them so they can be found again, and removes them when the trip is over. |
| **pre-departure-check** | Forty-eight hours out, re-reads the itinerary, verifies live what may have changed since it was written, and hands back a short ordered list of what is still open. |
| **travel-db-audit** | Sweeps the whole database for incomplete pages, stale figures, broken relations and trips wrongly split across pages. Runs unattended and stays silent when there is nothing to report. |

Run order: **nation-city-pages** builds the reference layer, **trip-itinerary** builds on it, **travel-scheduler** sets the reminders that trip needs, **pre-departure-check** closes the loop before departure, **travel-db-audit** keeps the whole thing honest over time.

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

Needs the Notion connector. `trip-itinerary` and `pre-departure-check` also need Spark or Gmail, and Google Calendar. `travel-scheduler` needs the trigger tools of the `claude-code-remote` MCP server, and nothing else.

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
