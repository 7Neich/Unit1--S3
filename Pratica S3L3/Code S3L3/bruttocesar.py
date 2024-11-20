## Alfabeto ita con 21 lettere
ita_alphabet = "ABCDEFGHILMNOPQRSTUVZ"

def brute_force_caesar(ciphertext, alphabet):
    
    brute_force_results = {}
    for shift in range(len(alphabet)):
        plaintext = ""
        for char in ciphertext.upper():
            if char in alphabet:
                index = (alphabet.index(char) - shift) % len(alphabet)  # Decifra con shift
                plaintext += alphabet[index]
            else:
                plaintext += char  # Mantieni invariati i caratteri non alfabetici
        brute_force_results[shift] = plaintext
    return brute_force_results

def main():
   
    print("Benvenuto nel brutto force del cifrario di Cesare!")
    
    # Chiedi all'utente il messaggio cifrato
    ciphertext = input("Inserisci il messaggio cifrato: ").strip()
    
    # Esegui il brute force
    results = brute_force_caesar(ciphertext, ita_alphabet)
    
    # Mostra i risultati all'utente
    print("\nRisultati del brute force:")
    for shift, plaintext in results.items():
        print(f"Shift {shift}: {plaintext}")

# Esegui il programma principale
if __name__ == "__main__":
    main()