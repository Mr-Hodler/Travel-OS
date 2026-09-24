# Travel spec, canonical

**This file is the canonical specification for the Travel data source.** The
Notion default template, page `1da87313-332c-808c-9e0b-df99c23f031e`, is a
mirror of this file. Where the two diverge, this file wins and the Notion
template is the one that has to be brought into line.

The direction of truth was reversed on 2026-09-24. Before that date Notion was
the master and `knowledge/templates/travel-template.md` was its snapshot. That
snapshot is kept as history and is no longer the specification.

This spec carries the whole structure of the template, section by section, table
by table, toggle by toggle, plus the additions the template did not have. This
template carries no Jarvis instruction callout, so nothing was dropped. The red
`CRITICAL NOTES` callout is part of the page and stays.

Section names, their emoji and their numbering are kept exactly as they read in
Notion.

---

# ✈️ Travel Brief — \[TRIP NAME\]
**Travelers:** \[Names\]
**Duration:** \[X days\] \| \[Start Date\] - \[End Date\]
**Total Cost:** CHF \[Total\] (CHF \[Per Person\] per person)
**Regola:** un viaggio una pagina, anche a cavallo di più paesi. Two countries in one trip is still one page, and splitting it is the defect this rule exists to stop.
<callout icon="🚨" color="red_bg">
	**DA RISOLVERE**
	This is the part of the page that is worth the most. It is filled by actively going to look for what is still open, not by waiting for it to surface on its own.
	Every open point gets a number, the list is ordered by urgency with the most urgent first, and each point carries the single action that closes it.
	1. **\[Open point\]**, action that closes it: \[one action, one owner, one deadline\]
	2. **\[Open point\]**, action that closes it: \[one action, one owner, one deadline\]
	3. **\[Open point\]**, action that closes it: \[one action, one owner, one deadline\]
	A point leaves this callout when it is closed, not when it is old. An empty DA RISOLVERE means every point was closed, and it is only true if someone looked.
</callout>
<details>
<summary>**Modo semplificato**</summary>
	Not every trip needs the whole page. Four days in Warsaw does not get a template built for three weeks in China.
	**Da tenere sempre:** the header, DA RISOLVERE, section 1 with the home transfers, section 2, the Detailed Daily Schedule table, Conflitti di agenda, the cost summary with its two groups, Emergency Contacts, and Prima di partire in the final checklist.
	**Si possono omettere su un viaggio non complesso:** Plan B weather alternatives, the Tours pickup summary when there are no tours, Food Restrictions when nobody has any, the medications list beyond a basic kit, the full packing list, the Nightlife recommendations, the Activities Status Summary and Trip Reminders.
	**Regola:** leaving a section out is a decision, and it gets written down here, so the next reader knows it was omitted on purpose and not forgotten.
</details>
<callout icon="⚠️" color="red_bg">
	**CRITICAL NOTES**
	Add any critical information here (allergies, special requirements, emergency contacts, etc.)
