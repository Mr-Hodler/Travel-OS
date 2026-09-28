# Nations spec, canonical

**This file is the canonical specification for the Nations data source.** The
Notion default template, page `29287313-332c-80ee-9aa7-cf580f5b2bd3`, is a
mirror of this file. Where the two diverge, this file wins and the Notion
template is the one that has to be brought into line.

The direction of truth was reversed on 2026-09-24. Before that date Notion was
the master and `knowledge/templates/nations-template.md` was its snapshot. That
snapshot is kept as history and is no longer the specification.

This spec carries the whole structure of the template, section by section, table
by table, toggle by toggle, plus the additions the template did not have. The
Jarvis instruction callouts are not reproduced: a specification does not need
instructions on how to fill itself. They stay in the Notion template, which is
where they are read.

Section names, their emoji and their numbering are kept exactly as they read in
Notion.

**No trip data on this page.** It is permanent. Dates, flights, times, the address of the accommodation and
booking references live on the Travel page of that trip, never here. The test: a line that becomes false
next month because the trip is over is in the wrong place. Rule in `knowledge/page-standard.md`,
`City and Nations pages carry no trip data`.

**Density.** What is measured is the **visible text**, not the characters of the markdown: table markup is
not read, so it does not count. Every heavy section carries **two levels**, the operational essentials
visible when the section opens and one toggle `Dettaglio: <what it holds>` with all the rest. Nothing is
deleted, it is moved one level down. Caps on the visible text: **900** for what an open section shows,
**1,200** for `⚡ Scheda rapida`, **1,200** for the `🔁 Da riverificare` toggle, **2,500** for the
first level of `Storia del paese`, **300** for a table cell, **4 lines** for a callout, **3 consecutive
lines** of prose. The `Dettaglio` toggles have no cap. **Declared exception: `Do`, `Don't` and the two food
tables stay at the first level of section 7.** The budget, the three cutting levers and the form rules are
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
<td>**Ingresso per svizzeri**</td>
<td>visa or no visa, maximum stay, document required</td>
</tr>
<tr>
<td>**Emergenze**</td>
<td>the numbers, police, ambulance, fire</td>
</tr>
<tr>
<td>**Ambasciata CH**</td>
<td>city, phone, out of hours consular number</td>
</tr>
<tr>
<td>**Ambasciata IT**</td>
<td>city, phone, out of hours consular number</td>
</tr>
<tr>
<td>**Valuta e tasso**</td>
<td>currency, rate against CHF, the date of the rate</td>
</tr>
<tr>
<td>**Cambio rapido**</td>
<td>**10, 50, 100 and 500 CHF** in local currency at the rate on the row above, plus the reverse for one round local amount. It is there to price something at a glance in front of a shelf. Where the local currency is the CHF the row is dropped</td>
</tr>
<tr>
<td>**Prefisso internazionale**</td>
<td>the country code, and how a local number is dialled: the trunk zero, whether it is dropped from abroad, mobile against landline</td>
</tr>
<tr>
<td>**Presa elettrica**</td>
<td>socket type, voltage, whether an adapter is needed from Switzerland</td>
</tr>
<tr>
<td>**Acqua del rubinetto**</td>
<td>drinkable or not</td>
</tr>
<tr>
<td>**SIM**</td>
<td>operator, price, eSIM or physical</td>
</tr>
<tr>
<td>**Crypto**</td>
<td>legal state and what is actually usable on the ground</td>
</tr>
<tr>
<td>**Da non dire**</td>
<td>the one subject that causes real offence</td>
</tr>
</table>

Below the table, **one single line**: time difference from Lugano, language, drives on the right or the
left, time format.

## 🔁 Da riverificare prima di partire {toggle="true"}
	**Second block of the page, and it is a toggle.** Max **1,200** visible characters. A dry list, no
	introductory sentence, every entry carrying its `(sez. N)` pointer and the date it was last checked. A
	check older than the trip is a defect.
	- **Regole di ingresso, visti e documenti** (sez. 1)
	- **Situazione sicurezza e avvisi di viaggio** (sez. 2)
	- **Tassi di cambio e costi tipici** (sez. 4)
	- **Chi governa oggi** (sez. 8)

---

