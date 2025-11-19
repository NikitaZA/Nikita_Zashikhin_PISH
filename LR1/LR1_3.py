a = int(input())
b = int(input())


if a <= b and abs(a) <= 100 and abs(b) <= 100:
    
    sum_squares = 0

    for i in range(a, b + 1):
        sum_squares += i ** 2
        print(sum_squares)

else:
    print("Ошибка: Введенные числа не соответствуют условиям.")
