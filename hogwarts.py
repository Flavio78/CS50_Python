def main():
    printStudents4()

def printStudents1():
    students = ["Hermione", "Harry", "Ron"]
    for student in students:
        print(student)

def printStudents2():
    students = ["Hermione", "Harry", "Ron"]
    for i in range(len(students)):
        print(i + 1, students[i])

def printStudents3():
    # students = ["Hermione", "Harry", "Ron", "Draco"]
    # houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]
    print("printStudents3")
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
        }
    for student in students:
        print(student, students[student], sep=", ")

def printStudents4():
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus" : "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus" : "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus" : "Jack Russel terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus" : None},
    ]
    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=", ")

main()