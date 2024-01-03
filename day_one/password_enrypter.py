word_to_encrypt = "Ariana Lemus Buzano"
special_simbols = "!@#$%^&*()_+"
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 15
word_encrypted = ""

for i in word_to_encrypt.lower():
    positionLetter = alphabet.find(i)
    newPosition = (positionLetter + shift) % 26
    word_encrypted += alphabet[newPosition]

print(word_encrypted)

