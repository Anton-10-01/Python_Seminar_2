# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите кол-во монеток: "))
a = 0
b = 0
i = 0
while i < n:
    k = int(input("Введите 0 или 1: "))
    if (k == 0):
        a += 1
    elif (k == 1):
        b += 1
    else:
        print("Ошибка ввода")
        break
    i = i + 1
if (a < b):
    print("Минимальное число монеток, которые нужной перевернуть: ", a)
elif (b < a):
    print("Минимальное число монеток, которые нужной перевернуть: ", b)