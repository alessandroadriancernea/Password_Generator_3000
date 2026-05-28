# Documento dei Requisiti - Progetto 3M

## 1. 🎨 Titolo del progetto

► 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝟑𝟎𝟎𝟎

## 2. 🚩 Obiettivo

L'obiettivo è far decidere all'utente se vuole generare una password oppure se preferisce eseguire un attacco di decodifica brute-force non intelligente. In alternativa, l'utente può usare una password già esistente per testarla con lo stesso metodo.

## 3. Attori 👥

Utente ⇨ l'utente decide se generare una password scegliendo tra tre livelli di difficoltà (facile, medio, difficile). Dopo aver generato la password, può scegliere se verificarla con un tentativo di decodifica o se mantenerla.

## 4. 📜 Requisiti funzionali

Funzionalità principali:
- avviare il programma con un menu numerato
- gestire l'input dell'utente per scegliere tra generazione e verifica password
- mostrare i risultati e le statistiche in modo chiaro

## 5. 📋 Gestione del progetto

- interfaccia a console chiara
- gestione degli errori di input
- codice organizzato in più file (package, moduli)
- commenti e documentazione di base

## 6. 🗂️ Scelta dei package Python

- Package scelti:
  - `random` (standard): genera password casuali
  - `string` (standard): fornisce insiemi di caratteri come lettere, numeri e simboli
  - `time` (standard): misura i tempi e gestisce ritardi per l'animazione di stato
  - `sys` (standard): scrive lo stato sul terminale senza andare a capo ogni volta
  - `wordfreq` (esterno): genera liste di parole frequenti per l'attacco dizionario
  - `colorama` (esterno): colora il testo del terminale per rendere l'output più leggibile
- Perché li abbiamo scelti: sono utili per gestire generazione password, tempo, output terminale e attacchi di codifica in modo semplice
- Come li usiamo nel progetto: `random` e `string` per la generazione password, `time` per il tempo e l'animazione, `sys` per aggiornare la barra di stato, `wordfreq` per la lista di parole e `colorama` per il colore del testo

## 7. 📑  Suddivisione del lavoro

- Studente A: `Alessandro` - si occupa dell'input della password casuale e della decifrazione
- Studente B: `Felipe` - gestione della password dell'utente e verifica della sicurezza

## 8. ⚒️  Flusso del programma

- menu iniziale in cui l'utente seleziona un numero
- può generare una password, verificare la propria password oppure uscire dal programma
- visualizzazione dei risultati finali

## 9. ⏱️ Cronoprogramma (Gantt semplificato)

- Settimana 1: scelta del tema, ricerca dei package, stesura requisiti
- Settimana 2: progettazione, divisione del lavoro, avvio sviluppo
- Settimana 3: completamento funzionalità, test, integrazione package
- Settimana 4: rifinitura, documentazione, consegna

## 10. 📝 Note aggiuntive

Tema semplice, senza interfaccia grafica avanzata; tutto su CMD e in modo statico. Può contenere anche ASCII art.
Idee future: se possibile, aggiungere una schermata base fuori dal CMD.
Difficoltà previste: gestione della decodifica, organizzare tutto nel `menu.py` e imparare a usare i package.