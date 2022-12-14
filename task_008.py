# Напишите программу, которая принимает на вход координаты точки (X и Y)
# причем X не равно 0 и Y не равно 0 и выдает номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится)
# Пример
# x=34; y=-30 -> 4
# x=2; y=4 -> 1
# x=-34;y=-30 -> 3

coordinate_x = int(input('Введите координату X точки: '))
coordinate_y = int(input('Введите координату Y точки: '))

while coordinate_x == coordinate_y == 0:
    print('X не должно равняться 0 и Y не должно равняться 0')
    coordinate_x = int(input('Введите координату X точки: '))
    coordinate_y = int(input('Введите координату Y точки: '))

print()
if coordinate_x > 0 and coordinate_y > 0:
    print(f'x={coordinate_x}; y={coordinate_y} -> 1')
elif coordinate_x > 0 and coordinate_y < 0:
    print(f'x={coordinate_x}; y={coordinate_y} -> 4')
elif coordinate_x < 0 and coordinate_y > 0:
    print(f'x={coordinate_x}; y={coordinate_y} -> 2')
elif coordinate_x < 0 and coordinate_y < 0:
    print(f'x={coordinate_x}; y={coordinate_y} -> 3')
elif coordinate_x == 0:
    print('Точка находится на оси Oy')
else:
    print('Точка находится на оси Ox')
