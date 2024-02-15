# a number prime is divisible by 1 and the same number
# 2 is no prime


def prime_checker(number: int):
    is_prime = True
    if number == 2 or number % 2 != 0:
        is_prime = False
    return is_prime


number = int(input("Please introduce a number: "))
is_prime = prime_checker(number)
if is_prime:
    print("El numero no es primo.")
else:
    print("El numero si es primo.")
