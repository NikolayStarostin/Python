# Задача 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите шестизначное число: '))
num_1 = ticket // 100000
num_2 = ticket // 10000 % 10
num_3 = ticket // 1000 % 10
num_4 = ticket // 100 % 10
num_5 = ticket // 10 % 10
num_6 = ticket % 10
if (num_1 + num_2 + num_3) == (num_4 + num_5 + num_6):
    print(f'{ticket} -> "yes"')
else:
    print(f'{ticket} -> "no"')