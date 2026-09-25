# Report shape

Italian, no em dashes, no en dashes. Two forms only: the clean form and the findings form. Nothing in
between, and never a preamble about what was checked before the reader knows whether anything is wrong.

## Clean run

One line, and stop.

```
Audit Travels & City, <data>: nessun problema. <N> pagine elencate, <M> aperte.
```

## Findings run

```
# Audit Travels & City, <data>

<N> problemi: <n> alta, <n> media, <n> bassa. Pagine elencate <N>, aperte <M>.

| Pagina | Tipo | Problema | Gravità | Azione consigliata |
| --- | --- | --- | --- | --- |
| [Krakow](url) | City | placeholder `[Hotel 1]` e `[Club 1]` nella sezione 6, tre celle vuote in sezione 8 | Alta | completare con nation-city-pages, viaggio il 14/03 |
| [Poland 🇵🇱](url) | Nation | governo non aggiornato, footer 2024-11 | Alta | verificare chi governa e aggiornare sezione politica |
| [Belgrade](url) | City | relazione `Nation` vuota | Alta | corretto: impostata su Serbia 🇷🇸 |
| [Vietnam 2025](url) | Travel | `Dates` chiuse da 210 giorni | Bassa | archiviare, decisione dell'utente |
| [Dubai & Emirates](url) | City | corpo 106.835 caratteri su un tetto di 42.000, sezione 7 da 18.074, una cella da 1.470 | Media | comprimere con travel-db-repair, nessun dato va perso |
| [Poland 🇵🇱](url) | Nation | toggle `Storia del paese` da 11.003 caratteri su un tetto di 3.500, e collocato sopra la sezione 1 invece che dentro | Media | comprimere e annidare dentro la sezione 1 con travel-db-repair |

## Correzioni applicate
- Belgrade: impostata la relazione `Nation` su Serbia 🇷🇸, unica corrispondenza.

## Da verificare
- Krakow: prezzo del day pass in sezione palestre, footer di 14 mesi, non verificato in questo giro.
```

## Rules the table obeys

- Ordered by `Gravità`, then by how soon a trip depends on the page. An Alta on a page nobody travels to in
  the next three months sits below an Alta on next week's destination.
- `Problema` names the token, the field or the section. "Incompleta" is not a finding, `placeholder [Hotel 1]
  in sezione 6` is.
- A density finding carries **the measured number against the cap** and names the longest section, so
  `corpo 106.835 caratteri su un tetto di 42.000, sezione 7 da 18.074`. The word `lunga` is not a finding.
- `Azione consigliata` is one imperative line and names who does it: `nation-city-pages` in enrichment mode,
  `trip-itinerary`, or the user.
- A fix applied automatically appears in the table with `corretto:` and again under `Correzioni applicate`.
  A change that is not in the report did not happen.
- `Da verificare` collects every suspicion the run did not confirm, with the age that raised it. It is the
  agenda for the next run, so it is never left out to make the report look shorter.
