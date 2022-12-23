# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from math import fabs

list = [1.1, 1.2, 3.1, 5, 10.01]

list_second = []
sum = 0

for i in list:
    if fabs(i) % 1 != 0:                            # поскольку функция fabs перед расчетом модуля агумента преобразует тип аргумента к вещественному числу, проверку на вещественное число исключил
        list_second.append(round(fabs(i) % 1, 2))   

min = list_second[0]
max = list_second[0]

for i in list_second:
    if i < min:
        min = i
    if i > max:
        max = i

sum = max - min
print(list, '=>', sum) 
