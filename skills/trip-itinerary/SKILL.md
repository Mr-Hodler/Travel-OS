---
name: trip-itinerary
description: >-
  Build the single Travel page for a trip in the Notion Travels & City database, with flights, transfers,
  accommodation, events and a day-by-day table taken from the real bookings in email and calendar, never
  reconstructed from memory. One trip is one page even when it crosses several cities or several countries.
  Produces the red DA RISOLVERE callout that names every agenda conflict, missing code and unbooked leg
  while there is still time to fix it. Use when the user says "fai l'itinerario", "pagina viaggio per",
  "organizza il viaggio a", "metti i dati di volo e hotel", "prepara la pagina del viaggio",
  "build the itinerary", "trip page for", "put the flight and hotel data in", or hands over a booking
  confirmation and expects a page out of it.
---

# Trip Itinerary

The operational skill of Travel OS. It turns what is already sitting in four mailboxes and a calendar into one Travel page that answers, for any hour of the trip, where he is supposed to be and what he is missing. Its value is not the pretty table. It is the red callout at the top that says the 14:00 call falls while he is at 10.000 metres and the lockbox code never arrived.

## When to use
- "Fai la pagina per Helsinki + Varsavia."
- A flight or hotel confirmation lands and the trip has no page yet.
- The trip exists as a page but new bookings have arrived and the day-by-day table is stale.

Not for: writing or refreshing the Nation and City pages behind the trip, which is `nation-city-pages`. Not for the final sweep 48 hours out, which is `pre-departure-check`.

## Mandatory reading, before writing anything

- `knowledge/notion-travel-db.md`: the three data sources, the exact property names, the relation order, the naming conventions.
- `knowledge/page-standard.md`: the output contract, the style rules, the verification pass.
- `knowledge/research-standard.md`: what must be checked live, and the rule that trip data comes from the inbox and not from the web.
- `references/inbox-harvest.md`: the query patterns per account and the subagent brief for oversized results.
- `references/page-skeleton.md`: the simplified section list, the table columns, the row colours.

Then `notion-fetch` the Travel template (`1da87313-332c-808c-9e0b-df99c23f031e`). The ids in the knowledge file save a search, they do not replace reading the template.

## One trip, one page

A trip that touches Helsinki and Warsaw is one Travel page with two `Nations` relations, two `City` relations, and one day-by-day table that runs straight through the border. Splitting by city has been done once and was wrong: it duplicates the flight, hides the transfer between the two legs, and makes the conflict callout impossible because no single page sees the whole week.

Relations resolve one way. The Nation pages exist before the City pages, and both exist before the trip, or the relations have to be patched by hand afterwards.

## Data collection

Everything factual comes from the inbox and the calendar. Nothing is reconstructed from the conversation, and nothing is rounded: a PNR, a lockbox code, a departure time and a price are either exact or useless.

1. **Spark, all four accounts.** `search` with a `newer_than:` filter over the window that contains the booking traffic, then `emails` with `from:` for the senders that are already known to matter: Navan, Trip.com, Airbnb, Booking, the airline itself, the event organiser. Run per account. A confirmation sitting in the account nobody thinks of is the usual cause of a missing leg.
2. **Gmail**, for the account it covers, whenever a Spark result is truncated to the preheader. Spark returns enough to tell you the email exists; Gmail returns the body with the code in it.
3. **Google Calendar**, over the trip dates plus a day either side: meetings, side events, and the recurring commitments that nobody thinks of as travel-relevant until they collide with a flight.

**When a search result is too large.** Spark searches over a wide window can exceed the token limit and get written to a file instead of returned. Do not read that file into the main context: it will fill it with hundreds of irrelevant messages and the page will be written with no room left to think. Delegate it to a subagent with an explicit extraction brief, naming the fields wanted back and the format, so what returns is a compact table of bookings and not raw mail. `references/inbox-harvest.md` carries the brief to hand over.

## Page structure

Reproduce the template. For a trip that is not complex, the simplified shape in `references/page-skeleton.md` applies: flights and transfers, accommodation, one single chronological table holding every fixed commitment, the day-by-day block G1 to Gn, the free day if there is one, per-city logistics, the checklist. One table for the whole trip, not one per city.

Travel rows, meaning flights and transfers, get a green row background. Days that are fully committed by work get a blue one. The colours are the fastest read on the page: green is when he is moving, blue is when he is not free.

## The DA RISOLVERE callout

A red callout at the very top of the page, before section 1. This is the part of the page that is worth the most, and it has to be hunted for rather than waited for. Nothing arrives labelled as a problem.

Look for, at minimum:

- **Agenda conflicts.** A call scheduled while he is in the air, a meeting that starts before the transfer from the airport can plausibly end, two commitments in two cities on the same afternoon.
- **Missing data.** A lockbox or door code that was promised and never sent, an address with no street number, a transfer that nobody booked, a return leg that does not exist, an event ticket that was never confirmed.
- **Awkward limits.** No checked baggage on a week-long trip, a fare with no changes allowed, a card that will not work at the destination, a hotel with no early check-in on a morning arrival.
- **Inconsistencies.** What he told somebody in an email against what the ticket says. If he wrote "arrivo lunedì sera" and the ticket lands Tuesday 01:20, both parties are wrong and somebody is waiting at the airport on the wrong day.

Each entry is one line: what is wrong, and the one action that closes it. An item with no action is an observation, and observations go elsewhere in the page.

## Arithmetic and sanity checks

Run these before the page is called finished. Each one has failed in real life.

- **Sum the costs**, and split them into what the employer pays and what he pays. A total that mixes the two is useless to both. State the exchange rate and its date where a conversion is involved.
- **Check the flight times against the time zones.** A departure and an arrival that imply a two hour flight on a route that takes five means the arrival is in local time and the duration in the page is wrong.
- **Check the check-out time against the flight time.** This is the classic failure: a 06:40 flight and an 11:00 check-out means either the last night is wasted or the last night was never booked. Say which.
- Check that every day between the first arrival and the last departure has a bed assigned to it. A gap of one night is a booking nobody made.

## Daily suggestions that survive contact with the day

He works remotely and trains every day. That means the realistic unit is a two hour slot, not a free day. One suggestion per day, placed in a slot that actually exists, near where he is already going to be. A day that work has taken entirely stays empty of tourism: writing three museums into it is a page that will be ignored, and a page that is ignored once stops being read.

The free day, if the trip has one, is the only place a half-day plan belongs.

## Output style

- The page is written in Italian. This skill is in English, the output is not.
- **No em dashes and no en dashes anywhere in the page.** Commas, full stops, colons. Standing rule, no exceptions.
- Correct accents: è, più, città, già, perché, martedì, attività. 24 hour times throughout.
- Prices in local currency with the CHF conversion and the rate stated.
- Real links only. A URL that cannot be found is written as a name without a link, never invented.
- A figure that cannot be verified is written `da verificare`, not guessed.

## Verification pass

Re-fetch the page and check it against `knowledge/page-standard.md`: no residual placeholder, no empty cell, no generic row, no template instruction block left behind, every section present and numbered as in the template. Then check the two things specific to this skill: the DA RISOLVERE callout is present and every entry in it names an action, and the day-by-day table has a row for every day from G1 to Gn with no gap.

## Handoff

The finished page is what `pre-departure-check` reads 48 hours before departure. Leave the open items in the callout rather than deleting them: that list is the input to the next skill, and a page that hides what is unresolved makes the pre-departure check start from nothing.
