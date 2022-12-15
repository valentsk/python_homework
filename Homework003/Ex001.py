# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

number = int(input('Введите число: '))
# sum = 0
# list_numbers = []
# for i in range(number):
#     list_numbers.append(random.randint(0, 10))
# print(list_numbers)
# for i in range(1, number, 2):
#     sum += list_numbers[i]
# print(sum)

list_numbers = [x = random.randint(0, 10) for x in range(number)]
print(list_numbers)
# list_numbers = filter(lambda x: x %9 == 0, range(10,100))