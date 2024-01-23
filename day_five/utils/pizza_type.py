def pizza_type():
    print("Pizza Type")
    print("Select: 1 for Medium.")
    print("Select: 2 for Large.")
    pizza_type = int(input("Enter your choice: "))
    if pizza_type == 1:
        return "Medium"
    elif pizza_type == 2:
        return "Large"
