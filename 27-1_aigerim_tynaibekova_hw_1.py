class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname}, Age: {self.age}, '
               f'Is_married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = 0.05 * (self.experience - 3) * self.salary
        return self.salary + bonus


teacher_info = Teacher('Timur Kim', 40, 'Single', 10, 80000)
teacher_info.introduce_myself()
salary = teacher_info.calculate_salary()
print(f"Teacher's salary: {salary}")


def create_students():
    students = []
    student_1 = Student('Alina Tilekova', 20, 'Single', {"math": 85, "english": 80, "geography": 85})
    student_2 = Student('Murat Radjapov', 23, 'Married', {"math": 70, "english": 85, "geography": 80})
    student_3 = Student('Aibek Asanaliev', 22, 'Single', {"math": 90, "english": 60, "geography": 90})
    students.extend([student_1, student_2, student_3])
    return students


students = create_students()
for student in students:
    student.introduce_myself()
    print(f"{student.fullname} marks: {student.marks}")
    print(f"{student.fullname} average mark: {student.average_mark()}")




