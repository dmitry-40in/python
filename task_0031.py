# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]


#         #0  1  2  3   4   5  6  7   8   9  10 11  12 13 14  15  16  17  18 19
# list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#        #    +                           +            +  +                  +
# a = 5
# b = 15

length = int(input('Введите длину списка: '))
list = [int(input(f'Введите элемент списка №{i}: ')) for i in range(length)]
a = int(input('Введите минимум: '))
b = int(input('Введите максимум: '))

result = [i for i in range(len(list)) if a <= list[i] <= b]

print(result)