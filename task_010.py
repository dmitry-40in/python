# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

dot_a_x = float(input('Введите координату X точки А: '))
dot_a_y = float(input('Введите координату Y точки А: '))
dot_b_x = float(input('Введите координату X точки B: '))
dot_b_y = float(input('Введите координату Y точки B: '))

resault = math.sqrt((dot_b_x - dot_a_x) ** 2 + (dot_b_y - dot_a_y) ** 2)
print(f'A({dot_a_x},{dot_a_y}); B({dot_b_x},{dot_b_y}) -> {resault}')