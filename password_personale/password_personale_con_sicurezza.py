"""Funzioni per valutare la sicurezza di una password.

Questo modulo espone `password_personale_con_sicurezza(password)` che prende
una password (stringa) e restituisce `True` se raggiunge un livello di sicurezza
considerato accettabile (livello >= 4), altrimenti `False`.

Il codice evita qualsiasi `input()` a livello di modulo, quindi è sicuro importarlo
senza avviare interazioni con l'utente.
"""

def password_personale_con_sicurezza(password: str) -> bool:
    """Valuta la password e restituisce True se è considerata sicura.

    Regole (semplice valutazione a punti):
    - >=8 caratteri -> +1
    - almeno una lettera maiuscola -> +1
    - almeno 5 lettere minuscole -> +1
    - almeno 5 cifre -> +1
    - almeno un carattere speciale -> +1

    Ritorna True se il punteggio è >= 4.
    """
    livello = 0

    if len(password) >= 8:
        livello = 1

    if any(char.isupper() for char in password):
        livello = max(livello, 2)

    if sum(char.islower() for char in password) >= 5:
        livello = max(livello, 3)

    if sum(char.isdigit() for char in password) >= 5:
        livello = max(livello, 4)

    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        livello = max(livello, 5)

    return livello >= 4
    