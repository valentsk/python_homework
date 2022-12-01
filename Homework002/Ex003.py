# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#


number = int(input('Введите число: '))
a = 1
sum = 0
list_result = []
for i in range(1, number + 1):
    a = round(((1 + 1 / i) ** i) , 2)
    sum += a
    list_result.append(a)
print(list_result)
print(f'Сумма элементов последовательности {sum}')