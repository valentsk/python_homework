# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

coor_xA = float(input('Введите координаты xA '))
coor_yA = float(input('Введите координаты yA '))
coor_xB = float(input('Введите координаты xB '))
coor_yB = float(input('Введите координаты yB '))

result = ((coor_xA - coor_xB) ** 2 + (coor_yA - coor_yB) ** 2) ** 0.5
print(f'Расстояние между точками {round(result, 2)}')
