def sum_num(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

def mult_num(x):
    mult = 1
    while x > 0:
        mult *= x % 10
        x //=10
    return mult

x = int(input("Введите число:"))
sum_result = sum_num(x)
mult_result = mult_num(x)

if sum_result == mult_result:
    print("Значения равны")
else:
    print("Значения не равны")
