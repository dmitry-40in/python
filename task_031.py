# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число начиная с 2: '))
while number <= 1:
    if number == 1:
        print('1 - не является ни простым ни составным числом. Так как имеет один натуральный делитель.')
    number = int(input('Введите натуральное число начиная с 2: '))

list = []
number_for_print = number

i = 2

while i <= number ** 0.5:
    if number % i == 0:
        list.append(i)
        number = int(number / i)
        i = 2
    else:
        i += 1
list.append(number)

print(f'Cписок простых множителей числа {number_for_print}: ', list)
