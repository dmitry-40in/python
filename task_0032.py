# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите А: '))
b = int(input('Введите В: '))


def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)


print(f'-> {power(a, b)}')