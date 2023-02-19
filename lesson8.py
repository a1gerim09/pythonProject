""" Работа с файлами. """
# w - write (перезапись)
# a - add (дозапись)
# x - бесконфликтный режим записи
# r - чтение

from random import choice

# with open('students.txt', 'r') as students:
#     students_list = students.readlines()
#     students_list = [i.rstrip() for i in students_list]
#     with open('materials.txt') as materials:
#         materials_list = materials.readlines()
#         materials_list = [i.rstrip() for i in materials_list]
#         with open('results.txt', 'a') as results:
#             while len(students_list) > 0:
#                 print("осталось студентов", len(students_list))
#                 chosen_student = choice(students_list)
#                 chosen_material = choice(materials_list)
#                 rate = int(input(
#                     f"{chosen_student}\n"
#                     f"тема: {chosen_material}:\n"
#                     f"оценка: "))
#                 results.write(
#                     f"имя: {chosen_student} тема: {chosen_material[:1]} "
#                     f"оценка: {rate}\n")
#                 students_list.remove(chosen_student)










import time

# with open('file.txt', 'r') as file:
    # print(file.readlines()[2])
    # for i in file.readlines():
    #     time.sleep(2)
    #     print(i)
    # for i in file.read():
    #     time.sleep(1)
    #     print(i, end='')

    # file.readline(4)
    # print(file.read())
    # print(file.readlines())

# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('file3.txt', 'x') as file:
#     file.write('\nтретья строка')
#


# w - write (перезапись)
# a - add (дозапись)
# x - бесконфликтный режим записи
# r - чтение


# file = open('file.txt', 'w')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('file2.txt', 'x') as file:
#     file.write('\nвторая строка')

