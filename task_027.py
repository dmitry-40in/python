# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.


number = '  234 -1434 16 -2   0  4   6 478     '

list = []
list_result = []

num = ""

for i in number:
    
    if i != " ":
        num += i
    else:
        list.append(num)
        num = ''
if number[len(number) - 1] != " ":
    list.append(int(num))

for i in range(len(list)):
    if list[i] != "":
        list_result.append(int(list[i]))

min = list_result[0]
max = list_result[0]

for i in range(len(list_result)):
    if min > list_result[i]:
        min = list_result[i]
    if max < list_result[i]:
        max = list_result[i]

print(list_result)
print('min =', min, 'max =', max)



# number = '  234 -1434 16 -2   0  4   6 478     '
# list_num = number.split()
# print(list_num)
# list_num=list(map(int, list_num))
# print(list_num)
# print(max(list_num), min(list_num))

