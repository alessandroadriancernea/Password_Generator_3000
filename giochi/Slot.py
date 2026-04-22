import random
import math

# Simboli disponibili e loro valore base
SIMBOLI = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
VALORI = {
    "🍒": 2,
    "🍋": 3,
    "🔔": 5,
    "⭐": 8,
    "7️⃣": 12
}

def gira_slot():
    """Genera una combinazione casuale di 3 simboli."""
    return [random.choice(SIMBOLI) for _ in range(3)]

def calcola_vincita(combinazione, puntata):
    """Calcola la vincita in base ai simboli usciti."""
    # Se tutti e 3 i simboli sono uguali → jackpot
    if combinazione.count(combinazione[0]) == 3:
        simbolo = combinazione[0]
        moltiplicatore = VALORI[simbolo]
        # Bonus: moltiplicatore aumentato con radice quadrata della puntata
        bonus = math.sqrt(puntata)
        return int(puntata * moltiplicatore + bonus)

    # Se solo 2 simboli sono uguali → piccola vincita
    for simbolo in SIMBOLI:
        if combinazione.count(simbolo) == 2:
            return int(puntata * (VALORI[simbolo] / 2))

    # Nessuna vincita
    return 0

def main():
    crediti = 1000

    print("🎰 Benvenuto alla Slot Machine!")
    print("Hai 1000 crediti iniziali.\n")

    while crediti > 0:
        print(f"Crediti attuali: {crediti}")
        try:
            puntata = int(input("Quanto vuoi puntare? (0 per uscire) "))
        except ValueError:
            print("Inserisci un numero valido.\n")
            continue

        if puntata == 0:
            break
        if puntata > crediti or puntata < 0:
            print("Puntata non valida.\n")
            continue

        crediti -= puntata

        # Gira la slot
        combinazione = gira_slot()
        print("Risultato:", " | ".join(combinazione))

        # Calcola vincita
        vincita = calcola_vincita(combinazione, puntata)
        crediti += vincita

        if vincita > 0:
            print(f"🎉 Hai vinto {vincita} crediti!\n")
        else:
            print("😢 Nessuna vincita.\n")

    print(f"\nGioco terminato. Crediti finali: {crediti}")
    print("Grazie per aver giocato!")


main()
