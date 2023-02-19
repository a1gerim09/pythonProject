from random import choice
from time import sleep

students = ['kurmanzhan', 'argen', 'azamat', 'aigerim']
data = {}

while len(students) != 0:
    seconds = 20
    print(students)
    chosen = choice(students)
    name = input(f'отвечает: {chosen}: ')
    while seconds != 0:
        print(seconds)
        sleep(1)
        seconds -= 1
    try:
        rate = int(input(f'rate for {chosen}: '))
        if rate < 1 or rate > 5:
            raise ValueError('Недопустимая оценка. Введите оценку от 1 до 5')
    except ValueError as e:
        print(e)
        continue
    except Exception:
        print('Недопустимый ввод. Введите допустимое число.')
        continue
    data[chosen] = rate
    students.remove(chosen)

for name, rate in data.items():
    print(name, ":", rate)

print(sum(data.values()) / len(data))