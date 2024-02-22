user_input = 0

while user_input <= 1:
    user_input = int(input("Please enter a number: "))

pos_div = [x for x in range(2, user_input)]

is_prime = True

for num in pos_div:
    if user_input % num == 0:
        is_prime = False
        
if is_prime:
    print("This is a prime number.")
    
else:
    print("This is not a prime number.")