# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

min = int(input('Задайте минимальное значение числа для формирования списка: '))
max = int(input('Задайте максимальное значение числа для формирования списка: '))
length = int(input('Задайте длину списка: '))

list = [random.randint(min, max) for i in range(length)]
print(list)

result = []
check = True

for i in list:
    for j in result:
        if i == j:
            check = False
    if check == True:
        result.append(i)
    check = True

print(result)
