# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]



# a = [i for i in range(1, 10) if i%2==0]
# print(a)

# a = [12, 22, 32, 42, 25, 26, 27]
# for index, value in enumerate(a):
#     print(f'index = {index}, value = {value}')

# day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# result = list(zip(month, day))
# print(result)

# result = lambda a,b : a + b ## def result(a, b): return a + b
# print(result(10, 1))

# list_a = [1, 2, 3, 4, 5]
# print(list_a)
# list_a = list(map((lambda a: a**a), list_a))
# print(list_a)

# list_b = [5, 22, 7, 1, 0, - 22, 342]
# # result = list(filter(lambda i: i <= 1, list_b))
# # print(result)
# result = sorted(list_b, key=lambda i: i)
# print(result)


list_one = [1, 2, 3, 5, 7, 8, 9, 10]
list_two = [1, 2, 4, 8, 9]

result = list(filter(lambda i: i in list_one, list_two))

print(result)
