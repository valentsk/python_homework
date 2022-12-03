# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

number = int(input('Введите число: '))
list_numbers = []
for i in range(number):
    list_numbers.append(round(random.randint(0, 100) / random.randint(0, 100), 2))
print(list_numbers)

list_fractions = []
for i in range(number):
    list_fractions.append((round(list_numbers[i] % 1 * 100)))
print(list_fractions)
index_min = list_fractions[0]
index_max = list_fractions[0]

for i in range(number):
    if list_fractions[i] < list_fractions[index_min]:
        index_min = i
    if list_fractions[i] > list_fractions[index_max]:
        index_max = i
print(f'Разница = {list_fractions[index_max] - list_fractions[index_min]}')