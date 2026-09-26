# City spec, canonical

**This file is the canonical specification for the City data source.** The
Notion default template, page `1da87313-332c-8122-bfbb-d15925c0082c`, is a
mirror of this file. Where the two diverge, this file wins and the Notion
template is the one that has to be brought into line.

The direction of truth was reversed on 2026-09-24. Before that date Notion was
the master and `knowledge/templates/city-template.md` was its snapshot. That
snapshot is kept as history and is no longer the specification.

This spec carries the whole structure of the template, section by section, table
by table, toggle by toggle, plus the additions the template did not have. The
Jarvis instruction callout is not reproduced: a specification does not need
instructions on how to fill itself. It stays in the Notion template, which is
where it is read. The `Read first: open the Nation page` callout is part of the
page and stays.

Section names, their emoji and their numbering are kept exactly as they read in
Notion.

**Density.** What is measured is the **visible text**, not the characters of the markdown: table markup is
not read, so it does not count. Every heavy section carries **two levels**, the operational essentials
visible when the section opens and one toggle `Dettaglio: <what it holds>` with all the rest. Nothing is
deleted, it is moved one level down. Caps on the visible text: **900** for what an open section shows,
**1,200** for `⚡ Scheda rapida`, **1,200** for the `🔁 Da riverificare` toggle, **1,300** for the
first level of `City History`, **300** for a table cell, **4 lines** for a callout, **3 consecutive lines**
of prose. The `Dettaglio` toggles have no cap. The budget, the three cutting levers and the form rules are
in `knowledge/page-standard.md`, sections `Density budget`, `How to write a line` and `No lists in prose`.
**A table beats a paragraph whenever there are more than two comparable entries, and an enumeration is
never written as prose.**


---

## ⚡ Scheda rapida

**First block of the page, outside every toggle, and it carries no toggle itself.** Max **1,200** visible
characters. Two columns, and the rows come in this order:

<table fit-page-width="true" header-row="true">
<tr>
<td>Voce</td>
<td>Dato</td>
</tr>
<tr>
<td>**Aeroporto verso centro**</td>
<td>the mode, the minutes, the price</td>
</tr>
<tr>
<td>**Biglietto urbano**</td>
<td>single fare, day pass, where it is bought</td>
</tr>
<tr>
<td>**Emergenze**</td>
<td>the numbers that work in this city</td>
</tr>
<tr>
<td>**Ospedale**</td>
<td>name, district, whether it takes foreigners directly</td>
</tr>
<tr>
<td>**Farmacia 24h**</td>
<td>name and address of one that is really open at night</td>
</tr>
<tr>
<td>**Palestra day pass**</td>
<td>name, district, price of a single entry</td>
</tr>
<tr>
<td>**SIM o eSIM**</td>
<td>operator, price, where it is activated</td>
</tr>
<tr>
<td>**Pagamenti**</td>
<td>cards or cash, and whether Bitcoin is spendable anywhere here</td>
</tr>
<tr>
<td>**Dove stare**</td>
<td>one district, and the reason it is that one</td>
</tr>
<tr>
<td>**Da non fare**</td>
<td>the one thing that gets a foreigner in trouble here</td>
</tr>
</table>

Below the table, **one single line**: currency and rate against CHF, time difference, language.

## 🔁 Da riverificare prima di partire {toggle="true"}
	**Second block of the page, and it is a toggle.** Max **1,200** visible characters. A dry list, no
	introductory sentence, every entry carrying its `(sez. N)` pointer and the date it was last checked. A
	check older than the trip is a defect.
	- **Prezzi e orari** (sez. 7, 8, 9)
	- **Giorni di chiusura e festivi nella finestra di viaggio** (sez. 2, 7)
	- **Ospedali, farmacia 24h e numeri** (sez. 3)
	- **Ingressi singoli in palestra** (sez. 7)
	- **Rischi stagionali contro le date reali** (sez. 3)
	- **Locali e ristoranti che esistono ancora** (sez. 7, 8)

---

<callout icon="📌" color="yellow_bg">
	Read first: Open the Nation page for country‑level rules and info . Then use this City page for local details only.
