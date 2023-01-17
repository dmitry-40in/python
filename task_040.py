# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)

# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.
# ЧИСЛО ПОВТОРЕНИЙ СОСТОИТ ИЗ ОДНОЗНАЧНОГО ЧИСЛА (1 - 9) (иначе с входными данными числами не работает - много вариантов)

#number = '1111111111111111112222334445'
#number = '842233355555555555555555555555555555555555555555'
# эти числа при кодировании выглядят одинаково: 18142233415
# соответственно раскодировать однозначно их нельзя, так?

#number = '6A1F2D7C1A7E'
#number = '1111111111111111112222334445'

print('Для RLE-сжатия данных введите: 1; для RLE-восстановления данных введите: любой дрйгой символ')
choice = input('Ваш выбор? ')

number = input('Введите данные: ')


def RLE_compression_module(x):
    result = ''
    prev_char = number[0]
    counter = 0
    for i in number:
        if i == prev_char:
            counter += 1
        else:
            result += str(counter) + str(prev_char)
            prev_char = i
            counter = 1
    result += str(counter) + str(prev_char)

    print(result)


def RLE_data_recovery_module(x):
    result = ''
    digit = True
    count = 0
    for i in x:
        if digit:
            count = int(i)
            digit = False
        else:
            result += i * count
            digit = True
    print(result)


if choice == '1':
    RLE_compression_module(number)
else:
    RLE_data_recovery_module(number)
