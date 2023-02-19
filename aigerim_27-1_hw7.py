ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))

print(list(map(lambda x: x ** 2, evens)))


def list_by_index(lst=ten):
    while True:
        try:
            idx = int(input('Введите индекс числа (для выхода введите - 11): '))
            if idx == 11:
                break
            print(lst[idx])
        except ValueError:
            print('Недопустимый ввод. Введите только цифры.')
        except IndexError:
            print('Такого индекса нет. Введите индекс от 0 до', len(lst) - 1)


list_by_index()
