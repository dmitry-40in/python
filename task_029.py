# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = 6
b = 4

# for i in range(1, a*b):
#     if i%a==0 and i%b==0:
#         print(i)
#         break

for i in range(max(a, b), a*b, max(a, b)):
    print(i)
    if i%a==0 and i%b==0:
        print(i)
        break

