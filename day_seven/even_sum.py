number_list = input("Please introduce numbers: ").split()
int_number_list = []
numbers_sum = 0

print(number_list)

for numbers in range(0, len(number_list)):
    int_number_list.append(int(number_list[numbers]))

if len(number_list) == 0:
    print("Please introduce some number")
else:
    for number in range(0, len(number_list)):
        if int_number_list[number] % 2 == 0:
            numbers_sum += int_number_list[number]
    print(f"The sum of all even numbers is: {numbers_sum}")
