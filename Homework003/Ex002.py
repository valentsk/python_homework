# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

number = int(input('Введите число: '))
list_numbers = []
for i in range(number):
    list_numbers.append(random.randint(0, 10))
print(list_numbers)

list_result = []
if  number % 2 == 0:
    for i in range(int(number / 2)):
        list_result.append(list_numbers[i] * list_numbers[len(list_numbers) - 1 - i])
else:
    for i in range(int(number / 2 + 1)):
        list_result.append(list_numbers[i] * list_numbers[len(list_numbers) - 1 - i])

print(list_result)