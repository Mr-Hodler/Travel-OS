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

**Nation pages.** A `<details>` toggle titled `Storia del <paese>`, placed before section 1. The template has no history section and one is wanted. Dense prose that explains why the country is the way it is today, not a chronology of dates.

**City pages.** The `City History` toggle must be written dense. One line is a failure.

**City pages, section 8 food.** Two separate lists, not one:
- `Da provare, buoni`, the dishes worth eating
- `Da provare, strani o divisivi`, the ones that test a foreigner

For every entry: what it is, what to expect, and where to actually get it with a real address.

**Culture sections.** Concrete `Do` and `Don't` lists, specific to the place. Include the taboos that would cause real offence, and say why. Generic guidebook politeness is filler.

**Politics.** Who governs today, by name, web-verified. Never from model memory.

**Embassies.** Swiss and Italian, with address, phone, email and the out-of-hours consular emergency number.

**Work sections.** The reader does Bitcoin business development. Local crypto regulation and its current real state, exchanges, community, VC, and how business is actually conducted on the ground.

**Gym and daily routine.** Day-pass gyms with prices near where the reader is staying. He trains every day.

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
- every link is the official site of the thing it names, or there is no link, per the link contract above
- no generation residue anywhere: no `utm_source=`, no `([turn0searchNN])`, no search result URL in place of a site
- the generation marker is present: `Ultimo aggiornamento` carries the date and the spec version followed

A page that fails any of these is not finished.