## 1. 🛂 Entry, Visas, and Rules {toggle="true"}
	<details>
	<summary>**Storia del paese**</summary>
		**Two levels.** This first level is one line per period, **max 2,500 visible characters**, and it carries no dates, no names of rulers and no figures: those go into the nested toggle below. A few words more than a bare timeline, and not a book: one line per period with the fact that explains why that period still matters today. **Nested inside section 1 as its first block**, not placed before it: the first thing the page shows must be operational.
		- **Archi storici principali:** the eras that formed the country, one line each, from origin to today.
		- **Cosa spiega il paese di oggi:** which of those arcs still decides how the place works now, its borders, its institutions, its wealth, its neighbours and its open wounds.
		- **Perché il lettore ne ha bisogno:** what he would misread on the ground without it, in conversation, in a negotiation and standing in front of a monument.
		<details>
		<summary>**Dettaglio: date, nomi e cifre**</summary>
			The chronology itself: dates, the rulers and the treaties by name, the figures. No cap. Everything the first level had to leave out sits here, and nothing is deleted in order to keep the first level short.
		</details>
	</details>
	- Guidance
		- Official links to use: immigration portal, visa page, Swiss embassy, Italian embassy
		- Always state maximum stay length and possible extensions with sources
		- Specify documents required at border check and any photo specifications
		- Note any mandatory registration on arrival with hotel/authorities
		- Highlight sensitive rules: prescription medicines, drones, communication devices, alcohol
		<table fit-page-width="true" header-row="true">
<tr>
<td>Type</td>
<td>Length</td>
<td>Multiple entry</td>
<td>Where to apply</td>
<td>Notes</td>
</tr>
<tr>
<td>Visa-free (if applicable)</td>
<td></td>
<td></td>
<td>—</td>
<td></td>
</tr>
<tr>
<td>E‑visa</td>
<td></td>
<td></td>
<td>Official portal</td>
<td></td>
</tr>
<tr>
<td>Business</td>
<td></td>
<td></td>
<td>Embassy/Consulate</td>
<td></td>
</tr>
		</table>
	- Entry flow (compact)
		1. Passport validity ≥ 6 months
		2. Proof of onward ticket and accommodation address
		3. Accommodation registration (by hotel/host, where applicable)
	- Border checklist
		- Passport
		- Proof of exit
		- Accommodation booking
		- Health insurance
		- Proof of funds
	- Key requirements
		- Visa for Swiss citizens:
		- Entry requirements (documents, photos, funds):
		- Permitted stay and extensions:
		- Registration obligations on arrival:
	- Important local laws
		- Drugs:
		- Alcohol:
		- Sexual conduct & LGBTQ+ rights:
		- Photography permissions:
		- Religious/Political expression:
		- Legal ages (drinking/smoking):
	- Tax & work (optional)
		- Tax implications for long stays or remote work:
## 2. 🛡️ Safety & Risk Management {toggle="true"}
	- Guidance
		- Sources: official travel advisories (CH, IT, UK, US) and the country’s Interior Ministry/Civil Protection
		- Numbers: verify national numbers and regional exceptions; add tourist hotline if available
		- Seasonal risks: monsoon, typhoon, heatwaves, floods, air quality; specify timing and affected areas
		- Common scams: taxis without meter, currency swap scams, staged accidents, fake inspections; what to do
		- Health: animal bites, mosquitoes, water and ice; post-exposure protocols (e.g., rabies)
		- Useful contacts: CH and IT embassies/consulates, national health hotlines, anti-terror numbers
		- Maps: link maps of major hospitals and ERs in the capital and target cities
		- Insurance: note common exclusions and risky sports; keep insurance card handy
	<callout icon="⚠️" color="yellow_bg">
		Top 3 risks for this country:
		1)
		2)
		3)
	</callout>
	- Emergency numbers
		<table fit-page-width="true" header-row="true">
