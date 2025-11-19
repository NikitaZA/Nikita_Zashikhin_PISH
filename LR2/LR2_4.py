def sum_num(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

x = int(input("Введите число:"))
result = sum_num(x)
print(result)     
