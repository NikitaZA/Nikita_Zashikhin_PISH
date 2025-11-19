n = int(input())

if 1 <= n <= 100:
    
     for i in range(1, n + 1):
        square = i ** 2
        cube = i ** 3
        print(square, cube)

else:
    print("Ошибка: Введено неверное число.")
