---
name: travel-db-repair
description: >-
  Ripara le pagine difettose del database Notion Travels & City. `travel-db-audit` trova i difetti, questa
  li chiude: duplicati e pagine obsolete parcheggiate fuori dai database senza cancellare niente, relazioni
  ricucite leggendole dal contenuto della pagina, dati falsi verificati sul web e corretti citando la fonte,
  fonti finte rimosse invece che sostituite, pagine vecchie migrate alla spec corrente dopo la mappatura
  blocco per blocco, e la cosmetica fatta in blocco. Usala quando l'utente dice "ripara il database viaggi",
  "sistema le pagine sbagliate", "migra le pagine vecchie al template", "chiudi i duplicati", "ricuci le
  relazioni", "togli i link finti", oppure in inglese "repair the travel database", "fix the broken pages",
  "migrate old pages", "close the duplicates", "rewire the relations". Parallelizza per gruppo di pagine e
  mai per tipo di difetto. Non cancella niente e non usa `replace_content` su una pagina che ha contenuto.
---

# Travel DB repair

`travel-db-audit` finds the defects. This skill closes them. The audit lists and routes, this one writes:
page by page, class by class, in the order that returns the most working database per unit of writing.

Everything below comes out of one real maintenance pass over 81 pages of the Travels & City database. The
order of the six classes is the order that pass should have followed and did not, and the operating rules
are the ones it paid for.

## Read first, every run

| File | What it settles |
| --- | --- |
| `knowledge/notion-travel-db.md` | the three data sources, the exact and complete property schemas, relation direction, the one trip one page rule, the naming conventions |
| `knowledge/page-standard.md` | what complete means, **the density budget and the form rules in `How to write a line`**, the link contract, the generation marker, the style rules, the verification pass |
| `knowledge/research-standard.md` | which facts have to be checked live, the fallback when the search budget runs out, and how an unconfirmed figure is marked |
| `knowledge/templates/nations-spec.md` | the current required shape of a Nations page, which is the target of a generation migration |
| `knowledge/templates/city-spec.md` | the same for City |
| `knowledge/templates/travel-spec.md` | the same for Travel |
| `knowledge/template-sync.md` | that the spec wins over the Notion template, and that the three template pages themselves are edited by addition only |

## Input

A defect list. Normally the report from `travel-db-audit`, otherwise a scope from the user: one data
source, one cluster of pages, one page. **Repair without a defect list is a rewrite**, and rewriting a page
that was already correct is the one way this skill can make the database worse.

## The six repair classes, in order of return

Work down the list. The order is not preference, it is yield: the first two classes fix more of the
database for less writing than the last two, and a run that starts at class 5 spends its whole budget on
one page while the navigable database stays broken.

### 1. Duplicates and obsolete pages

Highest return in the whole skill, and almost no writing.

**Nothing is deleted.** The steps, in this order:

1. **Choose the survivor by which page holds more real content**, not by which was edited last, not by
   which has the nicer title, not by which the relations already point at. Count filled sections, filled
   table cells and real addresses. A page created yesterday with three filled sections loses to a page from
   last year with nine.
2. **Move into the survivor what only the loser has.** Read both. A single verified address, a working
   opening time, a gym with a real day pass price: these are the reason the loser is not simply abandoned.
   This is the only writing this class does.
3. **Repoint the relations** at the survivor, on every page that pointed at the loser.
4. **Move the loser out with `notion-move-pages`**, under one parking page that sits outside the three data
   sources. Last step, because once the page leaves the data source its properties and its relations are no
   longer there to read.
5. **Write on the loser why it is parked and what replaces it**, with a link to the survivor and the date.
   One short block at the top. A parked page with no note is an orphan that somebody reopens in six months.

One parking page per run, named for the run. The user deletes it with one click when he is satisfied, which
is why no page in this skill is ever deleted by an agent: deletion is one click for him and irreversible
for us.

### 2. Relations

The defect that makes the database unnavigable, and the cheapest one to close: it is a property write, no
page content is touched.

- **Read the relation off the page content, do not guess it.** A city goes on a trip's `City` relation
  because the page says he went there, not because the city is in that country and the dates roughly fit.
  A nation page mentioning a city in a list of neighbours is not a visit.
- **Set `Nation` on the City**, which auto-fills `Cities` on the Nation. The reverse does not resolve.
- **Check which data source a relation field points at.** A `City` field pointing at Nations, or a `Nations`
  field pointing at City, looks populated in the view and matches nothing in any query. It is the one
  relation defect that survives a visual check.
- A relation pointing at a page that class 1 parked is repointed, not left dangling.

### 3. Objectively false data

