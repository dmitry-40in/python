# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# если 0 не считает правильно переделать


number = int(input('Введите десятичное число: '))
list = []
result = ''

if number != 0:
    while number // 2 != 0:
        l = number % 2
        number = number // 2
        list.append(l)
    list.append(1)

    for i in range(len(list) - 1, -1,  -1):
        result += str(list[i])
else:
    result = 0

print(result)
