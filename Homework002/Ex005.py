# Реализуйте алгоритм перемешивания списка.

import random

test_string = 'Реализуйте алгоритм перемешивания списка. Задайте список из N элементов, заполненных числами из промежутка [-N, N].'
list_strings = test_string.split()
print(list_strings)
for i in range(len(list_strings)):
    temp = list_strings[i]
    random_position = random.randint(0,len(list_strings)-1)
    list_strings[i] = list_strings[random_position]
    list_strings[random_position] = temp
print(list_strings)

