from utils.pizza_type import pizza_type


def pizza_func():
    print("I'm a pizza function!")
    print("How do you want your pizza?")
    pizza = []
    add_peperoni = input("Do you want pepperoni? ")
    add_pine_apple = input("Do you want pine apple? ")
    add_meat = input("Do you want meat? ")
    # Pizza Type is imported from utils/pizza_type.py
    pizza.append(pizza_type())
    if add_peperoni == "yes":
        pizza.append("pepperoni")
    if add_pine_apple == "yes":
        pizza.append("pine apple")
    if add_meat == "yes":
        pizza.append("meat")
    else:
        # Default case
        print("Invalid input!")
    return pizza
