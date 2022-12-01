# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

number = int(input('Введите число: '))
list_numbers = []
for i in range(- number, number + 1):
    list_numbers.append(i)
print(list_numbers)

with open('text.txt', 'w') as file_data:
    file_data.writelines(f'{str((random.randint(0, len(list_numbers))))}\n')
    file_data.writelines(f'{str((random.randint(0, len(list_numbers))))}\n')

with open('text.txt', 'r') as file_data:
    # print(file_data.read())
    string_positions = file_data.read()

list_positions = string_positions.split()
print(list_positions)

multipl = list_numbers[int(list_positions[0])] * list_numbers[int(list_positions[1])]
print(f'Произведение элементов {multipl}')
