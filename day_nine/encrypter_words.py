def encrypt(shift: int, word: str):
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
        " ",
        "w",
        "x",
        "y",
        "z",
        ",",
        ".",
    ]

    encypted_word_index = []
    encrypted_word = ""
    shifted_alphabet = alphabet[shift:]
    shifted_alphabet += alphabet[:shift]
    for letter in word:
        if letter == " ":
            encypted_word_index.append("-")
        else:
            encypted_word_index.append(alphabet.index(letter))
    for index in encypted_word_index:
        encrypted_word += shifted_alphabet[index]
    return encrypted_word


word = input("Introduce the phrase that do you want to encrypt: ").lower()
shift = int(input("introduce the shift of your password: "))
encrypted_word = encrypt(shift, word)
print(encrypted_word)
