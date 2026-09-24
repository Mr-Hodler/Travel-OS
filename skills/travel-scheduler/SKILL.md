---
name: travel-scheduler
description: >-
  Owns the scheduled tasks of the travel system: creates, names, converts to UTC and maintains the
  reminders that fire `pre-departure-check`, `travel-db-audit` and the pre-trip refresh of the nation and
  city pages. It does not do their work, it sets and keeps their timers. Usala quando l'utente dice
  "imposta i promemoria del viaggio", "schedula il check pre partenza", "metti l'audit del database
  ricorrente", "quali task viaggio sono attivi", "cancella i task del viaggio finito", oppure in inglese
  "set up travel reminders", "schedule the pre departure check", "make the travel db audit recurring",
  "which travel tasks are active". Creates tasks only with the claude-code-remote trigger tools, never with
  the in-process cron tools, whose tasks die with the session and never fire. Converts Europe/Zurich local
  times to UTC and reports the local time next to the cron.
---

# Travel Scheduler

Every other skill in Travel OS declares when it wants to run. None of them owns the mechanism. This one
does. It creates the scheduled tasks, names them so they can be found again months later, turns the
intended local time into an expression that means the same thing in UTC, tells the user whether the task
will actually be allowed to act when it fires, and deletes it when the trip it belongs to is over.

It never does the work of the skill it schedules. A run of this skill produces tasks and a report about
tasks: not an itinerary, not a pre-departure list, not an audit.

## When to use
- A Travel page exists and the reminders around that trip have to be set.
- The monthly audit is not scheduled yet, or it is scheduled and keeps failing.
- The user asks what is currently active, or a trip moved, or a trip is over and its tasks have to follow.

Not for: running the checks. The pre-departure pass is `pre-departure-check`, the sweep is
`travel-db-audit`, the page refresh is `nation-city-pages` in enrichment mode. This skill points at them,
it does not stand in for them. And not before a Travel page exists: the fire times of a trip's tasks are
derived from the `Dates` start on that page, so with no page there is nothing to derive. Say so and stop.

## Read first, every run

| File | What it settles |
| --- | --- |
| `knowledge/notion-travel-db.md` | how to identify the pages a task prompt has to name: the three data sources, the `Dates` range on Travel, the relations that say which nation and city pages a trip touches, the naming conventions |
| `references/task-prompts.md` | the prompt written out in full, one per task family, ready to be filled and passed to `create_trigger` |

## The three task families

| Family | Shape | Cadence | Invokes |
| --- | --- | --- | --- |
| **Pre-departure** | one-shot, two per trip | 48 hours and 12 hours before the `Dates` start | `pre-departure-check` on that trip page |
| **Database audit** | recurring | monthly | `travel-db-audit` over the whole database |
| **Page refresh** | one-shot, one per trip | about 10 days before the `Dates` start | `nation-city-pages` in enrichment mode on the destination pages |

**Pre-departure, two firings per trip.** The 48 hour task carries the full pass, while there is still time
to book a transfer, chase a code or move a meeting. The 12 hour task carries the short pass over blocking
items and what goes stale fastest. Both are one-shots with an absolute instant, `run_once_at`, computed
from the trip dates, because the schedule belongs to the trip and not to the calendar. Two tasks, not one
recurring task with logic inside it.

**Database audit, monthly and recurring.** The only family that needs a cron expression. It is silent when
the database is clean, which is the property that makes a monthly job survive past the third month, so an
audit task that reports nothing is working rather than broken.

**Page refresh, about 10 days out.** The nation and city pages behind a trip were written whenever they
were written. Prices, opening hours, closing days, entry rules and who governs may all have moved since,
and the itinerary is built on top of those pages. Ten days is early enough that the refreshed page still
changes what gets booked, and late enough that what it checks is the state that will hold on the travel
dates. The task names the destination pages explicitly and asks for enrichment, never for a rewrite: a
page that loses a good address because starting over was easier is a regression.

## The right tool, and the wrong one

Scheduled tasks are created **only** with the trigger tools of the `claude-code-remote` MCP server:
`create_trigger`, `send_later`, `list_triggers`, `update_trigger`, `delete_trigger`. `create_trigger` is
the one that builds a trip task, with `run_once_at` for the one-shots and `cron_expression` for the monthly
audit. `send_later` schedules a message back into the conversation that is open right now, so it is a nudge
inside a session and not a travel task: it is the wrong choice for anything that has to start on its own
with nobody present.

**Never `CronCreate`, `CronList` or `CronDelete`.** Those run in an in-process scheduler that lives inside
the session. Whatever they schedule is discarded when the session ends, so the task never fires, and
nothing reports the loss: the tool returns success, the user is told the reminder is set, and 48 hours
before departure absolutely nothing happens. This section exists to prevent exactly that. If a task was
ever set up with them, it does not exist. Recreate it with `create_trigger` and say that the earlier one
never would have fired.

