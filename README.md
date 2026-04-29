# Documento dei Requisiti - Progetto 3M

## 1. 🎨Titolo del progetto

Password Generator 3000

## 2. 🚩Obiettivo

Apre una GUI e ti chiede di scegliere la lunghezza della password, la complessità e blocca le password troppo facili, poi prova a decifrarle

## 3. 👥Attori

Utente -> Decide se vuole generare una password randomica o usare la sua password e in tutti e due i casi vien

## 4. 📜Requisiti funzionali

Funzionalità principali:
- Avviare il programma con un menu a numeri.
- Gestire input dell'utente (se vuole verificare la password o generarla nuova).
- Mostrare risultati o statistiche

## 5. 📋Gestione del progetto

- Interfaccia a console chiara
- Gestione degli errori di input
- Codice organizzato in più file(Package, Moduli)
- Commenti e documentazione base

## 6. 🗂️Scelta del package Python

- Package scelto: `Random, String, Time`
- Perché lo abbiamo scelto: `Gli abbiamo scelti perchè ci facilitano il lavoro e non sono troppo complessi`
- Come lo usiamo nel progetto: `Ad esempio se la password va bene è verde, random per generare la password in modo casuale e String perchè ci fa usare le stringhe meglio e Time perchè ci servivano delle animazioni.`

## 7. 📑Suddivisione del lavoro

- Studente A: `Alessandro` Si occupa del input password casuale e della decifrazione
- Studente B: `Felipe` Gestione Password dell'utente (verifica password)

## 8. ⚒️Flusso del programma

- Menu iniziale (Dove l'utente deve selezionare un numero).
- Può generare password, può verificare se la tua password è sicura o uscire dal programma. `Potrebbe esserci altro`
- Risultati finali.

## 9. ⏱️Cronoprogramma (Gantt semplificato)

- Settimana 1: scelta del tema, ricerca package, stesura requisiti
- Settimana 2: progettazione, divisione del lavoro, avvio sviluppo
- Settimana 3: completamento funzionalità, test, integrazione package
- Settimana 4: rifinitura, documentazione, consegna

## 10. 📝Note aggiuntive

Aggiungi qui commenti sul tema, sulle idee future o sulle difficoltà previste.

Tema semplice senza schermata avanzata, tutto sul CMD e statico, potrebbe contenere ASCII art
Idee future: se possibile mettere una schermata basica fuori dal cmd
Difficoltà previste: decodif, organizzare tutto nel main() e imparare i package