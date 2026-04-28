from input_password.password_personale import inserisci_password
import string
import random

password_corretta = inserisci_password()

charset = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

def incrementa(lista_indici, base):
    i = len(lista_indici) - 1
    while i >= 0:
        if lista_indici[i] < base - 1:
            lista_indici[i] += 1
            return lista_indici
        lista_indici[i] = 0
        i -= 1
    return None

def brute_force(password_target):
    tentativi = 0
    lunghezza = 1

    while True:
        indici = [0] * lunghezza

        while indici is not None:
            tentativo = ''.join(charset[i] for i in indici)
            tentativi += 1

            # aggiorna la stessa riga (senza andare a capo)
            print(f"\rTentativi: {tentativi}", end="", flush=True)

            if tentativo == password_target:
                print("\n\nPassword trovata!")
                print(f"Password: {tentativo}")
                print(f"Tentativi totali: {tentativi}")
                return tentativo

            indici = incrementa(indici, len(charset))

        lunghezza += 1


# esecuzione
brute_force(password_corretta)