<tr>
<td>Service</td>
<td>Number</td>
<td>Notes</td>
</tr>
<tr>
<td>Emergency / Civil protection</td>
<td>112</td>
<td>National hotline (if applicable)</td>
</tr>
<tr>
<td>Police</td>
<td>113</td>
<td></td>
</tr>
<tr>
<td>Fire</td>
<td>114</td>
<td></td>
</tr>
<tr>
<td>Ambulance</td>
<td>115</td>
<td></td>
</tr>
<tr>
<td>Emergenza consolare CH</td>
<td></td>
<td>Swiss FDFA Helpline, 24/7, not the embassy switchboard</td>
</tr>
<tr>
<td>Emergenza consolare IT</td>
<td></td>
<td>Italian Unità di Crisi, 24/7, not the consulate switchboard</td>
</tr>
		</table>
	- **⚠️ Zone da evitare**, mandatory. **It is always there, and where there is nothing to avoid it says so in one line**: a page that leaves it out gives the reader no way to tell safe from unchecked. On a Nations page these are regions and border strips. No euphemism: if it is pickpocketing it says pickpocketing, if it is after dark it says after dark. Columns, in this order: `Zona` · `Cosa succede` · `Quando` · `Cosa fare invece`.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Zona</td>
<td>Cosa succede</td>
<td>Quando</td>
<td>Cosa fare invece</td>
</tr>
<tr>
<td>**\[Region or border strip\]**</td>
<td>\[what happens there, named plainly\]</td>
<td>\[time of day, season, or always\]</td>
<td>\[the route, the region or the behaviour that replaces it\]</td>
</tr>
		</table>
	- Geopolitical Risk and situation (eg War, riots)
		-
	- Common risks and scams
		-
	- Seasonality and severe weather
		-
	- Additional
		- Terrorism risk & political stability:
		- Local crime trends:
		- Current security advisories:
		- Military/surveillance presence:
		- Tourist scams or police harassment:
		- Dangerous animals or insects:
		- Endemic diseases or health risks:
		- Sexual health risks / STDs prevalence and advice:
		- National helplines and consular contacts (CH/IT):
## 3. 🧬 Health {toggle="true"}
	- Vaccines by traveler profile
		<table fit-page-width="true" header-row="true">
<tr>
<td>Profile</td>
<td>Vaccines</td>
<td>Notes</td>
</tr>
<tr>
<td>Routine</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Urban tourist</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Rural / Long‑stay</td>
<td></td>
<td></td>
</tr>
		</table>
	- Endemic diseases and prevention
		<table fit-page-width="true" header-row="true">
<tr>
<td>Risk</td>
<td>Prevention</td>
<td>Notes</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
		</table>
	- Minimum health insurance
		- High coverage limit
		- Medical evacuation
		- Activities covered (e.g., motorbike)
	- Indicators
		- Required or recommended vaccinations:
		- Disease risks:
		- Healthcare quality index + hospital access:
		- Insurance recommendations:
## 4. ⚙️ Utilities & Daily Life {toggle="true"}
	- Currency and exchange
		- ISO code, typical ATM fees, avoid DCC, best practices
	- Electricity and plugs
		<table fit-page-width="true" header-row="true">
<tr>
<td>Voltage</td>
<td>Frequency</td>
<td>Plug types</td>
<td>Adapter</td>
</tr>
<tr>
<td>220V</td>
<td>50Hz</td>
<td>Type A / C (country-specific)</td>
<td>Universal advised</td>
</tr>
		</table>
	- Mobile networks (tourist)
		<table fit-page-width="true" header-row="true">
<tr>
<td>Operator</td>
<td>Coverage</td>
<td>Tourist package</td>
<td>Where to buy</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>Airport / Store</td>
</tr>
		</table>
	- Water and hygiene
		- Tap water:
		- Ice:
		- Teeth:
	- Apps to download
		- Grab, Google Maps, Translate, Weather, Air Quality
	- Other indicators
		- Currency exchange best practices:
		- Cost of living (high/medium/low):
		- Mobile and internet (penetration/reliability):
		- Water potability:
	- **Costi tipici nel paese**
		<table fit-page-width="true" header-row="true">
