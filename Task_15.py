# Задача №15.
# Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. Но вот незадача: арбузов слишком много 
# и он не знает как же выбрать самый легкий и самый тяжелый арбуз? 
# Помогите ему! Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

quant = int(input('Введите количество арбузов '))
min_weight = 30000
max_weight = 1

for i in range(quant):
    weight = randint(1, 30000)
    print(weight)
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight
print(f'Для себя {max_weight}')
print(f'Для тещи {min_weight}')
