birthday = int(input('Введите день рождения: '))
month = (input('Введите месяц рождения: ')).lower()

if (21 <= birthday <= 31 and month == 'март') or (1 <= birthday <= 20 and month == 'апрель'):
    print('Ваш знак зодиака: Овен')
elif (21 <= birthday <= 30 and month == 'апрель') or (1 <= birthday <= 21 and month == 'май'):
    print('Ваш знак зодиака: Телец')
elif (22 <= birthday <= 31 and month == 'май') or (1 <= birthday <= 21 and month == 'июнь'):
    print('Ваш знак зодиака: Близнецы')
elif (22 <= birthday <= 30 and month == 'июнь') or (1 <= birthday <= 22 and month == 'июль'):
    print('Ваш знак зодиака: Рак')
elif (23 <= birthday <= 31 and month == 'июль') or (1 <= birthday <= 21 and month == 'август'):
    print('Ваш знак зодиака: Лев')
elif (22 <= birthday <= 31 and month == 'август') or (1 <= birthday <= 23 and month == 'сентябрь'):
    print('Ваш знак зодиака: Дева')
elif (24 <= birthday <= 30 and month == 'сентябрь') or (1 <= birthday <= 23 and month == 'октябрь'):
    print('Ваш знак зодиака: Весы')
elif (24 <= birthday <= 31 and month == 'октябрь') or (1 <= birthday <= 22 and month == 'ноябрь'):
    print('Ваш знак зодиака: Скорпион')
elif (23 <= birthday <= 30 and month == 'ноябрь') or (1 <= birthday <= 22 and month == 'декабрь'):
    print('Ваш знак зодиака: Стрелец')
elif (23 <= birthday <= 31 and month == 'декабрь') or (1 <= birthday <= 20 and month == 'январь'):
    print('Ваш знак зодиака: Козерог')
elif (21 <= birthday <= 31 and month == 'январь') or (1 <= birthd26ay <= 19 and month == 'февраль'):
    print('Ваш знак зодиака: Водолей')
elif (20 <= birthday <= 29 and month == 'февраль') or (1 <= birthday <= 20 and month == 'март'):
    print('Ваш знак зодиака: Рыбы')
else:
    print('Не верный формат заполения, смотрите пример.'   # перед вводом будет пример/формат ввода данных
          '\n 1) в месяце только 30 дней;'
          '\n 2) в феврале только 29 дней;'
          '\n 3) месяц писать только латинскими буквами.')

