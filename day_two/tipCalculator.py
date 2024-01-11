print("Welcome to the tip calculator.")
check = input("How much was your check? ")
people = input("How many people are splitting the check? ")
pople_string = str(people)
how_much_tip = input("What percentage would you like to tip? ")
percentage_tip = int(how_much_tip) / 100
tip = int(check) * percentage_tip
pay_per_person = (int(check) + tip) / int(people)
print("Each person should pay:" + str(pay_per_person) + " dollars.")
