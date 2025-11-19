def nod(a, b): 
    while a != 0 and b != 0:
        if a > b: 
            a = a - b
        else: 
            b = b - a 
    return max(a, b)
        
a = int(input("Введите число:"))
b = int(input("Введите число:"))
result = nod(a,b)
print(result)       