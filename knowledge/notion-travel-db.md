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

**Nations**: `Name` (title), `Continent` (select: South America, North America, Europe, Asia, Africa), `Cities` (relation to City), `Attachments` (url), `Created`.

**City**: `Name` (title), `Nation` (relation to Nations), `Maps` (url), `Attachments` (url), `Last edited time`.

**Travel**: `Place Trip` (title), `Dates` (date range, set via `date:Dates:start`, `date:Dates:end`, `date:Dates:is_datetime`), `Nations` (relation, multiple), `City` (relation, multiple), `People` (text), `Drive link` (url), `userDefined:URL` (url), `Attachements` (file).

Note the property is spelled `Attachements` on Travel. That is the existing schema, do not correct it.

## Relations resolve one way

Setting `Nation` on a City page auto-fills `Cities` on the Nation page. So **create the nation page first**, then the city with its `Nation` already set, then the trip with both relations. Creating in the wrong order means going back to patch relations by hand.

## Naming conventions, as used

- Nations: English name plus flag emoji. `Finland 🇫🇮`, `Poland 🇵🇱`, `Dominican Republic 🇩🇴`
- Cities: English name, single word where one exists. `Helsinki`, `Warsaw`, `Krakow`, `Belgrade`. A second local name only when the page is genuinely known by both (`Beijing Pechino`)
- Trips: destination plus purpose or year. `Helsinki + Warsaw 🇫🇮🇵🇱 BTCHEL 2026`, `Vietnam 2025`
- Icons: flag emoji on nation and city pages, `✈️` on trip pages
- `Maps` on a city page: a Google Maps place URL for the city

## One trip, one page

A trip that touches several cities or several countries is **one** Travel page with multiple `Nations` and `City` relations and one day-by-day table. Never split a single trip across pages by city. Splitting was a mistake made once and corrected.

## Reference pages worth reading for density

- City done well: `3c187313-332c-8116-8735-e845f4716a77` (Santo Domingo)
- Nation done well: `3de87313-332c-813e-886f-c8928a857182` (Finland)
- Trip done well: `3de87313-332c-819c-bdd2-f819c8fd6853` (Helsinki + Warsaw)
