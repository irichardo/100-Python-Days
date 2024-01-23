print("Thank you for your order!")
size = input("\nWhat size pizza would you like? (S, M, or L) ")
add_peperoni = input("Would you like to add peperoni? (Y or N) ")
add_cheese = input("Would you like to add extra cheese? (Y or N) ")
check_extra = 0
if size == "S":
    check_extra += 2
if size == "M":
    check_extra += 3
if size == "L":
    check_extra += 5
if add_peperoni == "Y":
    check_extra += 1
if add_cheese == "Y":
    check_extra += 3
print(f"Your final bill is: ${15 + check_extra}")
