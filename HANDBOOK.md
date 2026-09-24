# Travel OS handbook

The README presents Travel OS. This document is the manual you open with a skill about to run. For each of the six skills: the question it answers, the cases where it is the wrong tool, what it needs from you and from the skill upstream of it, exactly what lands in Notion when it finishes, how it works and the one or two rules that make its output different from a generic version of the same document, and what reads that output afterwards.

The order below is the order the skills actually run. `nation-city-pages` builds the reference layer, `trip-itinerary` builds the trip on top of it, `travel-scheduler` puts that trip's reminders in place, `pre-departure-check` verifies the trip 48 hours out when the first of those reminders fires, `travel-db-audit` keeps all of it honest between trips, and `travel-db-repair` closes what the audit finds. The last two are a pair and they run in that order: the audit is read only by design and the repair skill is the only one allowed to write against its findings.

One rule sits above all six. The Notion environment already exists and is correct. No skill adds a property, renames a data source, or creates a parallel database. They fill and repair what is there.

---

## 1. nation-city-pages

**The question it answers.** What does he need to know about this country and this city before any trip to it exists, written as one Nations page per country and one City page per city, each filled to its template and specific enough to act on in the taxi from the airport.

**When not to use it.** Not for the trip itself, which is `trip-itinerary`, and not for the sweep 48 hours out, which is `pre-departure-check`. Not on a page that is already specific and correct: enrichment mode diffs the page against the template and fills only the gaps, so a page that loses a good address because starting over was easier is a regression, not an update. Not for anything structural: a missing property or a second database is out of scope by design. And not before checking for an existing page, because duplicates are the most expensive defect in this database: relations then point at the wrong half of a country.

**What it needs from you.** The targets, as country names, city names or both. A trip ask like "Helsinki + Warsaw" expands on its own into two nations and two cities, some of which may already exist. Nothing else, because the content comes from live research and not from the conversation.

**What it needs from upstream.** Nothing. This is the first skill in the chain. It carries an internal order instead: the nation page is created before the city page, because setting `Nation` on a City auto-fills `Cities` on the Nation and not the other way round, so a city written first has to have its relations patched by hand.

