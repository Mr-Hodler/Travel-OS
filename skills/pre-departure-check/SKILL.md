---
name: pre-departure-check
description: >-
  Run the check 48 hours before a trip leaves. Re-reads the Travel page and verifies every open item is
  closed: online check-in done, missing bookings made, access codes received, transfers arranged. Then
  verifies live what can have changed since the page was written: real weather on the dates, transport
  strikes and works, gate or terminal changes, opening hours and closures, security advisories, exchange
  rates. Checks the calendar for meetings other people added during the trip. Returns a short action list
  ordered by deadline with blocking items first, and updates the Notion page. Use when the user says
  "check pre partenza", "sono pronto per il viaggio", "cosa mi manca prima di partire",
  "controlla il viaggio di domani", "pre departure check", "am I ready to travel", or when the scheduled
  48 hour or 12 hour run fires.
---

# Pre Departure Check

The last pass over a trip before it starts. The Travel page was written days or weeks ago and two kinds of rot have set in since: things that were open and never got closed, and things that were correct and have since changed. This skill closes the first and catches the second, and it outputs actions rather than prose.

## When to use
- 48 hours out, on schedule, or whenever he asks.
- 12 hours out, as the short second pass over the blocking items only.
- Any time a trip is imminent and he wants to know what is missing rather than what is planned.

Not for: building the page in the first place, which is `trip-itinerary`. If no Travel page exists, say so and stop. This skill verifies a page, it does not substitute for one.

## Mandatory reading

- `knowledge/notion-travel-db.md`: where the Travel page lives, the exact property names, the one trip one page rule.
- `knowledge/page-standard.md`: the style contract the updated page must still obey.
- `knowledge/research-standard.md`: what has to be checked live rather than recalled, and how to source it.
- `references/live-checks.md`: the check list, the source per item, and what counts as a change worth flagging.

## Step 1. Close what was left open

`notion-fetch` the Travel page and read the DA RISOLVERE callout and the tables under it. Every open item is verified against reality, not against the page:

- **Online check-in.** Done or not done, per leg. If the window has opened and it is not done, that is a blocking item with a deadline, because seat and baggage cost more at the desk.
- **Bookings that were missing.** The transfer, the return leg, the last night, the restaurant that needed a reservation. Search the inbox again: half of these were booked and the page never got updated.
- **Access codes.** Lockbox code, door code, wifi, building entry. A code promised in a message and never sent is the item that ruins an arrival at 01:20.
- **Transfers.** Airport to accommodation at both ends, in both directions, at the actual arrival time. A public transport link that does not run at 01:20 is the same as no transfer.

An item the page listed as open and that is now closed gets marked closed with the evidence, the booking reference or the message it came from. An item still open with no action left available gets restated as a constraint rather than a task.

## Step 2. Verify live what may have changed

Everything in `references/live-checks.md`, checked at the source rather than recalled. The high-yield ones:

- **Weather on the actual dates**, not the seasonal average. It determines what goes in the bag, and it is the single most common reason a packing list written a month ago is wrong.
- **Strikes and works on transport.** Rail replacement, metro line closures, an air traffic control strike on the departure day. Check the operator and the national rail or airport site, not aggregators.
- **Gate or terminal change.** Terminals get reassigned weeks ahead and the confirmation email is never reissued. A terminal wrong by one is an hour lost.
- **Opening hours and closures** for anything in the plan: the museum's weekly closing day, a public holiday nobody outside the country knows about, a venue that has closed permanently since the page was written.
- **Security and entry advisories** for the destinations, from the official ministry source.
- **Exchange rate**, refreshed, with the date, because the cost split in the page was computed at an older rate.

## Step 3. Check the calendar for collisions born after the page

Other people add meetings. Re-run the calendar over the trip dates plus a day either side and compare against the chronological table on the page. Anything new that lands during a flight, during a transfer, or in a slot the page had marked as committed elsewhere is a conflict, and it is a conflict that did not exist when the page was written, which is exactly why it has to be looked for now.

Recurring commitments count. A weekly call that was harmless in the office is a conflict on a travel day.

## Step 4. Output

One short list of actions. Nothing else. Prose here is a cost, because the list gets read standing up on the way out.

Ordered by deadline, blocking items at the top. Each line: the action, the deadline, and why it blocks. A blocking item is one where the trip goes wrong if it is not done: check-in window closing, a leg that does not exist, no bed for a night, no way to get in the door. Everything else is ordered behind them by when it stops being possible.

Then update the Notion page: rewrite the DA RISOLVERE callout to hold only what is still open, mark the closed items closed with their evidence, correct any table cell that the live checks proved wrong, and refresh the footer date. The page and the list agree when this is finished, or the next run starts from the wrong baseline.

## Guardrails

- **No email is sent and nothing is booked without explicit confirmation.** The skill can draft the message asking the host for the code and show it, and it can name the booking to make and its price, but the send and the purchase are his. This is not negotiable, a trip is full of non-refundable actions.
- Never close an item because it is probably fine. Closed means evidence was found.
- Never invent a replacement for something that turned out closed or cancelled without saying it is a suggestion.
- A figure that cannot be verified is written `da verificare`.

## Output style

- The action list and the page are written in Italian. This skill is in English, the output is not.
- **No em dashes and no en dashes anywhere.** Commas, full stops, colons. Standing rule, no exceptions.
- Correct accents: è, più, città, già, perché, martedì. 24 hour times throughout.
- Real links only, never an invented URL.

## Running on schedule

Two runs per trip, from the Travel page dates.

**48 hours before departure.** The full pass, all four steps. This is the run that still leaves time to book a transfer, chase a code or move a meeting.

**12 hours before departure.** The short pass: blocking items only, plus the checks that go stale fastest, weather, strikes, gate and terminal, plus any calendar event added since the first run. No page rewrite unless something material changed, because a page edited twice in a day for nothing is noise.

To schedule it, derive the two fire times from the `Dates` start on the Travel page and set one-off runs rather than a recurring job: the schedule belongs to the trip, not to the calendar. The prompt each run carries names the trip and the page id explicitly, because a scheduled run starts with no memory of the conversation that created it. When a trip's dates move, the two runs are re-derived, and the old ones are removed rather than left to fire against a date that no longer exists.
