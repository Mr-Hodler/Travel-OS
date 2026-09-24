---
name: nation-city-pages
description: >-
  Compila le pagine Nations e City del database Notion Travels & City fino al template completo, in tre
  modi: nuova pagina nazione, nuova pagina città, arricchimento di una pagina esistente incompleta. Usala
  quando l'utente dice "fai la pagina nazione", "aggiungi la città", "pagina Notion per <paese>",
  "arricchisci la pagina di <città>", "manca la scheda del paese", "completa questa pagina", oppure in
  inglese "add a country page", "city page for", "fill the nation page", "enrich this city page". Ricerca
  live prima, template dopo. Nazione prima della città, perché la relazione risolve in una sola direzione.
  Copre storia, le due liste di cibo buono e cibo strano, Do e Don't concreti, politica verificata,
  ambasciate CH e IT, lavoro tarato su Bitcoin business development, palestre con day pass, e chiude con
  la passata di verifica che dichiara la pagina finita.
---

# Nation and City pages

The reference layer of the Travels & City database. One page per country, one page per city, each complete
to its template. Trip pages read from these, so a thin nation page degrades every itinerary built on top of
it. The target is not a page that looks finished, it is a page the reader can act on in the taxi from the
airport: a real address, a real price, a real opening time, a named minister.

## Read first, every run

All three, before writing anything. They are bundled into this package at these paths.

| File | What it settles |
| --- | --- |
| `knowledge/page-standard.md` | the fill contract, what is always required on top of the template, the link contract, the generation marker, the style rules, the verification pass |
| `knowledge/notion-travel-db.md` | data source ids, property schemas, relation direction, naming conventions, the reference pages worth copying for density |
| `knowledge/research-standard.md` | what has to be checked live and what can be written from knowledge |

The environment exists and is correct. Never add a property, rename a data source, or create a parallel
database.

## Three modes

| Mode | Triggered by | Scope |
| --- | --- | --- |
| **New nation** | "fai la pagina nazione", a trip to a country with no page | one Nations page, full template, plus the history toggle |
| **New city** | "aggiungi la città", a trip to a city with no page | one City page, full template, `Nation` relation and `Maps` set at creation |
| **Enrichment** | "arricchisci", "completa", a page flagged by `travel-db-audit` | fetch the page, diff it against the template, fill only the gaps and re-verify anything that rots |

Enrichment is not a rewrite. Keep what is already specific and correct, replace what is placeholder,
generic or stale. A page that loses a good address because it was easier to start over is a regression.

## Order of operations

1. **Resolve the targets and check for duplicates.** `notion-query-data-sources` on Nations and City,
   match by normalised name (ignore flag emoji, ignore local variants) before creating anything. A trip
   ask like "Helsinki + Warsaw" expands to two nations and two cities, some of which already exist.
2. **Research, with the template still closed.** Full pass per the research standard. Opening the template
   first anchors the work on document mechanics instead of on what is true.
3. **Fetch the template and the reference page.** `notion-fetch` the data source's default template, and
   the Finland page for nations or the Santo Domingo page for cities, to calibrate density. The ids in
   `knowledge/notion-travel-db.md` save a search, they do not replace reading the template.
4. **Create the nation page first.** Setting `Nation` on a City auto-fills `Cities` on the Nation, and not
   the other way round. City before nation means going back to patch relations by hand.
5. **Create the city page with `Nation` and `Maps` already set.** Relations set at creation, not patched
   after.
6. **Fill every point.** Reproduce every numbered toggle section, every sub-heading, every table with the
   same columns in the same order, every `<details>` block. Then answer each point in one dense line.
   A point left empty, generic, or still carrying the template placeholder is a defect, not brevity.
7. **Strip the scaffolding.** Remove the `Jarvis` callout, the `Operational instructions` block and any
   `Guidance` meta-block. Keep the `Read first: open the Nation page` callout on city pages, translated.
8. **Run the verification pass below.** Not optional, and not from memory of what you wrote.

## What the template does not cover and must be there anyway

| Required | Where | What makes it pass |
| --- | --- | --- |
| `Storia del <paese>` | nation, a `<details>` toggle before section 1 | dense prose on why the country is the way it is today, not a chronology of dates |
| `City History` | city, the existing toggle | written dense. One line is a failure |
| Two food lists | city, section 8 | `Da provare, buoni` and `Da provare, strani o divisivi` kept separate. Per entry: what it is, what to expect, and where to get it with a real address |
| Do and Don't | culture sections, both page types | concrete and local, including the taboos that cause real offence and why. Generic guidebook politeness is filler |
| Politics | nation | who governs today, by name, web verified. Never from model memory |
| Embassies | nation | Swiss and Italian: address, phone, email, and the out of hours consular emergency number |
| Work | both | the reader does Bitcoin business development. Local crypto regulation and its current real state, exchanges, community, VC, and how business is actually conducted on the ground |
| Gym and routine | city | day pass gyms with prices near where the reader is staying. He trains every day |

