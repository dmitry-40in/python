# 39(2). Создайте программу для игры в ""Крестики-нолики"".
# Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка,
# внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9),
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу
# ( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

import random

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wins_index = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
    0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def win_check(a, b):
    for i in b:
        if a[i[0]] == a[i[1]] == a[i[2]]:
            check = True
            break
        else:
            check = False
    return check


def no_turn_check(y):
    for i in y:
        if type(i) == int:
            check = False
            break
        else:
            check = True
    return check


def print_field(x):
    print()
    # как это работает, особенно * перед [] и зачем в список превращать?
    print(*[i for i in x[0:3]])
    print(*[i for i in x[3:6]])
    print(*[i for i in x[6:9]])
    print()


print_field(field)

player_one = 'Первый игрок (ходит "Х")'
player_two = 'Второй игрок (ходит "O")'
current_player = random.choice([player_one, player_two])

game_over = False

while not game_over:
    if current_player == player_one:
        symbol = 'X'
        number = int(input(f'{player_one}, введи номер клетки для хода: '))
        while field[number - 1] == 'X' or field[number - 1] == 'O':  # зачем использовать continue?
            number = int(input('Клетка занята, выбери другую клетку: '))
        field[number - 1] = symbol
    else:
        symbol = 'O'
        number = int(input(f'{player_two}, введи номер клетки для хода: '))
        while field[number - 1] == 'X' or field[number - 1] == 'O':
            number = int(input('Клетка занята, выбери другую клетку: '))
        field[number - 1] = symbol
    print_field(field)
    current_player = player_one if current_player == player_two else player_two

    game_over = win_check(field, wins_index)  # + no_turn_check(field)

current_player = player_one if current_player == player_two else player_two
print(f'Победитель - {current_player}')