<tr>
<td>Voce</td>
<td>Valuta locale</td>
<td>CHF</td>
<td>Note</td>
</tr>
<tr>
<td>Caffè</td>
<td></td>
<td></td>
<td>Bar, at the counter</td>
</tr>
<tr>
<td>Pranzo</td>
<td></td>
<td></td>
<td>Simple meal, one person</td>
</tr>
<tr>
<td>Cena</td>
<td></td>
<td></td>
<td>Mid range restaurant, one person</td>
</tr>
<tr>
<td>Taxi urbano</td>
<td></td>
<td></td>
<td>Typical urban run, about 5 km</td>
</tr>
<tr>
<td>Birra</td>
<td></td>
<td></td>
<td>Bar, 0.5 l</td>
</tr>
<tr>
<td>Supermercato settimanale</td>
<td></td>
<td></td>
<td>One person, seven days</td>
</tr>
		</table>
		- **Cambio usato per la conversione:** state the rate and the date it was read. A conversion without a rate beside it is not verifiable.
	- **Budget giornaliero**, mandatory, **one single line**: the realistic spend per day on a work trip, and what that figure covers. Hotel, meals, urban transport and a coffee, stated as a range where the range is real.
	- **`Clima mese per mese`**, mandatory. A table, **all twelve months**, one row each. It replaces seasonal prose, which the reader has to deduce a month out of. Columns: `Mese` · `Min / Max media` · `Pioggia o neve` · `Nota`.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Mese</td>
<td>Min / Max media</td>
<td>Pioggia o neve</td>
<td>Nota</td>
</tr>
<tr>
<td>**Gennaio**</td>
<td>\[-2 / 3 °C\]</td>
<td>\[days of rain or snow, and which of the two\]</td>
<td>\[the one thing that changes the day: daylight hours, wind, humidity\]</td>
</tr>
<tr>
<td>**Febbraio**</td>
<td>\[min / max\]</td>
<td>\[rain or snow\]</td>
<td>\[the deciding detail\]</td>
</tr>
		</table>
	- **`Quando andare e quando no`**, mandatory, **three or four lines**: the best months, the months to avoid and why, and the bridges and dead periods when nothing gets decided. It is not the holidays table in section 7, which says what closes on a given date.
	- **`Orari di negozi, banche e uffici`**, mandatory. A compact table with the exceptions that matter, the Saturday, the Sunday, the long lunch break and the one weekday something is shut. Columns: `Cosa` · `Orario` · `Eccezioni`.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Cosa</td>
<td>Orario</td>
<td>Eccezioni</td>
</tr>
<tr>
<td>**Negozi**</td>
<td>\[weekday hours\]</td>
<td>\[Saturday, Sunday, the long lunch break\]</td>
</tr>
<tr>
<td>**Banche**</td>
<td>\[weekday hours\]</td>
<td>\[the afternoon window, the day they shut\]</td>
</tr>
<tr>
<td>**Uffici pubblici**</td>
<td>\[weekday hours\]</td>
<td>\[counter hours against office hours, booking required\]</td>
</tr>
<tr>
<td>**Supermercati**</td>
<td>\[weekday hours\]</td>
<td>\[Sunday, public holidays\]</td>
</tr>
		</table>
	- **`Rimborso IVA per residenti svizzeri`**, mandatory. **Switzerland is outside the EU and the entitlement is real, so it is not left off the page.** Minimum spend per receipt, the VAT rate and what actually comes back, where the form is stamped, what has to be shown at the counter, and the deadline to claim it. Where the country refunds nothing to a Swiss resident, the page says that instead.
## 5. ✈️ National Transportation {toggle="true"}
	- How to book
		<table fit-page-width="true" header-row="true">
<tr>
<td>Mode</td>
<td>App/Site</td>
<td>Booking window</td>
<td>Notes</td>
</tr>
<tr>
<td>Domestic flight</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Train</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Bus/Coach</td>
<td></td>
<td></td>
<td></td>
</tr>
		</table>
	- Roads and driving
		- IDP, helmet, rain, night driving, insurance
	- **`Voli diretti dalla Svizzera`**, mandatory. Columns: `Da` · `A` · `Compagnia` · `Durata` · `Frequenza`. `Da` covers **Zurigo, Ginevra, Basilea and Milano**, and a route that does not exist is written as not existing rather than left out, because an empty row and a missing row read the same and mean the opposite.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Da</td>
