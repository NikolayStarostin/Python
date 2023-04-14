# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трехзначное число: '))
first_digit = num // 100
second_digit = num // 10 % 10
third_digit = num % 10
sum = first_digit + second_digit + third_digit
print(f'{num} -> {sum} ({first_digit} + {second_digit} + {third_digit})')