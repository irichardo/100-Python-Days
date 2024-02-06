number = int(input("Please, introduce your number: "))
sum_evem_number = 0
for number in range(2, number + 1, 2):
    sum_evem_number += number
print(f"The sum of the all numbers is {sum_evem_number}")
