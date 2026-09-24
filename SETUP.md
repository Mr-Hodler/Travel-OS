# Setup

What Travel OS needs before it can do anything, and how to tell that it actually responds. Six skills, one
Notion database, one Drive folder, four connectors.

## Install

```
/plugin marketplace add Mr-Hodler/Travel-OS
/plugin install travel-os
```

One install brings all six skills and the shared `knowledge/` folder with them. This repo ships no `dist/`
and that is deliberate: single skill packages would be one more thing that can silently diverge from source,
for no gain when the plugin installs everything at once.

## Repository layout

```
Travel-OS/
├── .claude-plugin/
│   ├── plugin.json           identity and version
│   └── marketplace.json      the repo as a one plugin marketplace
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md          frontmatter plus the spec
│       └── references/       what that skill reads
├── knowledge/                the shared standards, bundled into every package
│   └── templates/            the canonical spec of each data source
├── scripts/build.py          verifies, then packages
├── README.md  HANDBOOK.md  CHANGELOG.md  ROADMAP.md  SETUP.md  CLAUDE.md
└── LICENSE  .gitignore
```

Edit in `skills/` and in `knowledge/`. Everything under `knowledge/` is copied into every package by
`build.py`, so a skill installed on its own still resolves the standards it cites.

## Connectors, per skill

| Skill | Notion | Mail | Calendar | Drive | Web | Trigger tools |
| --- | --- | --- | --- | --- | --- | --- |
| `nation-city-pages` | read and write | no | no | no | required, every run | no |
| `trip-itinerary` | read and write | required | required | required | context only | no |
| `travel-scheduler` | read only | no | no | no | no | required |
| `pre-departure-check` | read and write | required | required | no | required | no |
| `travel-db-audit` | read, limited write | no | no | read only | targeted checks | no |
| `travel-db-repair` | read and write | no | no | read only | required | no |

What each column means in practice:

- **Notion.** The connector is required by all six skills, always. Without it nothing in Travel OS has
  anything to work on. The parent page is **Travels & City** and the three data sources under it are Nations,
  City and Travel. Ids are in `knowledge/notion-travel-db.md`.
- **Mail.** `trip-itinerary` and `pre-departure-check` read bookings out of the inbox rather than from the
  conversation, which means **Spark across all four accounts**, or Gmail where Spark truncates a body to a
  preheader. Either one works, both together works better: Spark covers the accounts Gmail does not.
- **Calendar.** Google Calendar, for the same two skills, over the trip dates plus one day either side. It is
  what catches the meeting somebody else added on a travel day.
- **Drive.** Google Drive, for the trip folders. `trip-itinerary` needs it to find and link the trip folder,
  `travel-db-audit` and `travel-db-repair` read it to check that folders and pages correspond. None of the six
  skills writes to Drive.
- **Web.** Live research. Everything `knowledge/research-standard.md` lists as a live check goes through it:
  who governs, prices, opening hours, entry rules, whether a venue still exists.
- **Trigger tools.** `travel-scheduler` needs the `claude-code-remote` MCP server and its four tools,
  `create_trigger`, `list_triggers`, `update_trigger`, `delete_trigger`. Nothing else uses them and there is
  no fallback worth using: the in process cron tools create tasks that die with the session, report success,
  and never fire.

## The Drive folder

Root: **`05_Viaggi`**. One folder per trip, named `YYYY.MM_Destinazione`, where `YYYY.MM` is the month the
trip starts. `2027.01_El Salvador + Rep. Dominicana` is the model.

Inside it, one canonical name per kind of document: `Transport/` for every leg, `Stay/` for every night,
`ID & Visa/<Person>/` for identity papers, `99_Cancellati/` for the refund trail. Two digit `NN_` prefixes
inside `Transport/` and `Stay/` follow the order of the trip, so the folder list reads as the itinerary reads.

The join between the two halves of the system is the `Drive link` property on the Travel page, pointing at the
**folder** and never at a file inside it. Folder names and page titles drift apart on purpose, so the link and
not the name is what matches them.

Full detail, the observed state of the root today, the legacy forms that are not renamed, and which documents
are sensitive and never enter a Notion page: `knowledge/drive-convention.md`.

On this machine the root is a connected folder and appears at `$HOME/mnt/05_Viaggi` inside the device shell.

## First use

1. **Connect Notion**, and confirm the assistant can see the **Travels & City** parent page.
2. **Connect Drive**, and confirm `05_Viaggi` is visible with its trip folders.
3. **Connect Spark or Gmail, and Google Calendar**, if trips are in scope and not just reference pages.
4. **Install the `claude-code-remote` MCP server** if the scheduled tasks are wanted.
5. **Run `travel-db-audit` once, on demand.** It is the cheapest first run in the repo: three queries, no
   page opened unless triage flags it, and the report tells you the real state of the database before you
   write anything into it.
6. **Fix what the audit found, with `travel-db-repair`**, before creating anything new. A new page created
   beside a duplicate makes the duplicate worse.
7. **Then the normal order**: `nation-city-pages` for the reference layer, `trip-itinerary` for the trip,
   `travel-scheduler` for that trip's reminders, `pre-departure-check` when the first reminder fires.

## How to verify that everything responds

Five checks, in order. Each one fails loudly, which is the point: the failures this list is looking for are
otherwise invisible.

| Check | Ask for | It responds correctly when |
| --- | --- | --- |
| Notion reachable | fetch the **Travels & City** parent page | the three data sources come back, Nations, City and Travel |
| Schema correct | fetch one City page | it carries `Name`, `Nation`, `Maps`, `Attachments`, `Last edited time`. `Maps` exists, and a run that reports it missing is wrong |
| Drive reachable | list `05_Viaggi` one level deep | the trip folders come back, `YYYY.MM_Destinazione` |
| Mail and calendar reachable | search the inbox with a `newer_than:` filter, list the calendar over any week | results, not an authorisation error. A silent empty result on a week that has events is a connector problem, not an empty week |
| Trigger tools reachable | `list_triggers` | it returns, empty or not. If the tool is not there, `travel-scheduler` cannot create a task that survives the session and must say so rather than using the in process cron tools |

Then the repo itself:

```
python3 scripts/build.py --check
```

Six skills verified, no `FAIL`, no dangling citations. Frontmatter that does not parse, a `name` that does not
match its folder, a description over 1024 characters and a cited file that does not exist are all invisible
otherwise: the file looks correct, and either the skill never installs or the agent runs without half its
instructions.

```
python3 scripts/build.py
```

Builds `dist/<name>.skill` for each skill, bundles `knowledge/` and the `LICENSE` into every archive, and
prints `SHARED MISSING` if that bundle did not land. Run it when you want the packages; the plugin does not
need them.

## Ownership

Proprietary and confidential. Internal use only, see `LICENSE`, which `build.py` bundles into every package so
a `.skill` that leaves this repo carries its terms with it.
