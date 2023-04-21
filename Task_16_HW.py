# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

size = int(input("Введите количество элементов в массиве: "))
list = [randint(1, size) for _ in range(size)]
print(*list)
number = int(input("Введите число, проверяемое на повторы: "))
print(f"-> {list.count(number)}")


# Второй вариант:

from random import randint

size = int(input("Введите количество элементов в массиве: "))
list = [randint(1, size) for _ in range(size)]
print(*list)
number = int(input("Введите число, проверяемое на повторы: "))
count = 0
for i in list:
    if i == number:
        count += 1
print(f"-> {count}")