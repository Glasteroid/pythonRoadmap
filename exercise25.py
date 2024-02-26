import random

if __name__ == '__main__':
    user_number = int(input("Please choose a number between 0 and 100: "))
    
    computer_guess = 50
    
    guesses = 0
    
    while True:        
        user_choice = input("Is {} higher, lower, or equal to your number? ".format(computer_guess).lower())
        
        if user_choice == 'higher':
            guesses += 1
            computer_guess -= 1
                    
        elif user_choice == 'lower':
            guesses += 1
            computer_guess += 1
        
        else:
            guesses += 1
            print("{} is your number!".format(computer_guess))
            print("It took me {} guesses to find your number!".format(guesses))
            break