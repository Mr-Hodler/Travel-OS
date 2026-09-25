# Changelog

## 1.4

**The pages were measured, and the measurement did not say what anybody expected.**

The feedback was blunt. The pages had become a broth of words. Reading one city took two hours and the
information he needed was not findable in it. **Half the current text would have been more than enough.**
The length reference he named was the Chinese city pages, as he had made them: straight to the point, no
useless words, no verbosity, ordered, with links and bold where they help the eye land on the datum.
Nothing was to be lost.

So fourteen live pages were fetched and counted before anything was written: Chongqing, Guangzhou and
Shenzhen as the named reference, then Zurich, Warsaw, Helsinki, Davos, Viareggio, Lugano, Dubai, and the
Poland, Finland, Switzerland and Thailand nation pages. **The Chinese pages are not shorter.** Median body
of the three: **83,804 characters**. Median of the other seven city pages: **84,569**. The ratio is 0.99.
The reference the feedback was anchored to had drifted along with everything else, because those pages have
been through the same enrichment passes as the rest, and there was no short page left in the database to
copy. Dubai measured 106,835, Viareggio 98,864, Warsaw 93,344, and Lugano, the shortest city page at
48,823, is not the worst one to read.

That result decided the method. "Start from the Chinese median and do not exceed it by much" would have set
a cap of 84,000 characters and changed nothing, so the caps are derived from the one number the feedback
actually gave, which is **half**, and from the operational rule behind it: a datum is found in twenty
seconds, a page is read in five minutes.

**The density budget, now in `knowledge/page-standard.md` and repeated in every skill that writes a page:**

| Cap | Limit | What it was measured against |
| --- | --- | --- |
| City page body, total | **42,000 characters** | half the City median of 84,569 |
| Nations page body, total | **32,000 characters** | Nations median 52,595, so above half of it. Switzerland 38,966 and Thailand 35,295 are the closest today, Poland 97,892 is the outlier |
| One numbered section | **4,500 characters** | section medians 6,925 city and 4,331 nation. The worst single section measured **21,499**, and on nine city pages out of ten the worst one is section 7, attractions |
| History toggle | **3,500 characters** | `City History` median 3,522, Switzerland 3,107, Thailand 3,175, against Poland's `Storia` at 11,003 |
| One table cell | **300 characters** | the median cell is 25 characters, so the cap only touches outliers. Between 1 and 12 cells per page exceed it today, the worst 1,470 |
| One block of prose | **3 consecutive lines** | measured runs of consecutive prose lines run from 3 to 8 |

**The caps are measured, not estimated.** `notion-fetch` the page and count the characters of the
`<content>` block, markup included, and per section count from one `## N.` heading to the next. That was
chosen because it is the only count two agents will agree on and because it needs no tooling that does not
already exist in every skill. A page over its cap is compressed and then saved, never saved and flagged.

**Caps alone would have produced shorter pages that are just as hard to read**, which is why the other half
of the change is a form contract, `How to write a line` in the same file. **A table beats a paragraph**
whenever there are more than two comparable entries: tables are now stated to be the default format of this
database and prose the exception, which is the reverse of what the style rules said before. One line, one
fact, with no sentence whose job is to say that the fact is interesting. Bold goes on the search key, the
name or the price or the time the eye is hunting for, never on a whole clause, because a page where
everything is bold has nothing bold. The link goes on the name, never on `clicca qui` and never on a
sentence. Connective and editorial sentences go outright, `vale la pena notare che` and `è importante
ricordare che` and every variant, with the fact behind them kept. No datum lives in two sections, because a
figure written twice becomes two figures that disagree. A caution clause becomes `da verificare` or one note
at the end of the section, never a paragraph of hedging. `Do`, `Don't` and `Cosa non dire` are lists on both
page types, never paragraphs, because a paragraph of etiquette advice is unreadable at the moment it is
needed, which is standing in a room.

**And the rule that governs all of them, stated everywhere the caps are stated: compressing is not cutting.**
Every fact, figure, address, opening hour, link and `da verificare` entry survives the pass. Only the words
around them go. A page whose character count fell because content left it has not been compressed, it has
been damaged, and the damage is invisible in exactly the way a fake source is invisible: the page looks
tidy, reads well, and no longer holds what the reader opened it for. It is the same principle as
`what comes out of a table moves, it is not deleted` from 1.3, applied to prose.

**The history toggle moved inside section 1.** It used to sit above the first numbered section on nation
pages, which meant the page opened with a history lesson when what the reader wanted was a phone number.
`nations-spec.md` now carries `Storia del paese` as a nested `<details>` inside `1. Entry, Visas, and
Rules`, `city-spec.md` states that `City History` is nested inside `1. Quick links` and stays there, and a
toggle floating above section 1 is now a pre-1.4 generation defect the repair skill moves rather than
rewrites.

