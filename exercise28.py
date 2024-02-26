def max_three(num1, num2, num3):
    max = num1
    
    if num2 > max:
        max = num2
        
    if num3 > max:
        max = num3
        
    return max

print(max_three(1, 3, 20))