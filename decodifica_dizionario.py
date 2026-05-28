# Decodifica_dizionario = attacco basato su parole comuni da dizionario

from time import time

from wordfreq import top_n_list


def format_time(seconds):
    """Restituisce una rappresentazione del tempo in ore, minuti e secondi."""
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    return f"{minutes}m {seconds}s"


def load_common_words(language='en', count=2000000):
    """Carica una lista di parole comuni nella lingua richiesta."""
    try:
        return top_n_list(language, count)
    except Exception:
        print(f"Attenzione: lingua '{language}' non riconosciuta. Uso inglese.")
        return top_n_list('en', count)


def dictionary_attack(password_target: str, language: str = 'en', count: int = 2000000):
    """Prova a indovinare la password usando parole comuni dal dizionario."""
    word_list = load_common_words(language, count)
    total_words = len(word_list)
    start_time = time()

    for attempt_index, current_word in enumerate(word_list, start=1):
        elapsed_time = time() - start_time
        speed = attempt_index / elapsed_time if elapsed_time > 0 else 0
        words_left = total_words - attempt_index
        eta_seconds = words_left / speed if speed > 0 else 0

        print(
            f"\rTentativi: {attempt_index}/{total_words} | "
            f"Velocità: {speed:.2f} tentativi/s | "
            f"Rimanente stimato: {format_time(eta_seconds)}",
            end="",
            flush=True,
        )

        if current_word == password_target:
            total_time = time() - start_time
            print("\n\n✅ Password trovata!")
            print(f"Password: {current_word}")
            print(f"Tentativi totali: {attempt_index}")
            print(f"Tempo impiegato: {format_time(total_time)}")
            return current_word

    print("\n\n🔎 Password non trovata nella lista delle parole comuni.")
    return None


def main():
    password_to_search = input("> Inserisci la password da cercare: ").strip()
    if not password_to_search:
        print("Devi inserire una password valida.")
        return

    language = input("Lingua del dizionario (es. en, it) [en]: ").strip().lower()
    if not language:
        language = "en"

    count = 2000000
    print("Caricamento in corso...")
    dictionary_attack(password_to_search, language=language, count=count)


if __name__ == "__main__":
    main()
