# Travel OS, working context

Read this first, then the files in `knowledge/`. This repo is the plugin that manages the existing Notion
**Travels & City** database: six skills, three shared standards, three canonical page specs.

> Proprietary and confidential. Internal use only, see `LICENSE`.

## Operator

**Aron Clementi (Clem)**, Lugano. Does Bitcoin business development, travels for it, trains every day. The
pages this repo writes are written for him and for nobody else: that is why the work sections cover how
business is actually conducted on the ground rather than a country's GDP, why a gym line carries a day pass
price near where he sleeps, and why food is two lists instead of one.

## Style, and it is not negotiable

- **Italian in everything that goes to the user**, and in every page written into Notion. The repo's own files
  are in English.
- **No em dashes and no en dashes.** Anywhere, in any language, in prose or in a table. Commas, full stops,
  colons. This is a standing rule with no exceptions, and it is checked in every verification pass.
- **Correct accents**: è, più, città, già, perché, martedì, attività, connettività. Writing `e` where `è`
  belongs makes the page ungrammatical, and it has shipped twice.
- 24 hour times. Prices in local currency with a CHF conversion and the rate with its date.
- Where a figure cannot be verified, `da verificare`. Never a guess, and never a placeholder.
- **A page has a character budget and a form contract**, see the section below. Prose is the exception in
  this database, a table is the default.

## Density, and the numbers are the rule

The pages had become a broth of words: two hours to read one city and the datum not findable. Measured on
2026-09-25 across fourteen live pages, the median City body was **84,569 characters** and the three Chinese
city pages named as the length reference measured **83,804**, so the reference had drifted too and there is
no short page left to copy. The caps below are the reader's own "half would have been enough", made
checkable. Full derivation in `knowledge/page-standard.md`, `Density budget`.

| Cap | Limit |
| --- | --- |
| City page body, total | **42,000 characters** |
| Nations page body, total | **32,000 characters** |
| One numbered section | **4,500 characters** |
| History toggle, `City History` or `Storia del paese` | **3,500 characters** |
| One table cell | **300 characters** |
| One block of prose | **3 consecutive lines**, then a table or a list |

**Measured, not estimated:** count the characters of the `<content>` block as `notion-fetch` returns it,
markup included. Per section, from one `## N.` heading to the next. A page over a cap is compressed and then
saved, never saved and flagged.

**Form, because caps alone give shorter pages that still cannot be read.** Full rules in
`knowledge/page-standard.md`, `How to write a line`.

- **A table beats a paragraph** whenever there are more than two comparable entries. **Tables are the
  default format of this database, prose is the exception.**
- **One line, one fact.** No sentence explaining that the fact is interesting.
- **Bold on the search key**, the name or the price or the time. Never on a whole clause.
- **The link on the name.** Never on `clicca qui`, never on a sentence.
- **No connective or editorial sentences.** `vale la pena notare che`, `è importante ricordare che` and
  every variant go, the fact behind them stays.
- **No datum in two sections.** Written twice, it becomes two figures that disagree.
- **A caution clause becomes `da verificare`**, or one note at the end of the section.
- **`Do`, `Don't` and `Cosa non dire` are lists**, never paragraphs, on both page types.
- **The history toggle is nested inside section 1** on both page types, never above it.
- **Compressing is not cutting.** Every fact, figure, address, hour, link and `da verificare` entry
  survives, only the words around them go. A count that fell because content left the page is damage, not
  compression.

## The repo standard

`../SKILL-REPO-STANDARD.md` in the skill workspace is the standard every skill repo here follows, and this one
follows it. What it means day to day:

- Source in `skills/<name>/SKILL.md`, frontmatter `name` equal to the folder name.
- Every `description` is a `>-` block scalar, non empty, under 1024 characters. A plain scalar breaks the
  moment the text contains `: `, and the symptom is a skill that silently never installs.
- Everything a skill reads lives in its own `references/`, with one exception: the genuinely cross skill
  standards in `knowledge/`, which `build.py` bundles into every package at the path the citations already use.
- A skill never cites a file that is not there. A dangling citation does not error, the agent simply proceeds
  without the rules it was told to follow.
