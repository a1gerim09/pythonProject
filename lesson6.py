""" Функции, аргументы: *args, **kwargs."""

# DRY - don't repeat yourself

# print(len('123')+7)



# def max1(iterable):
#     iterable = sorted(iterable)
#     return iterable[-1]
#
# print(max1([11, 4, 7, 9]))



# def max1(iterable):
#     max_value = 0
#     for i in iterable:
#         if i > max_value:
#             max_value = i
#     return max_value
#
# print(max1([3, 7, 2, 3, 9]))




# def len1(iterable):
#     counter = 0
#     for _ in iterable:  # _ когда временная переменная не используется
#         counter += 1
#     return counter
#
# print(len('123') +7)
# print(len1('123') +7)

# def show_object(name, surname):  # name - required positional argument
#     print('name:', name, 'surname:', surname)# surname - not required positional
#
# show_object('peter', 'parker') # peter - required positional argument
# show_object(surname='lee', name='bruce') # keyword argument

# def get_square(width: int, lenght: int)-> int:
#     """ Принимает 2 числа (ширина, длина), возвращает площадь прямоугольника"""
#     return width * length
# print(get_square().__doc__)


# def plus(*args):
#     print(type(args))
#     return sum(args)
#
# print(plus(2, 2, 4, 5, 9))
#
# def calculate1(num1, operator, num2):
#     if operator == '-':
#         return num1 - num2
#     elif operator == '+':
#         return num1 + num2
# print(calculate1(5, '+', 9))
# print(calculate1(5, '-', 9))


contacts = {
    'sam': '0500100200',
    'aza': '0700223311',
    'uri': '0555788877'
}

def new_contact(name, phone):
    if name not in contacts.keys():
        contacts[name] = phone
    else:
        contacts[name] = {contacts[name]}
        contacts[name].add(phone)
def delete(name):
    if name in contacts.keys():
        del contacts[name]
    else:
        print(f'нет такого контакта {name}')

delete('sam')
print(contacts)
# new_contact('rita', '055756465')
# new_contact('aza', '0555265465')
# print(contacts)