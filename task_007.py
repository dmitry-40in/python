# Напишите программу для проверки истинности утверждения
# ¬(X ∨ Y ∨ Z) = ¬X ∧ ¬Y ∧ ¬Z
# для всех значений предикат

print(' X | Y | Z | ¬(X ∨ Y ∨ Z) | ¬X ∧ ¬Y ∧ ¬Z ')

marker_true = True
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f' {x} ', end="|")
            print(f' {y} ', end="|")
            print(f' {z} ', end="|")

            result_one = not (x or y or z)
            result_two = not x and not y and not z

            print(f'     {result_one}    ', end="|")
            print(f'     {result_two}       ')

            if result_one != result_two:
                marker_true = False

print()

if marker_true:
    print('Утверждения ¬(X ∨ Y ∨ Z) = ¬X ∧ ¬Y ∧ ¬Z истинно')
else:
    print('Утверждения ¬(X ∨ Y ∨ Z) = ¬X ∧ ¬Y ∧ ¬Z ошибочно')
