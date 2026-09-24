# The Drive trip folder convention

Every trip has, or should have, one Google Drive folder. That folder holds the original documents:
the booking PDFs, the tickets, the vouchers, the identity papers, the spreadsheets. Notion holds the
operational page built from them. This file records what the Drive folder actually looks like today,
fixes the standard to follow from here on, and lists where Drive and the Notion Travel data source
disagree.

Root: `05_Viaggi`, mounted locally as a connected folder. On this machine it appears at
`$HOME/mnt/05_Viaggi` inside the device shell.

Counted on 2026-09-24: 9 trip folders, 49 subfolders, 91 files plus one `.DS_Store`. By extension:
69 pdf, 5 gsheet, 3 gdoc, 2 html, 8 images (jpeg, jpg, png, PNG, HEIC), 1 pkpass. The gsheet and
gdoc files are Drive shortcut stubs holding a `doc_id`, not local documents.

## What is actually there

```
05_Viaggi/
  2022_Londra ESL/                        flat, 6 pdf: accommodation confirmation, booking
                                          confirmation, ESL file, student guide, school, residence
  2023_Belgrado - Serbia/                 flat, 1 pdf: GoToGate_FB.pdf
  2025.04_Bangkok/                        flat, 2 pdf: "Volo andata_ <PNR>.pdf",
                                          "Volo-Ritorno_GoToGate.pdf"
  2025.06_Cina/
    Itinerario e Costi_Cina_2025.gsheet   the costs and itinerary sheet
    Guida sintetica (ma completa) alla Cina.gdoc
    China Trip Info Aron<>Wendy.gdoc
    Aron_account-statement.gsheet         financial
    Wendy account-statement_...gsheet     financial
    Volo Milano > Shenzhen/               Itinerario.pdf + Ricevuta elettronica.pdf
    Volo Zhanjiang > Sanya/               same two files
    Volo Sanya > Pechino/                 same two files
    Volo Pechino > Milano/                same two files
    Hotel Shenzhen/                       "Dati per il check-in presso <id>.pdf",
                                          "English Check-in Voucher (For Visa Application).pdf",
                                          "Ricevuta elettronica prenotazione hotel <id>.pdf"
    Hotel Sheraton Zhanjiang/             same three files
    Hotel Swiss Benjing/                  same three files
    Hotel Sanya Marriot Yalong bay, Hannan/   EMPTY
  2025.08_Sardegna/                       flat: Itinerario e costi.gsheet,
                                          Biglietto_<numbers>.pdf, CondizioniGenerali_IT.pdf,
                                          2023_Prices_Itineraries.pdf
  2025.12_Vietnam/
    Vietnam SpreadSheet.gsheet            the costs sheet, named off pattern
    Untitled document.gdoc                unnamed
    Allergy_notice_Lambertini.PNG         health
    booking.pkpass
    civitatis.com_it_voucher_<long token>_1.pdf
    Volo 1 Andata - Milano > Hanoi - 3 Dec/    Itinerario.pdf, "Volo Milano > Hanoi - 3 Dec.pdf",
                                          "relativo alla ricevuta elettronica.pdf"
    Volo 2 - Hanoi > Da Nang - 8 Dec/     same three shapes
    Volo 3 - Da Nang > HCMC - 12 Dec/     same three shapes
    Volo 4 Ritorno - HCMC > Milano - 17 Dec/  same three shapes
    Stay/                                 Couise_book_917451.pdf,
                                          "HCMC - 12 17 - Reservation Details - <code>.pdf",
                                          "Hanoi - 4 7 Dec - Reservation Details - <code>.pdf"
      Hotel Hoi an/                       the three Trip.com hotel files plus
                                          "Hoi An - 8 12 Dec - Sen Village ... .pdf"
    ID & Visa Aron/                       Aron_VietNam_eVisa_<number>.pdf        SENSITIVE
    ID & Visa Lambe/                      IMG_6419.PNG                          SENSITIVE
  2026.01_El Salvador/                    flat, 3 pdf: two KLM booking pages, RC3TS93RQK.pdf
  2026.06_China Bro Trip/
    Bros Trip China 2026 Guide v3.pdf     deliverable, lives only in Drive
    China_Bros_Trip_2026.html             deliverable, self contained page, lives only in Drive
    Agenda-Visit to BYD at June 17th 2026.pdf
    Transport/
      01.1_Volo Andata - Milano > ChongQing - 8.06.2026/      EMPTY
      01.2_Volo Ritorno - HongKong > Milano - 21.06.2026/     EMPTY
      01.3_Treno - ChongQing > Guangzhou - 13.06.2026/        EMPTY
    Stay & Hotel/
      02.1_Hotel ChongQing/  02.2_Hotel GuangZhou/
      02.3_Hotel HongKong/   02.4_Hotel Shenzhen/             ALL FOUR EMPTY
      Screenshot hotel x Trip.com/        5 WhatsApp jpeg
    XX_Passaporti/
      Passaporti /                        4 files, trailing space in the folder name  SENSITIVE
      Prenotazioni/                       the real bookings, buried under a passport folder
        Voli/Milano - Chongqing/          itinerary and receipt pdf, plus "Jack volo/" with a
                                          second copy for another traveller
        Voli/Hong Kong - Milano/          itinerary and receipt pdf
        Hotel/MUSA Muye Chongqing 09 05-13 05/     receipt pdf, check-in voucher pdf
        Hotel/Yumanju Hotel Guangzhou 13 05-16 05/ receipt pdf, voucher pdf, 1 png
        Treni/Chongqingxi - Guangzhounan/ 1 pdf
        Cancellati/                       cancelled hotel vouchers and a cancelled ticket
  2027.01_El Salvador + Rep. Dominicana/
    Piano voli 2027.01 - El Salvador + Rep. Dominicana.html   the only file, lives only in Drive
```

