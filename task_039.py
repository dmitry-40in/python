# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать,
#               чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

import random
import time

amount_of_candy = 221

player_turn = random.randint(1, 2)

take_some_candies = 0

player_one_number_of_candies = 0
player_two_number_of_candies = 0

while amount_of_candy != 0:
    if player_turn % 2 == 1:
        print('Ход первого игрока')
        print('Сейчас в куче конфет:', amount_of_candy)
        take_some_candies = int(input('Сколько конфет возьмешь? '))
        if amount_of_candy < 28:
            while take_some_candies > amount_of_candy or take_some_candies < 1:
                print(f'Можно взять от 1 до {amount_of_candy} конфет')
                take_some_candies = int(input('Сколько конфет возьмешь? '))

        else:
            while take_some_candies > 28 or take_some_candies < 1:
                print('Можно взять от 1 до 28 конфет')
                take_some_candies = int(input('Сколько конфет возьмешь? '))

        player_one_number_of_candies += take_some_candies
        amount_of_candy -= take_some_candies
        take_some_candies = 0
        player_turn = player_turn % 2 + 1
        print('У тебя всего конфет:', player_one_number_of_candies)
        print('В куче осталось конфет:', amount_of_candy)
        print()

    else:
        print('Ход второго игрока')
        print('Сейчас в куче конфет:', amount_of_candy)
        take_some_candies = int(input('Сколько конфет возьмешь? '))
        if amount_of_candy < 28:
            while take_some_candies > amount_of_candy or take_some_candies < 1:
                print(f'Можно взять от 1 до {amount_of_candy} конфет')
                take_some_candies = int(input('Сколько конфет возьмешь? '))

        else:
            while take_some_candies > 28 or take_some_candies < 1:
                print('Можно взять от 1 до 28 конфет')
                take_some_candies = int(input('Сколько конфет возьмешь? '))

        player_two_number_of_candies += take_some_candies
        amount_of_candy -= take_some_candies
        take_some_candies = 0
        player_turn = player_turn % 2 + 1
        print('У тебя всего конфет:', player_two_number_of_candies)
        print('В куче осталось конфет:', amount_of_candy)
        print()

if player_turn % 2 == 0:
    print(
        f'Победил первый игрок. Собрал конфет: {player_one_number_of_candies}')
else:
    print(
        f'Победил второй игрок. Собрал конфет: {player_two_number_of_candies}')
