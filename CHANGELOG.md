# Changelog

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
