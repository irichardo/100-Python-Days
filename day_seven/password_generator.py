import random


def password_generator():
    """
    Return a password with all the security that we need for more security.
    :params simbols_for_password
    """
    letters = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["{", "}", "$", "#", "@", "!", "&", "*", "("]
    password_characters = []
    while True:
        try:
            print("Welcome to the python password Generator.")
            letters_for_password = int(
                input("How many letters do you like for your password: \n")
            )
            simbols_for_password = int(
                input("How many symnos do you like for your password: \n")
            )
            numbers_for_password = int(
                input("How many numbers do you like for your password: \n")
            )
            for letter in range(0, letters_for_password + 1):
                password_characters.append(random.choice(letters))
            for symbol in range(0, simbols_for_password + 1):
                password_characters.append(random.choice(symbols))
            for number in range(0, numbers_for_password + 1):
                password_characters.append(random.choice(numbers))
            random.shuffle(password_characters)
            password = ""
            for char in password_characters:
                password += char
            print(password)
            return password
            # if not isinstance(letters_for_password, float or int):
        # print("Only numbers, no letters")
        except ValueError:
            print(ValueError)
    # else:
    # simbols_for_password = input("How many simbols do you like for your password: \n")


print(password_generator())