**New entries in the specs, all of them synthetic by construction.** City section 2 gains
**`Top quartieri dove stare`**, with Quartiere, Per chi, Prezzo, Tempo dal centro and Nota, three to five
rows and no more, built to answer `dove dormo` in a single row: `Per chi` picks one profile and not three,
`Tempo dal centro` is minutes and the mode rather than the word `central`, and `Nota` is the one detail that
decides it. City section 10 gains **`Centri finanziari e distretti business`**, where they physically are by
district and by the landmark a taxi understands with the time from the centre, and **`Come fare business
qui`** as a dry list of seven points and never prose. Nations section 6 has `Fare business nel paese`
restated as a dry list. And the duplicated bullets in City section 8, where `Where to eat` appeared three
times and `What to try` twice, were collapsed: an agent reading that spec wrote the same content three times,
which was a direct contribution to the length this release exists to cut.

**`travel-db-audit` gained a defect class, `page over the density cap`**, with the procedure to measure it
rather than judge it: count the `<content>` block for the body, split on `## ` headings for the sections and
report the longest by name, then three spot checks for the history toggle, the longest `<td>` cell and the
longest run of consecutive prose lines. It is free on any page the audit already opened, so it is never a
reason to open one and never skipped on one that is open. A density finding carries the measured number
against the cap, so `corpo 106.835 caratteri su un tetto di 42.000, sezione 7 da 18.074`: the word `lunga`
is not a finding, for the same reason `incompleta` was never one.

**`travel-db-repair` gained the compression pass** as a seventh class, with the order of operations that
makes it cheap: measure first so the work starts on the section that is actually over rather than the one
that reads badly, then per section turn comparable runs into tables, delete the connectives, move bold onto
the key and the link onto the name, reduce cautions to `da verificare` and delete the second copy of any
repeated datum leaving a pointer behind. The class is listed last and flagged with the warning that its
obvious shortcut, deleting rows, is its failure mode.

**Not done here, deliberately.** No Notion page was rewritten in this release. The caps were set, measured
and written into the repo so that the agents that do rewrite the pages work to a number instead of to an
adjective.

## 1.3

**Sixth skill, `travel-db-repair`, written out of a real maintenance pass over 81 pages of the Travels & City database.**

The pass was run by hand because there was no skill for it. `travel-db-audit` was built to find defects and route them, and it was deliberately allowed to apply only three mechanical corrections: everything else was proposed. What nobody had noticed is that proposals with no destination accumulate. The audit was working exactly as specified and the database was getting worse, because a finding that is reported every month and fixed by nobody is indistinguishable from a finding that was never made. `travel-db-repair` is the write half of that pair, and the audit's routing section now names it.

**What the pass taught, in the order it taught it.**

The first lesson is that the classes of defect have wildly different returns and the order they are worked in decides how much of the database comes back. Six classes, ranked:

1. **Duplicates and obsolete pages.** The highest return in the whole skill and almost no writing, because the fix is a move and a note rather than a rewrite. Nothing is deleted. The survivor is chosen by **which page holds more real content**, counted as filled sections, filled cells and real addresses, not by which was edited last and not by which the relations already point at: a page created yesterday with three filled sections loses to a page from last year with nine. What only the loser has is moved into the survivor first, the relations are repointed, and only then does the loser go out with `notion-move-pages` under a single parking page outside the three data sources, with a block at its top saying why it is parked, what replaces it and when. The move is last because once a page leaves the data source its properties and relations are no longer there to read. The user deletes the parking page with one click, which is the reason no agent in this repo deletes a page: one click for him, irreversible for us.
2. **Relations.** The defect that makes the database unnavigable, and the cheapest to close, because it is a property write and no page content is touched. Two rules that cost time: **read the relation off the page content rather than guessing it**, so a city goes on a trip because the page says he went there and not because the country and the dates roughly fit, and **check which data source a relation field points at**, because a `City` field pointing at Nations looks populated in the view and matches nothing in any query. That last one is the only relation defect that survives a visual check.
3. **Data that is objectively false.** Not thin and not stale: wrong. A callout carrying another country's figures, a tax that had been abolished given as due, a boarding time earlier than the departure time. Verified on the web and corrected citing the source and the date of consultation. An internal contradiction is a finding on its own: two blocks giving different numbers for the same thing means at least one is false and both get checked.
4. **Fake sources.** The most dangerous class, and the one that justifies the whole skill, because it is invisible: the page looks filled, reads as researched, and cannot be checked. Two signals, both real. Dozens of `Link` cells all pointing at the same generic portal, which means nobody looked anything up and the table is decoration. And generation residue: `utm_source=chatgpt.com` tails, `([turn0searchNN])` markers, a search result URL standing in for a site. **The rule has no exception: look for the real official site, and if it is not found remove the link and leave the name.** A name with no link is honest and searchable in five seconds; a plausible link to the wrong place costs him the trip. And never replace a fake link with another generic one, which closes the finding on paper and leaves the page exactly as unverifiable as it was.
5. **Generation migration.** The structural defect: the templates evolve and the pages written against the previous version do not, so a page can be complete against the spec of a year ago and incomplete against the current one with nothing on it that looks wrong. Every block of the old page is mapped to the spec section it belongs to, the five counts are written down, and only then is the page restructured. It is the **only** case in Travel OS where `replace_content` is allowed on a page that has content, and only with the map in hand. A block with no target section is content to keep, not content to drop.
6. **Cosmetics.** Empty callouts, orphan bullets, missing accents, toggle titles truncated mid word, instructions to the assistant still in the page, residual placeholders. Mechanical, done in bulk across the cluster, and last because it is the only class where a reader who notices the defect can ignore it.

