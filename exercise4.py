number = int(input("Please enter a number: "))

possible_div = range(1, number + 1)

for num in possible_div:
    if number % num == 0:
        print(str(num))