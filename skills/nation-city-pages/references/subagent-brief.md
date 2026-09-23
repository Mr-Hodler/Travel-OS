# Subagent brief

Hand this over verbatim, one subagent per page, with the four placeholders filled. It exists so a subagent
that never saw the conversation still writes a page that passes the parent's verification pass.

---

You are writing one page in the Notion database **Travels & City**. Your target is
`<NATION or CITY>` named `<TARGET NAME>`. Do not touch any other page.

**Read these three files in full before writing anything:**

- `knowledge/page-standard.md`
- `knowledge/notion-travel-db.md`
- `knowledge/research-standard.md`

**Your template** is the default template of the `<NATION or CITY>` data source. Fetch it with
`notion-fetch` at id `<TEMPLATE ID>` and reproduce its structure to the letter: every numbered toggle
section in order, every sub-heading, every table with the same columns in the same order, every `<details>`
block.

**Your density calibration** is `<REFERENCE PAGE ID>`. Fetch it. Your page is expected to be that dense.
One dense line per point, and no point skipped.

**Sequence.** Research first, with the template closed. Everything the research standard lists as live
gets a live check in this run: who governs, prices, opening hours and closing days, the exchange rate with
its date, entry rules, the crypto regulatory state, whether each venue you name still exists. Only then
open the template and write.

**On top of the template, always:** the history toggle written as dense prose on why the place is the way
it is today; concrete local `Do` and `Don't` with the reason a taboo matters; on a city page, section 8
split into `Da provare, buoni` and `Da provare, strani o divisivi`, each entry with what it is, what to
expect and a real address; on a nation page, who governs by name and both the Swiss and Italian embassies
with address, phone, email and the out of hours consular emergency number; a work section written for a
reader who does Bitcoin business development, so regulation and its real current state, exchanges,
community, VC and how business is actually done on the ground; on a city page, day pass gyms with prices
near where the reader stays, because he trains every day.

**Strip before finishing:** the `Jarvis` callout, the `Operational instructions` block, any `Guidance`
meta-block. On a city page keep the `Read first: open the Nation page` callout, translated.

**Style.** Italian. No em dashes and no en dashes, ever. Correct accents. 24 hour times. Prices in local
currency with the CHF conversion and the rate stated. `da verificare` where a figure could not be
confirmed. Real official links only, never an invented URL.

**Relations.** A city page is created with `Nation` and `Maps` already set. Never create the nation page
yourself: if it does not exist, stop and report that, because the relation resolves from city to nation
only and the parent controls the order.

**Before you report back**, re-fetch your page and check it against the verification pass in
`SKILL.md`. Then reply with: the page id, the page URL, the verification result line by line, every point
you had to leave as `da verificare` and why, and nothing else. Do not paste the page text.
