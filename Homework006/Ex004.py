# Задайте список из N элементов, заполненных числами из промежутка [-N, N]

import random

number = int(input('Введите число '))
list_numbers = []

# for i in range(number):
#     list_numbers.append(random.randint(-number, number))

list_numbers = [random.randint(-number, number) for i in range(number)]

print(list_numbers)