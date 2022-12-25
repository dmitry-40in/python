# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

a = 1
b = -3
c = -4

d = b**2 - 4 * a * c

if d > 0:
    x1 = ((-1) * b + pow(d, 0.5)) / 2 * a
    x2 = ((-1) * b - pow(d, 0.5)) / 2 * a
    print('x1 =', x1, 'x2 =', x2)
elif d == 0:
    x = (-1) * b / 2 * a
    print('x =', x)
else:
    print('нет корней')


# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4*a*c
# if d<0:
# print("корней нет")
# elif d == 0:
# x = (-1)*b/2*a
# print(x)
#
# else:
# x1 = (-b + math.sqrt(d))/2*a,2
# x2 = (-b - math.sqrt(d))/2*a
# print(x1,x2)