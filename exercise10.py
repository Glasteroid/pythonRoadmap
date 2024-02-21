def overlap(list1, list2):
    list1 = set(list1)
    
    unique_elem = [x for x in list1 if x in list2]
    
    print(unique_elem)
    
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap(a, b)