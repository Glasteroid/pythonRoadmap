def fib_sequence():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    
    i = 1
    
    if count == 0:
        fib = []
        
    elif count == 1:
        fib = [1]
        
    elif count == 2:
        fib = [1, 1]
        
    elif count > 2:
        fib = [1, 1]
        
        for i in range(count - 2):
            fib.append(fib[i] + fib [i + 1])
        
    return fib

print(fib_sequence())

        
        

