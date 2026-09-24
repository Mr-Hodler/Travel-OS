# Roadmap

Undated, ordered by what would earn its place next.

## Shipped

**`travel-db-repair`, in 1.3.** Worth recording that it was never on this list. The gap it closes was created by
a deliberate design decision in `travel-db-audit`, that the audit reports and routes and does not fix, and
nobody wrote down that the other half of the pair was missing. It took a manual maintenance pass over 81 pages
to notice that findings with no destination accumulate, and that a monthly audit whose findings are never closed
is indistinguishable from an audit that was never run. Nothing else on the Likely list below was closed by 1.3.

## Likely

**Populate `Maps` on the City data source, in bulk.** The property exists, it is a url on City, and it is empty
on most city pages, which is why two separate runs concluded it did not exist at all. One mechanical pass: a
Google Maps place URL per city, set **at property level** and not written into the page body, where it leaves the
property empty and the link invisible to every query. Cheap, unambiguous, and it is what makes the database view
usable from a phone in a taxi. A `travel-db-repair` run with this as its only class would close it in one pass.

**Close the `da verificare` backlog before a trip, not on a cadence.** Every run that hits the shared web search
budget leaves marked figures behind, which is correct behaviour and the reason the marker exists. What is missing
is the other end: nothing collects them. They accumulate across runs, on exactly the pages a trip is about to be
built on, and the current schedule closes them by accident at best. Wanted: a pass that gathers every
`da verificare` on the pages a trip relates to and closes them, driven by the trip date rather than by the month.
Probably a mode of `pre-departure-check` or of `travel-db-repair` rather than a seventh skill.

**Backfill the generation marker.** Pages written before 1.3 carry a footer date and no spec version, so the
first migration after this one still has to open every page once to find out which generation it belongs to. A
one off pass that reads each page, decides which spec it matches and writes the marker would make every later
migration a footer read. It is a cost paid once against a cost paid every time.

**`trip-debrief`.** After a trip, fold what was learned back into the city and nation pages: the restaurant that
was closed, the transport connection that worked better than the one in the page, the gym that was actually used.
Right now that knowledge stays in the itinerary and dies with it.

**Cost reconciliation.** The itinerary carries planned cost. Nothing checks it against what was actually spent,
so the benchmarks in section 9 of the city pages never improve from real data.

**A packing profile.** The template has a generic packing list. What is actually needed is a per-climate,
per-purpose profile that knows this traveller brings a laptop, trains daily, and goes to conferences.

## Maybe

**Flight and hotel watch.** Monitoring a booked trip for schedule changes and cancellations, rather than
discovering them at the airport. Worth it only if the airline notifications prove unreliable.

**A second traveller.** Everything currently assumes one person. Group trips would need per-person flight and
accommodation blocks and a way to say who is doing what on which day.

**A repair regression check.** The audit after a repair run should find the repaired pages clean. Comparing the
two reports automatically would turn the repair log into something that can be checked rather than something that
is trusted. Worth it only once repair runs are frequent enough for the comparison to have a baseline.

## Decided against

**Building the Notion structure.** The environment is correct and stays as it is. Travel OS manages it, it does
not migrate or redesign it.

**A dist/ directory that ships.** With a plugin, one install brings every skill. Single-skill packages would be
one more thing that can silently diverge from source, for no gain.

**Letting an agent delete a Notion page.** Settled during the 1.3 maintenance pass. A duplicate is parked under a
page outside the databases with a note saying why and what replaced it, and the user deletes that one page with a
single click. Deletion is one click for him and irreversible for us, and the asymmetry is the whole argument.
