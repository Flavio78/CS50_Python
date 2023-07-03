import csv


def main():
    # readFile7()
    writeFile3()


def readFile1():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")


def readFile2():
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append(f"{name} is in {house}")

    for student in sorted(students):
        print(student)


def readFile3():
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)

    for student in sorted(students, key=get_house, reverse=True):
        print(f"{student['name']} is in {student['house']}")


def readFile4():
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)

    for student in sorted(students, key=lambda student: student["name"], reverse=True):
        print(f"{student['name']} is in {student['house']}")


def readFile5():
    students = []
    with open("students_home.csv") as file:
        for line in file:
            name, home = line.rstrip().split(",")
            student = {"name": name, "home": home}
            students.append(student)

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['home']}")


def get_name(student) -> str:
    return student["name"]


def get_house(student) -> str:
    return student["house"]


def readFile6():
    students = []
    with open("students_home.csv") as file:
        reader = csv.reader(file)
        for name, home in reader:
            students.append({"name": name, "home": home})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


def readFile7():
    students = []
    with open("students_home2.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


def writeFile2():
    name = input("What's your name? ")
    home = input("What's your home? ")

    with open("students2.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, home])


def writeFile3():
    name = input("What's your name? ")
    home = input("What's your home? ")

    with open("students3.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


if __name__ == "__main__":
    main()
