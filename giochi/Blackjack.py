import random


def regole():
    print("Benvenuto al Blackjack!")
    print("Regole del gioco:")
    print("1. L'obiettivo è avvicinarsi il più possibile a 21 senza superarlo.")
    print("2. Ogni giocatore riceve due carte iniziali.")
    print("3. Puoi scegliere di 'chiedere' (ricevere un'altra carta) o 'stare' (mantenere le carte attuali).")
    print("4. Se superi 21, perdi automaticamente.")
    print("5. Il dealer gioca dopo di te e deve seguire regole specifiche per decidere se chiedere o stare.")
    print("6. Se il dealer supera 21, vinci automaticamente.")
    print("7. Se sia tu che il dealer restate sotto o uguali a 21, vince chi ha il punteggio più alto.")
    print("Buona fortuna!")

def inzio_gioco():
    carte = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Valori delle carte (11 rappresenta l'Asso)
    mano_giocatore = [random.choice(carte), random.choice(carte)]
    mano_banco = [random.choice(carte), random.choice(carte)]
    print(f"Le tue carte: 🃏{mano_giocatore} | Totale: {sum(mano_giocatore)}\n")
    print(f"Carte del banco: 🃏{mano_banco} | Totale: {sum(mano_banco)}\n")
    
    scelta = input("🃏 Vuoi chiedere un'altra carta? (s/n) ").lower()
    if scelta == 's':
        nuova_carta = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        mano_giocatore.append(nuova_carta)
        print(f"Hai ricevuto: {nuova_carta} | Nuovo totale: {sum(mano_giocatore)}")
        if sum(mano_giocatore) > 21:
            print("Hai superato 21! Hai perso.")
            return False
        elif scelta == 'n':
            return True
        else:
            print("Scelta non valida. Per favore rispondi con 's' o 'n'.")
        return mano_giocatore, mano_banco
    # da completare: logica del banco, confronto finale, gestione dell'Asso (11 o 1) e loop di richiesta carte.0

def main():
    print("🎲 Benvenuto al Blackjack!")
    print("1. 📜 Regole")
    print("2. 🕹️ Inizia il gioco")
    print("3. 🃏 Chiedi un'altra carta")
    print("6. 👋 Esci")
    scelta = int(input("Scegli un'opzione: "))
    
    if scelta == 1:
        regole()
        return main()
    elif scelta == 2:
        inzio_gioco()
    elif scelta == 3:
        pass
    elif scelta == 6:
        print("Arrivederci!")


main()