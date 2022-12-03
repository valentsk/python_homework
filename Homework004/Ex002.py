# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))

list_result = []
i = 2
while number >= i:
    if number % i == 0:
        list_result.append(i)
        number = number // i
        i -= 1
    i +=1
print(list_result)

