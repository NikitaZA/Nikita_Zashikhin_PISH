def function(x):
    if x >= 2:
        return  x ** 2 + 4 * x + 5
        
    elif x < -2:
        return  4
       
    else:
       return x ** 2

x = float(input("Введите число:"))
result = function(x)
print(result)
        



         