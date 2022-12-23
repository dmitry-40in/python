# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

#list = [2, 3, 4, 5, 6]
list = [2, 3, 5, 6]

result = []

for i in range(int(len(list) / 2)):
    result.append(list[i] * list[int(len(list)) - 1 - i])
if len(list) % 2 == 1:
    result.append(list[int(len(list) / 2)] ** 2)

print(list, '=>', result)