<td>A</td>
<td>Compagnia</td>
<td>Durata</td>
<td>Frequenza</td>
</tr>
<tr>
<td>**Zurigo**</td>
<td>\[airport\]</td>
<td>\[carrier\]</td>
<td>\[h:mm\]</td>
<td>\[flights per day or per week, and the seasonal window\]</td>
</tr>
<tr>
<td>**Ginevra**</td>
<td>\[airport\]</td>
<td>\[carrier\]</td>
<td>\[h:mm\]</td>
<td>\[frequency\]</td>
</tr>
<tr>
<td>**Basilea**</td>
<td>\[airport\]</td>
<td>\[carrier\]</td>
<td>\[h:mm\]</td>
<td>\[frequency\]</td>
</tr>
<tr>
<td>**Milano**</td>
<td>\[airport\]</td>
<td>\[carrier\]</td>
<td>\[h:mm\]</td>
<td>\[frequency\]</td>
</tr>
		</table>
	- **`Fuori città`**, mandatory, **at least three destinations**. On a Nations page they are the places worth using the main cities as a base for, a full day out or one overnight, and never a local activity inside a city. Columns: `Meta` with the link · `Come si arriva e quanto` · `Cosa ci fai` · `Costo` · `Giornata o pernottamento`.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Meta</td>
<td>Come si arriva e quanto</td>
<td>Cosa ci fai</td>
<td>Costo</td>
<td>Giornata o pernottamento</td>
</tr>
<tr>
<td>**\[Destination 1\]**</td>
<td>\[from which city, the mode, the minutes and the fare\]</td>
<td>\[what is actually done there\]</td>
<td>\[local currency / CHF\]</td>
<td>\[day trip or one night\]</td>
</tr>
<tr>
<td>**\[Destination 2\]**</td>
<td>\[mode, minutes, fare\]</td>
<td>\[what is done there\]</td>
<td>\[local currency / CHF\]</td>
<td>\[day trip or one night\]</td>
</tr>
<tr>
<td>**\[Destination 3\]**</td>
<td>\[mode, minutes, fare\]</td>
<td>\[what is done there\]</td>
<td>\[local currency / CHF\]</td>
<td>\[day trip or one night\]</td>
</tr>
		</table>
	- Additional
		- Domestic airlines and routes:
		- Rail systems and apps:
		- Bus and coach networks:
		- Road conditions:
		- Border crossing info:
## 6. 📡 Working: Bitcoin & Tech {toggle="true"}
	- Compliance and legal landscape
		- Crypto: legal tender? payments? licensed exchanges?
		- VPN: legal? common usage?
	- Digital nomad readiness
		<table fit-page-width="true" header-row="true">
<tr>
<td>City</td>
<td>Coworking</td>
<td>Avg. speed</td>
<td>Notes</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
		</table>
	- Indicators
		- Crypto legality:
		- Bitcoin ATM coverage & crypto‑friendly places:
		- VPN legality & censorship status:
		- Digital nomad readiness:
	- **Fare business nel paese**, a dry list and never prose. One line per entry, the answer first and no run up to it. If an entry needs more than two lines it belongs in a table.
		- **Orari di lavoro:** office hours, the lunch break and how long it really lasts, which day the working week starts and ends
		- **Stile delle riunioni:** punctuality, hierarchy in the room, who speaks and who decides, how much small talk comes before business, slides or conversation
		- **Mesi morti per le ferie:** the weeks when nothing is decided, national holidays and school breaks included
		- **Stile di negoziazione:** direct or indirect, how a no is actually said, haggling or fixed terms, what a handshake commits to
		- **Tempi decisionali:** how long from first meeting to signature, how many levels sign off, what usually stalls
		- **Registro delle email:** formal or informal opening, titles, which language to write in, expected reply time and what silence means
## 7. 🕍 Culture & Identity {toggle="true"}
	**Declared exception to the 900 character cap:** `Do`, `Don't` and the two food tables stay at the **first level** of this section. They are what the reader opens it for. Everything else in the section, the holidays table and the `Additional` block, goes into `Dettaglio: feste, religione, lingua, galateo`.
	- **Do**, explicit and specific to this country, never generic guidebook politeness. **List form, never a paragraph.**
		- One line per item, with the reason it matters here
	- **Don't**, explicit and specific to this country. **List form, never a paragraph.**
		- One line per item, with what actually happens if you do it
	- **Cosa non dire**, the subjects that cause real offence here. **List form, never a paragraph.** Not awkwardness, offence.
		- One line per item, with why it lands badly
	- **Cibo da provare**, at the first level of this section. Dishes, desserts, drinks, and where it is eaten cheaply. Columns, in this order: `Piatto` · `Cosa è` · `Dove`, the venue with its link or the kind of place · `Costo`.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Piatto</td>
