# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого?

number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))

if number_one == number_two ** 2 or number_two == number_one ** 2:
    print('Да')
else:
    print('Нет')
