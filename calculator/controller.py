from sum import summation
from subtraction import subtraction
from multiplication import multi
from div import division
from division_int import division_intiger
from div_remainder import remainder_div


from view import choice_the_type_of_numbers

from view import entering_int_numbers
from view import entering_complex_numbers
from view import mathematical_operation
from view import print_result

def calc() -> None:
    """Калькулятор для действительных и комплексных чисел"""
    if choice_the_type_of_numbers():
        a, b = entering_int_numbers()
        c = mathematical_operation()
        if c == '+':
            d = summation(a, b)
        if c == '-':
            d = subtraction(a, b)
        if c == '*':
            d = multi(a, b)
        if c == '/':
            d = division(a, b)      
        if c ==  '//':
            d = division_intiger(a, b)        
        if c == '%':
            d = remainder_div(a, b)    
        print_result(str(a), str(b), c, str(d))
    else:
        a, b = entering_complex_numbers()
        c = mathematical_operation()
        if c == '+':
            d = summation(a, b)
        if c == '-':
            d = subtraction(a, b)
        if c == '*':
            d = multi(a, b)
        if c == '/':
            d = division(a, b)      
        if c ==  '//':
            print('Недопустимая операция над комплексными числами')
            quit()       
        if c == '%':
            print('Недопустимая операция над комплексными числами')
            quit() 
        print_result(str(a), str(b), c, str(d))
#calc()