### Where the naming is incoherent today

- **Two trip folder forms.** `2022_Londra ESL` and `2023_Belgrado - Serbia` use `YYYY_`. The six
  folders from 2025 on use `YYYY.MM_`.
- **Transport.** Flight folders sit at trip root as `Volo <A> > <B>` in `2025.06_Cina`, as
  `Volo <N> <Andata|Ritorno> - <A> > <B> - <D Mon>` in `2025.12_Vietnam`, and inside a `Transport/`
  container with `NN.N_` prefixes in `2026.06_China Bro Trip`. Three forms, three trips.
- **Accommodation.** `Hotel <name>` at trip root in `2025.06_Cina`, `Stay/` in `2025.12_Vietnam`,
  `Stay & Hotel/` in `2026.06_China Bro Trip`.
- **Identity papers.** `ID & Visa <Person>` in `2025.12_Vietnam`, `XX_Passaporti/Passaporti /` in
  `2026.06_China Bro Trip`, with a trailing space in the inner folder name.
- **`2026.06_China Bro Trip` is internally contradictory.** `Transport/` and `Stay & Hotel/` carry
  the tidiest names in the whole root and are empty. The documents they describe are under
  `XX_Passaporti/Prenotazioni/`, which by its name should hold passports only.
- **Dates inside names disagree with the trip.** The trip runs 8 to 21 June 2026 and the transport
  leaf folders say `8.06.2026` and `13.06.2026`, but the hotel folders say `09 05-13 05` and
  `13 05-16 05`. One of the two writes the month wrong, or the format is `DD MM` in one place and
  something else in the other. Not resolved here, flagged.
- **Folder month against trip start.** `2025.06_Cina` is the folder for a trip whose Notion dates
  start 2025-05-21. The `YYYY.MM` should be the start month.
- **The costs sheet has three names.** `Itinerario e Costi_Cina_2025`, `Itinerario e costi`,
  `Vietnam SpreadSheet`.
- **Empty folders.** 8 of the 49 subfolders hold nothing: one hotel in `2025.06_Cina` and seven in
  `2026.06_China Bro Trip`.
- **Untitled files.** `Untitled document.gdoc` in `2025.12_Vietnam`.

## The standard from here on

### Trip folder

`YYYY.MM_Destinazione`, where `YYYY.MM` is the month the trip starts and `Destinazione` is the
destination as a person would say it. `2027.01_El Salvador + Rep. Dominicana` is the model. The
`YYYY_` form of 2022 and 2023 is legacy: it is not renamed, it is not repeated. The dotted month is
chosen because it sorts chronologically inside a year, which a bare year does not, and because it
matches the Notion `Dates` start month, which is what makes the two systems joinable by eye.

### Subfolders, one canonical name each

