""" Структуры данных: списки, срезы, кортежи."""

# list - список (изменяемый тип данных)
# tuple - кортеж

# numbers = ((1, 2), (4, 7))
# print(id(numbers))
# numbers += (3, 6, 7)
# print(id(numbers))

# numbers = list(numbers)
# numbers.append(34)
# numbers = tuple(numbers)

# print(numbers)

# weekend_days = ('sunday', 'saturday', 'monday')
#
# for i in weekend_days:
#     if i == 'monday':
#         break
#     print(i)
# else:
#     print('цикл завершен')


# print(weekend_days)
# new = tuple('oop')
# new = tuple('23')
# new = tuple([int(i) for i in new])
# print(new)

# print(type(weekend_days))

# print(type(objects))

# data = [['fuel', 2, 2], ['team', 2, 2]]
#
# for i in data:
#     print(f'word: {i[0]} cons: {i[1]} vow: {i[2]}')

# numbers = ['qwe', 23, 'sdf', 45, 2.5, True, 8.5]
# # numbers = [i for i in numbers if type(i) not in [int, float]]
# numbers = [i*2 for i in numbers]
# print(numbers)

# for i in numbers:
#     print(type(i))



# sogl = 'qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджчсмтьб'
# glas = 'aieouyёуеыаоэяию'
#
# while True:
#     vowels = 0
#     consonants = 0
#     word = input('Введите слово: ').lower()
#     if word == 'exit':
#         break
#     for letter in word:
#         if letter in glas:
#             vowels += 1
#         else:
#             consonants += 1
#     data.append([word, consonants, vowels])
#     print(
#         f'Слово: {word} \n'
#         f'Количество букв: {len(word)} \n'
#         f'Гласных: {vowels} \nСогласных: {consonants}'
#     )
#
# print(data)



# new = list(range(1, 6))

# objects = ['бегайым', "арген", "эльхан", "азамат", "курманжан"]
# new = objects.copy()
#
# print(id(objects))
# print(id(new))
#
# print(objects == new)
# print(objects is new)
#
# print(objects)
# print(new)
# new[0] = 'amir'


"""изменение"""
# new_sorted = sorted(objects)
# print(objects)
# print(new_sorted)
# objects[3], objects[4] = objects[4], objects[3]
# objects.reverse()
# objects = objects[::-1]
# objects[-3] += 3
# objects[3:5] = ['php', 'c++']
# objects[objects.index(13)] = [23, 45, 6]
# objects.sort(key=len, reverse=True)

# print(objects)

"""добавление"""
# objects.append('python')
# objects.insert(4, new)
# objects.extend(new)
# objects += new

"""удаление"""
# del objects[0]
# objects.remove(24)
# objects.remove('python')
# deleted = objects.pop(1)
# print(deleted)
# objects.clear()

# print(objects)
# print(objects[3:6])
# print(objects, new, sep='\n')

