# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = input('Введите строку: ')
find_string = 'абв'
list_str = list(str.split)
result = map(lambda x: if find_string in x, list_str)
print(result(list_str))