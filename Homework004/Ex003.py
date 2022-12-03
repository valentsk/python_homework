# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list_random = []
for i in range(random.randint(5,11)):
    num_random = random.randint(1,11)
    list_random.append(num_random)

print(list_random)

list_res = []
for i in range(len(list_random)):
    if list_random.count(list_random[i]) == 1:
        list_res.append(list_random[i])

print(list_res)