""" Введение в Pyton: Встроенные функции, переменные, комментарии.
Базовые типы данных: строки, целые и дробные числа"""


# print('Hello world!')
#
# name = 'Jack'
# surname = input('укажите фамилию: ')
# age = 21
# height = 1.75
#
# print(type(age), type(height))
# var1 = 5
# print('Hello,', name)
# print('Hello' + name + surname)
# print('Hello {} {}'.format(name, surname))
# print(f'Hello {name.upper()} {surname}')


chui = int(input('Введите показатель: '))
naryn = int(input('Введите показатель: '))
issyk_kul = int(input('Введите показатель: '))
talas = int(input('Введите показатель: '))
osh = int(input('Введите показатель: '))
dzhal_abad = int(input('Введите показатель: '))
batken = int(input('Введите показатель: '))
average = (chui + naryn + issyk_kul + talas + osh + dzhal_abad + batken) / 7
print('Средний показатель температуры воздуха по КР на сегодня ', round(average, 1), '°C')