</callout>
---
## 1. ✈️ Flights & Transfers {toggle="true"}
### Transfer da e verso casa
The home to airport leg is the one that is always missing. Both directions, both dates, both priced.
- **Andata, casa → aeroporto:** \[Mode\] \| departure \[HH:MM\] \| arrival \[HH:MM\] \| \[X h XX min\] \| CHF \[Amount\] \| booked: \[Yes/No + reference\]
- **Ritorno, aeroporto → casa:** \[Mode\] \| departure \[HH:MM\] \| arrival \[HH:MM\] \| \[X h XX min\] \| CHF \[Amount\] \| booked: \[Yes/No + reference\]
- **Margine sul check-in:** minutes between arriving at the airport and the bag drop or check in deadline
- **Chi porta e chi riprende:** driver, parking, or the last public departure that still works
- **Piano B:** what to do if this leg fails, the alternative mode and its last usable departure
### Pre-departure Ground Transfer
- **Transport:** \[Mode\] → \[Destination\]
- **Date & Time:** \[HH:MM\] — <mention-date start="YYYY-MM-DD"/>
- **Duration:** \[X h XX min\]
### International Flights
**Outbound: \[Origin\] → \[Destination\]** — \[Date\]
- **Flight:** \[Airline\] \[Flight Number\] (via \[Hub\] if applicable)
- **Route:** \[CODE HH:MM\] → \[CODE HH:MM\] (\[Duration\])
- **Passengers:** \[Name 1\] (\[Passport\]) + \[Name 2\] (\[Passport\])
- **PNR:** \[Booking Code\]
- **Cost:** CHF \[Amount\]
**Return: \[Origin\] → \[Destination\]** — \[Date\]
- **Flight:** \[Airline\] \[Flight Number\] (via \[Hub\] if applicable)
- **Route:** \[CODE HH:MM\] → \[CODE HH:MM\] (\[Duration\])
- **PNR:** \[Booking Code\]
- **Cost:** CHF \[Amount\]
### Internal Flights / Transfers
- 🚆 / ✈️ / 🚖 From \[Location\] to \[Destination\]
	- \[Time\] \| \[Company/Platform\]
	- **Cost:** CHF \[Amount\]
