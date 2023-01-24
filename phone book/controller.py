import import_data, export_data


def start() -> None:
    """Запускает работу телефонного справочника"""
    choice = input('\
Для добавления контакта введите 1\n\
Для вывода списка контактов введите 2\n\
Для вывод только имени и фамилии введите 3\n\
Чтобы отсортировать по имени введите 4\n\
Чтобы отсортировать по id введите 5\n\
Для выхода введите 6\n\
Ваш выбор: \
')
    while choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6':
        choice = input('\
Для добавления контакта введите 1\n\
Для вывода списка контактов введите 2\n\
Для вывод только имени и фамилии введите 3\n\
Чтобы отсортировать по имени введите 4\n\
Чтобы отсортировать по id введите 5\n\
Для выхода введите 6\n\
Ваш выбор: \
')
    if choice == '1':
        import_data.save_data(import_data.imp_data())
    if choice == '2':
        export_data.exp_data()
    if choice == '3':
        export_data.exp_name_and_surname()
    if choice == '4':
        export_data.sorting_by_name()
    if choice == '5':
        export_data.sorting_by_id()
    else: 
        quit()
