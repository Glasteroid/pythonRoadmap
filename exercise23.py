def file_overlap(file1, file2):
    list_1 = []
    list_2 = []
        
    with open(file1) as f1, open(file2) as f2: 
        for x, y in f1 and f2:
            list_1.append(x)
            list_2.append(y)
            
    list_1 = set(list_1)
    list_2 = set(list_2)
    
    overlap = [list_1.intersection(list_2)]
    
    print(overlap)
    
file_overlap()
    
    