---
## 2. 🏨 Accommodations
### \[City/Location Name\] — \[Area\] (\[Dates\]) {toggle="true"}
- **Property:** \[Hotel/Airbnb Name\]
- **Address:** \[Full Address\]
- **Check-in:** \[Day Date\], \[HH:MM\] \| **Check-out:** \[Day Date\], \[HH:MM\]
- **Host/Contact:** \[Name\] \| **Phone:** \[Number\]
- **Confirmation:** \[Booking Code\]
- **Cost:** CHF \[Amount\] (\[X nights\])
- **Area Notes:** \[Brief description of neighborhood, proximity to attractions, safety\]
- **WiFi:** \[Available/Password if provided\]
### \[City/Location Name\] — \[Area\] (\[Dates\]) {toggle="true"}
- **Property:** \[Hotel/Airbnb Name\]
- **Address:** \[Full Address\]
- **Check-in:** \[Day Date\], \[HH:MM\] \| **Check-out:** \[Day Date\], \[HH:MM\]
- **Host/Contact:** \[Name\] \| **Phone:** \[Number\]
- **Confirmation:** \[Booking Code\]
- **Cost:** CHF \[Amount\] (\[X nights\])
- **WiFi:** \[Available/Password if provided\]
---
## 3. 🗓️ Day-by-Day Itinerary
### 📋 Action Items — To Book & Prepare
- [ ] \[Tour/Activity Name\] — \[Date\] — \[Booking Link\]
- [ ] \[Document to prepare\]
- [ ] \[Item to purchase\]
---
### Impegni remoti e call
A work trip from the road carries calls that land inside the days. They are not tours and they do not belong in the tour rows.
<table fit-page-width="true" header-row="true">
<tr>
<td>**Data**</td>
<td>**Ora locale**</td>
<td>**Ora Lugano**</td>
<td>**Impegno**</td>
<td>**Partecipanti**</td>
<td>**Durata**</td>
<td>**Dove serve stare**</td>
<td>**Stato**</td>
</tr>
<tr>
<td>\[Day Date\]</td>
<td>\[HH:MM\]</td>
<td>\[HH:MM\]</td>
<td>\[Call or meeting name\]</td>
<td>\[Who\]</td>
<td>\[X min\]</td>
<td>\[Quiet room, hotel, coworking, a phone is enough\]</td>
<td>\[Confermata / Da spostare\]</td>
</tr>
<tr>
<td>\[Day Date\]</td>
<td>\[HH:MM\]</td>
<td>\[HH:MM\]</td>
<td>\[Call or meeting name\]</td>
<td>\[Who\]</td>
<td>\[X min\]</td>
<td>\[Where it has to be taken from\]</td>
<td>\[Confermata / Da spostare\]</td>
</tr>
</table>
---
## 🗓️ Detailed Daily Schedule
Green - Travel Days
Blue - Full Day Tours/Activities
**Note:** Consider +30min buffer time between activities for traffic/delays
<table fit-page-width="true" header-row="true">
<colgroup>
<col width="150">
<col width="145">
<col>
<col width="401">
<col width="426">
<col width="379">
<col>
<col>
<col>
</colgroup>
<tr>
<td>**Day**</td>
<td>**Location**</td>
<td>**Accommodation**</td>
<td>**Morning**</td>
<td>**Afternoon**</td>
<td>**Evening**</td>
<td>**Cost (CHF)**</td>
<td>**Link & Source**</td>
<td>**Status**</td>
</tr>
<tr color="green_bg">
<td>**G1**\[Day Date\]</td>
<td>\[Origin\] → \[Dest\]</td>
<td>In flight</td>
<td>\[HH:MM\] \[Transport details\]<br>\[HH:MM\] ✈️ \[Flight\] \[Route\]</td>
<td>In flight</td>
<td>Overnight travel</td>
<td>\[Amount\]</td>
<td>\[Booking Platform\]</td>
<td>✅ Booked</td>
</tr>
<tr>
<td>**G2**\[Day Date\]</td>
<td>\[City\]</td>
<td>🏨 \[Accommodation Name\]</td>
<td>\[HH:MM\] \[Activity\]</td>
<td>\[Activity/Free time\]</td>
<td>\[HH:MM\] \[Activity\]</td>
<td>—</td>
<td>—</td>
<td>·</td>
</tr>
<tr color="blue_bg">
<td>**G3**\[Day Date\]</td>
<td>\[Tour Name\]</td>
<td>🏨 \[Accommodation Name\]</td>
<td>\[HH:MM\] \[Pickup details\]<br>\[HH:MM\] \[First activity\]</td>
<td>\[HH:MM\] \[Activity\]<br>\[HH:MM\] \[Activity\]</td>
<td>\[HH:MM\] \[Return/Evening activity\]</td>
<td>\[Amount\]</td>
<td>\[Booking Link\]</td>
<td>✅ Booked / To Book</td>
</tr>
</table>
### 💵 Cost Summary {toggle="true"}
- **Flights (international):** CHF \[Amount\] \| Status: \[Paid/Pending\]
- **Flights (domestic):** CHF \[Amount\] \| Status: \[Paid/Pending\]
- **Lodging:** CHF \[Amount\] (\[Breakdown by city\]) \| Status: \[Paid/Pending\]
- **Tours & Activities:** CHF \[Amount\] \| Status: \[Paid/Pending\]
- **Ground transport:** CHF \[Amount\] \| Status: \[Paid/Pending\]
**Total confirmed:** CHF \[Amount\] (CHF \[Per Person\] per person)
**Total paid:** CHF \[Amount\]
**Total pending:** CHF \[Amount\]
**Note:** Variable expenses (meals, local transport, tips) are not included in the total.
**A carico azienda**
- \[Line item\]: CHF \[Amount\] \| Status: \[Paid/Pending\] \| how it is reclaimed and with which receipt
- \[Line item\]: CHF \[Amount\] \| Status: \[Paid/Pending\]
**Totale a carico azienda:** CHF \[Amount\]
**A carico mio**
- \[Line item\]: CHF \[Amount\] \| Status: \[Paid/Pending\]
- \[Line item\]: CHF \[Amount\] \| Status: \[Paid/Pending\]
**Totale a carico mio:** CHF \[Amount\]
**Nota:** every line above sits in exactly one of the two groups, and the two totals add up to the total confirmed. A line nobody has assigned yet goes in DA RISOLVERE.
### 🌦️ Plan B — Weather-Dependent Alternatives {toggle="true"}
- **If \[Primary Activity\] is cancelled due to weather:**
	- Option A: \[Alternative indoor activity\] — \[Location/Cost\]
	- Option B: \[Alternative covered activity\] — \[Location/Cost\]
- **Rainy day recommendations:**
	- \[Museum/Indoor attraction\] — \[Details\]
	- \[Covered market/Shopping area\] — \[Details\]
