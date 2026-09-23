# Travel OS

![version](https://img.shields.io/badge/version-1.0-blue)

Four skills that manage the Notion **Travels & City** database. The database already exists and is correct. Travel OS does not redesign it, it keeps it filled, current and usable.

## Why this exists

The Notion environment was built once, carefully: a Nations database for country-level rules, a City database for local detail, a Travel database for the operational itinerary, each with a complete default template. The templates were the good part. The failure mode was never the structure, it was filling it: sections left generic, tables half empty, placeholders shipped as if they were content, a single trip split across two pages because it crossed a border.

Travel OS closes that gap. Every skill in it reads the same three shared standards, and every page it writes goes through a verification pass before it is called finished.

## The catalog

| Skill | What it does |
| --- | --- |
| **nation-city-pages** | Fills Nations and City pages to the template, point by point. Researches first, writes second, and adds the things the template does not cover but the reader wants: history, the two food lists, concrete Do and Don't, verified politics, embassies, the Bitcoin business layer. |
| **trip-itinerary** | Builds the Travel page from real data harvested out of Spark, Gmail and Calendar. Flights with PNRs, accommodation with confirmation codes, side events, and a red callout at the top listing every agenda conflict and missing piece it found. |
| **pre-departure-check** | Forty-eight hours out, re-reads the itinerary, verifies live what may have changed since it was written, and hands back a short ordered list of what is still open. |
| **travel-db-audit** | Sweeps the whole database for incomplete pages, stale figures, broken relations and trips wrongly split across pages. Runs unattended and stays silent when there is nothing to report. |

Run order: **nation-city-pages** builds the reference layer, **trip-itinerary** builds on it, **pre-departure-check** closes the loop before departure, **travel-db-audit** keeps the whole thing honest over time.

## Shared standards

Three files in `knowledge/`, bundled into every package so a skill installed on its own still resolves them:

- **`notion-travel-db.md`** the map: data source ids, property schemas, the direction relations resolve, naming conventions, and the one-trip-one-page rule
- **`page-standard.md`** the fill contract: reproduce the template to the letter, fill every point, and the verification pass that decides whether a page is finished
- **`research-standard.md`** what must be checked live every time, what can be written from knowledge, and where trip data actually comes from

## Install

```
/plugin marketplace add Mr-Hodler/Travel-OS
/plugin install travel-os
```

Needs the Notion connector. `trip-itinerary` and `pre-departure-check` also need Spark or Gmail, and Google Calendar.

## What's new in 1.0

First release. Four skills, three shared standards, extracted from the Helsinki and Warsaw trip of September 2026 after the same mistakes were made by hand and corrected.

---

See `HANDBOOK.md` for skill by skill usage. Proprietary and confidential, internal use only.
