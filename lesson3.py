""" Циклы  For, While """
# i - item, iterable

eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
rus = "йцукенгшщзхъфывапролджэячсмитьбю "

while True:
    word = input('\nвведите слово: ').lower()
    if word == 'exit' or word == 'учше':
        break
    for letter in word:
        if letter in eng:
            print(rus[eng.index(letter)], end='')
        else:
            print(eng[rus.index(letter)], end='')


# ghbdtn
# пщщвигн
# иулyfpfh


# cash = 100
# years = 5
# percents = 0.05
#
# for year in range(1, years+1):
#     cash += cash * percents
#     print(f'год: {year} {cash}')


# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             print(i, j, k)

# for number in range(1, 11):
#     if number % 2 != 0:
#         print(number)

# word = "geektech"
#
# for letter in word:
#     if letter == 't':
#         continue
#     print(letter)


# word = "трактор синий"
# c = 0
#
# while c != len(word):
#     print(word[c])
#     c += 1


# rounds = 0
#
# while rounds != 5:
#     rounds += 1
#     if rounds == 3:
#         continue
#     print(f'круги: {rounds}')


# from time import sleep
# amount = int(input('сколько раз будем повторять код? '))
#
# attempts = 3
#
# while attempts != 0:
#     time = input(f'введите время суток: \nосталось попыток {attempts}: ')
#
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print("hello, i don't know time!")
#         attempts -= 1
#         if attempts == 0:
#             seconds = 20
#             while seconds != 0:
#                 print(seconds)
#                 sleep(1)
#                 seconds -= 1
#             attempts = 3


# c = 0
# while c != 100:
#     c += 1
#     if c % 2 != 0:
#         print('мы пропустили нечетное число')
#         continue
#     print('hello', c)

# number = 0
#
# for number in range(10):
#     if number == 5:
#         break    # break here
#
#     print('Number is ' + str(number))
#
# print('Out of loop')