## Three rules that do not come from the template

The template says what sections a page has. These three say whether the page can be trusted, and all three
were added after a maintenance pass found pages that passed the template check and failed the reader.

**The link contract.** Every link is the official site of the thing it names, or there is no link. If the
official URL cannot be found, write the name without a link: a name is honest and searchable, a plausible
link to the wrong place is not. Never leave generation residue in a URL, `utm_source=` tails or
`([turn0searchNN])` markers, and never let a table fill up with rows all pointing at the same generic portal.
Full rule in `knowledge/page-standard.md`.

**The generation marker.** The `Ultimo aggiornamento` block at the end of the page carries the date **and the
version of the spec the page was written against**, for example `Spec seguita: city-spec.md, Travel OS 1.3`.
A date alone does not say whether the page is behind the current structure, and without the marker the only
way to find out is to open every page and compare it section by section.

**`notion-fetch` can return a stale snapshot.** Before a structural intervention on an existing page, in
enrichment mode above all, force a refresh with a micro edit and fetch again. Editing against a snapshot that
no longer matches the page puts the change in the wrong place, and neither the call nor the page reports it.

## Parallelising several pages

When more than one page is wanted in a run, fan out, but keep the write order intact.

- **One nation or one city per subagent.** Never two subagents on the same page: the second overwrites the
  first silently.
- **Two waves.** All nations first, wait for them to land, then all cities, each setting its own `Nation`
  relation. Fanning out both at once produces cities whose relation target does not exist yet.
- **Each subagent gets the same kit**: the fetched template markdown, the three knowledge files, its target
  name, the reference page id for density, and `references/subagent-brief.md`, which is the brief to hand
  over verbatim.
- **A subagent returns the page id and its verification result**, not the page text. The parent re-runs the
  verification pass on every page: subagents mark their own homework generously.

## Verification pass

Re-fetch the written page, then work down this list. A page that fails any line is not finished.

- [ ] no residual placeholder: `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`,
      `[Amount]`, `YYYY-MM-DD`
- [ ] no empty table cell, and no table row still generic
- [ ] every template section present, in order, numbered as in the template
- [ ] no `Jarvis`, `Operational instructions` or `Guidance` block left in the page
- [ ] the nation history toggle exists and is prose, the city history toggle is more than one line
- [ ] the two food lists are two lists, and every entry has an address
- [ ] the governing figures are named and were web checked in this run
- [ ] both embassies carry address, phone, email and the emergency number
- [ ] gyms carry a day pass price
- [ ] prices in local currency with a CHF conversion and the rate stated, 24 hour times
- [ ] no em dash and no en dash anywhere in the prose
- [ ] accents correct: è, più, città, già, perché, martedì, attività, connettività
- [ ] every link is real and official, nothing invented, `da verificare` where a figure could not be confirmed
- [ ] naming and icon per convention: nation is English name plus flag emoji, city is the English name,
      icon is the flag
- [ ] footer carries the date the page was brought current
- [ ] every link is the official site of the thing it names, or the name carries no link at all
- [ ] no `utm_source=`, no `([turn0searchNN])`, no search result URL standing in for a site
- [ ] the generation marker names the spec version the page follows, not only the date
- [ ] on a City page, `Maps` is populated as a property, not written as a row inside the page body

## Output style

The page is written in **Italian**. No em dashes and no en dashes, ever: commas, full stops, colons. Prose
where prose reads better than bullets. 24 hour times. Prices in local currency with the CHF conversion and
the rate. Where a figure cannot be verified, `da verificare` rather than a guess.

## Guardrails

- Never invent a link, a price, an address or a name. A missing URL means the name without a link.
- Never state who governs, a fare, or an opening time from model memory. Those are live checks every run.
- A restaurant recommended as open when it has closed is worse than no recommendation. Confirm the venue
  exists before listing it.
- Where two sources disagree, say so in the page instead of picking silently.
- Check for an existing page before creating one. Duplicates are the single most expensive defect in this
  database, because relations then point at the wrong half of a country.

## Downstream

Complete nation and city pages are what `trip-itinerary` and `pre-departure-check` read. `travel-db-audit`
sends pages back here when they decay.