**What you get back.** One Nations page, or one City page created with `Nation` and `Maps` already set, reproducing the data source's default template to the letter: every numbered toggle section in order, every sub-heading, every table with the same columns in the same order, every `<details>` block, every point answered in one dense line. On top of the template: a `Storia del <paese>` toggle before section 1 on a nation page and a dense `City History` toggle on a city page; section 8 food split into `Da provare, buoni` and `Da provare, strani o divisivi`, each entry with what it is, what to expect and a real address; concrete local `Do` and `Don't` including the taboos that cause real offence and why; who governs today by name, web verified; the Swiss and Italian embassies with address, phone, email and the out of hours consular emergency number; a work section on the local crypto regulatory state, exchanges, community and VC; day pass gyms with prices near where he is staying. The scaffolding is gone: no `Jarvis` callout, no `Operational instructions` block, no `Guidance` meta-block, while the `Read first: open the Nation page` callout stays on city pages, translated. The page is Italian, carries the date it was brought current in the footer, and has been through the verification pass on a re-fetch rather than from memory of what was written.

**How it works.** Three modes: new nation, new city, and enrichment of an existing incomplete page. Resolve the targets and check for duplicates by normalised name first, ignoring flag emoji and local variants. Then research. Then fetch the template plus the reference page for density, Finland for nations, Santo Domingo for cities. Then create, nation before city, relations set at creation. Then fill, strip the scaffolding, and verify.

Two rules make the output different from a guidebook page. The first is that **research happens with the template still closed**: opening the template first anchors the work on document mechanics instead of on what is true, which is exactly how sections come out plausible and generic, and it is why nothing that rots is ever written from model memory. Who governs, prices, opening hours, closing days, entry rules, the regulatory state and whether a venue still exists are live checks in this run, every run, and a figure that cannot be confirmed is written `da verificare` instead of guessed. The second is that **the layer above the template is written for one reader**, who does Bitcoin business development and trains every day: that is why the work section covers how business is actually conducted on the ground rather than the country's GDP, why the gym line carries a day pass price near his accommodation, and why food is two lists instead of one.

When several pages are wanted in a run, fan out one page per subagent, never two on the same page, in two waves: all nations, wait for them to land, then all cities each setting its own `Nation`. Each subagent gets `references/subagent-brief.md` verbatim plus the fetched template, the three knowledge files, its target name and the reference page id, and returns the page id and its verification result rather than the page text. The parent re-runs the verification pass on every page, because subagents mark their own homework generously.

**What consumes it.** `trip-itinerary` and `pre-departure-check` read these pages, so a thin nation page degrades every itinerary built on top of it. `travel-db-audit` sends pages back here in enrichment mode when they decay.

---

## 2. trip-itinerary

**The question it answers.** For any hour of this trip, where is he supposed to be, and what is he missing, as one Travel page assembled from the bookings that already exist in email and calendar.

**When not to use it.** Not for writing or refreshing the Nation and City pages behind the trip, which is `nation-city-pages`. Not for the final sweep 48 hours out, which is `pre-departure-check`. Not to reconstruct a booking from the conversation: if the confirmation is not in an inbox or on the calendar, the fact does not go on the page as a fact. And never to split one journey into one page per city.

**What it needs from you.** The trip, named by destinations and dates, or simply a booking confirmation that has landed with no page to hold it. Everything factual is then harvested, not asked for.

**What it needs from upstream.** The Nation pages and the City pages the trip touches, from `nation-city-pages`, before the trip page is created. Relations resolve one way, so nations exist before cities and both exist before the trip, or the relations have to be patched by hand afterwards.

**What you get back.** One Travel page, in Italian, with multiple `Nations` and `City` relations and, above section 1, the red **DA RISOLVERE** callout. Then flights and transfers one row per leg with carrier, flight number, PNR, route with terminals, local times, baggage, fare conditions, price and who paid; accommodation one row per stay with full address, check-in and check-out times, access method and the code itself, host contact, price and cancellation deadline; one single chronological table holding every fixed commitment for the whole trip in time order, across every city; the day-by-day blocks G1 to Gn with no gap; the free day if the trip has one; per-city logistics; the checklist; the cost table with the split by payer. Travel rows carry a green row background, days that work has taken in full carry a blue one, and nothing else is coloured.

**How it works.** Read the five mandatory files, fetch the Travel template, then harvest: Spark `search` bounded by `newer_than:` across all four accounts followed by `emails` with `from:` for the senders known to matter, Navan, Trip.com, Airbnb, Booking, the operating airline, the event organiser; Gmail for the body when Spark truncates to a preheader; Google Calendar over the trip dates plus a day either side. A search result too large to return is written to a file, and that file goes to a subagent with the extraction brief in `references/inbox-harvest.md`, never into the main context, because a page written with no room left to think is the failure that brief exists to prevent. Then the arithmetic: sum the costs split by payer with the exchange rate and its date, check flight durations against the time zones, check the check-out time against the departure time, and check that every night between first arrival and last departure has a bed assigned to it.

Two rules make this different from a tidy itinerary. The first is **one trip, one page**, even across borders: splitting by city duplicates the flight, hides the transfer between the legs, and makes the conflict callout impossible, because no single page then sees the whole week. The second is that **the DA RISOLVERE callout is hunted for rather than waited for**, since nothing arrives labelled as a problem. It looks for agenda conflicts such as a call scheduled while he is at altitude, missing data such as a lockbox code promised and never sent, awkward limits such as no checked baggage on a week-long trip, and inconsistencies between what he told somebody in an email and what the ticket says. Each entry is one line: what is wrong and the one action that closes it. An item with no action is an observation, and observations live elsewhere on the page. The same logic governs the daily suggestions: one per day, in a two hour slot that actually exists near where he is already going, and a day work has taken entirely stays empty of tourism, because a page that gets ignored once stops being read.

**What consumes it.** `pre-departure-check` reads the finished page 48 hours before departure, and the open items in the callout are its input. Leave them in the callout rather than deleting them: a page that hides what is unresolved makes the next skill start from nothing. `travel-db-audit` checks the page for split trips, broken relations and thin content over time.

---

## 3. travel-scheduler

**The question it answers.** The other skills know when they want to run. Who actually makes them run, at a time that means what it says, with a prompt that works in a session that remembers nothing, and who clears the tasks away when the trip is over.

**When not to use it.** Not to do any of the work it schedules: the pre-departure pass is `pre-departure-check`, the sweep is `travel-db-audit`, the page refresh is `nation-city-pages` in enrichment mode. Not before a Travel page exists, because the fire times of a trip's tasks are derived from the `Dates` start on that page and a guessed date is worse than no task: with no page it says so and stops. Not to schedule an itinerary build, which is an event and not a date. And never to schedule anything that sends a message, books a transfer or makes a purchase.

**What it needs from you.** The trip, or nothing at all when the ask is the monthly audit or an inventory of what is active. The dates, the destinations, the page ids and the related Nation and City pages are all read off the Travel page rather than asked for.

**What it needs from upstream.** The Travel page from `trip-itinerary`, for its `Dates` and its relations, before any trip task can be created. The audit task needs nothing upstream: it is scheduled once and stays.

**What you get back.** The tasks themselves, and a short report in Italian listing, per task, the name, the intended fire time in local time, the expression or the timestamp actually stored, and the approval setting. Three families. Two one-shot pre-departure tasks per trip, at 48 and at 12 hours before departure, calling `pre-departure-check` in full and short pass. One one-shot page refresh about ten days out, calling `nation-city-pages` in enrichment mode on the destination pages, because prices, opening hours, entry rules and who governs may have moved since those pages were written and the itinerary stands on them. One recurring monthly audit calling `travel-db-audit`, silent when the database is clean. Names are fixed, `Viaggio <destinazione> <data> - pre partenza 48h` and its siblings plus `Travel DB - audit mensile`, so a trip's tasks group together in `list_triggers` and a finished trip's tasks can be found and deleted rather than left to expire.

**How it works.** `list_triggers` first, so a second copy of a task does not land beside the first. Read the Travel page for dates, destinations and relations. Compute each fire instant in local time, convert it, then create: `run_once_at` for the one-shots, `cron_expression` for the monthly audit, both through `create_trigger`. Report what was created with the approval setting. On maintenance runs the same inventory drives the rest: a trip whose dates moved has its tasks updated with `update_trigger`, which keeps the run history, a finished trip has its tasks deleted, a fired one-shot is left alone because disabling itself is what it is supposed to do, and a `last_run` that comes back FAILED twice is opened and read rather than recreated blindly.

Two rules make this different from setting a reminder. The first is that **only the tools that outlive the session may create a task**, which means the `claude-code-remote` trigger tools and never `CronCreate`, `CronList` or `CronDelete`. Those run in an in-process scheduler that lives inside the session, so the task is discarded when the session ends: the call reports success, the user is told the reminder is set, and 48 hours before departure nothing fires and nothing reports the loss. It is the one defect in this repo that is invisible from both ends, which is why the skill names the forbidden tools explicitly instead of merely recommending the right ones. The second is that **a task is written for an amnesiac**: every firing starts a fresh session with no memory of the conversation, so the prompt names the page id with its title, the dates in full, the skill and its mode and the expected output, and every time is converted from Europe/Zurich to UTC with the day fields shifted when the conversion crosses midnight and the intended local time reported beside the expression. A prompt that says "controlla il viaggio" and a cron written in local time both fail the same way, at the moment nobody is watching.

**What consumes it.** The scheduled runs of `pre-departure-check`, `nation-city-pages` and `travel-db-audit`, each of which arrives with the prompt this skill wrote and nothing else. The user consumes the report, and `list_triggers` is the record afterwards.

---

## 4. pre-departure-check

**The question it answers.** The page was written days or weeks ago, so what is still open, what has changed since, and what has to happen before he walks out of the door.

**When not to use it.** Not to build the page: if no Travel page exists, the skill says so and stops, because it verifies a page and does not substitute for one. Not as the place to close an item on a guess, since closed means evidence was found. And not as an agent of purchase: nothing is sent and nothing is booked without explicit confirmation, a trip being full of non-refundable actions.

**What it needs from you.** The trip, or nothing at all when the scheduled run fires. A scheduled run carries the trip name and the page id in its own prompt, because it starts with no memory of the conversation that created it.

**What it needs from upstream.** The Travel page from `trip-itinerary`, with its DA RISOLVERE callout intact, and behind it the Nation and City pages the trip relates to.

**What you get back.** Two things. First, one short action list in Italian and nothing else, ordered by deadline with blocking items at the top, each line being the action, its deadline and why it blocks. A blocking item is one where the trip goes wrong if it is not done: a check-in window closing, a leg that does not exist, a night with no bed, no way to get in the door. Second, the Notion page updated: the DA RISOLVERE callout rewritten to hold only what is still open, closed items marked closed with their evidence, the booking reference or the message it came from, any table cell the live checks proved wrong corrected, and the footer date refreshed. The page and the list agree when the run finishes, or the next run starts from the wrong baseline.

**How it works.** Four steps. Close what was left open, verifying each item against reality rather than against the page: online check-in per leg, the bookings that were missing, the access codes, the transfers at both ends at the actual arrival time. Verify live everything in `references/live-checks.md`, weather on the real dates, strikes and works, gate and terminal, opening hours and closing days, public holidays, whether a venue still exists, security and entry advisories, the refreshed exchange rate. Re-run the calendar over the trip dates plus a day either side and compare it against the chronological table, because other people add meetings and a weekly call that was harmless in the office is a conflict on a travel day. Then output.

Two rules keep the list worth reading. The first is that **every line has to require an action, so the skill is explicit about what is not a flag**: a forecast that shifts by one degree, a rate that moves under one percent, an advisory reworded with no change of substance, a gate not yet published. Reporting those trains him to skim, and a list that gets skimmed has no function. The second is the **separation of the two kinds of rot**, things that were open and never closed against things that were correct and have since changed, with sourcing discipline on the second: the airport over a flight tracker, the operator over a news article, the ministry over a travel blog, and where two sources disagree both go in the list, labelled as disagreeing, rather than one being picked silently.

**On schedule.** Two one-off runs per trip, derived from the `Dates` start on the Travel page rather than from a recurring job, because the schedule belongs to the trip and not to the calendar. `travel-scheduler` is what creates and maintains those two runs. At 48 hours, the full pass, all four steps, while there is still time to book a transfer, chase a code or move a meeting. At 12 hours, the short pass over blocking items plus what goes stale fastest, weather, strikes, gate and terminal, plus any calendar event added since the first run, with no page rewrite unless something material changed. When a trip's dates move, both runs are re-derived and the old ones removed rather than left to fire against a date that no longer exists.

**What consumes it.** He does. The updated callout is also the baseline for the 12 hour run, and `travel-db-audit` reads the page afterwards like any other.

---

## 5. travel-db-audit

**The question it answers.** What in this database is quietly wrong, before a trip finds it instead.

**When not to use it.** Not to fix content: everything beyond three mechanical corrections is proposed and routed, not done. Not to delete or merge: a duplicate is reported with which copy should survive and why, and the merge is the user's call. Not to archive: the Travel schema has no status property, so the report hands over the list and the move is his. Not to open the whole database, which is a cost with no finding attached.

**What it needs from you.** Nothing. On demand it takes an optional scope, and unattended it derives everything from the database each time, with no stored previous report and no request for one.

**What it needs from upstream.** Nothing, and that is the point: it audits whatever the other three skills have left behind.

**What you get back.** A report in Italian in one of exactly two shapes, per `references/report-template.md`. Clean: one line, `Audit Travels & City, <data>: nessun problema`, with the count of pages listed and pages opened, and nothing else. Findings: the counts by severity, then a table of Pagina, Tipo, Problema, Gravità and Azione consigliata, then `Correzioni applicate`, then `Da verificare`. `Problema` names the token, the field or the section, so "Incompleta" is not a finding while `placeholder [Hotel 1] in sezione 6` is. `Azione consigliata` is one imperative line naming who does it: `nation-city-pages` in enrichment mode, `trip-itinerary`, or the user. Rows are ordered by severity and then by how soon a trip depends on the page. Severity is fixed so two runs agree: Alta is anything that will mislead on a trip inside the next 90 days, or a broken relation that hides a page from the trip that needs it; Media is incomplete or stale with nothing imminent depending on it; Bassa is cosmetic, naming and archiving.

Six classes are detected: incomplete pages by residual placeholder token, empty cell, generic row, missing or misnumbered section, or a leftover scaffolding block; stale data by footer date and `Last edited time` followed by a targeted live check, at 12 months, or at 6 months when a Travel page with dates inside the next 90 days relates to it; broken relations; split trips; duplicates by normalised name; and archivable trips whose dates ended more than 90 days ago.

**How it works.** Three `notion-query-data-sources` calls on Nations, City and Travel return names, relations, dates and last edited time for the whole database, which is enough to produce four of the six classes with no page opened at all. Triage from that listing, then fetch only the suspects, plus the pages attached to a trip in the next 90 days, plus the oldest handful by footer date.

Two rules separate this from a generic database report. The first is **list, do not fetch, and state the coverage**: the run says how many pages were listed and how many were opened, so the reader can see what the report does and does not cover instead of assuming it saw everything. The second is that **age is a suspicion, not a finding**: a cheap high value live check is run where it is worth it, who governs and the exchange rate, and anything else stays recorded as `da verificare` with the age that raised it, never as a corrected value the run did not verify. The three safe fixes it may apply without asking are mechanical, unambiguous and reversible, deleting a leftover `Jarvis`, `Operational instructions` or `Guidance` block, setting a City's `Nation` when exactly one Nation page matches, and adding a missing `Nations` relation on a Travel that already relates to a City of that nation, and each one appears in the table marked `corretto` and again under `Correzioni applicate`, because a change that is not in the report did not happen.

**Unattended.** Fit for a monthly schedule, plus seven days before the start date of any Travel page. The monthly task itself is owned by `travel-scheduler`. It is **silent when clean**, one line and no notification, because a monthly audit that always says something is an audit nobody reads after the third month. Unattended it reports Alta and Media only, Bassa being noise with no person present to say whether it matters, and those findings are still there on the next on demand run. The three safe fixes still apply and are still reported, and nothing else writes when no one is there to confirm.

**What consumes it.** The findings route out: incomplete or stale Nation and City pages to `nation-city-pages` in enrichment mode, split trips and thin itineraries to `trip-itinerary`, and merges, renames and archiving to the user.

---

## 6. travel-db-repair

**The question it answers.** The audit said what is wrong. Who makes it right, without deleting anything, without
two agents overwriting each other, and without a rewrite turning a page that was merely defective into a page
that has lost content.

**When not to use it.** Not to find the defects, which is `travel-db-audit`: repair without a defect list is a
rewrite, and rewriting a page that was already correct is the one way this skill makes the database worse. Not to
fill a page that is simply thin, which is `nation-city-pages` in enrichment mode: a thin page goes there, a page
that is wrong, duplicated, unlinked or written against an old spec comes here. Not to delete anything, ever, and
not to touch the three `*-template.md` historical snapshots. Not on the same pages another agent is working, which
is the whole of the parallelisation rule below.

**What it needs from you.** A defect list, normally the report from `travel-db-audit`, otherwise a scope: one data
source, one cluster of pages, one page. Nothing else, because what a page should say is in the specs and what is
wrong with it is in the report.

**What it needs from upstream.** `travel-db-audit`, for the list. It also needs the three canonical specs in
`knowledge/templates/`, which are the target of a generation migration, and `knowledge/template-sync.md`, which
says the spec wins over the Notion template.

**What you get back.** The repaired pages, and one repair log in Italian per run, shaped by
`references/repair-log.md`: one row per page with the classes repaired, what changed named as a field, a block or
a token, and the section count before and after, which is the column that catches a repair that ate content. Plus
a parking register naming every duplicate that was moved out, where it went, which page survived and what was
moved into it before the move, and the sentence saying the parking page can be deleted with one click. Plus
`Da verificare` and `Non riparato`, which are the input of the next run and are never left out to make the log
look shorter.

**How it works.** Six repair classes in a fixed order, and the order is yield rather than preference. **1.
Duplicates and obsolete pages**, the highest return in the skill and almost no writing: choose the survivor by
which page holds more real content, move into it what only the loser has, repoint the relations, then move the
loser out with `notion-move-pages` under a parking page outside the databases and write on it why it is parked and
what replaced it. The move is last, because once the page leaves the data source its properties and relations are
no longer there to read. **2. Relations**, the defect that makes the database unnavigable and the cheapest to
close, read off the page content and never guessed, with an eye on the relation field that points at the wrong
data source and therefore looks populated while matching nothing. **3. Data that is objectively false**, a callout
carrying another country's figures, an abolished tax given as due, a boarding time before the departure time:
verified on the web and corrected with the source and the date. **4. Fake sources.** **5. Generation migration**,
mapped block by block against the current spec before anything is written. **6. Cosmetics**, mechanical and done
in bulk across the cluster.

Two rules make this different from a cleanup pass. The first is that **nothing is deleted and everything that is
removed goes somewhere**: a duplicate is parked with a note rather than deleted, a Top 10 cut to Top 5 sends the
other five into a line of text underneath, a block with no home in the new structure goes under the nearest
section rather than out of the page. Deleting is one click for the user and irreversible for us, which is the
whole reason the parking page exists. The second is that **parallelisation is by group of pages and never by class
of defect**: two agents working the same pages with `update_content` overwrite each other silently, because the
second write lands against a block index the first one moved and neither call reports anything. Each agent gets a
whole data source or a disjoint cluster and does all six classes inside it.

Three more rules carry most of the remaining cost. `replace_content` is forbidden on a page that has content, with
one exception, the generation migration, and only after the mapping worksheet in `references/generation-map.md` is
complete. `notion-fetch` can return a stale snapshot, so a structural intervention forces a refresh with a micro
edit and fetches again, or the edit is computed against a page that no longer exists. And a placeholder is worse
than a declared hole: where the data does not exist the page says it was never recorded, because `[Amount]` left
in a page reads as a field somebody will fill and nobody will.

**What consumes it.** The next run of `travel-db-audit`, which should find the same pages clean. If it does not,
the repair log says what was done and the difference is a finding about this skill rather than about the page.

---

## The three shared standards

All three live in `knowledge/` and are bundled into every package at that same path, so a skill installed on its own still resolves them. Every skill that writes a page reads all three before writing anything, on every run, not once at install time. `travel-scheduler` writes no page: it reads `notion-travel-db.md` alone, to resolve the ids and dates its task prompts have to name. `travel-db-repair` reads all three plus the three canonical specs and `template-sync.md`, because a generation migration is a write against the spec and not against the page it finds.

| File | What it settles | Read it when |
| --- | --- | --- |
| `notion-travel-db.md` | the parent page, the three data source and template ids, the property schemas including the `Attachements` misspelling that stays, the direction relations resolve, the naming conventions, the reference pages worth reading for density, the one trip one page rule | before touching Notion, in any skill, and before creating anything with a relation |
| `page-standard.md` | that the template is the specification and that the canonical form of it is the matching `*-spec.md` in this repo, what is always required on top of it, the style rules, and the verification pass that decides whether a page is finished | before writing a page, and again on the re-fetch at the end; `travel-db-audit` reads it as the definition of incomplete |
| `research-standard.md` | what must be checked live every time, what may be written from knowledge, sourcing preference, and the rule that trip data comes from the inbox and never from the web | before research, in any skill; it is also what tells `travel-db-audit` which facts rot |

The ids in `notion-travel-db.md` save a search. They do not replace fetching and reading the template.

Beside the three standards, `knowledge/templates/` holds the canonical specification of each data source: `nations-spec.md`, `city-spec.md` and `travel-spec.md`. Since 1.2 the repo is the source of truth for the templates and the Notion default templates are the mirror, aligned to the specs. A skill reads the spec to know the required shape of a page without a Notion round trip, and where a spec and the live Notion template disagree the spec wins and the Notion template is what needs bringing into line. Fetching the live template is still worth doing on a run that writes a page, as a check that the two have not drifted, and `knowledge/template-sync.md` says how to re-check and how to push a change through. The three `*-template.md` files beside the specs are historical snapshots of 2026-09-24, before the 1.2 additions, and are not the specification.

One limit survives the reversal and is worth knowing: the template Notion holds is the one applied when someone clicks New page inside the database by hand. A skill writing through the API follows the spec and is unaffected; a page created by hand starts from whatever Notion holds, which is why the two are kept aligned rather than allowed to drift.

## Connectors required

| Skill | Notion | Mail | Calendar | Web |
| --- | --- | --- | --- | --- |
| `nation-city-pages` | required, read and write | no | no | required, every run, for everything the research standard lists as live |
| `trip-itinerary` | required, read and write | required: Spark across all four accounts, Gmail where Spark truncates a body | required: Google Calendar over the trip dates plus one day either side | only for context, never for booking facts |
| `pre-departure-check` | required, read and write | required, to re-check bookings and codes | required, to catch meetings added after the page was written | required, for every item in `references/live-checks.md` |
| `travel-scheduler` | required, read only, for the `Dates` and the relations of the trip a task is built around | no | no | no |
| `travel-db-audit` | required, read and limited write | no | no | targeted checks only, where cheap and high value |
| `travel-db-repair` | required, read and write | no | no | required, to verify a false figure before correcting it and to find the real official link behind a fake one |

The plugin as a whole therefore needs the Notion connector, plus Spark or Gmail and Google Calendar for the two trip skills, and Google Drive for the trip folders that `trip-itinerary` links and the two maintenance skills read. `SETUP.md` carries the full matrix, the first use sequence and the five checks that tell you whether each connector actually responds. `travel-scheduler` needs one thing no other skill uses, the trigger tools of the `claude-code-remote` MCP server: `create_trigger`, `list_triggers`, `update_trigger`, `delete_trigger`. Without them it cannot create a task that survives the session, and there is no fallback worth using.

## Build and verify

```
python3 scripts/build.py --check
```

Verification only, nothing built, exit code non-zero if any skill fails. Per skill it checks that `skills/<name>/SKILL.md` exists, that the frontmatter parses as real YAML with PyYAML when it is installed and with a fallback parser that catches the one construct that silently breaks it, a plain scalar containing `: `, that the frontmatter `name` equals the folder name, and that `description` is non-empty and under 1024 characters. All four failures are invisible otherwise: the file looks correct and the skill simply never installs.

It then reports dangling citations as a warning rather than a failure. Every `references/`, `templates/`, `examples/`, `adapters/` or `knowledge/` path any Markdown file in the skill mentions is resolved against the skill folder and the repo root, and anything missing is printed, because a skill told to read a file that is not there does not error, it proceeds without the rules it was given. Citations under a deferred marker such as "to create" or "created at runtime" are skipped, and a sibling skill's file cited without `../` is reported with the correction, since a zip cannot hold a path above its own root.

```
python3 scripts/build.py
python3 scripts/build.py trip-itinerary
```

The full build packages each skill into `dist/<name>.skill`, a zip with `SKILL.md` at the archive root, then bundles `knowledge/` into every archive at `knowledge/` and the `LICENSE` alongside it, and prints `SHARED MISSING` when that bundle did not land. Timestamps are fixed, so a rebuild with no content change produces an identical file instead of a diff. Naming a skill on the command line builds only that one.

Run `--check` before every commit, and read the warning lines as well as the exit code.