</callout>
## 1. 🔗 Quick links & Essential resources {toggle="true"}
	- **Custom map:**
	- **Local transport:** PDF/official app
	- **Official website:** city/tourism portal
	- **Offline maps:** Google Maps / [Maps.me](http://Maps.me)
	- **Essential apps:** Transit • Ride‑hailing • Translation • Payments
	- **See also:** \[Nation page\] for national rules
	<details>
	<summary>**City History **</summary>
		Explain here the History of the city, the past, the history, why is known (wars, tech, politics, culture, and so on) , the local context and the highlight to know about the place.
		**Two levels.** This first level is one line per period, **max 1,300 visible characters**, and it carries no dates, no names and no figures: those go into the nested toggle below.
		**Nested inside section 1 and it stays there**, never lifted above the first numbered section: the page opens with links and numbers, not with a history lesson.
		<details>
		<summary>**Dettaglio: date, nomi e cifre**</summary>
			The chronology itself: dates, the people and the events by name, the figures. No cap. Everything the first level had to leave out sits here, and nothing is deleted in order to keep the first level short.
		</details>
	</details>
## 2. 🏙️ Local context (city‑only) {toggle="true"}
	- **Country:** \[\[Link to Nation page\]\] • **Time zone:** GMT±X (DST: \[Yes/No\])
	- **Language use (city variations):** \[text\]
	- **Key districts:** \[District 1\] (center/business) • \[District 2\] (expat/quiet) • \[District 3\] (local)
	- **Where to stay:** snapshot
		<table fit-page-width="true" header-row="true">
<tr>
<td>Area</td>
<td>Vibe</td>
<td>Safety</td>
<td>Cost</td>
<td>Notes</td>
</tr>
<tr>
<td>\[Area A\]</td>
<td>trendy/quiet</td>
<td>low/med/high</td>
<td>\$/\$\$/\$\$\$</td>
<td>\[centrality, connections\]</td>
</tr>
<tr>
<td>\[Area B\]</td>
<td>nightlife/central</td>
<td>low/med/high</td>
<td>\$/\$\$/\$\$\$</td>
<td>\[weekend noise, etc.\]</td>
</tr>
<tr>
<td>\[Area C\]</td>
<td>local/green</td>
<td>low/med/high</td>
<td>\$/\$\$/\$\$\$</td>
<td>\[parks, families\]</td>
</tr>
		</table>
	- **Dove stare, quartiere per quartiere**, the `Top quartieri dove stare` table, which answers `dove dormo` in one row. Mandatory columns: `Quartiere` · `Per chi va bene` · `Costo` · `Cosa evitare`. It replaces the
	  `Where to stay` snapshot above as the one a reader actually uses, and every column is filled.
	  Three to five rows, no more: a list of twelve districts answers nothing.
		<table fit-page-width="true" header-row="true">
<tr>
<td>**Quartiere**</td>
<td>**Per chi**</td>
<td>**Prezzo**</td>
<td>**Tempo dal centro**</td>
<td>**Nota**</td>
</tr>
<tr>
<td>**\[Quartiere 1\]**</td>
<td>\[business, prima volta, vita notturna, famiglia, lungo soggiorno: pick one, not three\]</td>
<td>\[local currency / CHF a notte, fascia reale\]</td>
<td>\[minutes and the mode, so 12 min metro, not "central"\]</td>
<td>\[the one thing that decides it, noise, safety after dark, dead on Sundays\]</td>
</tr>
<tr>
<td>**\[Quartiere 2\]**</td>
<td>\[who it is for\]</td>
<td>\[local currency / CHF a notte\]</td>
<td>\[minutes and the mode\]</td>
<td>\[the deciding detail\]</td>
</tr>
<tr>
<td>**\[Quartiere 3\]**</td>
<td>\[who it is for\]</td>
<td>\[local currency / CHF a notte\]</td>
<td>\[minutes and the mode\]</td>
<td>\[the deciding detail\]</td>
</tr>
		</table>
	- **When to visit:** city seasonality
		<table fit-page-width="true" header-row="true">
<tr>
<td>Period</td>
<td>Weather</td>
<td>Crowds</td>
<td>Notes</td>
</tr>
<tr>
<td>\[Dec–Apr\]</td>
<td>\[Dry, 25–35 °C\]</td>
<td>High</td>
<td>\[book ahead\]</td>
</tr>
<tr>
<td>\[May–Nov\]</td>
<td>\[Rainy, 24–32 °C\]</td>
<td>Medium</td>
<td>\[daily showers\]</td>
</tr>
		</table>
	> City quirks: \[tap water quality\] • \[air/smog link\] • \[quiet hours/noise bylaws\]
## 3. 🛡️ Safety & health (city‑only) {toggle="true"}
	### **Emergencies (city use):** Police \[XXX\] • Ambulance \[XXX\] • Fire \[XXX\] • Tourism \[XXX\]
	- **Areas to watch or avoid:** \[concise list with reasons\]
	- **Common scams & counter‑moves:** \[short bullets\]
	- **Health:** city
		<table fit-page-width="true" header-row="true">
<tr>
<td>**Facility**</td>
<td>Type</td>
<td>Address</td>
<td>Phone</td>
<td>Notes</td>
</tr>
<tr>
<td>**\[Hospital 1\]**</td>
<td>Private</td>
<td>\[address\]</td>
<td>+XX</td>
<td>ER 24/7</td>
</tr>
<tr>
<td>**\[Hospital 2\]**</td>
<td>Public</td>
<td>\[address\]</td>
<td>+XX</td>
<td>Largest</td>
</tr>
<tr>
<td>**\[Clinic\]**</td>
<td>Travel med</td>
<td>\[address\]</td>
<td>+XX</td>
<td>Vaccines</td>
</tr>
<tr>
<td>**Farmacia 24h**</td>
<td>Pharmacy</td>
<td>\[address\]</td>
<td>+XX</td>
<td>Open 24/7, name and address verified, walking time from the accommodation</td>
</tr>
		</table>
	- **Tourist police / Alerts app:** \[unit & phone\] • Official city alert app \[link\]
	- **Sexual health:** Testing \[links\] • PEP/PrEP \[availability\] • Condoms \[where\]
	- **Rischi stagionali:** filled against the real travel window, not in general
		- **Finestra di viaggio:** the actual dates the reader will be here
		- **Clima e fenomeni attesi in quella finestra:** heat, cold, rain, wind, snow, air quality, daylight hours
		- **Rischi sanitari di quella finestra:** insects, pollen, water, respiratory season
		- **Cosa cambia in pratica:** what to pack, what to move indoors, which hours to avoid
## 4. 🚦 Mobility & infrastructure {toggle="true"}
	- **Arrival/Departure:**
		<table fit-page-width="true" header-row="true">
<tr>
<td>Hub</td>
<td>Distance</td>
<td>Options</td>
<td>Time</td>
<td>Price (CHF)</td>
</tr>
<tr>
<td>\[Airport (CODE)\]</td>
<td>\[X\] km</td>
<td>Ride‑hailing / Taxi / Train‑Bus</td>
<td>20–30 min</td>
<td>\[X–Y\]</td>
</tr>
<tr>
<td>\[Main station\]</td>
<td>\[central\]</td>
<td>Metro/Tram/Bus</td>
<td>5–15 min</td>
<td>\[X\]</td>
</tr>
		</table>
	- **Urban transport:**
		- **Best for visitors:** \[choice\] — \[why\]
		- **Metro/Tram:** lines, tickets, passes (link)
		- **Bus:** useful routes, app
		- **Taxis:** reliable companies, red flags
		- **Walking:** walkable areas and notes
	- **Driving & rentals:** traffic, IDP, parking, ZTL/LEZ (city link)
	- **Time guide:** Airport→Center \[20 min\] off‑peak / \[60+ min\] peak
	- **Back to Nation:** national SIM, electricity, and holiday rules → \[\[Nation page\]\]
## 5. 📶 Connectivity & tech (city‑only) {toggle="true"}
	- **SIM & eSIM:** operators present; eSIM available → prices/ID rules on Nation page
	- **Internet & power:** typical Wi‑Fi quality/security; note unusual power quirks
	- **Work‑friendly spots:** coworkings and cafés with reliable Wi‑Fi
## 6. 🧭 Culture & customs (city specifics) {toggle="true"}
	**`Cosa fare e cosa non fare` is mandatory here**, and it is the `Do` and `Don't` pair below: two dry bullet lists, one attribute per line, at the **first level** of the section. Everything else in the section goes into `Dettaglio: frasi, feste, galateo d'affari`.
	- **Do**, explicit and specific to this city, never generic guidebook politeness. **List form, never a paragraph.**
		- One line per item, with the reason it matters here
	- **Don't**, explicit and specific to this city. **List form, never a paragraph.**
		- One line per item, with what actually happens if you do it
	- **Cosa non dire**, the subjects that cause real offence in this city. **List form, never a paragraph.** Not awkwardness, offence.
		- One line per item, with why it lands badly
	- **Useful phrases:** with pronunciation
	- **Festivals & city holidays:** with impact
	- **Business culture & etiquette:**
		- **Negotiation style:** \[direct/indirect\] • \[hierarchical/flat\] • \[formal/casual approach\]
		- **Meeting protocol:** \[punctuality expectations\] • \[dress code\] • \[business card exchange\]
		- **Gift-giving customs:** Appropriate gifts \[wine, fruit, local delicacies\] • Avoid \[list\] • Presentation \[wrapped/unwrapped, both hands\]
		- **Business dining:** \[expectations\] • \[who pays\] • \[toast protocol\]
		- **Local business quirks:** \[e.g., birth chart significance, seasonal greeting cards, etc.\]
## 7. ⭐ Attractions & experiences {toggle="true"}
	- **Day trips (≤3h):** \[1–5 bullets or table if needed\]
	- **Must-see & Unique experiences**
		<table>
<tr>
<td>**Attraction/Experience**</td>
<td>**Type**</td>
<td>**Why**</td>
<td>**Hours**</td>
<td>**Entry (CHF)**</td>
<td>**Link & URL**</td>
<td>Notes</td>
</tr>
<tr>
<td>**\[Landmark\]**</td>
<td>Must-see</td>
<td>\[historic/unique\]</td>
<td>08:00–18:00</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[tip\]</td>
</tr>
<tr>
<td>**\[Museum\]**</td>
<td>Must-see</td>
<td>\[highlight\]</td>
<td>09:00–17:00</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[free day\]</td>
</tr>
<tr>
<td>**\[Market\]**</td>
<td>Must-see</td>
<td>\[culture\]</td>
<td>06:00–18:00</td>
<td>0</td>
<td>\[link\]</td>
<td>\[best time\]</td>
</tr>
<tr>
<td>**\[Square\]**</td>
<td>Must-see</td>
<td>\[highlight\]</td>
<td>09:00–17:00</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[free day\]</td>
</tr>
<tr>
<td>**\[Mall\]**</td>
<td>Must-see</td>
<td>\[highlight\]</td>
<td>09:00–17:00</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[free day\]</td>
</tr>
<tr>
<td>**\[Experience 1\]**</td>
<td>Unique</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Experience 2\]**</td>
<td>Unique</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Experience 3\]**</td>
<td>Unique</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
		</table>
	- **Hidden gems:**
		<table>
