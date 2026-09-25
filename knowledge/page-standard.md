# Page standard

The contract every page written into the Travels & City database obeys.

## The template is the specification

The specification lives in this repo. `knowledge/templates/nations-spec.md`,
`knowledge/templates/city-spec.md` and `knowledge/templates/travel-spec.md` are
canonical: they carry the whole structure of their data source plus the additions
the Notion template did not originally have, and they are what a skill reads to
know the required shape of a page. The default template in Notion is a mirror of
the spec and is kept aligned with it; where the two diverge the spec wins.
`knowledge/template-sync.md` holds the direction of truth, the alignment
procedure and the one limit that matters, which is that a page created by
clicking New page in Notion starts from the Notion template and not from the
spec. The three `*-template.md` files are historical snapshots of how the
templates looked before 2026-09-24 and are not the specification.

Each data source has a default template. It is complete and it was designed deliberately. Reproduce its structure to the letter:

- every `## N. <emoji> <Heading> {toggle="true"}` section, in order, numbered as in the template
- every sub-heading under it
- every table, with the same columns in the same order
- every `<details><summary>` toggle

Then fill every single point. **A point left empty, generic, or still carrying the template placeholder is a defect, not brevity.** Synthetic and complete are not in tension: one dense line per point, never a point skipped.

Remove from the finished page: the `Jarvis` instruction callout, the `Operational instructions` block, and any `Guidance` meta-block. Keep the `Read first: open the Nation page` callout on city pages, translated.

## What the template does not cover but is always required

Everything in this section is now also written into the three specs, so a skill
reading the spec finds it in place. It is repeated here because this file is the
fill contract and the reasons belong with it.

**Nation pages.** A `<details>` toggle titled `Storia del paese`, **nested inside section 1** as the first block of `1. Entry, Visas, and Rules`. It used to sit before section 1 and it was moved in 1.4: the first thing the page shows must be operational, not historical. Dense prose on why the country is the way it is today, not a chronology of dates, inside the 3,500 character cap above.

**City pages.** The `City History` toggle is nested inside section 1 and written dense. One line is a failure, and so is anything over the 3,500 character cap above.

**City pages, section 8 food.** Two separate lists, not one:
- `Da provare, buoni`, the dishes worth eating
- `Da provare, strani o divisivi`, the ones that test a foreigner

For every entry: what it is, what to expect, and where to actually get it with a real address.

**Culture sections.** Concrete `Do` and `Don't` lists, specific to the place. Include the taboos that would cause real offence, and say why. Generic guidebook politeness is filler.

**Politics.** Who governs today, by name, web-verified. Never from model memory.

**Embassies.** Swiss and Italian, with address, phone, email and the out-of-hours consular emergency number.

**Work sections.** The reader does Bitcoin business development. Local crypto regulation and its current real state, exchanges, community, VC, and how business is actually conducted on the ground.

**Gym and daily routine.** Day-pass gyms with prices near where the reader is staying. He trains every day.

## Density budget

Measured on 2026-09-25 across fourteen live pages of the database. The City median body was
**84,569 characters**, and the three Chinese city pages held up as the length reference measured
**83,804**: they are not shorter than the rest, the whole database drifted together. The reader's
verdict was that half the text would have been more than enough. The caps below are that halving,
made checkable.

**The rule the caps serve:** a datum is found in twenty seconds, a page is read in five minutes.

| Cap | Limit | Measured against |
| --- | --- | --- |
| City page body, total | **42,000 characters** | half the City median of 84,569. Chinese reference median 83,804, Dubai 106,835, Lugano 48,823 |
| Nations page body, total | **32,000 characters** | Nations median 52,595, so above half of it. Switzerland 38,966 and Thailand 35,295 are the closest today, Poland 97,892 is the outlier |
| One numbered section | **4,500 characters** | section medians today: 6,925 on a city page, 4,331 on a nation page. The worst single section measured 21,499 |
| History toggle, `City History` or `Storia del paese` | **3,500 characters** | `City History` median 3,522, Switzerland 3,107, Thailand 3,175. Poland's `Storia` measured 11,003 |
| One table cell | **300 characters** | the median cell is 25 characters. Between 1 and 12 cells per page exceed 300 today, the worst 1,470 |
| One block of prose | **3 consecutive lines**, then it becomes a table or a list | measured runs of consecutive prose lines run from 3 to 8 |

**How to measure it before saving.** `notion-fetch` the page and count the characters of the
`<content>` block, markup included. That is the number the caps are written in and the only count two
agents will agree on. Per section, count from one `## N.` heading to the next. A page over its cap is
not saved: it is compressed, then saved.

**What the budget buys.** 42,000 characters over ten sections plus a preamble and two footer blocks is
about 3,700 characters a section, roughly 530 words, under a minute at skim speed. The preamble plus
the three toggles a reader actually opens comes to about 16,000 characters, and that is the five minute
page.

**The budget is a ceiling, not a target.** A city with less to say is written shorter. Lugano at 48,823
characters is the shortest city page in the database and it is not the worst one.

## How to write a line

The caps say how much. This section says how, and it is where the characters are actually recovered.

- **A table beats a paragraph.** Whenever there are more than two comparable entries, they go in a
  table. **Tables are the default format of this database and prose is the exception**, used only where
  the entries are not comparable and the reasoning itself is the content.
