# Task prompts

The text that goes into `create_trigger` as `prompt`, one template per task family.

Every firing starts a fresh session that has never seen the conversation these tasks were created in. A
prompt that reads well here and relies on nothing else is the only kind that works. Fill every angle
bracket before creating the task, and never leave one as a placeholder: an unfilled bracket fires, and the
session tries to interpret it.

The prompts are in Italian, which is the language the invoked skills are triggered and answer in. Ids come
from the Travel page and its relations, per `knowledge/notion-travel-db.md`.

---

## 1. Pre-departure, 48 hours

Name: `Viaggio <destinazione> <data> - pre partenza 48h`
Shape: one-shot, `run_once_at` = departure instant minus 48 hours, converted to UTC.

```
Esegui il check pre partenza completo per il viaggio "<titolo pagina Travel>",
pagina Notion id <page-id>, date <YYYY-MM-DD> a <YYYY-MM-DD>, partenza il
<YYYY-MM-DD> alle <HH:MM> ora locale da <aeroporto o stazione>.

Usa la skill pre-departure-check in passata completa, tutti e quattro i passi.
Le pagine di riferimento del viaggio sono <Nation: id> e <City: id>.

Produci la lista di azioni in italiano, ordinata per scadenza con i bloccanti in
testa, e aggiorna la pagina Notion: callout DA RISOLVERE riscritto con solo
quello che è ancora aperto, voci chiuse marcate con la prova, celle corrette,
data in footer aggiornata.
```

## 2. Pre-departure, 12 hours

Name: `Viaggio <destinazione> <data> - pre partenza 12h`
Shape: one-shot, `run_once_at` = departure instant minus 12 hours, converted to UTC.

```
Esegui la passata corta pre partenza per il viaggio "<titolo pagina Travel>",
pagina Notion id <page-id>, partenza il <YYYY-MM-DD> alle <HH:MM> ora locale.

Usa la skill pre-departure-check in passata corta: solo voci bloccanti, più meteo,
scioperi e lavori, gate e terminal, e gli eventi aggiunti in calendario dopo la
passata delle 48 ore.

Produci la lista di azioni in italiano. Non riscrivere la pagina se non è
cambiato niente di materiale.
```

## 3. Page refresh, about 10 days out

Name: `Viaggio <destinazione> <data> - rinfresco pagine`
Shape: one-shot, `run_once_at` = 10 days before departure at 09:00 local, converted to UTC.

```
Rinfresca le pagine di riferimento del viaggio "<titolo pagina Travel>", partenza
il <YYYY-MM-DD>.

Pagine da rinfrescare: Nations <id> (<nome paese>), City <id> (<nome città>).

Usa la skill nation-city-pages in modalità arricchimento, non in creazione: fai il
diff della pagina contro il template e riempi solo i buchi, non riscrivere quello
che è già specifico e corretto. Verifica live quello che può essere cambiato da
quando la pagina è stata scritta: prezzi, orari e giorni di chiusura, chi governa,
regole di ingresso, locali ancora aperti, tasso di cambio con la data.

Aggiorna la data in footer di ogni pagina toccata e riporta in italiano cosa è
cambiato, pagina per pagina.
```

## 4. Monthly database audit

Name: `Travel DB - audit mensile`
Shape: recurring, `cron_expression` in UTC. For 07:00 local on the first of the month: `0 5 1 * *` in
summer time, `0 6 1 * *` in winter time.

```
Esegui l'audit mensile del database Notion Travels & City.

Usa la skill travel-db-audit in modalità non presidiata: riporta solo gravità Alta
e Media, applica le tre correzioni meccaniche sicure e elencale nel report, non
scrivere niente altro.

Se non c'è niente da segnalare, rispondi con la sola riga di database pulito e
nient'altro.
```

---

## Before creating any of these

- `list_triggers` first. A second copy of the audit task, or of a trip's 48 hour task, doubles the output
  and halves the trust in it.
- Every angle bracket filled, no exceptions.
- The fire instant computed from local time and written in UTC, with the local time reported to the user.
- The approval setting stated when the task is confirmed. Without automatic approval the run stops at the
  first Notion write and produces nothing.
