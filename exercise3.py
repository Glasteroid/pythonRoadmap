a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_5(given_list):
    less_than5 = []
    
    for item in given_list:
        if item < 5:
            less_than5.append(item)
            
    print(less_than5)
            
less_5(a)