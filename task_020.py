# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = ['a', 'b', 'c', 1, 2, 3, 101]

for i in list:
    if type(i) == int:
        print(list.index(i))



print()

list_2 = ['qwe', 'qwead', '12']

for i in list_2:
    if i.isdigit():
        print(list_2.index(i))

