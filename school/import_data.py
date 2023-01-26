def add_student(dict_journal:dict) -> None:
    """Добавление нового студента (Поля - имя, фамилия)"""

    if dict_journal != {}:
        for i in dict_journal:
            for j in 




        print('Добавляем нового студента в систему.')
        studen_name = input('Введите имя студента: ')
        student_surname = input('Введите фамилию студента: ')
        dict_journal[f'{studen_name} {student_surname}'] = {}
    else:
        print('qwerty')


def add_subject(dict_journal:dict) -> None:
    """Добавление предмета (добавляется всем ученикам сразу)"""

    print('Добавляем новый премет.')
    new_subject = input('Введите название предмета: ')
    if dict_journal == {}:
        print('Невозможно добавить предмет. Предварительно добавьте студента')
    else:
        for i in dict_journal:
            dict_journal[i][new_subject] = []


def get_key_name(dict_journal:dict) -> str:
    """Возвращает ключ ФИ по выбору номера из списка"""

    list_key = []
    for i in dict_journal:
        list_key.append(i)
    for indx, name in enumerate(list_key, start=1):
        print(f'{indx}: {name}')
    index_name = int(input('Выберите номер студента: ')) 
    if index_name < 1 or index_name > len(list_key):
        print('Студента с таким номером не существует.')
    else:
       key_name = list_key[index_name - 1] 
       return key_name


def get_key_subject(dict_journal:dict) -> str:
    """Возвращает ключ предмета ранее выбранного студента по выбору номера из списка"""
    key_name = get_key_name(dict_journal)
    print()

    list_key = []
    for i in dict_journal[key_name]:
        list_key.append(i)
    for indx, name in enumerate(list_key, start=1):
        print(f'{indx}: {name}')
    if list_key == []:
        print('Ни одного предмета не задано.\nПеред выставлением оценки задайте предмет.')
    else:
        index_name = int(input('Выберите номер предмета: '))
        if index_name < 1 or index_name > len(list_key):
            print('Предмета с таким номером не существует.')  
        else:
            key_subject = list_key[index_name - 1]
            return key_subject, key_name
            

def add_score(dict_journal:dict) -> None:
    """Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )"""

    print('Добавляем оценку студенту.')

    key_subject, key_name = get_key_subject(dict_journal)
    print()

    score = int(input('Введите оценку: '))
    if score >= 2 and score <= 5:
        dict_journal[key_name][key_subject].append(score)
    else:
        print('Оценка может быть только: 2, 3, 4, 5.')
    

