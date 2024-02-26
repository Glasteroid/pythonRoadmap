import random

def pick_word():
    with open('sowpods.txt', 'r') as open_file:
        word_list = [x.strip() for x in open_file]
        
        word = word_list[random.randint(0, len(word_list))]
        
        return word
    
print(pick_word())