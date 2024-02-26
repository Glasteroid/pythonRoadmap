import random

def pick_word():
    with open('sowpods.txt', 'r') as open_file:
        word_list = [x.strip() for x in open_file]
        
        word = word_list[random.randint(0, len(word_list))]
        
        return word
    
def guess_letter(word):
        x = []
        
        for _ in range(len(word)):
            x.append("_")
            
        print(str("".join(x)))
        
        while True:
            user_guess = input("Guess your letter: ").upper()    
            
            if user_guess in word:
                letter_indexes = [i for i in range(len(word)) if word[i] == user_guess]
                for index in letter_indexes:
                    x[index] = user_guess
                print(str("".join(x)))
                
                if word == str("".join(x)):
                    print("You guessed the word!")
                    break
            
            else:
                print("Incorrect!") 
    
if __name__ == '__main__':
    print("Welcome to Hangman!")
    word = pick_word()
    
    guess_letter(word)