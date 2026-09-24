# Template sync

## What the mirrors are

`knowledge/templates/` holds a verbatim snapshot of the three default page
templates that live in the Notion database "Travels & City":

| Mirror file | Data source | Notion page id |
| --- | --- | --- |
| `knowledge/templates/nations-template.md` | Nations | `29287313-332c-80ee-9aa7-cf580f5b2bd3` |
| `knowledge/templates/city-template.md` | City | `1da87313-332c-8122-bfbb-d15925c0082c` |
| `knowledge/templates/travel-template.md` | Travel | `1da87313-332c-808c-9e0b-df99c23f031e` |

They exist for two reasons.

1. A skill can learn the required structure of a page (which sections exist, in
   what order, which tables and which instruction callouts) by reading a file in
   this repo, with no Notion round trip and no extra latency or token cost.
2. The structure stays readable, reviewable and versioned in git even when
   Notion is unreachable, when the account has no access, or when someone is
   reading the repo offline.

The mirrors keep Notion flavored markdown exactly as the API returns it:
`{toggle="true"}` on section headings, `<table>` and `<tr>` / `<td>` blocks,
`<details>` / `<summary>` blocks, `<callout>` blocks, `<mention-date>` tags, tab
indentation, and the backslash escaped brackets in placeholders. Nothing was
rewritten, translated, shortened or cleaned up. The instruction callouts
addressed to Jarvis are part of the template and are kept on purpose.

## Notion is the source of truth

The mirrors are snapshots, not the master. If the live template in Notion and
the mirror in this repo disagree, Notion wins and the mirror is stale. A skill
that is actually writing a page should fetch the live template as well and
follow that; the mirror is for knowing the shape ahead of time, not for
overriding what Notion says.

Never edit a mirror to change the template. Edit the template in Notion, then
re-snapshot the mirror from it.

## Current snapshot

Snapshot taken: 2026-09-24.

Section counts at snapshot time, useful as a quick staleness signal:

- Nations: numbered sections 1 to 9.
- City: numbered sections 1 to 10, plus the City History `<details>` block in
  section 1.
- Travel: numbered sections 1 to 5, plus the unnumbered appendices (Detailed
  Daily Schedule, Tours pickup summary, Activities Status Summary, Notes and
  Reminders with the medications and packing `<details>` blocks, Trip
  Reminders).

## How to re-check

1. Fetch each of the three page ids above with the Notion fetch tool, one call
   per page. Confirm the result is complete: `truncated` must not be set, and
   `unknown_block_count` must be zero or absent.
2. Diff the returned page content against the body of the matching mirror,
   that is, everything after the `---` separator under the mirror header.
3. If they are identical, nothing to do.
4. If they differ, replace the mirror body with the fresh content verbatim,
   update the "Snapshot taken" date in the mirror header and in this file, and
   add a line to `CHANGELOG.md` saying which template changed and when.

Worth doing whenever a template is edited on Notion, and otherwise once in a
while as part of a repo audit. It is cheap: three fetches and three diffs.
