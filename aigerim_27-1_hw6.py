# функция “Перемножение чисел”

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_numbers(2, 3, 4, 5))


# Функция “Зеркальная строка” (вариант1)

def palindrome(string, *args):
    if string == string[::-1]:
        return True
    else:
        return False
print(palindrome(input()))


# Функция “Зеркальная строка” (вариант2)

def is_palindrome(string, optional_string = 'hello'):
    if string == string[::-1]:
        return True
    else:
        return False
print(is_palindrome('hello'))
print(is_palindrome('madam'))


# Функция “Калькулятор”

def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '-/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return 'invalid operator'
print(calculator((int(input('Введите первое число: '))),
                 (input('Введите оператор: ')),
                 int(input('Введите второе число: '))))

