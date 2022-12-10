# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str = input('Введите строку: ')
# str = 'иииииииииииии абв авбддддддд вввввввввв ддадададаабвжж не удалитьабв'
find_string = 'абв'
list_str = list(str.split())
list_result = list(map(lambda x: x.replace(x,'') if find_string in x else x, list_str))
print(' '.join(list_result))