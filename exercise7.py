def only_even(given_list):
    even = [x for x in given_list if x % 2 == 0]
    print(even)
    
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

only_even(a)