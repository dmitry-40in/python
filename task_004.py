# Напишите программу, которая будет принимать на вход дробь и показывает
# первую цифру дробной части числа
#
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

number = float(input('Введите число: '))
new_number = int(number % 1 * 10)
if new_number != 0:
    print(new_number)
else:
    print('нет')


# # через строку другой вариант
# n = input()
# a = n.split(".") # одну строку с помощью функции split() делим на двестроки 
#                  # разделитель выбираем "."
# print(a) # целая часть первым элементом в списке, дробная часть стала вторым элементов
#          # в списке. Например 12.32 -> ['12', '32']

# print(a[1][0]) # Вывести на экран первое число второго элемента
# обратились к 1 элементу (второй в списке с индексом 1) и там к 0 эелменту (первый в списке с индексом 0)

