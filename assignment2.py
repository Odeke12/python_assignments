students = []

print("Enter the names of the students to register")
print("Enter q to stop entering the names")

#Add students till the user enters q to quit
while True:
    name = input("Enter name : ")
    students.append(name)
    if name == "q":
        break

print("Names of students")
for name in students:
    print(name)