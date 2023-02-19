class Person:
    def __init__(self, full_name, age):
        self.__full_name = full_name
        self.__age = age

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age

if __name__ == '__main__':
    student = Person('Argen', 20)
    print(student.full_name + ' ' + str(student.age))