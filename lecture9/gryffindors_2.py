def main():
    students = ["Hermione", "Harry", "Ron"]
    gryffindors = gryffindors3(students)
    print(gryffindors)
    print_rank2(students)


def gryffindors1(students: list[str]) -> []:
    gryffindors = []

    for student in students:
        gryffindors.append({"name": student, "house": "Gryffindor"})
    return gryffindors


def gryffindors2(students: list[str]) -> []:
    gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
    return gryffindors


def gryffindors3(students: list[str]) -> []:
    gryffindors = {student: "Gryffindor" for student in students}
    return gryffindors


def print_rank1(students: list[str]) -> None:
    for i in range(len(students)):
        print(i + 1, students[i])


def print_rank2(students: list[str]) -> None:
    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()
