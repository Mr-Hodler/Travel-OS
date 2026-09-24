# Changelog

## 1.2

**The direction of truth is reversed: the repo is the source of truth for the three page templates, and the templates in Notion are the mirror.**

In 1.1 Notion held the master and `knowledge/templates/*-template.md` held a verbatim snapshot of it. That arrangement could describe the templates and never improve them: an addition had to be made in Notion by hand first, and until someone did, the repo was the wrong place to write down what a page should contain. Three files are now canonical, `knowledge/templates/nations-spec.md`, `city-spec.md` and `travel-spec.md`. Each carries the whole structure of its data source, section by section, table by table, toggle by toggle, plus the additions below. The three `*-template.md` files are kept as history: they are the snapshot of 2026-09-24 as the templates stood before the additions, which is what makes the change readable as a diff. They are not maintained and nothing reads them to decide how a page should look.

The three Notion default templates were brought up to the specs the same day, by addition only. Every section, table, row and callout that was already there was left exactly as it was, the Jarvis instruction callouts included, and the new blocks were inserted around them. `insert_content` was used where appending was enough and `update_content` with targeted replacements where a table row or a block had to land at a precise point; `replace_content` was not used on those three pages and should not be. Section counts before and after: Nations 9 and 9, City 10 and 10, Travel 5 and 5, with the new unnumbered blocks on top.

What each template gained:

- **Nations.** A `Storia del paese` toggle before section 1, with the arcs to cover and why the reader needs them. In section 2, rows for the CH and IT consular emergency numbers, distinct from the embassy switchboard, because the switchboard is closed when it matters. In section 4, a `Costi tipici nel paese` table, caffè, pranzo, cena, taxi urbano, birra and a weekly supermarket shop, in local currency and CHF with the rate and its date stated. In section 6, a `Fare business nel paese` block: working hours, meeting style, the dead months for holidays, negotiation style, decision timelines and the register of emails. In section 7, explicit `Do` and `Don't` lists plus a `Cosa non dire` line for the subjects that cause real offence. In section 8, `Chi governa oggi` by name with a verification date beside it. At the end, `Ultimo aggiornamento` and `Da riverificare prima di partire` listing what expires: entry rules, the security situation, who governs, and the rates.
- **City.** In section 3, a `Farmacia 24h` row with its address, and a `Rischi stagionali` block filled against the real travel window rather than in general. In section 6, explicit `Do` and `Don't` plus `Cosa non dire`. In section 7, an `Allenamento e wellness` table, Struttura, Tipo, Ingresso singolo, Orari, Indirizzo and Note, because the reader trains every day and what he needs is a gym with a day pass near where he sleeps, not a monthly membership. In section 8, two new tables added to what was already there, `Da provare, buoni` and `Da provare, strani o divisivi`, both with Piatto, Cosa è, Cosa aspettarsi, Dove and Prezzo. In section 9, `Chi accetta Bitcoin` in the city. In section 10, `Consolati e camere di commercio` and `Eventi tech ricorrenti`. At the end, the same two closing blocks.
- **Travel.** A red `DA RISOLVERE` callout at the top, above everything else, holding the open points numbered and ordered by urgency with the single action that closes each one, and saying that this is the part of the page worth the most and that it is filled by going to look rather than by waiting. In section 1, `Transfer da e verso casa`, both directions, because the home to airport leg is the one that is always missing. In section 3, an `Impegni remoti e call` table kept separate from the tours, since a trip worked from the road has calls landing inside the days. A new `Conflitti di agenda` section holding the five checks: a call inside a flight or a tour, a check-out that does not fit the departure, the time zone conversion, the closing days of what is meant to be seen, and Sundays and public holidays on reduced service. The cost summary split into `a carico azienda` and `a carico mio` with two distinct totals. A `Modo semplificato` block saying which sections to keep and which may be omitted, so four days in Warsaw does not get a template built for three weeks in China. A `Checklist finale` grouped by `Prima di partire` and then one group per city. And the `un viaggio una pagina` rule written on the page itself, including when the trip crosses more than one country.

The limit is stated in `knowledge/template-sync.md` rather than left implicit: the template Notion holds is the one applied when someone clicks New page inside the database by hand, and nothing in this repo can intercept that click. The repo being the source of truth decides which document is edited first and which one wins an argument. It does not remove the obligation to push every change through to Notion, because a spec that moves ahead alone means a hand-created page starts from an older structure.