---
## ⚠️ Conflitti di agenda
The checks to run against the filled itinerary. Each one is either clear or it becomes a numbered point in DA RISOLVERE. Found by the tool, never by the reader on the day.
- [ ] **Call durante un volo o un tour:** every remote commitment cross checked against the flight windows and the tour windows
- [ ] **Check-out incompatibile con l'orario del volo:** the hours between check out and departure, and where the luggage sits in between
- [ ] **Fuso orario:** every call time converted both ways, and the days a time zone shift pushes a call into the night or into a travel leg
- [ ] **Giorni di chiusura:** whatever is meant to be seen, checked against the day it actually closes, museums, markets and offices included
- [ ] **Domeniche e festivi:** shops, pharmacies, banks and public transport on reduced service on the days the itinerary assumes normal service
---
## 🚐 Tours — Pickup & Meeting Points Summary
### \[Tour Name\] (\[Date\]) {toggle="true"}
- **Pickup:** \[HH:MM\] at \[Address/Location\]
- **Provider:** \[Company Name\]
- **Contact:** \[Email/Phone\]
- **Booking:** \[Platform + Link\]
- **Notes:** \[Special instructions, what to bring, etc.\]
### \[Tour Name\] (\[Date\]) {toggle="true"}
- **Pickup:** \[HH:MM\] at \[Address/Location\]
- **Provider:** \[Company Name\]
- **Meeting point:** \[Alternative location if applicable\]
- **Booking:** \[Platform + Link\]
---
## 4. 🧭 Logistics & Conditions
### Local Transport {toggle="true"}
- **\[App/Service\]:** \[Description and use case\]
- **\[App/Service\]:** \[Description and use case\]
- **Walking:** \[Notes on walkability\]
- **Bicycles/Scooters:** \[Rental info and costs\]
### Essential Apps {toggle="true"}
- **\[App Name\]:** \[Purpose\]
- **\[App Name\]:** \[Purpose\]
- **Google Maps:** Navigation (download offline maps)
- **Google Translate:** With camera function for menus
- **Currency converter**
### Local SIM & Connectivity {toggle="true"}
- **Recommended carriers:** \[Operator 1\] (CHF \[Amount\] for \[GB\] data) \| \[Operator 2\] (CHF \[Amount\] for \[GB\] data)
- **Where to buy:** Airport arrivals hall, convenience stores (\[Specific store names\])
- **WiFi availability:** All accommodations have WiFi. Public WiFi available at \[locations\]
- **VPN requirements:** \[Required/Not required for destination\]
- **Data needs estimate:** \[GB\] for \[X\] days (maps, messaging, occasional browsing)
### Weather Forecast (\[Month\]) {toggle="true"}
- **\[Region/City\]:** \[Temperature range\], \[Conditions\] — \[What to pack\]
- **\[Region/City\]:** \[Temperature range\], \[Conditions\] — \[What to pack\]
### Local Tips {toggle="true"}
- **Currency:** \[Local Currency\] — 1 CHF ≈ \[Exchange Rate\]
- **Cash:** \[Cash/card acceptance notes\]
- **Tipping:** \[Local tipping customs\]
- **Bargaining:** \[When and how to bargain\]
- **Scams:** \[Common scams to watch for\]
- **Dress code:** \[Cultural considerations\]
- **Language:** \[Useful phrases or communication tips\]
### Emergency Contacts {toggle="true"}
- **Local emergency number:** \[Number\] (police/ambulance/fire)
- **Travel insurance:** \[Company\] — \[Policy Number\] — Emergency hotline: \[Number\]
- **Embassy/Consulate:** Swiss Embassy/Consulate in \[City\] — \[Address\] — \[Phone\] — \[Email\]
- **Main accommodations:**
	- \[Hotel 1\]: \[Phone number\]
	- \[Hotel 2\]: \[Phone number\]
