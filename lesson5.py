"""Структуры данных: словари, множества."""
# dict - dictionary (словарь) изменяемый тип данных
# set - множество (изменяемый тип данных)
# print(type(student))
# {key: value}
# [object for loop condition]

# print(set('programming'))

# lagman = {"лапша", "мясо", "перец"}
# manty = {"мясо", "тесто", "лук"}
#
# print(lagman.union(manty))
# print(lagman | manty)
#
# print(lagman.intersection(manty))
# print(lagman & manty)
#
# print(lagman.difference(manty))
# print(lagman - manty)
#
# print(lagman.symmetric_difference(manty))
# print(lagman ^ manty)

# numbers1 = set([1, 2, 3, 2, 1, 4, 3])
# numbers2 = {1, 2, 3, 2, 1, 4, 3}
#
# numbers2.add(2)
# numbers2.remove(4)
#
# print(numbers2)

# print(numbers1)
# print(type(numbers2))

# data = ['cola', 'lays', 'cola', 'pepsi', 'lays', 'lays', 'lays', 'cola']
#
# res = {i: i for i in data}
# print(res)
# print(max(data, key=data.count))


# res = {i: data.count(i) for i in data}
# print(res)

# often = max(res.values())
# for i in data:
#     if data.count(i) == often:
#         often = i
# print(often)

# print(data)
# print(max(res.values()))
# print(data[max(res.values())])

# item = '{name}: {price} * {amount} = 50000'
# print(int(item.split()[-1]))

# from datetime import datetime
#
# data = {
#     'cola': 42,
#     'snickers': 55,
#     'bounty': 60,
#     'lays': 120
# }
#
# result = []
# bill = 0
#
# for name, price in data.items():
#     amount = int(input(f'укажите количество {name} ({price}): '))
#     sum_item = price * amount
#     result.append(f'{name}: {price} * {amount} = {sum_item}')
#     bill += int(result[-1].split()[-1])
#
# result.extend([bill, str(datetime.now())])
#
# for i in result:
#     print(i)


# sum, min, max, abs
# print(min([23, 0.1, 12, 34, 17, 0.4]))
# print(max((23, 0.1, 12, 34, 17, 0.4)))
# print(sum(range(1, 51)))

# regions = ["чуй", "ош", "нарын", "ыссык-куль", "джалал-абад", "талас", "баткен"]
# data = {i: int(input(f'введите температуру в {i.title()}')) for i in regions}
# sum_temps = sum(data.values())
# amount = len(regions)
# print(round(sum_temps / amount, 2))
# print(data)

# new = dict(enumerate('python'))
# new = dict([['one', 1], ['two', 2]])
# print(new)
# new = dict(name='donald', age=19, country='usa')
#
#
# student = {
#     'name': 'jack',
#     'age': 20,
#     'weight': 65.7,
#     'hobby': ['chess', 'english', 'books'],
#     'sex': 'male',
# }
#
# # print(student['nam'])
# print(student.get('name', 'нет такого ключа'))



# for k, v in student.items():
#     print(f'{k} >> {v}')

# for i in student:
#     print(f'{i}: {student[i]}')

# print(student.keys())
# print(student.values())
# print(student.items())

"""delete"""
# del student['hobby'][-1]
# deleted = student.pop('weight')
# del student['hobby']
# print(deleted)
# new['weight'] = deleted

"""edit"""
# student['sex'] = 'female'
# student['hobby'][0] = 'football'
# student['age'] += 1

"""add"""
# student['car'] = True
# student['hobby'].append('boxing')
# student.update(new)


""" Структуры данных: словари, множества"""

# data = {
#     'cola': 42,
#     'snickers': 55,
#     'bounty': 60,
#     'lays': 120
# }
# bill = 0
# result = []
#
# for name, price in data.items():
#     amount = int(input('укажите количество '))

data = ['cola', 'lays', 'twix', 'cola', 'mars', 'cola']
print(max(data, key=data.count))