- **One line, one fact.** No sentence whose job is to explain that the fact is interesting.
- **Bold goes on the search key**, the name, the price or the time the eye is hunting for. Never on a
  whole clause and never on a whole sentence: a page where everything is bold has nothing bold.
- **The link goes on the name.** Not on `clicca qui`, not on a whole sentence, not on a verb.
- **No connective, contextual or editorial sentences.** `vale la pena notare che`, `è importante
  ricordare che`, `da tenere presente che` and every variant are deleted outright. The fact behind them
  stays.
- **No repetition between sections.** A datum lives in exactly one place. Other sections name it and
  point at it, they do not restate it. A figure written twice becomes two figures that disagree.
- **A caution clause becomes `da verificare`**, or one note at the end of the section. It never becomes
  a sentence and it never becomes a paragraph of hedging.
- **`Do`, `Don't` and `Cosa non dire` are always lists**, one line per entry, on both page types. A
  paragraph of etiquette advice is unreadable at the moment it is needed, which is standing in a room.
- **Compressing is not cutting.** Facts, numbers, addresses, opening hours, links and `da verificare`
  entries all stay. If the character count fell because a fact left the page, that is not compression,
  it is data loss, and the page is worse than when it was too long.

**The history toggle is nested inside section 1, not placed before it.** On a City page `City History`
sits inside `1. Quick links & Essential resources`. On a Nation page `Storia del paese` sits inside
`1. Entry, Visas, and Rules`. A toggle floating above the first numbered section opens the page with a
history lesson when what the reader wanted was a phone number.

## Style

- Italian. Direct, concise, prose where prose reads better than bullets.
- **No em dashes or en dashes in prose.** Commas, full stops, colons. This is a standing rule with no exceptions.
- Correct accents: è, più, città, già, perché, martedì, attività, connettività. Writing `e` where `è` belongs makes the page ungrammatical.
- 24-hour times.
- Prices in local currency with a CHF conversion and the rate stated.
- Real official links only. If the URL cannot be found, write the name without a link. Never invent one.
- Where a figure cannot be verified, write `da verificare` rather than guessing.
- A date in the footer: when the page was last brought current.

## Link contract

Every link on a page is either the official site of the thing it names, or there is no link. There is no
third option, and "a link that is roughly about the right subject" is the defect this section exists to stop.

**Fake sources are the most dangerous defect a page can carry**, because they are invisible: the page looks
filled, reads as researched, and cannot be checked. Nothing about it is wrong on the surface.

The signals, both seen in real pages:

- **Many `Link` cells pointing at the same generic portal.** One row linking a national tourist board is
  normal. Fifteen rows all linking the same one means nobody looked anything up, and the table is decoration.
- **Generation residue.** `utm_source=chatgpt.com` and other tracking tails, `([turn0searchNN])` markers left
  in the text, a search result URL standing in for a site, a link whose visible text and whose target do not
  name the same thing.

The rule, without exception: **look for the real official site, and if it is not found remove the link and
leave the name.** A name with no link is honest, and the reader finds it in five seconds. A plausible link to
the wrong place costs him the trip.

**Never replace a fake link with another generic one.** Swapping one aggregator for another closes the
finding on paper and leaves the page exactly as unverifiable as it was.

Where one cell in a table is a fake source, the whole table is checked cell by cell. Fake links arrive in
batches, because whatever produced one produced the row beside it.

## Generation marker

Every page carries at the end an `Ultimo aggiornamento` block, and that block names **the date and the
version of the spec the page was written against**.

```
## 🗓️ Ultimo aggiornamento
- **Data:** 2026-09-24
- **Chi:** nation-city-pages
- **Cosa è cambiato:** one line, so the next reader knows what was touched
- **Spec seguita:** city-spec.md, Travel OS 1.3
```

The date alone is not enough. Templates evolve, and a page can be complete against the spec of a year ago
and incomplete against the current one with nothing on it that looks wrong. Without the marker, the only way
to find out which pages are behind is to open all of them and compare section by section, which is how a
migration ends up costing more than the writing it is meant to fix.

With the marker, a future migration reads the footer, compares the spec version against the current one, and
knows what is old without opening anything. `travel-db-audit` reads it the same way, and a page whose marker
names no spec version is itself a finding.

## The verification pass is not optional

After writing, re-fetch the page and check:

- no residual placeholder: `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`, `[Amount]`, `YYYY-MM-DD`
- no empty table cells
- no table row still generic
- no template instruction callout left in the page
- every section the template has is present and numbered correctly
- no em dashes in prose, no missing accents
- the body is inside its cap: 42,000 characters on a City page, 32,000 on a Nations page, counted on the
  `<content>` block as `notion-fetch` returns it
- no numbered section over 4,500 characters, no history toggle over 3,500, no table cell over 300
- no block of prose longer than 3 consecutive lines where a table or a list would carry it
- the history toggle is nested inside section 1, not floating above it
- `Do`, `Don't` and `Cosa non dire` are lists, not paragraphs
- no datum repeated in two sections
- every link is the official site of the thing it names, or there is no link, per the link contract above
- no generation residue anywhere: no `utm_source=`, no `([turn0searchNN])`, no search result URL in place of a site
- the generation marker is present: `Ultimo aggiornamento` carries the date and the spec version followed

A page that fails any of these is not finished.
