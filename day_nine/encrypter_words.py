alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def encrypt(shift: int, word: str):
    encrypted_word_index = []
    encrypted_word = ""
    for letter in word:
        encrypted_word_index.append(alphabet.index(letter))
    for index in encrypted_word_index:
        if index + shift >= len(alphabet):
            # To restart at the first alphabet item
            # Example 0 1 2 3
            case_residue = (index + shift) - len(alphabet)
            encrypted_word += alphabet[case_residue]
        else:
            encrypted_word += alphabet[index + shift]
    return encrypted_word


def decrypt(shift: int, word: str):
    decrypted_word_index = []
    decrypted_word = ""
    for letter in word:
        decrypted_word_index.append(alphabet.index(letter))
    for index in decrypted_word_index:
        if index - shift < 0:
            decrypted_word += alphabet[len(alphabet) + (index - shift)]
        else:
            decrypted_word += alphabet[index - shift]
    return decrypted_word

def encryptWord():
    word_to_encrypt = input("Please introduce the word that you want to encrypt: ").lower()
    shift = int(input("Please introduce the shift: "))
    word_encrypted = encrypt(word=word_to_encrypt,shift=shift)
    print(f"This is your word encrypted: {word_encrypted}")
    
def decryptedWord():
     word_to_decrypt = input("Please introduce the word that you want to decrypt: ").lower()
     shift = int(input("Please introduce the shift: "))
     word_decrypted =  decrypt(word=word_to_decrypt, shift=shift)
     print(f"This is your word decrypted: {word_decrypted}")

def security_controller():
    while True:
        try:
            decision = int(input("Please, introduce:\n 1. Encrypt.\n 2. Decrypt.\n"))
            if decision == 1:
                encryptWord()
            if decision == 2:
                decryptedWord()
        except Exception:
            print(Exception)

security_controller()