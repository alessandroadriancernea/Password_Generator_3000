import random
import string
import time
from colorama import Fore, Style

# Codici colore usando colorama
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

def genera_password():
    print("Scegli la difficoltà della password:")
    print("1. Facile (solo lettere, lunghezza 5-6)")
    print("2. Media (lettere e numeri, lunghezza 8-10)")
    print("3. Difficile (lettere, numeri e caratteri speciali, lunghezza 12-16)")
    
    scelta = input("Inserisci 1, 2 o 3: ").strip()
    
    if scelta == '1':
        charset = string.ascii_letters
        lunghezza = random.randint(5, 6)
        color = BLUE
    elif scelta == '2':
        charset = string.ascii_letters + string.digits
        lunghezza = random.randint(8, 10)
        color = MAGENTA
    elif scelta == '3':
        charset = string.ascii_letters + string.digits + string.punctuation
        lunghezza = random.randint(12, 16)
        color = YELLOW
    else:
        print("Scelta non valida. Generando password facile di default.")
        charset = string.ascii_letters
        lunghezza = random.randint(5, 6)
        color = BLUE
    
    password = ''.join(random.choice(charset) for _ in range(lunghezza))
    return password, color

# Esempio di utilizzo
if __name__ == "__main__":
    pwd, col = genera_password()
    print("Password generata: ", end="", flush=True)
    for char in pwd:
        print(f"{col}_", end="", flush=True)
        time.sleep(0.1)
        print(f"\b{col}{char}", end="", flush=True)
    print(RESET)