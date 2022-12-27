# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


with open('task_035_1.txt') as file:
    polynomial_one = file.readline()

with open('task_035_2.txt') as file:
    polynomial_one += ' + ' + file.readline()

polynomial_one_list = polynomial_one.split(' + ')

multiplier = 0
degree = ''
polynomial_result_list = []
dict_of_polynomial = {}
result = ''

for i in polynomial_one_list:
    if 'x' in i:
        if '*' in i:
            multiplier = int(i[:i.index('*')])
        else:
            multiplier = 1
        if '^' in i:
            degree = i[i.index('^') + 1:]
        else:
            degree = '1'
    else:
        multiplier = int(i)
        degree = '0'

    if degree in dict_of_polynomial:
        dict_of_polynomial[degree] = dict_of_polynomial[degree] + multiplier
    else:
        dict_of_polynomial[degree] = multiplier

for i in dict_of_polynomial:
    if i != '0':
        if i != '1':
            if dict_of_polynomial[i] == 1:
                polynomial_result_list.append('x^' + i)
            else:
                polynomial_result_list.append(
                    str(dict_of_polynomial[i]) + '*x^' + i)
        else:
            if dict_of_polynomial[i] == 1:
                polynomial_result_list.append('x')
            else:
                polynomial_result_list.append(
                    str(dict_of_polynomial[i]) + '*x')
    else:
        polynomial_result_list.append(str(dict_of_polynomial[i]))

result = ' + '.join(polynomial_result_list)

file = open('task_035_result.txt', 'w')
file.write(result)
file.close()
