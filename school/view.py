# Добавление нового студента (Поля - имя, фамилия)
# Добавление предмета (добавляется всем ученикам сразу)
# Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )
# Показ списка учеников (имена фамилия)
# Показ листа оценок конкретного ученика
# Выход из программы


def operation():
    """Выбор операции"""
    print('Добавить студента - 1\nДобавить предмет - 2\nДобавить оценку студенту по предмету - 3\nПоказать список студентов - 4\nПоказать лист оценок конкретного студента - 5\nВыход из программы - 6')
    print()
    action = input('Ваш выбор: ')
    return action


def add_student():
    # """Добавление нового студента (Поля - имя, фамилия)"""
    name = input('Введите имя нового студента: ')
    surname = input('Введите фамилию нового студента: ')
    fullname = name + ' ' + surname
    return fullname


def add_subject():
    """Добавление предмета (добавляется всем ученикам сразу)"""
    subject = input('Введите название нового предмета: ')
    return subject


def get_key_name(students_names):
    """Выбор ключа имени студента"""
    print('Выберите номер студента:')
    for i, name in enumerate(students_names, start=1):
        print(f'{i}. {name}')
    index_name = int(input('Номер: '))
    while index_name > len(students_names) or index_name < 1:
        print('Студента с таким номером не существует.')
        print()
        index_name = int(input('Введите номер студента: '))
    key_name = students_names[index_name - 1]
    print()
    return key_name


def add_mark(subjects, marks):
    """Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )"""
    print('Выберите предмет:')
    for i, subject in enumerate(subjects, start=1):
        print(f'{i}. {subject}')
    index_subject = int(input('Введите номер предмета: '))
    while index_subject > len(subjects) or index_subject < 1:
        print('Предмета с таким номером не существует.')
        print()
        index_subject = int(input('Введите номер предмета: '))
    key_subject = subjects[index_subject - 1]
    print()

    mark = int(input('Введите оценку: '))
    while mark not in marks:
        print('Оценка может примнимать значение: 2, 3, 4, 5')
        mark = int(input('Введите оценку: '))
    return key_subject, mark


def get_name_to_show(students_names):
    """Показ листа оценок конкретного ученика"""
    name = get_key_name(students_names)
    return name
