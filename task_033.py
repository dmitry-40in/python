# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Задайте значение натуральной степени k: '))
while k < 0:
    k = int(input('Задайте значение натуральной степени k: '))


result_list = []
result = ''

for i in range(k, -1, -1):
    multiplier = random.randint(0, 100)
    if multiplier != 0:
        if multiplier != 1:
            if i > 1:
                result_list.append(str(multiplier) + '*x^' + str(i))
            elif i == 1:
                result_list.append(str(multiplier) + '*x')
            else:
                result_list.append(str(multiplier))
        else:
            if i > 1:
                result_list.append('x^' + str(i))
            elif i == 1:
                result_list.append('x')
            else:
                result_list.append(str(multiplier))

if len(result_list) != 0:
    result = result_list[0]
    for i in range(1, len(result_list)):
        result += ' + ' + result_list[i]

print(result_list)

file = open('task_033.txt', 'w')
file.write(result)
file.close()
