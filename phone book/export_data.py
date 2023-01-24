def exp_data(data: str = 'phone_book.txt') -> None:
    """На вход получает файл и выводит его строки построчно"""
    print()
    with open(data, 'r') as phone_book:
        for i in phone_book.readlines():
            print(i, end = '')
    print()

# print(type(exp_data()))

def exp_name_and_surname(data: str = 'phone_book.txt') -> None:
    """Выводит только имя и фамилию потрочно"""
    with open(data, 'r') as phone_book:
        list = phone_book.readlines()
        # print(list)
    print()
    for i in list:
        # print(i)
        cont = i.split('|')
        # print(cont)
        # print(list)
        print(f'Name = {cont[1]}, surname = {cont[2]}')
    print()


def sorting_by_name(data: str = 'phone_book.txt') -> None:
    """Сортирует справочник по именам и перезраписывает его с отсортированными по именам строками"""
    with open(data, 'r') as phone_book:
        list = phone_book.readlines()
        list_of_list_cont = [] # что будет если уже тут убрать табуляцию выйти из with open() - ничего, ниже попробовал
        for i in list:
            cont = i.split('|')
            list_of_list_cont.append(cont)
        list_of_list_cont = sorted(list_of_list_cont, key = lambda i: i[1])
        # print(list_of_list_cont)
        data_string = ''
        for i in list_of_list_cont:
            cont = '|'.join(i)
            # print(cont)
            data_string += cont
        # print(data_string)
    with open(data, 'w') as phone_book:
        phone_book.write(data_string)
# sorting_by_name()


def sorting_by_id(data: str = 'phone_book.txt') -> None:
    """Сортирует справочник по id и перезраписывает его с отсортированными по именам строками"""
    with open(data, 'r') as phone_book:
        list = phone_book.readlines()
    list_of_list_cont = [] 
    for i in list:
        cont = i.split('|')
        list_of_list_cont.append(cont)
    list_of_list_cont = sorted(list_of_list_cont, key = lambda i: i[0])
    data_string = ''
    for i in list_of_list_cont:
        cont = '|'.join(i)
        data_string += cont
    with open(data, 'w') as phone_book:
        phone_book.write(data_string)
        