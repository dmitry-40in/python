# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число: '))

list_positive = [0, 1]
list_negative = [0, 1]
result = []

for i in range(2, number + 1):
    list_positive.append(list_positive[i - 2] + list_positive[i - 1])

for i in range(2, number + 1):
    list_negative.append(list_negative[i - 2] - list_negative[i - 1])

result = list_negative[::-1] + list_positive[1:]

print(result)
