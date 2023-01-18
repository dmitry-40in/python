# 42)Имеется упорядоченный список:

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for index, value in enumerate(list):
#     # print(f'index = {index}, value = {value}')
#     for i, v in enumerate(value):
#         # print(f'index = {index, i}, value = {v}')
#         if index == i:
#             list[index][i] = 0

# print(list)

for index, value in enumerate(list):
    value[index] = 0
print(list)