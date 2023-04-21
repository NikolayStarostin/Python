# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X . 
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

size = int(input("Введите количество элементов в массиве: "))
list = [randint(1, size) for _ in range(size)]
print(*list)
number = int(input("Введите число: "))
min_diff = list[0]
for i in list:
    diff = abs(i - number)
    if diff < min_diff:
        result = i
        min_diff = diff
print(result)