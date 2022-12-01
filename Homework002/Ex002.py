# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number = int(input('Введите число: '))
a = 1
list_result = []
for i in range(0, number):
    a *= (i + 1)
    list_result.append(a)
print(list_result)