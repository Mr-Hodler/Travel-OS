# Travel OS

![version](https://img.shields.io/badge/version-1.1-blue)

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

Beside them, `knowledge/templates/` mirrors the default page template of each of the three data sources, Nations, City and Travel, verbatim as the Notion API returns it, and `knowledge/template-sync.md` records when the snapshot was taken and how to re-take it. The mirrors let a skill know the required shape of a page with no Notion round trip, and keep that shape reviewable in git. They are snapshots and not the master: **Notion remains the source of truth**, so where a mirror and the live template disagree the live template wins and the mirror is stale, and a mirror is never edited to change a template.

## Install

```
/plugin marketplace add Mr-Hodler/Travel-OS
/plugin install travel-os
```

Needs the Notion connector. `trip-itinerary` and `pre-departure-check` also need Spark or Gmail, and Google Calendar. `travel-scheduler` needs the trigger tools of the `claude-code-remote` MCP server, and nothing else.

## What's new in 1.1

**`travel-scheduler`**, the fifth skill. `pre-departure-check` and `travel-db-audit` each declared the cadence they wanted and neither owned the mechanism, so the scheduling was improvised every time and mostly not done at all. It is now one skill: the two one-shot pre-departure runs per trip, a page refresh ten days out because the nation and city pages a trip is built on go stale while nobody is looking at them, and the monthly audit.

It exists mainly for one defect. A task created with the in-process cron tools is discarded when the session that created it ends: the call reports success, the user is told the reminder is set, and 48 hours before departure nothing fires and nothing reports the loss. `travel-scheduler` uses the `claude-code-remote` trigger tools only, writes each task prompt so it survives a cold start with no memory of the conversation, converts Europe/Zurich local time to UTC and reports both, and says whether the task is actually allowed to act when nobody is present to approve it.

Version 1.0 was the first release: four skills and three shared standards, extracted from the Helsinki and Warsaw trip of September 2026 after the same mistakes were made by hand and corrected.

---

See `HANDBOOK.md` for skill by skill usage. Proprietary and confidential, internal use only.
