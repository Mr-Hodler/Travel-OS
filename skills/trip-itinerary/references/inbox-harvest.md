# Inbox harvest

How the factual layer of a Travel page is gathered. Read with `knowledge/research-standard.md`, which sets the rule this file implements: trip data comes from the inbox, not from the web.

## Order of sources

| Source | Use for | Note |
| --- | --- | --- |
| Spark `search` | finding what exists, across all four accounts | `newer_than:` bounded to the booking window |
| Spark `emails` | pulling everything from one known sender | `from:` per sender, per account |
| Spark `thread` | the full exchange when a booking was changed | a rebooking lives in the reply, not the original |
| Gmail `search_threads` / `get_message` | the body Spark truncated to the preheader | only the account Gmail covers |
| Google Calendar `list_events` / `search_events` | meetings, side events, recurring commitments | trip dates plus one day either side |

## Senders that are already known to matter

Navan, Trip.com, Airbnb, Booking, the operating airline, the event organiser, the hotel itself when it writes directly. Query each by `from:` rather than hoping a keyword search surfaces it: a confirmation whose subject is a reference number matches nothing useful.

Run every query on all four accounts. A leg missing from the page is almost always a confirmation that landed in the account nobody checked.

## What to extract, per booking type

- **Flight**: carrier, flight number, PNR, departure airport and terminal, departure date and local time, arrival airport and terminal, arrival date and local time, baggage allowance, fare conditions, price, who paid.
- **Train or transfer**: operator, booking reference, pickup point, pickup time, destination, price, whether it is booked or only intended.
- **Accommodation**: property name, full address, check-in date and time, check-out date and time, access method and the code itself, host contact, price, cancellation deadline.
- **Event**: name, venue address, start and end, ticket state, whether attendance is confirmed to anybody.
- **Meeting**: counterparty, channel, start time in which time zone, whether it can be moved.

Quote codes, times and prices exactly. Never round, never normalise a time zone silently.

## When a search result overflows

A Spark search over a wide window can exceed the token limit, in which case the result is written to a file rather than returned. Reading that file into the main context fills it with hundreds of unrelated messages and leaves no room to write the page.

Delegate the read to a subagent. The brief it gets must be explicit about what comes back, or the subagent returns a summary and the exact codes are lost:

> Read the file at <path>. It contains raw email search results. Extract only travel bookings that fall between <start date> and <end date>. For each one return a row with: type (flight, train, transfer, accommodation, event), provider, booking reference or PNR exactly as written, start date and local time, end date and local time, location or address, price with currency exactly as written, and the sender address. Ignore marketing, newsletters, price alerts and anything outside the date range. Return a markdown table and nothing else. Do not summarise, do not round times, do not reformat reference codes. If a field is absent in the email write `assente` rather than inferring it.

The point of the last sentence is that `assente` is what feeds the DA RISOLVERE callout. A subagent that helpfully fills a gap destroys the signal the callout depends on.
