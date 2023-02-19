from random import randint as generate_number, choice
from person import Person
from calculator import subtraction, addition
from termcolor import colored, cprint
import emoji
from decouple import config

print(generate_number(1, 10))

teacher = Person('Jim', 25)
print(teacher.full_name + ' ' + str(teacher.age))

print(addition(8, 2))
cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
num = config('COMMENTED', default=0, cast=int)
print(num * 2)
# Hi my dear students