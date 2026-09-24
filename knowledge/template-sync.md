# Template sync

## Direction of truth

**The repo is the source of truth. The templates in Notion are the mirror.**

This was the other way round until 2026-09-24. Until that date the Notion
default template was the master and `knowledge/templates/*-template.md` held a
verbatim snapshot of it. On 2026-09-24 the three specs were written, the same
additions were applied to the three Notion templates, and the direction was
reversed: the spec in this repo is now the document that gets edited first, and
Notion is brought into line with it.

## Canonical files

These three are the specification. They are what a skill reads to know the
required shape of a page, and they are what gets edited when the template
changes.

| Canonical spec | Data source | Notion template page id |
| --- | --- | --- |
| `knowledge/templates/nations-spec.md` | Nations | `29287313-332c-80ee-9aa7-cf580f5b2bd3` |
| `knowledge/templates/city-spec.md` | City | `1da87313-332c-8122-bfbb-d15925c0082c` |
| `knowledge/templates/travel-spec.md` | Travel | `1da87313-332c-808c-9e0b-df99c23f031e` |

Each spec carries the whole structure of its data source, section by section,
table by table, toggle by toggle, plus the additions made on 2026-09-24. It does
not carry the Jarvis instruction callouts: a specification does not need
instructions on how to fill itself, and those callouts stay in Notion, which is
where they are read.

## Historical files

| Historical mirror | What it is |
| --- | --- |
| `knowledge/templates/nations-template.md` | Snapshot of the Notion Nations template as it stood on 2026-09-24, before the additions |
| `knowledge/templates/city-template.md` | Snapshot of the Notion City template as it stood on 2026-09-24, before the additions |
| `knowledge/templates/travel-template.md` | Snapshot of the Notion Travel template as it stood on 2026-09-24, before the additions |

They are kept for reference: they say what the structure used to be, which is
what makes the additions readable as a diff. They are not the specification and
they are not maintained. Nothing reads them to decide how a page should look.

They keep Notion flavored markdown exactly as the API returned it:
`{toggle="true"}` on section headings, `<table>` and `<tr>` / `<td>` blocks,
`<details>` / `<summary>` blocks, `<callout>` blocks, `<mention-date>` tags, tab
indentation, and the backslash escaped brackets in placeholders. Nothing in them
was rewritten, translated, shortened or cleaned up. Do not edit them.

## How the Notion templates are kept aligned

The three Notion default templates were brought up to the specs on 2026-09-24 by
addition only: every section, table, row and callout that was already there was
left exactly as it was, including the Jarvis instruction callouts, and the new
sections and tables were inserted around them. `insert_content` was used where
appending was enough, `update_content` with targeted replacements where a table
row or a block had to land at a precise point. `replace_content` was not used on
those three pages and should not be.

When a spec changes from here on:

1. Edit the spec in this repo first. It is the document that decides.
2. Apply the same change to the matching Notion template, by addition where the
   change is an addition. Use `insert_content` to append, `update_content` for a
   targeted insertion. Never `replace_content` on these three pages.
3. Re-fetch the page and confirm nothing was lost: every pre-existing section is
   still there, and the count of numbered sections has gone up or stayed the
   same, never down.
4. Add a line to `CHANGELOG.md` saying which template changed and when.

## How to re-check that the two are still aligned

1. Fetch each of the three page ids above with the Notion fetch tool, one call
   per page. Confirm the result is complete: `truncated` must not be set, and
   `unknown_block_count` must be zero or absent.
2. Compare the returned content against the matching spec, that is, everything
   after the `---` separator under the spec header. The expected differences are
   the Jarvis instruction callouts, which exist only in Notion.
3. Anything else that differs is a divergence. The spec wins: bring the Notion
   template up to the spec, by addition, and do not edit the spec to match
   Notion.
4. Confirm the numbered section counts match: Nations 9, City 10, Travel 5.

Worth doing whenever a spec is edited, and otherwise once in a while as part of
a repo audit. It is cheap: three fetches and three comparisons.

## The limit, stated plainly

**The template that Notion holds is the one that gets applied when someone
clicks New page inside the database by hand.** Notion applies its own default
template, not a file in this repo. Nothing in this repo can intercept that
click.

So the two have to be kept aligned anyway. If the spec moves ahead and the
Notion template is not updated with it, a page created by hand starts from an
older structure, and the gap is invisible until someone reads the page and finds
a section missing. The repo being the source of truth decides which document is
edited first and which one wins an argument. It does not remove the obligation
to push the change through to Notion.

A skill that writes a page through the API follows the spec and is unaffected. A
human clicking New page is the case this limit is about.

## Current state

Direction reversed: 2026-09-24.
Specs written and Notion templates aligned: 2026-09-24.
Historical mirrors snapshotted: 2026-09-24, pre-additions.

Section counts, useful as a quick staleness signal:

- Nations: numbered sections 1 to 9, plus the `Storia del paese` `<details>`
  block before section 1, and the `Ultimo aggiornamento` and `Da riverificare
  prima di partire` blocks at the end.
- City: numbered sections 1 to 10, plus the City History `<details>` block in
  section 1, and the `Ultimo aggiornamento` and `Da riverificare prima di
  partire` blocks at the end.
- Travel: numbered sections 1 to 5, plus the `DA RISOLVERE` callout and the
  `Modo semplificato` block at the top, the `Conflitti di agenda` section, and
  the unnumbered appendices (Detailed Daily Schedule, Tours pickup summary,
  Activities Status Summary, Notes and Reminders with the medications and packing
  `<details>` blocks, Trip Reminders, Checklist finale).
