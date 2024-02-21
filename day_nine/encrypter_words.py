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
            print(decrypted_word_index)
        else:
            decrypted_word += alphabet[index - shift]
    return decrypted_word


word = input("Introduce the phrase that do you want to encrypt: ").lower()
shift = int(input("introduce the shift of your password: "))
encrypted_word = encrypt(shift, word)
decrypted_word = decrypt(shift, encrypted_word)
print(decrypted_word)
