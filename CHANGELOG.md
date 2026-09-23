# Changelog

## 1.0

First release.

Four skills: `nation-city-pages`, `trip-itinerary`, `pre-departure-check`, `travel-db-audit`. Three shared standards in `knowledge/`, bundled into every package.

Extracted from the Helsinki and Warsaw trip of September 2026, where four of the defects this repo now prevents happened in sequence:

- **Template sections filled generically.** The Nations and City templates were complete and were treated as a suggestion. History, food, customs and politics came back thin and had to be rewritten in a second pass. `page-standard.md` now makes the template the specification and defines the verification pass that decides whether a page is finished.
- **One trip split across two pages.** Helsinki and Warsaw were written as separate itineraries because they were separate cities. They were one trip. `notion-travel-db.md` now states the rule and `trip-itinerary` enforces it.
- **Agenda conflicts found by the reader, not by the tool.** A recurring call sat inside the return flight window and nobody noticed until the page was read. `trip-itinerary` now hunts for those actively and puts them in a red callout at the top.
- **Prose written without accents.** Two itinerary pages shipped with `e` where `è` belonged, plus the em dashes that are a standing prohibition. Both are now explicit checks in the verification pass.

The build script is the standard one, with `SHARED` reduced to `knowledge/` since this repo has no `templates/`.