- **Tour operators emergency contact:** \[If applicable\]
### \[City\] — Nightlife/Activities Recommendations {toggle="true"}
**\[Category\]:**
- \[Venue Name\] — \[Description, price range\]
- \[Venue Name\] — \[Description, price range\]
**\[Category\]:**
- \[Venue Name\] — \[Description, price range\]
### \[City\] — Wellness (Spa, Gym, etc.) {toggle="true"}
**Spa & Massage:**
- **\[Venue Name\]** — \[Services, specialties, price range\]
**Gyms:**
- **\[Gym Name\]** — \[Facilities, day pass info, location\]
---
## 5. 📂 Travel Docs & Attachments
### Drive Folder
[**Trip Main Folder**](Drive-Link-Here)
### Visa Documents
- \[Traveler Name\] E-Visa/Visa: \[Download Link or stored in Drive\]
	- Code: \[Visa Code\]
	- Valid: \[Date Range\]
	- \[Entry type\]
### Food Restrictions & Allergy Management {toggle="true"}
**\[Person Name\] — \[Allergy Type\]**
- **Allergens:** \[List all allergens including hidden ingredients like fish sauce\]
- **Severity:** \[Mild/Severe/Life-threatening\]
- **Translation card:** \[Link to translated allergy card in local language\]
- **Key phrases in \[Local Language\]:**
	- "I am allergic to \[allergen\]" — \[Translation\]
	- "Does this contain \[allergen\]?" — \[Translation\]
	- "No fish sauce please" — \[Translation\]
- **Pre-verified safe restaurants:**
	- \[Restaurant Name\] — \[Address\] — \[Notes on safe options\]
	- \[Restaurant Name\] — \[Address\] — \[Notes on safe options\]
- **Emergency supplies:**
	- \[Supermarket name\] near accommodations for safe packaged food
	- EpiPen location: \[If applicable\]
