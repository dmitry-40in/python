import view

data = {}
students_names = []
subjects = []
marks = (2, 3, 4, 5)


def start():
    while True:
        print()
        print('Выберите операцию:')
        print()
        choice = view.operation()
        print()

        if choice == '1':
            print('Добавляем нового студента.')
            name = view.add_student()
            while name in students_names:
                print('Студент с таким именем уже существует. Придумайте другое имя.')
                name = view.add_student()

            students_names.append(name)
            data[name] = {}
            if subjects:
                for i in subjects:
                    data[name][i] = []

        if choice == '2':
            print('Добавляем новый предмет.')
            subject = view.add_subject()
            for i in students_names:
                data[i][subject] = []
            subjects.append(subject)

        if choice == '3':
            name = view.get_key_name(students_names)
            subject, mark = view.add_mark(subjects, marks)
            data[name][subject].append(mark)

        if choice == '4':
            for i, name in enumerate(students_names, start=1):
                print(f'{i}. {name}')

        if choice == '5':
            name = view.get_name_to_show(students_names)
            print(name, ':')
            for i in data[name]:
                print(f'    {i}:', *data[name][i])

        if choice == '9':
            print('data:', data)
            print('students_name:', students_names)
            print('subjects:', subjects)

        if choice == '6':
            print('Досвидания!')
            quit()
