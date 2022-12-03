# Вычислить число c заданной точностью d
# #
# # Пример:
# #
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

number = int(input('Введите точность: '))

pi_leibnica = 0
num_leib = 4
for i in range(1, 10 ** 8, 4):
    pi_leibnica += num_leib / i - num_leib / (i + 2)
print(f'Число Пи = {pi_leibnica}')
str_pi = str(pi_leibnica)
print(f'Число Пи с задачнной точностью {number} = {str_pi[:number + 2]}')