<tr>
<td>**Place**</td>
<td>**Why**</td>
<td>**Hours**</td>
<td>**Entry (CHF)**</td>
<td>**Link & URL**</td>
<td>**Notes**</td>
</tr>
<tr>
<td>**\[Hidden 1\]**</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Hidden 2\]**</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Hidden 3\]**</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Hidden 4\]**</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Hidden 5\]**</td>
<td>\[description\]</td>
<td>\[hours\]</td>
<td>\[X\]</td>
<td>\[link\]</td>
<td>\[details\]</td>
</tr>
		</table>
	- **Top 5 Nightclubs:**
		- **Nightlife areas:** \[District 1\] (main bar strip) • \[District 2\] (clubs/EDM) • \[District 3\] (rooftop/upscale)
		<table>
<tr>
<td>**Club**</td>
<td>**Genre**</td>
<td>**Hours**</td>
<td>**Entry (CHF)**</td>
<td>**Link & URL**</td>
<td>**Notes & Type**</td>
</tr>
<tr>
<td>**\[Club 1\]**</td>
<td>\[House/Techno\]</td>
<td>23:00–06:00</td>
<td>\[X–Y\]</td>
<td>\[link\]</td>
<td>\[dress code, peak nights\]</td>
</tr>
<tr>
<td>**\[Club 2\]**</td>
<td>\[Hip-Hop/R&B\]</td>
<td>22:00–04:00</td>
<td>\[X–Y\]</td>
<td>\[link\]</td>
<td>\[VIP tables available\]</td>
</tr>
<tr>
<td>**\[Club 3\]**</td>
<td>\[EDM/Commercial\]</td>
<td>23:00–05:00</td>
<td>\[X–Y\]</td>
<td>\[link\]</td>
<td>\[tourist-friendly\]</td>
</tr>
<tr>
<td>**\[Club 4\]**</td>
<td>\[Underground/Techno\]</td>
<td>00:00–late</td>
<td>\[X–Y\]</td>
<td>\[link\]</td>
<td>\[locals' favorite\]</td>
</tr>
<tr>
<td>**\[Club 5\]**</td>
<td>\[Live music/Mixed\]</td>
<td>21:00–03:00</td>
<td>\[X–Y\]</td>
<td>\[link\]</td>
<td>\[rooftop terrace\]</td>
</tr>
		</table>
	- **Allenamento e wellness:** the reader trains every day, so he needs a gym with a single entry day pass near where he sleeps, not a monthly membership
		<table>
<tr>
<td>**Struttura**</td>
<td>**Tipo**</td>
<td>**Ingresso singolo**</td>
<td>**Orari**</td>
<td>**Indirizzo**</td>
<td>**Note**</td>
</tr>
<tr>
<td>**\[Gym 1\]**</td>
<td>Gym</td>
<td>\[local currency / CHF\]</td>
<td>\[hours\]</td>
<td>\[address\]</td>
<td>\[walking time from the accommodation, equipment, day pass rules\]</td>
</tr>
<tr>
<td>**\[Gym 2\]**</td>
<td>Gym</td>
<td>\[local currency / CHF\]</td>
<td>\[hours\]</td>
<td>\[address\]</td>
<td>\[details\]</td>
</tr>
<tr>
<td>**\[Pool\]**</td>
<td>Pool</td>
<td>\[local currency / CHF\]</td>
<td>\[hours\]</td>
<td>\[address\]</td>
<td>\[lanes, cap required, busy hours\]</td>
</tr>
<tr>
<td>**\[Spa / Sauna\]**</td>
<td>Spa</td>
<td>\[local currency / CHF\]</td>
<td>\[hours\]</td>
<td>\[address\]</td>
<td>\[booking needed, mixed or separate\]</td>
</tr>
<tr>
<td>**\[Studio / Climbing\]**</td>
<td>Studio</td>
<td>\[local currency / CHF\]</td>
<td>\[hours\]</td>
<td>\[address\]</td>
<td>\[drop in class times, gear rental\]</td>
</tr>
		</table>
## 8. 🍽️ Food & drink (city specialties) {toggle="true"}
	- **Where to eat:** Budget / Mid / Fine dining options
	- **Where to have breakfast:** best spots for morning meals
	- **Where to make groceries:** supermarkets and local markets
	- **Coffee & work:** 2 or 3 cafés with reliable Wi‑Fi
	- **Cibo da provare**, the `Da provare, buoni` table: the dishes worth eating, desserts and drinks included, each with a venue that actually serves it and where it is eaten cheaply. Mandatory columns: `Piatto` · `Cosa è` · `Dove` · `Costo`.
		<table>
<tr>
<td>**Piatto**</td>
<td>**Cosa è**</td>
<td>**Cosa aspettarsi**</td>
<td>**Dove**</td>
<td>**Prezzo**</td>
</tr>
<tr>
<td>**\[Dish 1\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
<tr>
<td>**\[Dish 2\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
<tr>
<td>**\[Dish 3\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
<tr>
<td>**\[Dish 4\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
<tr>
<td>**\[Dish 5\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
		</table>
	- **Cibo strano**, the `Da provare, strani o divisivi` table, a table of its own and never merged into the one above: what a foreigner needs to be able to recognise on a menu, listed honestly and not as a dare. Same mandatory columns.
		<table>
<tr>
<td>**Piatto**</td>
<td>**Cosa è**</td>
<td>**Cosa aspettarsi**</td>
<td>**Dove**</td>
<td>**Prezzo**</td>
</tr>
<tr>
<td>**\[Dish 1\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
<tr>
<td>**\[Dish 2\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
<tr>
<td>**\[Dish 3\]**</td>
<td>\[what it is\]</td>
<td>\[taste, texture, how it arrives\]</td>
<td>\[venue with a real address\]</td>
<td>\[local currency / CHF\]</td>
</tr>
		</table>
## 9. 💸 Costs & payments (city benchmarks) {toggle="true"}
	- **Accommodation/night:** by area and category
	- **Typical daily costs:**
	- **Payments:** cards, cash, crypto Bitcoin, local apps; ATMs and fees
	- **Chi accetta Bitcoin:** named venues in this city that actually take it, with address and whether it is on chain or Lightning, plus Bitcoin ATMs with their fees. A city with none says so.
	- **Cost of Living:** link
## 10. 💼 Business & work (city level) {toggle="true"}
	- **Consulates in city (CH/IT):** or refer to capital
	- **Ecosystem & networking:** coworks, accelerators, communities, hubs, regular meetups
	- **Fintech / Web3 / Bitcoin / Energy / Real Estate:** venues, local quirks, and key players
	- **Venture Capital and Funds:** active VCs, family offices, hedge funds, and angel networks
	- **Influential people:** key LinkedIn profiles, local thought leaders, and connectors to reach out to
	- **Business chambers:** Swiss Chamber, Swiss Global Enterprice, local chambers of commerce, and trade associations
	- **Industry-specific:** conferences, trade shows, and sector-specific events in the city
	- **Local companies:**  Local Big and relevant company, to be aware, visit or to make business with.
	- **Consolati e camere di commercio:** Swiss and Italian consular presence in this city with address, phone, email and the out of hours consular number, plus the Swiss chamber and the local chambers of commerce with the person to contact
	- **Eventi tech ricorrenti:** the conferences, meetups and hackathons that come back every year, the month each one falls in, and whether it is worth planning a trip around
	- **Centri finanziari e business district**, mandatory: where they physically are, by district name and by the
	  landmark or street a taxi understands, with the walking or transit time from the centre. Which sector
	  sits in which one, so banks here, tech there, the old exchange floor somewhere else. One line per
	  district, a table from four districts up. The answer to `where do I go for a meeting`, not an essay
	  on the local economy.
	- **Come fare business in città**, mandatory, a dry list and never prose. One line per entry, the answer first.
		- **Come si ottiene un primo incontro:** the channel that actually works here, introduction, cold
		  email, LinkedIn, an event, a chamber of commerce
		- **Dove si tengono gli incontri:** office, hotel lobby, restaurant, coworking, and which one signals what
		- **Chi decide nella stanza:** who to address, who is present but not deciding
		- **Cosa portare:** business cards, printed deck, nothing, and whether the card ritual matters
		- **Tempi di risposta e follow up:** how long silence means no, when to chase and how
		- **Lingua della riunione e delle email:** which one, and whether an interpreter is expected
		- **Cosa fa chiudere un affare qui e cosa lo uccide:** the local specific, not general advice
---
**The tail of the page is one single line**, and nothing else:

```
Aggiornata il <data>. Fonti: <elenco>.
```

No `🗓️ Ultimo aggiornamento` block, no note on compression, no declaration of density. They were
noise. The spec version goes on that same line whenever it is not the current one, as `spec city-spec.md
1.4`. `🔁 Da riverificare prima di partire` is not down here: it is the **second block of the page**,
at the top, and it is a toggle.

## Mandatory entries

New requirements, not options. A page missing one of them is incomplete.

| Entry | Where it sits |
| --- | --- |
| `Dove stare, quartiere per quartiere` | section 2, the `Top quartieri dove stare` table, or section 10 where it reads better |
| `Centri finanziari e business district` | section 10, with the real names of the zones and who sits in each |
| `Come fare business in città` | section 10: coworking with prices, where meetings are held, the real office hours |
| `Cosa fare e cosa non fare` | section 6, the `Do` and `Don't` pair, two dry lists |
| `Cibo strano` | section 8, its own table beside `Cibo da provare`, never merged into it |

## Mandatory table columns

Set in `knowledge/page-standard.md`, `No lists in prose`, and repeated here because this is the file a skill
reads to know the shape of a page.

| Kind of list | Columns, in this order |
| --- | --- |
| Things to see, attractions, experiences | `Luogo` with the link · `Cosa è e perché vale` · `Costo` · `Orari` · `Tempo che serve` · `Hidden gem` |
| `Cibo da provare` and `Cibo strano` | `Piatto` · `Cosa è` · `Dove` · `Costo` |
| Districts | `Quartiere` · `Per chi va bene` · `Costo` · `Cosa evitare` |
| Coworking, gyms, services | `Nome` with the link · `Zona` · `Prezzo` · `Note` |
| Events and conferences | `Evento` with the link · `Quando` · `Dove` · `Costo` |
| Venues, bars, restaurants, work cafes | `Nome` with the link · `Zona` · `Per cosa` · `Costo` |

The link goes on the name of the item, inside its cell. `💎` in the `Hidden gem` column only where it
truly is one. A missing datum is `da verificare`, and where a place has to be booked ahead it is said in the
`Orari` column.
