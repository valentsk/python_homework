# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce
import random

number = int(input('Введите число: '))
list_numbers = [random.randint(0, 10) for i in range(number)]
print(list_numbers)
del list_numbers[0::2]
print(list_numbers)
sum = reduce(lambda x, y: x + y, list_numbers)
print(sum)