def password_generator():
    """
    Return a password with all the security that we need for more security.
    :params simbols_for_password
    """
    while True:
        try:
            print("Welcome to the python password Generator.")
            letters_for_password = int(
                input("How many letteres do you like for your password: \n")
            )
            simbols_for_password = int(
                input("How many symnos do you like for your password.")
            )
            response = "Thanks for the data"
            return response
        # if not isinstance(letters_for_password, float or int):
        # print("Only numbers, no letters")
        except ValueError:
            print("Only numbers, no letters or float numbers.")
    # else:
    # simbols_for_password = input("How many simbols do you like for your password: \n")


print(password_generator())
