# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число: ')
sum = 0

result = lambda x: sum = int(x) if x.isdigit()
print(result(number))
print(sum)
#
# for a in number:
#
#     if a.isdigit():
#         sum += int(a)
#
# print(sum)