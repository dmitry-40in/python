def exp_data(data: str = 'phone_book.txt') -> str:
    """На вход получает файл и выводит его строки построчно"""
    print()
    with open(data, 'r') as phone_book:
        for i in phone_book:
            print(i, end = '')
    print()


