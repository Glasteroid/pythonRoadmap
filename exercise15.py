def rev_string():
    str = input("Please enter a sentence with more than one word: ")
    
    while len(str.split()) <= 1:
        str = input("Please enter a sentence with more than on word: ")
        
    words = str.split()
    
    return ' '.join(words[::-1])

print(rev_string())
        
    