Not thin, not stale: wrong. A callout carrying another country's figures, a tax that was abolished given as
due, a boarding time earlier than the departure time, an embassy address in the wrong city.

- Verify on the web, then correct **citing the source and the date of consultation** in the page.
- An internal contradiction is a finding on its own: two blocks on the same page giving different numbers
  for the same thing means at least one is false, and both get checked.
- Where the true value cannot be confirmed in this run, the false one is removed and `da verificare` takes
  its place. A wrong figure left in place because the right one was not found is the worst outcome
  available.

### 4. Fake sources

The most dangerous class, because it is invisible: the page looks filled and is not verifiable.

The signals:

- **Dozens of `Link` cells pointing at the same generic portal.** One row linking a tourist board is
  normal, fifteen rows all linking the same one means nobody looked anything up.
- **Generation residue.** `utm_source=chatgpt.com` and other tracking tails, `([turn0searchNN])` markers,
  a search result URL standing in for a site, a link whose text and target do not name the same thing.

The rule, and it has no exception: **look for the real official site, and if it is not found remove the
link and leave the name.** A name with no link is honest and a reader can search it in five seconds. A
plausible link to the wrong place costs him the trip.

**Never replace a fake link with another generic one.** Swapping one aggregator for another closes the
finding on paper and leaves the page exactly as unverifiable as it was.

A table where one cell is a fake source is checked cell by cell. Fake links arrive in batches, because
whatever produced one produced the row beside it.

### 5. Generation migration

The structural defect: the templates evolve and the pages written against the previous version do not. A
page can be complete against the spec of a year ago and incomplete against the current one, with nothing
on it that looks wrong.

The procedure, and the counting is not optional:

1. **Fetch the page and the current spec.** The spec is the target, per `knowledge/template-sync.md`.
2. **Map every block of the old page to the section of the spec it belongs to**, in a worksheet, before
   writing anything. `references/generation-map.md` is the shape.
3. **Count before writing**: sections on the old page, sections in the spec, blocks mapped, blocks with no
   home, spec sections with nothing mapped to them. A block with no home is content to keep, not content to
   drop, and it goes under the nearest section or into a clearly named leftover block.
4. **Restructure only after the map is complete.** This is the **only** case in which `replace_content` is
   allowed on a page that has content, and only with the map in hand.
5. **Re-fetch and compare the counts.** Nothing that was mapped is missing, and the section count has gone
   up or stayed level, never down.
6. **Write the generation marker.** `Ultimo aggiornamento` carries the date and the spec version the page
   now follows, so the next migration knows what is old without opening everything.

### 6. Cosmetics

Empty callouts, orphan bullets left from a deleted list, missing accents, toggle titles truncated
mid-word, instructions addressed to the assistant still sitting in the page, residual placeholders like
`[Amount]` and `YYYY-MM-DD`.

Mechanical, and therefore done in bulk across every page in the cluster in one pass rather than page by
page inside the other five classes. It is the last class because it is the only one where a reader who
notices the defect can ignore it.

## Compression, the seventh class

Added in 1.4, after the reader said the pages had become a broth of words and that half the text would
have been more than enough. It is listed after cosmetics because it is the widest class in the database:
measured on 2026-09-25, **the median City page body was 84,569 characters against a cap of 42,000**, and
the three Chinese city pages held up as the length reference measured 83,804, so every page is over.

**The caps, and they are in `knowledge/page-standard.md` under `Density budget`:**

Since 1.5 the metric is the **visible text**, not the characters of the markdown, and the lever is **two
levels per section**: the operational essentials visible when the section opens, one toggle
`Dettaglio: <what it holds>` with everything else. Nothing is deleted, it is moved one level down.

| Cap, on the visible text | Limit |
| --- | --- |
| What an open section shows, before its `Dettaglio` | **900 characters** |
| `⚡ Scheda rapida` | **1,200 characters** |
| `🔁 Da riverificare` toggle | **1,200 characters** |
| First level of the history toggle | **2,500 characters** |
| One table cell | **300 characters** |
| One callout | **4 lines** |
| One run of prose | **3 consecutive lines**, then a table or a list |
| A `Dettaglio` toggle | no cap |

On a Nations page, `Do`, `Don't` and the two food tables stay at the first level of section 7. The three
cutting levers, in order of return: merge table rows split for no reason, deduplicate across sections into a
`sez. N` pointer, turn descriptive prose into one fact per line.