| Canonical | Replaces | Holds |
| --- | --- | --- |
| `Transport/` | `Volo <A> > <B>` at root, `Volo <N> ...` at root | every leg: flights, trains, ferries, transfers |
| `Transport/NN_<Mode> <A> > <B> - DD.MM.YYYY/` | the three leaf forms above | one leg, its itinerary and its receipt |
| `Stay/` | `Hotel <name>` at root, `Stay & Hotel/` | every night: hotels, apartments, homestays, cruises |
| `Stay/NN_<City> <Property> - DD.MM-DD.MM/` | `Hotel <City>`, `MUSA Muye Chongqing 09 05-13 05` | one stay, its receipt and its check-in voucher |
| `ID & Visa/<Person>/` | `ID & Visa <Person>`, `XX_Passaporti/Passaporti/` | passports, visas, eVisas, ID cards, per person |
| `99_Cancellati/` | `Prenotazioni/Cancellati/` | bookings that were cancelled, kept for the refund trail |

`Transport/` wins over `Volo ...` because a trip has trains, ferries and transfers, and `Volo`
cannot name them: `2026.06_China Bro Trip` already has a train leg. `Stay/` wins over
`Stay & Hotel/` because a hotel is a stay, so the longer name says the same thing twice, and
because `Stay/` already covers the Airbnb and the cruise cabin. `ID & Visa/` wins over `Passaporti`
because the folder holds eVisas and ID photos as well as passports, and `Passaporti` is the narrower
of the two words. The `XX_` prefix is dropped: it bought nothing but sorting, and `99_` on the
cancelled folder does that job where it is actually needed.

Two digit `NN_` prefixes inside `Transport/` and `Stay/` follow the order of the trip, so the folder
list reads as the itinerary reads. `Prenotazioni/` as an intermediate level is dropped: every folder
under a trip is a booking, so the word adds a click and no information.

### Files at trip root

| Canonical name | What it is |
| --- | --- |
| `Itinerario e Costi YYYY.MM - <Destinazione>` | the gsheet that carries the day by day plan and the cost lines |
| `Guida YYYY.MM - <Destinazione>[ vN]` | the guide, gdoc, pdf or html |
| `Piano voli YYYY.MM - <Destinazione>` | a flight plan page when the trip has one |

`<Tipo documento> YYYY.MM - <Destinazione>` is the form already used by
`Piano voli 2027.01 - El Salvador + Rep. Dominicana.html`, the most recent file in the root, and it
is the one that survives being read out of context. A file called `Untitled document` or
`Vietnam SpreadSheet` is renamed the next time the trip is touched.

### File names inside a leg or a stay folder

Keep the provider's own names. `Itinerario.pdf`, `Ricevuta elettronica.pdf`,
`Ricevuta elettronica prenotazione hotel.pdf`, `Voucher per il check-in.pdf`,
`English Check-in Voucher (For Visa Application).pdf` are what Trip.com and the airlines send, they
are already unambiguous inside a folder that names the leg, and renaming them loses the ability to
match a file against the email it arrived in. What does get fixed: a trailing space, a name that is
only a token or a booking number with no word in it, and a second traveller's copy, which goes in
the same folder with the traveller's name appended rather than in a nested folder of its own.

## Division of labour between Drive and Notion

**Drive holds the originals.** Flight itineraries and receipts, hotel receipts and check-in
vouchers, train and ferry tickets, event tickets, activity vouchers, insurance papers, identity
documents, and the itinerary and costs spreadsheet. A document that arrived as a file stays a file,
in Drive, in the folder of the leg it belongs to.

**Notion holds the operational page.** The Travel page carries the data read out of those files in
a form a person can act on: times, airports, terminals, PNRs, addresses, check-in and check-out
times, door codes, prices, the day by day table, the DA RISOLVERE callout.

**The rule: a PDF is not transcribed into Notion, it is extracted and linked.** What goes on the
page is the handful of fields that matter at the moment of use. What stays in Drive is the document
itself. Pasting the body of a booking confirmation into a Notion page produces a page nobody reads
and a second copy that goes stale the moment the booking changes.

**`Drive link` is how the two halves find each other.** The Travel data source has a `Drive link`
url property for exactly this, and it is populated with the trip folder, not with a single file.
One trip, one folder, one link. A trip page with an empty `Drive link` is a defect, and
`travel-db-audit` reports it.

