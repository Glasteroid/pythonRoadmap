def check_pal(given_str):
    given_str = given_str.lower()
    
    if given_str[::-1] == given_str:
        print("This is a palindrome.")
    
    else:
        print("This is not a palindrome.")
    
check_pal("madam")