**The operating rules the pass paid for**, which are a dedicated section of the skill and a compact list in the new `CLAUDE.md`:

- **Parallelise by group of pages, never by class of defect.** Two agents working the same pages with `update_content` overwrite each other silently: the second write lands against a block index the first one moved, and neither call reports anything. Each agent gets a whole data source or a disjoint cluster and does all six classes inside it.
- **Never `replace_content` on a page that has content**, with the single exception above.
- **`notion-fetch` can return a stale snapshot.** Before a structural intervention, force a refresh with a micro edit and fetch again, or the edit is computed against a version of the page that no longer exists and lands in the wrong place.
- **A placeholder is worse than a declared hole.** Where the data does not exist, write that it was never recorded. `[Amount]` left in a page is a silent lie: it reads as a field somebody will fill, and nobody will.
- **Re-fetch and verify after every page**, not at the end of the cluster. The section count never decreases, and a page whose count went down is repaired while the cause is still on screen.
- **The web search budget is shared and finite**, across the run and across every subagent it fanned out. When it is exhausted, fall back to direct fetch on official URLs already known, then to the value already on the page with its date, then to `da verificare`. A figure that was not checked in this run is marked, never reported as current: one unchecked figure presented as verified makes every other figure on the page unusable.
- **What comes out of a table moves, it is not deleted.** A Top 10 cut to Top 5 sends the other five into a line of text underneath. The reason the row existed was that somebody wanted the information; the reason it left the table was layout, and layout is not a reason to lose content.

**A factual error about the schema is corrected.** Two agents asserted during the pass that the City data source has **no** `Maps` property. That is false. `Maps` is a url property on City, and the City schema is `Name` (title), `Nation` (relation to Nations), `Maps` (url), `Attachments` (url), `Last edited time`. No file in the repo had taken the claim on board, so nothing had to be unwritten, but the claim was made twice and would have been made a third time. `knowledge/notion-travel-db.md` now carries all three schemas as complete tables with their types and a note per property, and a dedicated block stating that `Maps` exists and that **it is populated at property level, not as a row inside the page body**: a Google Maps link written into a table row, a callout or a bullet leaves the property empty, the database view shows nothing, and the link is invisible to every query that lists the data source. A link in the body on top of the property is duplication, not redundancy.

**What the existing files gained, by addition only.**

- `knowledge/page-standard.md`: a **Link contract** section carrying the fake sources rule in full, and a **Generation marker** section requiring `Ultimo aggiornamento` to name the date **and the version of the spec the page was written against**, so a future migration reads the footer and knows what is behind without opening everything. A date alone does not say whether a page is a generation old. Three new lines in the verification pass, for the link contract, for generation residue in URLs, and for the marker.
- `knowledge/research-standard.md`: the fallback when the web search budget runs out, in order, and the rule that a figure not confirmed in this run is marked `da verificare` rather than reported.
- `skills/nation-city-pages/SKILL.md`: the link contract, the generation marker and the stale snapshot warning as a section of their own, plus four new lines in the verification pass, including that `Maps` is set as a property and not written into the page body.
- `skills/travel-db-audit/SKILL.md`: three new detection classes, fake sources, generation drift between pages written against different specs, and an empty `Maps` on a City page. Its routing section now names `travel-db-repair` as the destination of everything it is not allowed to fix.

**New at the repo root.** `SETUP.md`: the connector matrix per skill, Notion always, Spark or Gmail and Google Calendar for the two trip skills, Drive for the trip folders, the `claude-code-remote` trigger tools for `travel-scheduler`; the `05_Viaggi` folder convention and the `Drive link` join; the first use sequence, which starts with an audit and a repair before anything new is written, because a new page created beside a duplicate makes the duplicate worse; and five checks that say whether each connector actually responds. `CLAUDE.md`: what an agent reads before working in this repo, the style rules, the repo standard, the direction of truth between the repo and Notion, and the fourteen Notion operating rules in compact form.

Nothing was removed from any existing file. The three `knowledge/templates/*-template.md` historical snapshots are untouched.

`ROADMAP.md` gained what the pass surfaced: the `Maps` property to populate in bulk across the City data source, and the `da verificare` entries that accumulate across runs and have to be closed before a trip rather than carried into it.

Version 1.3 in `plugin.json`, in both places in `marketplace.json`, in the README badge and in this entry.

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
