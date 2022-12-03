# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число: '))
temp = number
res_str = ''
while number // 2 > 0:
    res_str += str(number % 2)
    number = number // 2
    if number == 1:
        res_str += '1'

print(f'dec {temp} = bin {res_str[::-1]}')
