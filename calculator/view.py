def choice_the_type_of_numbers() -> bool:
    """Выбор вида чисел с которыми работаем"""
    type_of_numbers = int(input('Введите "1" если работаем с действительными числами и "0" если работаем с комплексными числами: '))
    while type_of_numbers != 1 and type_of_numbers != 0:
       type_of_numbers = int(input('Введите "1" если работаем с действительными числами и "0" если работаем с комплексными числами: '))

    if type_of_numbers == 1:
        return True
    if type_of_numbers == 0:
        return False 
# print(choice_the_type_of_numbers())


def entering_int_numbers() -> int:
    """Ввод двух действительных чисел"""
    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))
    return number_one, number_two   
# a, b = entering_int_numbers()
# print(a)
# print(b)


def entering_complex_numbers() -> complex:
    """Ввод двух комплексных чисел"""
    number_one = complex(input('Введите первое число: '))
    number_two = complex(input('Введите второе число: '))
    return number_one, number_two
# a, b = entering_complex_numbers()
# print(a)
# print(b)
    

def mathematical_operation() -> str:
    """Ввод математической операции: +, -, *, /, //, %"""
    oper_list = ('+', '-', '*', '/', '//', '%')
    operation = str(input('Введите математическую операцию (+, -, *, /, //, %): '))
    while operation not in oper_list:
        operation = str(input('Введите математическую операцию (+, -, *, /, //, %): '))
    return operation
#print(mathematical_operation())

def print_result(numb_1: str, numb_2: str, oper: str, res: str):
    """Выводит строку с числами, операцияей и значение"""
    print()
    print(numb_1, oper, numb_2, '=', res)
    print()
#print_result('1', '2', '+', '3')
