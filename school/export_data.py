import import_data


def print_list_name_students(dict_journal:dict) -> None:
    """Показ списка учеников (имена фамилия)"""

    print('Список учеников:')
    j = 1
    for i in dict_journal:
        print(f'{j}. {i}')
        j+= 1


def add_score(dict_journal:dict) -> None:
    """Показ листа оценок конкретного ученика"""

    print('Лист оценок конкретного ученика')
    key_name = import_data.get_key_name(dict_journal)
    print()
    print(f'Лист оценок {key_name}:')
    for i in dict_journal[key_name]:
        print(f'{i}:',*dict_journal[key_name][i])
    