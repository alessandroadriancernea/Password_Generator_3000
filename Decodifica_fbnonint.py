# Decodifica_fbnonint = Decodifica_forzabruta_nonintelligente

import sys
import time

password_da_testare = input("> ")

# Alfabeto dei caratteri che vengono provati nella forza bruta.
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    parts = []
    if hours:
        parts.append(f"{hours}h")
    parts.append(f"{minutes}m")
    parts.append(f"{secs}s")
    return " ".join(parts)


def format_number(value):
    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value/1_000:.1f}K"
    return str(value)


def brute_force(password_target):
    # Contatore totale di tutte le combinazioni provate.
    totale_tentativi = 0

    # Quando inizia la prova, per calcolare i tempi.
    inizio_tempo = time.time()

    # Numero massimo di caratteri che viene provato.
    lunghezza_massima = 100

    # Mostra l'aggiornamento a ogni N tentativi, per non saturare il terminale.
    aggiorna_ogni = 200000

    # Frame animati che appaiono nella barra di progresso.
    animazione_frames = ["[>....]", "[=>...]", "[==>..]", "[===>.]", "[====>]", "[.====]", "[..===]", "[...==]", "[....=]", "[.....]"]
    intervallo_animazione = 0.15
    ultimo_update_animazione = time.time()

    # Convertiamo la password in byte per il confronto diretto.
    password_da_confrontare = password_target.encode("ascii", errors="ignore")
    alfabeto_bytes = charset.encode("ascii")
    alfabeto_lunghezza = len(alfabeto_bytes)
    scrivi_su_terminal = sys.stdout.write
    pulisci_terminal = sys.stdout.flush

    for lunghezza_corrente in range(1, lunghezza_massima + 1):
        # Quante combinazioni esistono per questa lunghezza.
        totale_combinazioni_per_lunghezza = alfabeto_lunghezza ** lunghezza_corrente
        tentativi_per_lunghezza = 0
        indice_animazione = 0

        print(f"\n=== Tentativo con {lunghezza_corrente} lettere ===")

        # Inizia con la prima combinazione, cioè tutti caratteri al primo simbolo.
        tentativo_corrente = bytearray([alfabeto_bytes[0]] * lunghezza_corrente)
        indici_posizione = [0] * lunghezza_corrente
        ultima_posizione_digit = lunghezza_corrente - 1

        while True:
            totale_tentativi += 1
            tentativi_per_lunghezza += 1

            # Controlla se la combinazione corrente è la password.
            if tentativo_corrente == password_da_confrontare:
                tempo_fine = time.time()
                print("\n\n✅ Password trovata!")
                print(f"Password: {password_target}")
                print(f"Prove totali eseguite: {totale_tentativi:,} ({format_number(totale_tentativi)})")
                print(f"Tempo totale impiegato: {format_time(tempo_fine - inizio_tempo)}")
                return bytes(tentativo_corrente)

            # Mostra lo stato solo ogni tot tentativi, per evitare troppi aggiornamenti.
            if tentativi_per_lunghezza % aggiorna_ogni == 0:
                tempo_trascorso = time.time() - inizio_tempo
                velocita_attuale = totale_tentativi / tempo_trascorso if tempo_trascorso > 0 else 0
                tentativi_rimanenti = totale_combinazioni_per_lunghezza - tentativi_per_lunghezza
                tempo_rimanente = tentativi_rimanenti / velocita_attuale if velocita_attuale > 0 else 0
                ora_ora = time.time()
                if ora_ora - ultimo_update_animazione >= intervallo_animazione:
                    indice_animazione += 1
                    ultimo_update_animazione = ora_ora
                frame_animazione = animazione_frames[indice_animazione % len(animazione_frames)]
                larghezza_barra = 30
                barre_piene = int(larghezza_barra * tentativi_per_lunghezza / totale_combinazioni_per_lunghezza)
                barra_di_progresso = "★" * barre_piene + "☆" * (larghezza_barra - barre_piene)
                scrivi_su_terminal(
                    f"\r{frame_animazione} Tempo passato: {format_time(tempo_trascorso)} | "
                    f"Tempo previsto: {format_time(tempo_rimanente)} | Velocità: {format_number(int(round(velocita_attuale)))} tentativi/s | "
                    f"Tentativi: {format_number(totale_tentativi)} | {barra_di_progresso}"
                )
                pulisci_terminal()

            # Avanza la combinazione corrente come se fosse un contatore in base N.
            posizione = ultima_posizione_digit
            while posizione >= 0:
                if indici_posizione[posizione] < alfabeto_lunghezza - 1:
                    indici_posizione[posizione] += 1
                    tentativo_corrente[posizione] = alfabeto_bytes[indici_posizione[posizione]]
                    break
                indici_posizione[posizione] = 0
                tentativo_corrente[posizione] = alfabeto_bytes[0]
                posizione -= 1

            # Se abbiamo azzerato tutti i digit, non ci sono più combinazioni a questa lunghezza.
            if posizione < 0:
                break

        # Pulisce la riga di stato prima di passare alla lunghezza successiva.
        scrivi_su_terminal("\r" + " " * 120 + "\r")
        pulisci_terminal()
        print()

    print("\n❌ Password non trovata entro il limite di lunghezza.")


if __name__ == "__main__":
    brute_force(password_da_testare)