**The spreadsheet is the overlap to watch.** `Itinerario e Costi` duplicates what the Notion Travel
page holds: three trips have one (`2025.06_Cina`, `2025.08_Sardegna`, `2025.12_Vietnam` as
`Vietnam SpreadSheet`) and six do not. Where both exist, the Notion page is the operational copy
and the sheet is the arithmetic: the sheet may hold the cost lines and the totals, the page holds
the plan. The same number is not maintained in both.

**Guides and html pages are deliverables that today live only in Drive.**
`Bros Trip China 2026 Guide v3.pdf`, `China_Bros_Trip_2026.html`,
`Piano voli 2027.01 - El Salvador + Rep. Dominicana.html`, `Guida sintetica (ma completa) alla
Cina.gdoc` and `China Trip Info Aron<>Wendy.gdoc` exist in no other system. They stay in Drive,
and the Notion page links them so the page is not the only thing that knows they exist.

## Sensitive documents

These stay in Drive. They are not copied into a Notion page, not attached to one, not quoted in
one, and they never enter this repository or any file it produces.

- **Identity.** Passports, visas, eVisas, ID cards. Today:
  `2025.12_Vietnam/ID & Visa Aron/`, `2025.12_Vietnam/ID & Visa Lambe/`,
  `2026.06_China Bro Trip/XX_Passaporti/Passaporti /` with four travellers' passports.
- **Visa support documents.** The `English Check-in Voucher (For Visa Application).pdf` files in
  `2025.06_Cina` and `2025.12_Vietnam` carry passport level personal data of more than one person.
- **Health.** `2025.12_Vietnam/Allergy_notice_Lambertini.PNG`.
- **Financial.** `2025.06_Cina/Aron_account-statement.gsheet` and the Wendy account statement
  beside it.

A Notion page may say that a visa exists and is valid, with its number redacted to the last
characters if a number is needed at all. It may not carry the scan, the full document number, or
another person's papers. Where a document belongs to a travelling companion and not to the account
owner, it stays where it is and is referred to, never republished.

## Gaps between Drive and Notion

The Notion Travel data source holds **9** trip pages, not 10, plus its default page template, which
is not a trip. Matching was done on destination and on `Dates` against the folder name.

### Trips with a Drive folder and no Notion page

| Drive folder | Note |
| --- | --- |
| `2022_Londra ESL` | 6 pdf, a language school stay, never entered Notion |
| `2023_Belgrado - Serbia` | 1 pdf. Distinct from the Notion page `Belgrade (Apr 2026)`, which is a different trip three years later |

### Trips with a Notion page and no Drive folder

| Notion page | Dates | Note |
| --- | --- | --- |
| `Belgrade (Apr 2026)` | 2026-04-19 to 2026-04-26 | no `2026.04_Belgrado` folder, and `Drive link` empty |
| `Helsinki + Warsaw 🇫🇮🇵🇱 BTCHEL 2026 e remote work` | 2026-09-22 to 2026-10-01 | no `2026.09_Helsinki + Warsaw` folder, and `Drive link` empty |

### Matched, but `Drive link` is empty

| Notion page | Drive folder that exists |
| --- | --- |
| `Bangkok Trip` | `2025.04_Bangkok` |

Three of the nine Travel pages have an empty `Drive link`: `Bangkok Trip`, `Belgrade (Apr 2026)`,
`Helsinki + Warsaw 🇫🇮🇵🇱 BTCHEL 2026 e remote work`.

### Matched, both sides present, `Drive link` populated

| Notion page | Drive folder |
| --- | --- |
| `China Trip` | `2025.06_Cina` |
| `Sardegna Trip` | `2025.08_Sardegna` |
| `Vietnam 2025` | `2025.12_Vietnam` |
| `San Salvador, El Salvador 🇸🇻` | `2026.01_El Salvador` |
| `China Bros Trip` | `2026.06_China Bro Trip` |
| `El Salvador + Rep. Dominicana 🇸🇻🇩🇴` | `2027.01_El Salvador + Rep. Dominicana` |

The folder name and the page title drift apart even where both exist: `Bro` against `Bros`,
`2026.01_El Salvador` against `San Salvador, El Salvador 🇸🇻`, `Cina` against `China Trip`. The
`Drive link` property, not the name, is the join. Nothing in this file authorises renaming anything
inside `05_Viaggi`: the standard applies to what is created from here on, and a legacy folder is
left alone unless the user asks for it to be moved.
