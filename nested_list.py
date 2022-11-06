students = [['Harry', -37.21], ['Berry', -37.21], ['Tina', -37.2], ['Akriti', -41], ['Harsh', -39]]

students = sorted(students, key=lambda x: (x[1], x[0]))
print(students)
for i in range(len(students) - 1):
    if students[i][1] != students[i + 1][1]:
        a = i + 1
        break
else:
    print("None")

second_grade = [students[a][0]]
for i in range(a, len(students) - 1):
    if students[i][1] == students[i + 1][1]:
        second_grade.append(students[i + 1][0])
    else:
        break

for name in second_grade:
    print(name)