`knowledge/page-standard.md` now points at the specs as the specification, with nothing removed from what it already said.

Version 1.2 in `plugin.json`, in both places in `marketplace.json`, in the README badge and in this entry.

## 1.1

Fifth skill: `travel-scheduler`. It owns the configuration and the maintenance of the travel system's scheduled tasks, and it does none of the work it schedules.

Two skills already declared the cadence they wanted. `pre-departure-check` asked for two one-off runs per trip, at 48 and at 12 hours, derived from the Travel page dates. `travel-db-audit` asked for a monthly sweep, silent when clean. Neither owned the mechanism, so the tasks were set up by hand when someone remembered, and five things went wrong that this skill now prevents:

- **Tasks created in the in-process scheduler never fired.** `CronCreate`, `CronList` and `CronDelete` schedule inside the session, so whatever they hold is discarded when the session ends. The call succeeds, the reminder is confirmed to the user, and 48 hours before departure nothing happens and nothing reports the loss. The skill forbids those three by name and creates every task with the `claude-code-remote` trigger tools, which outlive the session.
- **Prompts written as if the run had context.** Every firing starts a fresh session with no memory of the conversation that created the task, so "controlla il viaggio" fires into nothing. A task prompt now names the page id with its title, the trip dates, the skill and its mode, and what to produce. Four filled templates live in `references/task-prompts.md`.
- **Cron expressions written as local time.** They are evaluated in UTC and the user is in Europe/Zurich, UTC+2 in summer time and UTC+1 in winter time. Conversion is now mandatory, including shifting the day fields when it crosses midnight, and the intended local time is written next to the expression so the schedule can still be read six weeks later.
- **Tasks that fired and produced nothing.** Without automatic approval a run stops at the first action needing confirmation, which for these tasks is the first Notion write, with nobody present to answer. The approval setting is now stated in one line when the task is created, with where to change it.
- **Reference pages going stale under a booked trip.** A third task family was missing: a one-shot about ten days before departure that sends the destination pages to `nation-city-pages` in enrichment mode, since prices, opening hours, entry rules and who governs can all have moved since the page was written, and the itinerary is built on top of those pages.

Task names are fixed, `Viaggio <destinazione> <data> - pre partenza 48h` and its siblings, so a trip's tasks group together in `list_triggers` and a finished trip's tasks can be found and deleted instead of being left to expire.

Also in 1.1: `knowledge/templates/` mirrors the Nations, City and Travel default templates verbatim as the Notion API returns them, with `knowledge/template-sync.md` holding the snapshot date, the three page ids and the re-check procedure. A skill can now learn the required shape of a page without a Notion round trip, and the structure stays reviewable in git when Notion is unreachable. Notion stays the source of truth: where a mirror and the live template disagree the live template wins and the mirror is stale, and a mirror is never edited to change a template. The `SHARED` mapping bundles all of `knowledge/` into every package, so the mirrors travel with each skill and the build script needed no change, which is what the note at the end of the 1.0 entry below no longer describes.

Version 1.1 in `plugin.json`, in both places in `marketplace.json`, in the README badge and in this entry.

## 1.0

First release.

Four skills: `nation-city-pages`, `trip-itinerary`, `pre-departure-check`, `travel-db-audit`. Three shared standards in `knowledge/`, bundled into every package.

Extracted from the Helsinki and Warsaw trip of September 2026, where four of the defects this repo now prevents happened in sequence:

- **Template sections filled generically.** The Nations and City templates were complete and were treated as a suggestion. History, food, customs and politics came back thin and had to be rewritten in a second pass. `page-standard.md` now makes the template the specification and defines the verification pass that decides whether a page is finished.
- **One trip split across two pages.** Helsinki and Warsaw were written as separate itineraries because they were separate cities. They were one trip. `notion-travel-db.md` now states the rule and `trip-itinerary` enforces it.
- **Agenda conflicts found by the reader, not by the tool.** A recurring call sat inside the return flight window and nobody noticed until the page was read. `trip-itinerary` now hunts for those actively and puts them in a red callout at the top.
- **Prose written without accents.** Two itinerary pages shipped with `e` where `è` belonged, plus the em dashes that are a standing prohibition. Both are now explicit checks in the verification pass.

The build script is the standard one, with `SHARED` reduced to `knowledge/` since this repo has no `templates/`.
