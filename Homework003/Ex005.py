# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи

number = int(input('Введите число: '))

if number == 0:
    list_fibo = [0]
    list_fibo_neg = []
    print(list_fibo_neg + list_fibo)
elif number == 1:
    list_fibo = [0, 1]
    list_fibo_neg = [1]
    print(list_fibo_neg + list_fibo)
else:
    list_fibo = [0, 1]
    list_fibo_neg = []
    for i in range(2, number + 1):
        next_number = list_fibo[i - 1] + list_fibo[i - 2]
        list_fibo.append(next_number)
        list_fibo_neg.append((-1) ** (i + 1) * next_number) # F(-n) = (-1)^(n+1) * F(n)

# развернули массив негоФиб
    fibo_neg_return = []
    for i in range(len(list_fibo_neg)):
        fibo_neg_return.append(list_fibo_neg[len(list_fibo_neg) - i - 1])

    print(fibo_neg_return+list_fibo)