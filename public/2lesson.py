start = int(input("Введите первое число: "))
stop = int(input("Введите последнее число: "))
step = int(input("Введите шаг: "))
for i in range(start, stop, -step):
    print(i)
