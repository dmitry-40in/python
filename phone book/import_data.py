def imp_data() -> str:
    """Модуль ввода данных"""
    id = int(input('Введите id контакта: '))
    name = input('Введите имя контакта: ')
    surname = input('Введите фамилию контакта: ')
    phone_number = input('Введите номер телефона контакта: ')
    comment = input('Введите комментарий к контакту: ')
    result = str(id) + '|' + name + '|' + surname + '|' + phone_number + '|' + comment + '\n'
    return result
# print(imp_data())


def save_data(contact: str, data = 'phone_book.txt') -> None:
    """На вход получает строку с данными контакта и сохраняет ее в файл дополнительной строкой"""
    with open (data, 'a') as add_contact:
        add_contact.write(contact)
    print('Контакт сохранен')
