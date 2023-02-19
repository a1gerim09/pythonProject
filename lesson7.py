""" lambda, и работа с исключениями """

# lambda arguments: expression
# try:
#     some code
# except:
#     some code
# finally:
#     some code

from random import choice
from time import sleep

students = ['kurmanzhan', 'argen', 'azamat', 'aigerim']
data = {}

while len(students) != 0:
    seconds = 20
    print(students)
    chosen = choice(students)
    name = input(f'отвечает: {chosen}: ')
    # while seconds != 0:
    #     print(seconds)
    #     sleep(1)
    #     seconds -= 1
    try:
        rate = int(input(f'rate for {chosen}'))
        # if rate < 0 or rate > 5:
        #     raise ValueError("Invalid input. Please enter a rate between 0 and 10.")
    except ValueError:
            print('Такой оценки нет. Введите число от 1 до 5')

    data[chosen] = rate
    students.remove(chosen)

for name, rate in data.items():
    print(name, ":", rate)

print(sum(data.values()) / len(data))

# word = 'python'
# while True:
#     try:
#         ind = int(input('введите индекс: '))
#         print(word[ind])
#     except IndexError:
#         print('неверный индекс, такого нет')
#     except ValueError:
#         print('вводить только числа')

# name = 'aza'
#
# try:
#     print(name)
# except:
#     print('такой переменной нет')
# finally:
#     print('проверка завершена')


# print(int('dfg'))
# print('123'[5])
# print(10/0)
# print(23 + '23')


# plus = lambda number1, number2: number1 + number2
#
#
# def plus_d(n1, n2):
#     return n1 + n2

# print(type(plus))
# print(type(plus_d))

# print(plus(2, 3))
# print(plus_d(3, 2))


# list_numbers = [2, 1, 4, 5, 1, 4, 4]
#
# def most_frequence(iterable):
#     return sorted(iterable, key=iterable.count)
#
# print(most_frequence(list_numbers))

#     most_f = 0
#     for i in iterable:
#         if iterable.count(i) > most_f:
#             most_f = i
#
#     return f"объект: {most_f} найдено: {iterable.count(most_f)}"  #{most_f: iterable.count(most_f)}

# map, filter

# dct = {
#     'one': 1,
#     'three': 3,
#     'seven': 7,
#     'two': 2
# }
#
# print(dct)
# sort_dict = dict(sorted(dct.items(), key=lambda item: item[1]))
# print(sort_dict)

# numbers = list(range(1, 16))
# print(numbers)

# filtered = list(filter(lambda x: x % 2 == 0, numbers))
# filtered = [i for i in numbers if i > 7]
# print(filtered)

# mapped = tuple(map(lambda x: x**2, numbers))
# mapped = [i*3 for i in numbers]
# print(mapped)


# def show_words(iterable, func):
#     for i in iterable:
#         print(func(i))
#
#
# # def up_letter(word: str):
# #     return word.title()
#
# words = ['python', 'bishkek', 'kyrgyzstan']
#
# show_words(words, lambda word: word.upper())


# show_words(str.upper, words)
# show_words(words, up_letter)


# list_numbers = ['apple', 'banana', 'apple', 'melon']

# def max_num(list_numbers):
#     return max(list_numbers, key=list_numbers.count)
# print(max_num(list_numbers))

# list_numbers = [2, 1, 4, 5, 1, 4, 4]
#
# def most_frequence(iterable):
#     most_f = 0
#     for i in iterable:
#         if iterable.count(i) > most_f:
#             most_f = i
#     return {most_f: iterable.count(most_f)}
# print(most_frequence(list_numbers))
