# Generation mapping worksheet

The worksheet a class 5 generation migration fills **before** it writes anything. It exists because
`replace_content` on a page with content is irreversible, and the only thing that makes it safe is knowing,
block by block, where every block is going before the first write.

Target: `knowledge/templates/nations-spec.md`, `knowledge/templates/city-spec.md` or
`knowledge/templates/travel-spec.md`, whichever matches the data source. The spec is the target, never the
Notion template and never the historical `*-template.md` snapshot.

## Step 1: fetch both, and confirm the fetch is complete

The page and the spec. On the page fetch, `truncated` must not be set and `unknown_block_count` must be zero
or absent. A migration computed against a truncated fetch drops whatever was past the cut.

Force a refresh with a micro edit and fetch again before starting. A stale snapshot is the other way this
step fails silently.

## Step 2: the map

One row per block of the old page. Nothing is summarised and nothing is skipped: a block that looks like
scaffolding still gets a row, with `scaffolding` in the last column.

| # | Block on the old page | First words | Target section in the spec | Action |
| --- | --- | --- | --- | --- |
| 1 | heading | `## 1. 🛂 Ingresso e documenti` | section 1 | keep as is |
| 2 | table, 4 rows | `Visto, Durata, Costo` | section 1 | keep, add the two columns the spec has |
| 3 | callout | `Jarvis: compila questa sezione` | none | scaffolding, remove |
| 4 | bullet list, 6 items | `Caffè 1.20, pranzo 8` | section 4, `Costi tipici nel paese` | becomes a table row per item |
| 5 | paragraph | `La Polonia è entrata nella UE` | `Storia del paese` toggle | move into the toggle, it did not exist in the old spec |
| 6 | table, 10 rows | `Top 10 ristoranti` | section 8, `Da provare, buoni` | table cut to 5, the other 5 go to a line of text underneath |

`Action` is one of: keep as is, keep and extend, move, split, merge, becomes a row, scaffolding remove. Every
other verb means the block was not understood yet.

## Step 3: the counts, before writing

Write these five numbers down. They are the contract the migration is held to.

| Count | Value |
| --- | --- |
| Numbered sections on the old page | |
| Numbered sections in the spec | |
| Blocks on the old page | |
| Blocks mapped to a spec section | |
| Blocks with no target section | |
| Spec sections with nothing mapped to them | |

**A block with no target section is content to keep, not content to drop.** It goes under the nearest
section, or into a clearly named leftover block at the end of that section. The only blocks that leave the
page are the scaffolding ones: the `Jarvis` callout, the `Operational instructions` block, the `Guidance`
meta-block.

**A spec section with nothing mapped to it is a hole to fill**, and it is filled with real content or with
the line that says the data was never recorded. It is never filled with a placeholder.

## Step 4: write

Now, and only now, `replace_content` with the restructured page. This is the single case in Travel OS where
that call is allowed on a page that has content.

## Step 5: re-fetch and check the counts again

| Check | Passes when |
| --- | --- |
| Numbered sections | equal to the spec, and not lower than the old page had |
| Blocks mapped | every one of them is findable on the new page |
| Leftover blocks | present, named, not silently dropped |
| Placeholders | none, per the verification pass in `knowledge/page-standard.md` |
| Generation marker | `Ultimo aggiornamento` carries the date and the spec version now followed |

A count that came out lower is not accepted and not explained away. The page is repaired before the next one
is opened, because the mapping worksheet is still on screen and in an hour it will not be.

## What the worksheet is not

It is not a deliverable and it does not go to the user. It lives in the run and dies with it. What survives
is the row in the repair log, which names the spec version migrated from and to and the number of blocks
mapped, per `references/repair-log.md`.
