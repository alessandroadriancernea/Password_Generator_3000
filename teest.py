import time
from wordfreq import word_frequency,    top_n_list

# password_corretta = input("> ")
# wordlist = top_list("en", 20000)
wordlist = top_n_list("it", 200000)
print(wordlist)
exit(0)

def varianti(parola):
    return [
        parola,
        parola.capitalize(),
        parola + "123",
        parola + "!",
        parola + "2024"
    ]

def dictionary_attack(password_target):
    tentativi = 0
    start_time = time.time()

    for parola in wordlist:
        for variante in varianti(parola):
            tentativi += 1

            print(f"\rTentativi: {tentativi}", end="", flush=True)

            if variante == password_target:
                end_time = time.time()
                print("\n\nPassword trovata!")
                print(f"Password: {variante}")
                print(f"Tentativi: {tentativi}")
                print(f"Tempo: {end_time - start_time:.2f} sec")
                return variante

    print("\nPassword non trovata.")

dictionary_attack(password_corretta)


