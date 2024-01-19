height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

body_mass_index = weight / (height**2)
message = f"Your BMI is : {body_mass_index}"
if body_mass_index < 18.5:
    print(message, "Underweight")
elif body_mass_index < 25:
    print(message, "Normal weight")
elif body_mass_index < 30:
    print(message, "Overweight")
elif body_mass_index < 35:
    print(message, "Obesse")
elif body_mass_index > 35:
    print(message, "Clinically Obesse")