**How a page is compressed, in this order.** Measure first: `notion-fetch` and count the `<content>`
block, then each section from one `## N.` heading to the next, so the work starts on the section that is
actually over rather than on the one that reads badly. Then, per section: turn every run of more than two
comparable entries into a table, delete the connective and editorial sentences outright, move bold off
clauses and onto the name or the price or the time, move the link off the phrase and onto the name, reduce
each caution clause to `da verificare` or one note at the end of the section, and delete the second copy
of any datum that appears in two sections while leaving a pointer in its place. The section that is over
by the most on almost every city page is **section 7, attractions**, which measured up to 21,499
characters on its own.

**The rule that governs the whole class: compressing is not cutting.** Every fact, figure, address,
opening hour, link and `da verificare` entry survives. Only the words around them go. **This is the one
class of this skill where the obvious shortcut, deleting rows, is the failure mode**, and it is the same
rule as `what comes out of a table moves, it is not deleted` below. A page whose count fell because
content left it has been damaged, not repaired, and the damage is invisible in exactly the way a fake
source is invisible: the page looks tidy and no longer holds what the reader went there for.

**Structural fix that travels with the compression pass.** The history toggle is **nested inside section
1** on both page types. A `Storia del paese` toggle sitting above the first numbered section is a
generation defect from before 1.4: move it inside section 1 as its first block, do not rewrite it.

## Trip data on a permanent page, the eighth class

A City or Nations page is permanent. Dates, flight numbers, arrival and departure times, the address of the
accommodation, booking references and a line like `lavoro da remoto e palestra ogni giorno` belong to the
Travel page of that trip. **The test is mechanical: a line that becomes false next month because the trip is
over is on the wrong page.** It happened: an agent wrote the dates, the flights and the accommodation of the
Warsaw trip into the Warsaw City page, where every line was right for one week and wrong afterwards.

**The datum is not wrong, it is in the wrong place, so the repair is a move and never a deletion.** Deleting
it destroys a fact that was researched once and is nowhere else, and it is the same rule as
`what comes out of a table moves, it is not deleted` below.

**How a datum is moved, and the order is the whole procedure.**

1. **Find the destination first.** The Travel page for those dates: the one whose `City` relation points at
   this city and whose `Dates` contain the dates on the line. Read the relation off the content, never off a
   rough date match, per the operating rules below.
2. **No Travel page, no move.** `trip-itinerary` is what creates one, and this skill does not. Until it
   exists the lines stay where they are, collected into one `<details>` toggle on the City page titled
   `Da spostare sulla pagina Travel`, and the finding is reported open. **Nothing is removed before its
   destination exists**, because a move done in the wrong order is a deletion with extra steps.
3. **Write it to the Travel page, in the block that owns it.** Flights and times to the flight block, the
   accommodation with its address to the accommodation block, booking references to the field
   `knowledge/templates/travel-spec.md` gives them, the day by day lines into the day table. `insert_content`
   or a targeted `update_content`, never `replace_content` on a page that has content.
4. **Re-fetch the Travel page and confirm the lines are there**, verbatim, before touching the City page. A
   batched `update_content` is atomic and silent: it applies nothing and says nothing.
5. **Only then remove them from the City page**, in one contiguous operation per section rather than many
   micro edits, which drop the toggle.
6. **Keep the permanent version of the same fact on the City page.** The hotel address goes and the line on
   which district to sleep in stays. The gym of that trip goes and the day pass gyms stay. A flight number
   goes and `Aeroporto verso centro` stays. What is removed is the instance, not the knowledge.
7. **Re-fetch both pages.** The count of distinct numbers, links and proper names across the pair does not
   fall: it is the same inventory, on two pages instead of one.

**Report it as a move, naming both pages**, so the next audit does not read the City page as having lost
data.

## Operating rules, learned the expensive way

These cost more to learn than the classes above. None of them is a preference.

- **Parallelise by group of pages, never by class of defect.** Two agents working the same pages with
  `update_content` overwrite each other silently: the second write lands against a block index the first
  one moved, and neither reports anything. Assign each agent a whole data source or a disjoint cluster of
  pages, and let each one do all six classes inside its own cluster.
- **Never `replace_content` on a page that has content.** The one exception is the generation migration in
  class 5, and only with the map already made. Everywhere else it is `update_content` on a targeted block
  or `insert_content`.
- **`notion-fetch` can return a stale snapshot.** Before any structural intervention, force a refresh with
  a micro edit and fetch again, otherwise the edit is computed against a version of the page that no longer
  exists and lands in the wrong place.
- **A placeholder is worse than a declared hole.** Where the data does not exist, write that it was never
  recorded. `[Amount]` left in the page is a silent lie: it reads as a field somebody will fill, and nobody
  will.
- **Re-fetch and verify after every page**, not at the end of the cluster. The section count must never
  decrease. A page whose count went down is repaired before the next page is opened, because the cause is
  still on screen.
