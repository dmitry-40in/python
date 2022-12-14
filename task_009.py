# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (х и у)

part_number = int(input('Введите номер четверти: '))

while part_number < 1 or part_number > 4:
    print('Введен неверный номер четверти')
    part_number = int(input('Введите номер четверти: '))

if part_number == 1:
    print('x > 0, y > 0')
elif part_number == 2:
    print('x < 0, y > 0')
elif part_number == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')
