""" Логический тип данных, условные операторы"""

# time = 'day'
#
# if time == 'morning':
#     print('good morning')
#
# elif time == 'day':
#     print('good afternoon')
#
# elif time == 'evening':
#     print('good evening')
#
# else:
#     print('hello')


# word = 'geektech'
# print(word.isalpha())
# print(word.isnumeric())


# [start:stop:step]
# word = '123456789'
# first = int(word[:2])
# second = int(word[-2:])
# print(first + second)

# word = input('введите слово:').lower()
# reversed_word = word[::-1]
#
# if word ==reversed_word:
#     print(True)
# else:
#     print(f' {word} не равно обратному слову {reversed_word}')

login = 'aza@mail.ru'
password = 'qwer12'
input_login = input('укажите логин: ')
input_password = input('укажите пароль: ')
# if input_login == login:
#     print('логин верный')
#     if input_password == password:
#         print('пароль верный')
# else:
#     print('вы не прошли авторизацию')
# print('Вы успешно прошли авторизацию')
if input_login == login:
    input_password == input(f'логин верный \n укажите пароль для {input_login}: ')
    if input_password == password:
        input_password2 = input('подтвердите пароль: ')
        