## How a task prompt is written

Every firing starts a **fresh session with no memory of the conversation that created the task**. The
prompt is therefore a complete, standalone instruction, and it names, in this order:

- the Notion page, by id, with its title after the id so a human reading `list_triggers` recognises it
- the trip dates, written out, because the fresh session cannot infer them from context
- which skill to invoke, by name, and in which mode where the skill has modes
- what to produce, and where it lands: the action list in the reply, the page update in Notion

"Controlla il viaggio" does not work. It fires, the session has no trip, no page and no dates, and it
either asks a question nobody is there to answer or invents a plausible answer about the wrong trip. The
templates in `references/task-prompts.md` are the shapes that survive a cold start.

## Time zone

Cron expressions are evaluated in **UTC**. The user is in Lugano, Europe/Zurich, which is UTC+2 in summer
time and UTC+1 in winter time. Convert every intended local time before writing it, and if the conversion
crosses midnight, shift the day fields as well, both day of week and day of month, whichever the expression
uses. A monthly audit wanted at 07:00 local on the first of the month is `0 5 1 * *` in summer time and
`0 6 1 * *` in winter time. A task wanted at 00:30 local on Monday is `30 22 * * 0`, on the Sunday, because
in UTC it happens the previous evening.

The same conversion applies to the one-shot instants: `run_once_at` takes an absolute timestamp, so 48
hours before a 10:15 local departure is computed in local time and then written in UTC.

Always write the intended local time in a comment next to the cron in the report. An expression with no
local time beside it is unreadable six weeks later, including by the person who wrote it, and the reader
has no way to tell a deliberate UTC offset from a conversion that was never done.

## Approvals

A scheduled task runs when nobody is there to answer anything. If the task is not set to automatic
approval, the run stops at the first action that needs confirmation, which for these tasks is the first
Notion write or the first connector call, and it produces nothing at all. The failure is quiet: the task
fired, the run exists, and there is no output.

So when a task is created, say in one line which approval setting it got, and say that the user can switch
it to automatic approval in that task's own settings. A task that needs a human to approve its first action
is not a scheduled task, it is a notification.

## Maintenance

`list_triggers` is the inventory. Read it before creating anything, so a second copy of the monthly audit
does not end up beside the first, and read it when the user asks what is active.

- The pre-departure and page refresh one-shots **disable themselves after firing**. That is expected, and a
  fired one-shot is not a task to fix.
- The tasks of a finished trip are **deleted, not left to expire**. A dead trip's tasks in the list make the
  list unreadable, and the next person to look at it cannot tell which trips are live.
- When a trip's dates move, the fire times are re-derived and the tasks updated with `update_trigger`,
  which keeps the task identity and its run history. Delete and recreate only when the task has to change
  family.
- A `last_run` that comes back FAILED repeatedly means the task is not doing its job. Open it, read what it
  fired into, and fix the prompt, the approval setting or the page id it names. A task that fails silently
  every month is worse than no task, because it looks like coverage.

## What is never scheduled

- **No recurring itinerary build.** `trip-itinerary` runs when a trip and its bookings exist, which is an
  event and not a date. A monthly job that builds itineraries would produce pages for trips that do not
  exist.
- **Nothing that sends or buys.** No task sends an email, books a transfer, confirms a reservation or makes
  a purchase. Those are the actions Travel OS keeps in the user's hands on purpose, and a trip is full of
  non-refundable ones.

## Naming

Fixed, so the tasks group by trip and read in the right order in `list_triggers`:

| Task | Name |
| --- | --- |
| Pre-departure, full pass | `Viaggio <destinazione> <data> - pre partenza 48h` |
| Pre-departure, short pass | `Viaggio <destinazione> <data> - pre partenza 12h` |
| Page refresh | `Viaggio <destinazione> <data> - rinfresco pagine` |
| Monthly audit | `Travel DB - audit mensile` |

`<destinazione>` is the trip's destinations as the Travel page titles them, `<data>` is the month and year
of departure. There is one audit task, and its name carries no date because it is not tied to a trip.

## Output style

- The report to the user, and the prompt stored in each task, are in Italian. This skill file is in
  English, its output is not, and the task prompt is read by a session that will be triggering skills whose
  phrasing is Italian.
- The report lists, per task created: the name, the fire time in local time, the expression or timestamp
  actually stored, and the approval setting. Nothing else.
- **No em dashes and no en dashes anywhere.** Commas, full stops, colons. Standing rule, no exceptions.
- Correct accents: è, più, città, già, perché, martedì. 24 hour times throughout.
- A time that cannot be derived, because the Travel page has no `Dates` start, is reported as missing. It is
  never guessed, since a task that fires on a guessed date is worse than an absent one.
