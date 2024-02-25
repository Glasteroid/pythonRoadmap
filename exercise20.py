def elem_search(given_list, num):
    if num in given_list:
        return True
    
    else:
        return False
    
a = [1, 2, 3, 4]

print(elem_search(a, 4))