- No `examples/`, no source material, no dates or versions in filenames.
- One version number, in four places: `plugin.json`, both places in `marketplace.json`, the README badge and
  the top entry of `CHANGELOG.md`.

## The repo is the source of truth, Notion is the mirror

This was the other way round until 1.2. Now:

- `knowledge/templates/nations-spec.md`, `city-spec.md` and `travel-spec.md` are **canonical**. They are what a
  skill reads to know the required shape of a page.
- The three default templates in Notion are the **mirror**, kept aligned to the specs. Where the two diverge,
  the spec wins and the Notion template is what needs updating.
- A spec is edited first, then the change is pushed to the Notion template **by addition only**, with
  `insert_content` or a targeted `update_content`, never `replace_content`. Procedure in
  `knowledge/template-sync.md`.
- The three `*-template.md` files are historical snapshots of 2026-09-24 before the 1.2 additions. They are not
  the specification, nothing reads them to decide how a page should look, and **they are not edited**.
- The one limit that survives: a page created by clicking New page inside the database by hand starts from the
  Notion template, not from the spec. Nothing in this repo can intercept that click, which is why the two are
  kept aligned rather than allowed to drift.

## Operating rules on Notion

Compact, and each one is a defect that already happened.

1. **The environment is correct.** Never add a property, rename a data source, or create a parallel database.
   Fill and repair what is there.
2. **`Maps` exists on City.** It is a url property, and it is populated **at property level**, not as a row
   inside the page body. A link in the body leaves the property empty and the link invisible to every query.
3. **Relations resolve one way.** Nation page first, then the city with its `Nation` already set, then the trip
   with both relations. Set `Nation` on the City and `Cities` fills itself.
4. **Read a relation off the page content, do not guess it.** A city goes on a trip because the page says he
   went there, not because the dates roughly fit. And check which data source a relation field points at: a
   `City` field pointing at Nations looks populated and matches nothing.
5. **Parallelise by group of pages, never by class of defect.** Two agents on the same pages with
   `update_content` overwrite each other silently. One data source or one disjoint cluster per agent.
6. **Never `replace_content` on a page that has content.** One exception: a generation migration, and only
   after the block by block mapping is complete.
7. **`notion-fetch` can return a stale snapshot.** Before a structural intervention, force a refresh with a
   micro edit and fetch again, or the edit lands against a version that no longer exists.
8. **A placeholder is worse than a declared hole.** Where the data does not exist, write that it was never
   recorded. `[Amount]` left in a page is a silent lie.
9. **Re-fetch and verify after every page.** The section count never decreases.
10. **The web search budget is shared and finite.** When it runs out, fall back to direct fetch on official
    URLs already known and write `da verificare`, never a figure that was not checked.
11. **What comes out of a table moves, it is not deleted.** A Top 10 cut to Top 5 sends the other five to a line
    of text underneath.
12. **Nothing is deleted.** A duplicate is parked under a page outside the databases with a note saying why and
    what replaced it. Deleting is the user's click.
13. **Every link is the official site of the thing it names, or there is no link.** If the official URL cannot
    be found, the name stays and the link goes. Never swap a fake link for another generic one.
14. **Sensitive documents stay in Drive.** Passports, visas, eVisas, ID scans, health notes, account
    statements. They never enter a Notion page, a report, this repo, or anything it produces.

## Map

- `knowledge/` the shared standards: `notion-travel-db.md` the map of the database, `page-standard.md` the fill
  contract, `research-standard.md` what must be checked live, `drive-convention.md` the trip folder,
  `template-sync.md` the direction of truth, `templates/` the three canonical specs.
- `skills/` six skills. Reference layer: `nation-city-pages`. Trip: `trip-itinerary`,
  `pre-departure-check`. Timers: `travel-scheduler`. Maintenance: `travel-db-audit` finds,
  `travel-db-repair` fixes.
- `README.md` the presentation and the catalog. `HANDBOOK.md` skill by skill, in the order they run.
  `SETUP.md` connectors and first use. `CHANGELOG.md` version history with the reasoning. `ROADMAP.md` what is
  next.

## Verify before every commit

```
python3 scripts/build.py --check
```

Six skills, no `FAIL`, no dangling citations. Read the warning lines as well as the exit code: a dangling
citation is a warning and it is still a skill running without the rules it was given.
