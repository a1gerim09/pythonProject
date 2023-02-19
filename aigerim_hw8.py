with open("results.txt", "r") as f:
    print(f.read())
students = {}
with open("results.txt") as file:
    onstring = file.read().split("\n")[:-1]
for item in onstring:
    key = item.split()[1]
    value = item.split(" ")[-1]
    students[key] = value
file.close()
# print(students)
sort = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
top = dict(list(sort.items())[:3])
with open("sorted_results.txt", "w") as f:
    for i in top:
        f.write(f"{i}\n")

print(top)
