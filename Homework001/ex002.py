# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])
# для всех значений предикат.

def checkTrue(x):
    print(not (x[0] or x[1] or x[2]) == ((not x[0]) and (not x[1]) and (not x[2])))

checkTrue([False, False, False])
checkTrue([False, False, True])
checkTrue([False, True, False])
checkTrue([False, True, True])
checkTrue([True, False, False])
checkTrue([True, False, True])
checkTrue([True, True, False])
checkTrue([True, True, True])
