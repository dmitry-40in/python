# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import datetime

number_n = int(input('Введите число: '))

rand = datetime.datetime.now().microsecond
rand_2 = datetime.datetime.now().microsecond % (number_n + 1)

print(rand)
print(rand_2)

