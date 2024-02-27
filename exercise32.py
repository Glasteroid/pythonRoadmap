import random

def pick_word():
    with open('sowpods.txt', 'r') as open_file:
        word_list = [x.strip() for x in open_file]
        
        word = word_list[random.randint(0, len(word_list))]
        
        return word
    
def end_game(guesses):
    if guesses == 0:
        print("Sorry, out of guesses! End of the game!")
        return True

def  run_game(word):
        x = []
        
        for _ in range(len(word)):
            x.append("_")
            
        print(str("".join(x)))
        
        guesses = 6
        
        guess_set = set()
        
        while True:
            user_guess = input("Guess your letter: ").upper()
            guesses -= 1    
            
            if len(guess_set) >= 1:
                while user_guess in guess_set:
                    print("You already guessed this letter! Please choose another letter.")
                    user_guess = input("Guess your letter: ").upper()
                    
            guess_set.add(user_guess)
            
            if user_guess in word:
                letter_indexes = [i for i in range(len(word)) if word[i] == user_guess]
                for index in letter_indexes:
                    x[index] = user_guess
                print(str("".join(x)))
                
                if end_game(guesses):
                    break
                
                print("You have {} guesses left.".format(guesses))
                
                if word == str("".join(x)):
                    print("You guessed the word! It only took you one guess! What a magician!")
                    break
            
            else:
                print("Incorrect!")
                
                if end_game(guesses):
                    break
            
                print("You have {} guesses left.".format(guesses))
            
if __name__ == '__main__':
    print("Welcome to Hangman!")
    word = pick_word()
    
    run_game(word)