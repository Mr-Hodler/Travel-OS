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

## City and Nations pages carry no trip data

**They are permanent and independent of every trip.** Dates, flights, arrival and departure times, the
address of the accommodation, booking references, a line like `lavoro da remoto e palestra ogni giorno`:
**none of it goes on a City or a Nations page.** It lives on the Travel page of that trip and nowhere else.

**The test: if a line becomes false next month because the trip is over, it is in the wrong place.** What
stays true regardless of who passes through and when, stays.

The corollary: a City page is about the city, not about the posting. `Palestre con day pass` belongs on it,
`la mia palestra di questo viaggio` does not.

This is the correction of a defect that really happened, not a precaution. An agent wrote the dates, the
flights and the accommodation of the Warsaw trip into the Warsaw City page, where they were right for one
week and wrong for good afterwards. The data was not wrong, it was on the wrong page, which is why the fix
is a move and never a deletion: `travel-db-repair` carries it over to the Travel page.

## Density budget

The cap on markdown characters was the wrong metric. Table markup is not read, so counting it measured the
page against something no reader ever crosses. **What is measured is the visible text**: the text the eye
has to cross to find a datum, markup excluded.

And the lever is not a shorter page, it is **two levels in every heavy section**. First the operational
essentials, visible the moment the section opens. Then one toggle `Dettaglio: <what it holds>` carrying
everything else. **Nothing is deleted, it is moved one level down.**

Caps, all counted on the visible text:

| Cap | Limit |
| --- | --- |
| What an open section shows, before its `Dettaglio` toggle | **900 characters**, so 3 to 6 lines |
| `⚡ Scheda rapida` | **1,200 characters** |
| `🔁 Da riverificare prima di partire` toggle | **1,200 characters** |
| First level of the history toggle | **2,500 characters**, one line per period, carrying the fact that explains why that period matters today. A few words more than a bare timeline, and not a book. Dates, names and figures go into a nested `Dettaglio: date, nomi e cifre` |
| One table cell | **300 characters** |
| One callout | **4 lines** |
| One run of prose | **3 consecutive lines**, then a table or a list |
| A `Dettaglio` toggle | no cap. It holds everything the first level does not |

**The declared exception.** On a Nations page, `Do`, `Don't` and the two food tables stay at the **first
level of section 7**. They are what the reader opens that section for, and a toggle in front of them costs
a click at the moment they are needed.

**The three levers that actually cut, in order of return.**

1. **Merge table rows that were split for no reason.** Every pair of the shape `Voce` plus `Voce, la
   sanzione`, or `Voce` plus `Voce, come si sta`, becomes **one row**. It is the most profitable cut: it
   removes the markup and the repeated label at the same time.
2. **Deduplicate across sections.** The second copy becomes a one line pointer, `sez. N`. It is done in the
   less pertinent section, never in the one where the datum is actually used.
3. **Turn descriptive prose into one fact per line.**

Do not use the list to table lever on short lists: the markup costs more than it saves.

**Measured on the pilot, five pages, visible characters before and after:** Poland **83,139 to 15,059**,
Helsinki **80,208 to 10,628**, Warsaw to **10,713**, Kraków **44,822 to 17,465**, Finland **49,409 to
16,089**. **Zero facts lost**, verified by counting distinct numbers, links, proper names and
`da verificare` entries before and after.

**How to measure it.** `notion-fetch` the page, strip the markup, and count what is left section by
section with the `Dettaglio` toggles closed. `notion-fetch` on a page of this size exceeds the token limit
and saves to a file: it is analysed with python, never read into context.

**The budget is a ceiling, not a target.** A place with less to say is written shorter.

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
- **The form of a line is `**Etichetta.** dato, dato, dato.`** No opening sentence, no closing sentence,
  no comment around it.
- **Related facts are joined with ` · ` instead of opening a new line.** It is shorter and it reads better.
- **These formulas are forbidden, with every variant of them:** `è importante notare`, `va detto`,
  `vale la pena`, `da tenere presente`, `non è pignoleria`, `attenzione a`, `tieni presente`,
  `in generale`, `sostanzialmente`, `di fatto`, `il modo più rapido per`, `la parte che conta`,
  `il punto è che`, `tradotto`, `lettura utile`. They are deleted outright and the fact behind them stays.
- **No evaluative adjectives, no metaphors, no repeated emphasis, and no explaining why a rule is a rule.**
  The why is written only when it changes behaviour, and then in one line.
- **Dates as `GG.MM.AAAA` inside a table**, written out in full only in prose.
- **`da verificare` in backticks on every figure that expires.**

**The history toggle is nested inside section 1, not placed before it.** On a City page `City History`
sits inside `1. Quick links & Essential resources`. On a Nation page `Storia del paese` sits inside
`1. Entry, Visas, and Rules`. A toggle floating above the first numbered section opens the page with a
history lesson when what the reader wanted was a phone number.

## No lists in prose: tables and bullets

**Never an enumeration written as prose.** More than two items, each with more than one attribute, is a
**table**. One attribute per item is a **bullet list**. A paragraph that threads three venues and their
prices into one sentence is a defect even when it is short.

