import import_data
import export_data


data = {}

while True:
    print('Добавление нового студента - 1\nДобавление предмета - 2\nДобавление оценки - 3\nПоказать список учеников - 4\nВыход - 0')
    print()
    choice = input('Ваш выбор: ')
    if choice == '1':
        print()
        import_data.add_student(data)
        print()
    if choice == '2':
        print()
        import_data.add_subject(data)
        print()
    if choice == '3':
        print()
        import_data.add_score(data)
        print()
    if choice == '4':
        print()
        export_data.print_list_name_students(data)
        print()
    if choice == '5':
        print()
        export_data.add_score(data)
        print()
    if choice == '6':
        print()
        print(data)
        print()       

    if choice == '0':
        print('Досвидания!\n')
        quit()

    
