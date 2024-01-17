try:
    height = input("Enter your heihgt in m: ")
    weight = input("Enter your weight in kg: ")
    height_as_float = float(height)
    weight_as_int = int(weight)
    bmi = weight_as_int / height_as_float**2
    format_bmi = format(bmi, ".2f")
    print(f"your bmi is:{format_bmi}")
except ValueError:
    print("Numero No valido")
