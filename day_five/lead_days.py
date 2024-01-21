# Leap day is divisible by 4
# Leap year is divisible by 400
# Leap year is not divisible by 100


def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
        return leap


if is_leap(2020):
    print("Leap year")
else:
    print("Is not leap year")
