def main():
    readFile4()


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


def get_name(student) -> str:
    return student["name"]


def get_house(student) -> str:
    return student["house"]


if __name__ == "__main__":
    main()
