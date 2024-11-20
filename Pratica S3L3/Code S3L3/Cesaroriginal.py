# Alfabeto italiano con 21 lettere
ita_alphabet = "ABCDEFGHILMNOPQRSTUVZ"

# Funzione per crittografare o decrittografare con shift fisso di 3
def caesar_cipher_fixed(message, mode="encrypt"):
    shift = 3  # Shift fisso
    if mode == "decrypt":
        shift = -shift  # Inverte lo shift per la decrittazione
    result = ""
    for char in message.upper():
        if char in ita_alphabet:
            index = (ita_alphabet.index(char) + shift) % len(ita_alphabet)
            result += ita_alphabet[index]
        else:
            result += char  # Mantieni caratteri non alfabetici invariati
    return result

def main():
    print("Benvenuto a Cesare!" "\nGallia est omnis divisa in partes tres.")
    choice = input("Vuoi (E)ncrypt o (D)ecrypt? ").strip().lower()

    if choice == 'e':
        mode = "encrypt"
    elif choice == 'd':
        mode = "decrypt"
    else:
        print("Scelta non valida. Riprova.")
        return

    message = input("Inserisci il messaggio: ").strip()
    result = caesar_cipher_fixed(message, mode)
    print(f"Risultato: {result}")

# Esecuzione
if __name__ == "__main__":
    main()