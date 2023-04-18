# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. С клавиатуры вводятся число монет и сами монеты построчно.
# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

coins = int(input('Введите количество монет: '))
coins_left = 0
coins_right = 0
for i in range(coins):
    if input('Сторона монеты ') == '1':
        coins_right += 1
    else:
        coins_left += 1
if coins_left < coins_right:
    print(f'Количество монет, которые нужно перевернуть {coins_left}')
else:
    print(f'Количество монет, которые нужно перевернуть {coins_right}')