# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

number_n = int(input('Введите число N: '))
list = []
result = 1

for i in range(number_n):
    list.append(random.randint(-number_n, number_n))
print(list)

file = open("file.txt", "r")

for i in file:
    result *= list[int(i)]

print(result)
