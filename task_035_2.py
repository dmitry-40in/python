# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('task_035_1_classwork.txt') as file_of_n_natural_numbers:
    row_n = file_of_n_natural_numbers.readline()

print(row_n)

row_n = row_n.split() # наверное тут для преобразования в int можно ипользовать map()
print(row_n)

for i in range(len(row_n)):
    row_n[i] = int(row_n[i])

print(row_n)

for i in range(1, len(row_n)):
    if row_n[i] - 1 != row_n[i - 1]:
        print(f'пропущенное число {row_n[i] - 1}')
        exit()
