# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9


def arithmetic_progression(a, b, c, list):
    result = 0
    for i in range(c):
        result = a
        a = a + b
        list.append(result)
    return list

a = int(input("Введите первый элемент: "))
b = int(input("Введите введите значение разности: "))
c = int(input("Введите количество элементов: "))
list = []

print(arithmetic_progression(a, b, c, list))