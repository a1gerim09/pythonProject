import operator
# file = open('results.txt', 'r')


# Step 1: Read data from file
data = {}
with open("results.txt", "r") as f:
    for line in f:
        name, grade = line.strip().split(",")
        data[name] = int(grade)

# # Step 2: Create dictionary
student_grades = {}
for name, grade in data.items():
    student_name, student_surname = name.split(" ")
    student_grades[f"{student_name} {student_surname}"] = grade
#
# Step 3: Sort dictionary by value in descending order
sorted_grades = dict(sorted(student_grades.items(), key=operator.itemgetter(1), reverse=True))

# Step 4: Print top 3 students
top_3 = {k: sorted_grades[k] for k in list(sorted_grades)[:3]}
for student, grade in top_3.items():
    print(f"{student} - {grade}")

# Step 5: Create new text file
with open("sorted_results.txt", "w") as f:
    for student, grade in sorted_grades.items():
        f.write(f"{student}, {grade}\n")

# Step 6: Print contents of new text file
with open("sorted_results.txt", "r") as f:
    print(f.read())