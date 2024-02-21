import random

def guessing_game():
    random_num = random.randint(1, 9)
    
    while True:
        
        user_input = None
        
        while user_input not in range(1, 10):
            user_input = int(input("Guess a number between 1 and 9: "))
        
        guesses = 0
        
        if user_input == random_num:
            print("You guessed the number right!")
            break
            
        elif user_input > random_num:
            print("You guessed a number too high!")
            guesses +=1
            continue
            
        else:
            print("You guessed a number too low!")
            guesses +=1
            continue
        
    play_again = input("Would you like to play again? ").lower()
    
    if play_again == "yes":
        guessing_game()
        
guessing_game()
    