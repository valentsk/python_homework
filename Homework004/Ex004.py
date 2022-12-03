# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

stepen = random.randint(0, 101)
list_koef_stepen_x = []
list_koef_b =[]
list_result = []

for i in range(stepen):
    list_koef_stepen_x.append(i)
    list_koef_b.append(random.randint(0, 20))

with open('text.txt', 'w') as file_data:
    for i in range(len(list_koef_stepen_x) - 1, -1, -1):
        if list_koef_b[i] != 0:
            if i == 1:
                file_data.writelines(f'{list_koef_b[i]} * x + ')
            elif i == 0:
                file_data.writelines(f'{list_koef_b[i]} ')
            else:
                file_data.writelines(f'{list_koef_b[i]} * x^{list_koef_stepen_x[i]} + ')
    file_data.writelines(' = 0')