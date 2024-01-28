# Love Calculator
def love_calculator():
    first_name = input("Introduce your name: ")  # What's your name.
    second_name = input("Introduce the name of your partner: ")
    combined_names = first_name.lower() + second_name.lower()
    dictionary = ["true", "love"]
    love_count = sum(
        letter in dictionary[0] or letter in dictionary[1] for letter in combined_names
    )
    print(f"{love_count*10}% Love compatibility.")


love_calculator()
