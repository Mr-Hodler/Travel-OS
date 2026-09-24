# Repair log shape

Italian, no em dashes, no en dashes. The log is the only record that a repair happened: a change that is not
in the log did not happen, and the next audit has no way to tell a fix from a regression.

One log per run, not one per page. It is written at the end and it is short: what was repaired, what was
parked, what was left open.

## Header

```
# Riparazione Travels & City, <data>

<N> pagine aperte in <M> cluster. <n> riparate, <n> parcheggiate, <n> lasciate aperte.
Budget di ricerca web: <esaurito | sufficiente>.
```

## Per page, one row

| Pagina | Tipo | Classi riparate | Cosa è cambiato | Verifica |
| --- | --- | --- | --- | --- |
| [Krakow](url) | City | 2, 4, 6 | relazione `Nation` impostata su Poland 🇵🇱, sei link finti rimossi e nomi lasciati, tre accenti corretti | sezioni 10 prima, 10 dopo |
| [Warsaw](url) | City | 5 | migrata da spec 1.1 a spec 1.3, 34 blocchi mappati, 2 senza sezione spostati sotto la 7 | sezioni 8 prima, 10 dopo |
| [Vietnam 2025](url) | Travel | 3 | orario di imbarco 09:40 corretto in 11:40, fonte Vietnam Airlines, consultata il <data> | sezioni 5 prima, 5 dopo |

`Classi riparate` names the numbers from the skill, so the log can be read against it without prose.
`Cosa è cambiato` names the field, the block or the token. "Sistemata" is not a log entry.
`Verifica` carries the section count before and after. It is the one column that catches a repair that ate
content, and it is never left empty.

## Parking register

Every page moved out by class 1, with where it went and what replaced it.

```
## Pagine parcheggiate

Pagina di parcheggio: [Da cancellare, riparazione <data>](url). Cancellabile con un click.

| Pagina parcheggiata | Superstite | Perché | Cosa è stato travasato |
| --- | --- | --- | --- |
| Belgrado (vecchia) | [Belgrade](url) | tre sezioni compilate contro nove | indirizzo palestra con day pass, orario del mercato |
```

The survivor is named with a link on every row. The parking page is named once, with the sentence that says
it can be deleted, because that sentence is the reason nothing was deleted by the agent.

## Left open

```
## Da verificare

- Krakow: prezzo del day pass in sezione 7, budget di ricerca esaurito, ultimo dato noto <data>.
- Poland 🇵🇱: due link ufficiali non trovati, nomi lasciati senza link, sezione 10.

## Non riparato

- Helsinki: migrazione di generazione rinviata, 41 blocchi da mappare e cluster chiuso. Prossimo giro.
```

`Da verificare` and `Non riparato` are never omitted to make the log look better. They are the input of the
next run, and a run that hides them starts from a false baseline.

## Rules the log obeys

- One line per page and no prose paragraphs. The log is read to find out whether a page was touched, not to
  be told a story about the run.
- A page opened and found correct gets no row. A page opened and left broken gets a row under
  `Non riparato` with the reason.
- The web search budget state goes in the header, because it explains every `da verificare` below it.
- No passport, visa, ID number or another traveller's document detail appears anywhere in the log.
