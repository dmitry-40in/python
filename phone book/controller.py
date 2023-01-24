import import_data
import export_data


def start() -> None:
    """Запускает работу телефонного справочника"""
    choice = input('Для добавления контакта введите 1\nДля вывода списка контактов введите 2\nДля выхода введите 3\nВаш выбор: ')
    while choice != '1' and choice != '2' and choice != '3':
        choice = input('Для добавления контакта введите 1\nДля вывода списка контактов введите 2\nДля выхода введите 3\nВаш выбор: ')
    if choice == '1':
        import_data.save_data(import_data.imp_data())
    if choice == '2':
        export_data.exp_data()
    else: 
        quit()


start()
# import_data.save_data(import_data.imp_data())

# export_data.exp_data()2
