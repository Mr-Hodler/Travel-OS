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

## The verification pass is not optional

After writing, re-fetch the page and check:

- no residual placeholder: `[Area A]`, `[District 1]`, `[Hotel 1]`, `[Club 1]`, `[X]`, `[link]`, `[Amount]`, `YYYY-MM-DD`
- no empty table cells
- no table row still generic
- no template instruction callout left in the page
- every section the template has is present and numbered correctly
- no em dashes in prose, no missing accents

A page that fails any of these is not finished.
