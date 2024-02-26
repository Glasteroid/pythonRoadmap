def file_overlap(file1, file2):        
    with open(file1) as f1, open(file2) as f2: 
        list_1 = [eval(x.strip()) for x in f1]
        list_2 = [eval(y.strip()) for y in f2]
            
    list_1 = set(list_1)
    list_2 = set(list_2)
    
    overlap = list(list_1.intersection(list_2))
    
    print(sorted(overlap))
    
file_overlap('primenumbers.txt', 'happynumbers.txt') 