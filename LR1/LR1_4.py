n = input()


if len(n) <= 1:
    print ("Введенно однозначное число")
    flag = True
else:
        for i in range(1, len(n)):
            if n[i] < n[i-1]:
                flag = False
            break
if flag == True: 
    print("Да")
else:
    print("Нет")
