from password_personale.password_personale_con_sicurezza import password_personale_con_sicurezza
from password_generator.Generatore_Password import genera_password

def main():
    print("🎲 Benvenuto in Password Generator 3000! 🎲")
    print("Questo programma aiuta a generare password sicure e a verificarne la robustezza.")
    print("Scegli un'opzione:")
    print("1. Genera una password")
    print("2. Verifica la sicurezza di una password")
    print("3. Esci")

    scelta_menu = input("Inserisci la tua scelta: ").strip()

    if scelta_menu == "1":
        password_generata, colore_testo = genera_password()
        print(f"La password generata è: {colore_testo}{password_generata}")
    elif scelta_menu == "2":
        password_da_verificare = input("Inserisci la password da verificare: ")
        if password_personale_con_sicurezza(password_da_verificare):
            print("La password è sicura.")
        else:
            print("La password non è sicura. Si consiglia di cambiarla.")
    elif scelta_menu == "3":
        print("Grazie per aver utilizzato Password Generator 3000.")
    else:
        print("Scelta non valida. Per favore, riprova.")