<td>Cosa è</td>
<td>Dove</td>
<td>Costo</td>
</tr>
<tr>
<td>**\[Dish 1\]**</td>
<td>\[what it is, one line\]</td>
<td>\[venue with a link, or the kind of place\]</td>
<td>\[local currency / CHF\]</td>
</tr>
		</table>
	- **Cibo strano, quello che serve saper riconoscere nel menu**, a table of its own and never merged into the one above. Same columns.
		<table fit-page-width="true" header-row="true">
<tr>
<td>Piatto</td>
<td>Cosa è</td>
<td>Dove</td>
<td>Costo</td>
</tr>
<tr>
<td>**\[Dish 1\]**</td>
<td>\[what it is, and what a foreigner is actually served\]</td>
<td>\[venue with a link, or the kind of place\]</td>
<td>\[local currency / CHF\]</td>
</tr>
		</table>
	- Holidays with impact
		<table fit-page-width="true" header-row="true">
<tr>
<td>Date</td>
<td>Name</td>
<td>Impact</td>
</tr>
<tr>
<td></td>
<td></td>
<td>Closures/transport/alcohol</td>
</tr>
		</table>
	- Additional
		- Religions and dominant beliefs:
		- National language(s) + local dialects:
		- Useful phrases:
		- Ethnic groups & population:
		- Attitudes toward foreigners:
		- Traditional etiquette and respect forms:
## 8. 🏛️ Government & International Relations {toggle="true"}
	- Political system:
	- **Chi governa oggi:** head of state by name, head of government by name, party or coalition, with the date it was verified beside it. Web verified, never from memory.
	- Relationship with Switzerland and Italy:
	- Notable diplomatic issues or restrictions:
## 9. 🔗 Official References & Further Reading {toggle="true"}
	- Government travel portal:
	- Immigration office:
	- Digital nomad visa portal:
	- National tourism board:
	- Ministry of Health:
	- Central bank / currency authority:
---
**The tail of the page is one single line**, and nothing else:

```
Aggiornata il <data>. Fonti: <elenco>.
```

No `🗓️ Ultimo aggiornamento` block, no note on compression, no declaration of density. They were
noise. The spec version goes on that same line whenever it is not the current one, as `spec nations-spec.md
1.4`. `🔁 Da riverificare prima di partire` is not down here: it is the **second block of the page**,
at the top, and it is a toggle.

## Mandatory entries

New requirements, not options. A page missing one of them is incomplete. All of them in lean form: a table,
one row one fact, no prose around it.

| Entry | Where it sits |
| --- | --- |
| `Cibo da provare` and `Cibo strano` | section 7, two separate tables, both at the first level |
| `⚠️ Zone da evitare` | section 2. **Always present**, and where there is nothing to avoid it says so |
| `Cambio rapido` | `⚡ Scheda rapida`, right under the currency row. 10, 50, 100 and 500 CHF, dropped only where the local currency is the CHF |
| Prefisso internazionale | `⚡ Scheda rapida`, with how a local number is dialled |
| `Clima mese per mese` | section 4, all twelve months |
| `Quando andare e quando no` | section 4, three or four lines. Not the holidays table |
| `Orari di negozi, banche e uffici` | section 4, compact, with the exceptions that matter |
| `Rimborso IVA per residenti svizzeri` | section 4. Switzerland is outside the EU and the entitlement is real |
| `Budget giornaliero` | section 4, one line, and what the figure covers |
| `Voli diretti dalla Svizzera` | section 5, from Zurigo, Ginevra, Basilea and Milano |
| `Fuori città` | section 5, **at least three** destinations, a day out or one overnight |

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
| `⚠️ Zone da evitare` | `Zona` · `Cosa succede` · `Quando` · `Cosa fare invece` |
| `Fuori città` | `Meta` with the link · `Come si arriva e quanto` · `Cosa ci fai` · `Costo` · `Giornata o pernottamento` |
| `Clima mese per mese` | `Mese` · `Min / Max media` · `Pioggia o neve` · `Nota` |
| `Voli diretti dalla Svizzera` | `Da` · `A` · `Compagnia` · `Durata` · `Frequenza` |
| `Orari di negozi, banche e uffici` | `Cosa` · `Orario` · `Eccezioni` |

The link goes on the name of the item, inside its cell. `💎` in the `Hidden gem` column only where it
truly is one. A missing datum is `da verificare`.
