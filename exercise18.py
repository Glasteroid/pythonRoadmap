import random

def cows_bulls():
    print("Welcome to the Cows and Bulls Game!")
    
    random_num = str(random.randint(1000, 9999))
    
    list_random = list(map(int, random_num))
    
    guesses = 0
    
    while True:
        print(list_random)
        cows, bulls = 0, 0
        
        guess = int(input("Enter a number: "))
        
        list_guess = list(map(int, guess))
        
        for i in range(len(list_random)):          
                if list_guess[i] == list_random[i]:
                    cows += 1
                    list_guess.remove(list_guess[i])
                    list_random.remove(list_random[i])
                    
                elif list_guess[i] in list_random:
                    bulls += 1
                
        if cows == 4:
                print("You guessed the correct number!")
                continue
        
        guesses += 1        
        
        print("{0} cow(s), {1} bull(s)".format(cows, bulls))

cows_bulls()
       