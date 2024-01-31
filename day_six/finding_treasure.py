import random

game_over_message = ["Nice try, Game Over", "you need to improve your decistions"]
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
decisition = input(
    "You're at a crossroad where do you want to go? Type right or left: \n"
).lower()
if decisition == "right":
    print("You have fallen into a hole \n")
if decisition == "left":
    print(
        "You are on a bridge and you a meet a mouse talking mouse who tells you he can grant you a wish. \n"
    )
    decisition = input("What do you want to do. Accept the request?: Y/N \n").lower()
    if decisition == "y":
        print("The mouse gives you a map with instructions to find the treasure. \n")
        print(
            "You find the treasure in the map, are you going to the ship. Congratulations. "
        )
    else:
        print("The mouse puts a curse on you and you get old. \n")
        print(random.choice(game_over_message))

else:
    print(random.choice(game_over_message))
