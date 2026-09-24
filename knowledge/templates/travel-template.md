# Travel template, mirror

Mirror of the Notion default template for the Travel data source.
Source of truth: Notion page `1da87313-332c-808c-9e0b-df99c23f031e`. This file is a snapshot, not the master.
Snapshot taken: 2026-09-24.

Read this to know the required structure without a Notion round trip. When a
page is actually being written, fetch the live template as well: if the two
disagree, Notion wins and this mirror is stale.

---

# ✈️ Travel Brief — \[TRIP NAME\]
**Travelers:** \[Names\]
**Duration:** \[X days\] \| \[Start Date\] - \[End Date\]
**Total Cost:** CHF \[Total\] (CHF \[Per Person\] per person)
<callout icon="⚠️" color="red_bg">
	**CRITICAL NOTES**
	Add any critical information here (allergies, special requirements, emergency contacts, etc.)
</callout>
---
## 1. ✈️ Flights & Transfers {toggle="true"}
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
### 🌦️ Plan B — Weather-Dependent Alternatives {toggle="true"}
- **If \[Primary Activity\] is cancelled due to weather:**
	- Option A: \[Alternative indoor activity\] — \[Location/Cost\]
	- Option B: \[Alternative covered activity\] — \[Location/Cost\]
- **Rainy day recommendations:**
	- \[Museum/Indoor attraction\] — \[Details\]
	- \[Covered market/Shopping area\] — \[Details\]
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
*Have an amazing trip! 🌍*
