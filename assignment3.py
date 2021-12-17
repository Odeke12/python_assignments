students = {
    "Odeke": "",
    "Trevor":"",
    "Alice":""
}

#add values to the keys
for x in students:
    students[x] = input(f"Add registration number of {x} :")

#Display students
for x in students:
    print(f"{x} : {students[x]}")

