# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


initial_list = [8, 5, 2, 3, 4, 6, 1, 7]

list_result = []
flag = False

for i in range(len(initial_list) - 1):
    for j in range(i + 1, len(initial_list)):
        if initial_list[i] < initial_list[j]:
            first_index = i
            second_index = j
            flag = True
            break
    if flag == True:
        break

list_result.append(initial_list[first_index])
list_result.append(initial_list[second_index])

for i in range(second_index + 1, len(initial_list)):
    if initial_list[i] > list_result[-1]: # почему только такая запись получилась внутри range()
        list_result.append(initial_list[i])

print(list_result)