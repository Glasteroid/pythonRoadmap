name_counts = {}
    
with open('nameslist.txt', 'r') as open_file:
    for line in open_file:
        name = line.strip()
        
        if name in name_counts:
            name_counts[name] += 1
            
        else:
            name_counts[name] = 1
            
for x in name_counts.items():
    print(x)
             