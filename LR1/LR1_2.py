a = int(input())
b = int(input())


if a <= b and abs(a) <= 100 and abs(b) <= 100:
    
     for i in range(a, b + 1):
        square = i ** 2
        print(square)

else:
    print("Ошибка: Введенные числа не соответствуют условиям.")