### Booking Confirmations
All confirmations stored in Drive folder:
- Flight confirmations
- Accommodation confirmations
- Tour/activity vouchers
- Insurance documents
### Insurance
- **Provider:** \[Insurance Company\]
- **Policy Number:** \[Number\]
- **Coverage:** \[Brief description\]
- **Emergency Contact:** \[Phone/Email\]
---
## 🎯 Activities Status Summary
### ✅ Confirmed & Paid
- \[Activity/Booking\] — CHF \[Amount\]
- \[Activity/Booking\] — CHF \[Amount\]
### 📅 To Book Before Trip
- [ ] **\[Activity Name\]** (\[Date\]) — \[Booking Link\]
- [ ] **\[Activity Name\]** (\[Date\]) — \[Booking Link\]
### 🔍 Research & Decide
- \[Optional activity to research\]
- \[Restaurant reservations\]
- \[Additional services to book\]
---
## 💡 Notes & Reminders
<details>
<summary>**Medications & Products to Bring**</summary>
</details>
- [ ] **Antidiarrheal:** \[Product name\]
- [ ] **Intestinal antibiotic:** \[Product name\]
- [ ] **Antinausea:** \[Product name\]
- [ ] **Probiotics**
- [ ] **Antihistamine:** \[Product name\]
- [ ] **Fever reducer/Pain reliever:** \[Product name\]
- [ ] **Broad-spectrum antibiotic:** \[Product name\] (prescription)
- [ ] **Antibiotic cream:** \[Product name\]
- [ ] **Insect repellent:** DEET 30-50%
- [ ] **Cortisone cream:** For bites and stings
- [ ] **Disinfectant spray:** \[Product name\]
- [ ] **Sunscreen SPF 50+**
- [ ] **After sun/Aloe vera**
- [ ] **Band-aids:** Various sizes + blister patches
- [ ] **Hand sanitizer**
- [ ] **Eye drops**
- [ ] **Electrolyte supplements**
<details>
<summary>**🎒 Packing List**</summary>
</details>
**Clothing (climate: \[description\]):**
- [ ] T-shirts/light tops (\[Quantity\])
- [ ] Pants/shorts (\[Quantity\])
- [ ] Long clothing for temples/religious sites
- [ ] Swimwear (\[Quantity\])
- [ ] Comfortable walking shoes
- [ ] Sandals/flip-flops
- [ ] Rain jacket/windbreaker
- [ ] Light sweater/cardigan for AC
- [ ] Hat/cap with visor
- [ ] Sunglasses
- [ ] Underwear and socks (\[Quantity\])
**Accessories & Electronics:**
- [ ] Universal adapter (\[Plug type for destination\])
- [ ] Power bank
- [ ] Charging cables
- [ ] Headphones/earbuds
- [ ] Camera (optional)
**Hygiene & Health:**
- [ ] Sunscreen SPF 50+
- [ ] Insect repellent DEET 30-50%
- [ ] Personal medications (see list above)
- [ ] First aid kit
- [ ] Hand sanitizer
- [ ] Wet wipes
- [ ] Tissues
**Documents:**
- [ ] Passport + copy
- [ ] Visa (printed)
- [ ] Credit/debit cards
- [ ] Travel insurance documents
- [ ] Booking confirmations (printed)
- [ ] Emergency contact list
- [ ] Allergy cards (printed in local language)
**Other:**
- [ ] Small daypack for excursions
- [ ] Reusable water bottle
- [ ] Waterproof bags for electronics
- [ ] Luggage lock
- [ ] Travel snacks
**Before Departure:**
- [ ] Print/save offline: all booking confirmations, visas, important docs
- [ ] Download apps: \[List essential apps for destination\]
- [ ] Download offline maps for \[Cities\]
- [ ] Download offline translation packs for \[Language\]
- [ ] Notify bank/credit cards of travel dates and destinations
- [ ] Get local currency or locate ATMs at arrival airport
- [ ] Confirm travel insurance coverage
- [ ] Book remaining activities
- [ ] Take photos of important documents (store in cloud)
- [ ] Share itinerary with emergency contact at home
**Upon Arrival:**
- [ ] Get local SIM card (\[Recommended carrier\] at \[Location\])
- [ ] Download and configure essential local apps
- [ ] Get hotel business cards for taxi returns (one per accommodation)
- [ ] Exchange for small bills for tips and small purchases
- [ ] Confirm first tour pickup details with hotel/host
- [ ] Locate nearest supermarket for emergency food supplies
- [ ] Test allergy translation cards at first meal
**Daily Reminders:**
- [ ] Confirm dietary restrictions/allergies when ordering (show translation card)
- [ ] Stay hydrated (bottled water only in areas with unsafe tap water)
- [ ] Apply sunscreen every 2-3 hours
- [ ] Keep copies of important documents in cloud
- [ ] Keep small bills separate for daily expenses
- [ ] Charge devices overnight
- [ ] Check weather forecast for next day's activities
### ⏰ Trip Reminders
- [ ] \[Date, Time\] — \[Reminder for pickup/check-in/activity\]
- [ ] \[Date, Time\] — \[Reminder for pickup/check-in/activity\]
---
### ✅ Checklist finale
**Prima di partire**
- [ ] DA RISOLVERE empty, every numbered point closed
- [ ] Conflitti di agenda all checked, nothing left open
- [ ] Both home transfers booked, outbound and return
- [ ] Every booking reference written in the page and its confirmation in the Drive folder
- [ ] Documents, visa and insurance saved offline
- [ ] The two cost totals reconciled, a carico azienda and a carico mio
- [ ] Itinerary shared with the emergency contact at home
**\[City 1\]**
- [ ] Accommodation address and check in time confirmed with the host
- [ ] Airport to accommodation leg decided and priced
- [ ] Gym with a single entry day pass located near the accommodation
- [ ] The fixed appointments of this city confirmed, with the room the calls need
- [ ] What is meant to be seen here checked against its closing day
**\[City 2\]**
- [ ] Accommodation address and check in time confirmed with the host
- [ ] Airport or station to accommodation leg decided and priced
- [ ] Gym with a single entry day pass located near the accommodation
- [ ] The fixed appointments of this city confirmed, with the room the calls need
- [ ] What is meant to be seen here checked against its closing day
---
*Have an amazing trip! 🌍*