- **The web search budget is shared and finite.** When it runs out, switch to direct fetch on official URLs
  already known, and write `da verificare` rather than reporting a figure that was not checked. A run that
  spends its whole budget on page three leaves the rest of the cluster unverifiable.
- **What comes out of a table moves, it is not deleted.** A Top 10 cut to Top 5 sends the other five into a
  line of text underneath. The reason the row was in the table is that somebody wanted the information; the
  reason it left the table is layout, and layout is not a reason to lose content.

## Notion traps, every one of them verified on the page

These are not preferences and none of them reports an error when it happens.

- **Never modify the text of a section heading.** Notion rebuilds the block, and the rebuilt block loses
  `{toggle="true"}` and the indentation of its children. If a heading genuinely has to change, verify
  afterwards and restore both.
- **`update_content` in batch is atomic and silent.** One match that is not found means **nothing** is
  applied, and the call does not say so. Always verify by refetching.
- **Many micro operations on the same section make the toggle fall back.** A section is treated with **one
  single contiguous operation**, never with a sequence of small edits.
- **` + ` between two bold runs renders as a bullet.** Neither `\+` nor the HTML entity helps. Write `**+**`.
- **`` `da verificare` `` inside a bold run renders badly.** Write it outside the bold.
- **`replace_content` over 40,000 characters has to be split**: `replace_content` with the first block, then
  `insert_content` with `position: end`, one section at a time.
- **Omitting the closing `</details>` swallows the tail of the page.** Every toggle opened is closed,
  counted, before the write.
- **`notion-fetch` on these pages exceeds the token limit and saves to a file.** It is analysed with python
  via Bash, never read into context.
- **Never touch the database schema while repairing content**, and **diff the schema at the start and at the
  end of the pass**. A property that disappears takes its whole column with it and no page level check
  catches it, because the pages still look right.

## Order of operations

1. **Get the defect list.** The audit report, or run `travel-db-audit` first, or the user's scope.
2. **Group the pages into disjoint clusters**, one per agent, by data source or by country. Write the
   assignment down before anything starts: overlap is the failure this step exists to prevent.
3. **Per cluster, per page**: force the refresh, fetch, repair class 1 through 6 in order, re-fetch, verify,
   log.
4. **Reconcile the parking page** at the end: every parked page has its note, and no relation still points
   at one.
5. **Write the repair log.** Shape in `references/repair-log.md`.

## Verification, after every page

- [ ] the section count is the same or higher than before the repair, never lower
- [ ] nothing that was in the mapping worksheet is missing from the page
- [ ] no residual placeholder: `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`,
      `[Amount]`, `YYYY-MM-DD`
- [ ] every link is the official site of the thing it names, or there is no link
- [ ] no `utm_source=`, no `([turn0searchNN])`, no search result URL
- [ ] relations point at the surviving page and at the right data source
- [ ] `Maps` is populated on a City page, as a property and not as a row in the body
- [ ] `Drive link` is populated on a Travel page, with the folder and not a file
- [ ] no em dash and no en dash, accents correct: è, più, città, già, perché, martedì, attività
- [ ] `Ultimo aggiornamento` carries the date and the spec version the page now follows

## Guardrails

- **Never delete a page, a block or a table row that carries content.** Parked, moved, or written
  underneath. Deleting is the user's click.
- Never add a property, rename a data source, or create a database. The environment is correct.
- Never invent the corrected value. `da verificare` with the date is a legitimate result.
- Never touch `knowledge/templates/*-template.md`: they are historical snapshots, not the specification.
- The three Notion default template pages are edited by addition only, per `knowledge/template-sync.md`,
  and never with `replace_content`.
- `05_Viaggi` is read only here. No passport, visa or ID scan enters a Notion page or the repair log.
- Report in Italian. No em dashes and no en dashes.

## References

- `references/repair-log.md`: the shape of the repair log, which is the only record that a change happened.
- `references/generation-map.md`: the mapping worksheet a class 5 migration fills before it writes.

## Upstream and downstream

`travel-db-audit` is upstream: it produces the defect list and routes to here. `nation-city-pages` is the
other destination of that routing and this skill does not duplicate it: a page that is thin goes there to
be filled, a page that is wrong, duplicated, unlinked or written against an old spec comes here to be
repaired. After a repair run, the next audit should find the same page clean, and if it does not, the
repair log says what was done and the difference is a finding about this skill.

## Never touch the schema

Repair works on pages, not on the database definition. Do not add, rename or drop a property while repairing content: during the first real maintenance pass two City properties were dropped as a side effect and the loss was invisible at page level, because pages with a missing column still render correctly.

Fetch the schema of all three data sources before starting and compare it after finishing. If a property is gone, restore it and repopulate the column before declaring the pass done.
