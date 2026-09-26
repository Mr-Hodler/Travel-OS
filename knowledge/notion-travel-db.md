# The Notion Travels & City database

The environment already exists and is correct. Travel OS manages it, it does not redesign it. Do not add properties, rename data sources, or invent new databases.

Parent page: **Travels & City**, `b6473452-61d6-4e04-9d8b-1557b3a761d4`

## Three data sources

| Data source | Holds | collection id | Default template |
| --- | --- | --- | --- |
| **Nations** | one page per country, country-level rules | `1da87313-332c-803a-a665-000b88297da5` | `29287313-332c-80ee-9aa7-cf580f5b2bd3` |
| **City** | one page per city, local detail only | `1da87313-332c-81cb-ae6b-000b3a357428` | `1da87313-332c-8122-bfbb-d15925c0082c` |
| **Travel** | one page per trip, the operational itinerary | `1da87313-332c-8090-81ed-000b59c2150a` | `1da87313-332c-808c-9e0b-df99c23f031e` |

Always `notion-fetch` the template before writing. The ids above save a search, they do not replace reading the template.

## Property schemas

These are the three schemas in full. Nothing is missing from the lists below and nothing in them is
optional to know: a skill that guesses a property name writes to nowhere, and a skill that believes a
property is absent leaves it empty forever.

**Nations**, five properties:

| Property | Type | Notes |
| --- | --- | --- |
| `Name` | title | English name only. The flag goes in the page icon, never inside `Name` |
| `Continent` | select | South America, North America, Europe, Asia, Africa |
| `Cities` | relation to City | auto-filled from the City side, see below |
| `Attachments` | url | |
| `Created` | created time | read only, set by Notion |

**City**, five properties:

| Property | Type | Notes |
| --- | --- | --- |
| `Name` | title | English name, single word where one exists. No flag inside `Name`: the icon carries the flag of its nation |
| `Nation` | relation to Nations | set this one, it fills `Cities` on the nation |
| `Maps` | url | a Google Maps place URL for the city. **This property exists** |
| `Attachments` | url | |
| `Last edited time` | last edited time | read only, set by Notion |

**Travel**, nine properties:

| Property | Type | Notes |
| --- | --- | --- |
| `Place Trip` | title | destination plus purpose or year |
| `Dates` | date range | set via `date:Dates:start`, `date:Dates:end`, `date:Dates:is_datetime` |
| `Nations` | relation, multiple | every country the trip touches |
| `City` | relation, multiple | every city the trip touches |
| `People` | text | |
| `Drive link` | url | the trip folder under `05_Viaggi`, never a single file inside it |
| `userDefined:URL` | url | |
| `Attachements` | file | spelled this way in the schema |

Note the property is spelled `Attachements` on Travel. That is the existing schema, do not correct it.

### The `Maps` property on City exists, and it is a property

It has been claimed more than once that the City data source has no `Maps` property. That claim is false.
`Maps` is a url property on City, it sits in the table above, and a City page with `Maps` empty is an
incomplete page, not a page whose schema is missing something.

**It is populated at property level, not as a row inside the page.** A Google Maps link written into a
table row, a callout or a bullet in the page body does not populate `Maps`: the property stays empty, the
database view shows nothing, and the link is invisible to every query that lists the data source. Set the
property when the page is created, with the other relations, and leave the page body to the content that
belongs in it. A link in the body on top of the property is duplication, not redundancy: two copies that
drift.

## Every trip also has a Drive folder

The documents behind a trip live in Google Drive, not in Notion. One folder per trip, under the root
`05_Viaggi`, named `YYYY.MM_Destinazione`. It holds the originals: flight itineraries and receipts,
hotel receipts and check-in vouchers, train and ferry tickets, vouchers, identity papers, and the
itinerary and costs spreadsheet.

`Drive link` on the Travel page is populated with that folder, the folder itself and not one file
inside it. It is the only join between the page and the documents it was built from, because the
folder name and the page title drift apart: `2026.06_China Bro Trip` against `China Bros Trip`,
`2026.01_El Salvador` against `San Salvador, El Salvador`. A Travel page with an empty `Drive link`
is a defect even when the folder exists.

The rule that follows from the split: a booking PDF is not transcribed into the Notion page, it is
extracted and linked. The page carries the fields that matter at the moment of use, the folder keeps
the document. Passports, visas and ID scans stay in Drive and are never copied into a Notion page.

Full detail, the observed structure, the canonical subfolder names and the current gaps between
folders and pages: `knowledge/drive-convention.md`.

## Relations resolve one way

Setting `Nation` on a City page auto-fills `Cities` on the Nation page. So **create the nation page first**, then the city with its `Nation` already set, then the trip with both relations. Creating in the wrong order means going back to patch relations by hand.

## Naming conventions, as used

- Nations: English name, nothing else. `Finland`, `Poland`, `Dominican Republic`
- Cities: English name, single word where one exists. `Helsinki`, `Warsaw`, `Krakow`, `Belgrade`. A second local name only when the page is genuinely known by both (`Beijing Pechino`)
- Trips: destination plus purpose or year. `Vietnam 2025`
- `Maps` on a city page: a Google Maps place URL for the city

## Icons and titles: the flag lives in the icon

**The flag goes in the icon only, never inside `Name`.** A flag inside the title is what produces the
duplicate that normalises to the same string, `Poland` against `Poland 🇵🇱`, and it makes every
query match on a character nobody types. It also puts the same information on the page twice, in the icon
and in the title, and the two then drift.

**Every City page carries as its icon the flag of its own nation.** Not a city crest, not a photo, not a
pin: the flag of the country the `Nation` relation points at, so the database view reads as groups of
countries at a glance. A City page whose icon is not its nation's flag is a defect.

Trip pages keep `✈️` as their icon.

## One trip, one page

A trip that touches several cities or several countries is **one** Travel page with multiple `Nations` and `City` relations and one day-by-day table. Never split a single trip across pages by city. Splitting was a mistake made once and corrected.

## Reference pages worth reading for density

- City done well: `3c187313-332c-8116-8735-e845f4716a77` (Santo Domingo)
- Nation done well: `3de87313-332c-813e-886f-c8928a857182` (Finland)
- Trip done well: `3de87313-332c-819c-bdd2-f819c8fd6853` (Helsinki + Warsaw)

## A warning paid for in real damage

During the September 2026 maintenance the `Maps` and `Last edited time` properties of the City data source were **deleted by accident** while pages were being edited in parallel, and nobody noticed until a schema fetch was compared against an earlier one. Both were restored, and `Maps` was repopulated on all 45 City pages from the URL each page carried in its body.

Two rules follow from it:

- A schema is not a thing an agent changes while doing page work. `notion-update-data-source` is for a deliberate schema change, asked for and stated, never a side effect.
- **Fetch the data source schema at the start of a maintenance pass and compare it at the end.** A property that silently disappears takes every value in that column with it, and no page-level check catches it, because the pages still look right.
