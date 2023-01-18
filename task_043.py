# 43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip,filter,lambda

import random

# list_id = list(random.randint(1, 100) for i in range(10)) # random генерирует и повторяющиеся элменты. 
# Чтобы случайные элементы не повторялись используем random.sample - выбираем из сгенерированных послеовательно range(1,11) 10 неповторяющихся элементов
list_id = random.sample(range(1, 101), 10)


#list_name = list(input('Введите имя струдника: ') for i in range(1, 11))
list_name = ['wew','qwdqwd','qwdd','regtew','wefq','wqeh','cwcwq','rgwt','qecqe','cqwerg']

print(list_id)
print(list_name)

list_zip = list(zip(list_id, list_name))
print(list_zip)
print()

list_sorted = list(sorted(list_zip, key = lambda i: i[0]))
print(list_sorted)
print()

list_odd = list(filter(lambda x:x[0]%2, list_sorted))
print(list_odd)

name_list = list(map(lambda x:x[1], list_odd))
print(name_list)