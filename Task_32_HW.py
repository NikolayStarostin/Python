# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8 - рассматриваемый список
# 4 - начало диапазона
# 8 - конец
# Output:
# 2(7), 4(5), 5(8)

from random import randint as rnd

min = 10
max = 30

list = []
for i in range(10):
    list.append(rnd(1, 100))

list_of_index = []
for i in range(len(list)):
    if min <= list[i] <= max:
        list_of_index.append(i)

print(list)
print(list_of_index)