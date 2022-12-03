# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('text_one.txt', 'w') as file_data_one:
    file_data_one.writelines('5 * x^10 + 20 * x^9 + 18 * x^8 + 16 * x^6 + 4 * x^3 + 16 * x^2 + 2  = 0')

with open('text_two.txt', 'w') as file_data_two:
    file_data_two.writelines('16 * x^11 + 14 * x^10 + 6 * x^9 + 16 * x^8 + 19 * x^7 + 9 * x^6 + 11 * x^5 + 12 * x^4 + 9 * x^3 + 20 * x^2 + 5 * x + 12  = 0')

with open('text_one.txt', 'r') as file_data_one:
    string_positions_one = file_data_one.read()
    list_positions_one = string_positions_one.split(' + ')
    print(list_positions_one)

with open('text_two.txt', 'r') as file_data_two:
    string_positions_two = file_data_two.read()
    list_positions_two = string_positions_two.split(' + ')
    print(list_positions_two)
# коэффициенты b первые цифры
koef_b = []
for i in range(len(list_positions_one)):
    koef_b.append(list_positions_one[i].split(' '))
print(koef_b)

# коэффициенты степени последние
step_x = []
for i in range(len(koef_b)):
    for j in range(len(koef_b[i])):
        step_x.append(koef_b[i][j].split('^'))
print(step_x)

###############################################################
with open('text_three.txt', 'w') as file_data_three:
    file_data_three.writelines(string_positions_one + ' ' + string_positions_two)