The link goes **on the name of the item, inside the cell**, never on a line of its own.

Mandatory columns, by kind of list:

| Kind of list | Columns, in this order |
| --- | --- |
| Things to see, attractions, experiences | `Luogo` with the link · `Cosa è e perché vale` · `Costo` · `Orari` · `Tempo che serve` · `Hidden gem` |
| `Cibo da provare` and `Cibo strano` | `Piatto` · `Cosa è` · `Dove`, the venue with its link or the kind of place · `Costo` |
| Districts | `Quartiere` · `Per chi va bene` · `Costo` · `Cosa evitare` |
| Coworking, gyms, services | `Nome` with the link · `Zona` · `Prezzo` · `Note` |
| Events and conferences | `Evento` with the link · `Quando` · `Dove` · `Costo` |
| Venues, bars, restaurants, work cafes | `Nome` with the link · `Zona` · `Per cosa` · `Costo` |

In the `Hidden gem` column, `💎` goes only where it truly is one, so they are found at a glance. A
missing datum is `da verificare`, and where a place has to be booked ahead it is said in the `Orari` column.

**`Do` and `Don't` stay bullet lists.** One attribute per line is the whole point of them.

## How the activities are organised

An alphabetical list of monuments is of no use to anybody. The activities section is organised **by the way
it is used**, in this order:

1. **`Se hai mezza giornata` and `Se hai un giorno`.** Two or three lines each, what to do in concrete
   terms, nothing around it.
2. **`Da vedere, per zona`.** The big table with the mandatory columns above, **grouped by district and
   never in alphabetical order**, so it fits the way the day actually moves.
3. **`💎 Hidden gem`.** A **separate table**, never rows mixed into the one above. They are what the page is
   worth and they have to stand on their own.
4. **`Itinerari a piedi`.** One or two routes, each one a single row: where it starts, the stops, how long
   it takes.
5. **`Fuori città`.** The mandatory table of at least three destinations reachable for a full day or with
   one overnight, not local activities.

In the big table the `Orari` column also says **whether the place has to be booked ahead**, because that is
the information that makes a visit fail.

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

## The footer is one line

Every page ends with **one single line**, and nothing else:

```
Aggiornata il <data>. Fonti: <elenco>.
```

The `🗓️ Ultimo aggiornamento` block is gone, and so is every note on compression and every
declaration of density. They were noise: four lines of metadata standing in front of the reader to carry a
date and a name.

The spec version the page was written against still matters, and it goes on that same line whenever it is
not the current one, as `spec city-spec.md 1.4`. Templates evolve, and a page can be complete against last
year's spec and incomplete against the current one with nothing on it that looks wrong. Without it the only
way to find out which pages are behind is to open all of them and compare section by section, which is how
a migration ends up costing more than the writing it is meant to fix. `travel-db-audit` reads that line the
same way.

## The verification pass is not optional

After writing, re-fetch the page and check:

- no residual placeholder: `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`, `[Amount]`, `YYYY-MM-DD`
- no empty table cells
- no table row still generic
- no template instruction callout left in the page
- every section the template has is present and numbered correctly
- no em dashes in prose, no missing accents
- `⚡ Scheda rapida` is the first block of the page, outside every toggle, within **1,200** visible
  characters
- `🔁 Da riverificare prima di partire` is the second block and it is a toggle, within **1,200**
  visible characters
- every heavy section carries its own `Dettaglio` toggle, and what the section shows before that toggle is
  within **900** visible characters
- the first level of the history toggle is within **2,500** visible characters, one line per period with
  the fact that explains why it matters today, and the dates, names and figures in the nested
  `Dettaglio: date, nomi e cifre`
- no table cell over **300** characters, no callout over **4 lines**, no run of prose longer than
  **3 consecutive lines** where a table or a list would carry it
- on a Nations page, `Do`, `Don't` and the two food tables are at the first level of section 7
- no enumeration written as prose where the mandatory columns of its kind apply
- **no trip data anywhere on the page**: no dates, no flights, no accommodation address, no booking
  reference. Every line still true once the trip is over
- `⚠️ Zone da evitare` is present, and it says so explicitly where there is nothing to avoid
- `Cambio rapido` is in the `⚡ Scheda rapida`, with 10, 50, 100 and 500 CHF converted at the stated rate,
  except where the local currency is the CHF
- `Fuori città` carries **at least three** destinations, each with how it is reached and whether it is a day
  or an overnight
- the activities are grouped **by district**, not alphabetically, and the `💎 Hidden gem` entries are in a
  table of their own rather than mixed into the main one
- the `Orari` column says whether a place has to be booked ahead
- the history toggle is nested inside section 1, not floating above it
- no `🗓️ Ultimo aggiornamento` block left, and no declaration of density anywhere
- `Do`, `Don't` and `Cosa non dire` are lists, not paragraphs
- no datum repeated in two sections
- every link is the official site of the thing it names, or there is no link, per the link contract above
- no generation residue anywhere: no `utm_source=`, no `([turn0searchNN])`, no search result URL in place of a site
- the footer is the single line `Aggiornata il <data>. Fonti: <elenco>.`

A page that fails any of these is not finished.
