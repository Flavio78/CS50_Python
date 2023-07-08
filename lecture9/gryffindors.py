def main() -> None:
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]
    gryffindors4(students)


def gryffindors1(students: list) -> None:
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    print(*sorted(gryffindors), sep="\n")


def is_gryffindor(s) -> bool:
    return s["house"] == "Gryffindor"


def griffyndors2(students: list) -> None:
    griffyndors = filter(is_gryffindor, students)
    for gryffindor in sorted(griffyndors, key=lambda s: s["name"]):
        print(gryffindor["name"])


def gryffindors3(students: list) -> None:
    gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
    sorted_students = sorted(gryffindors, key=lambda s: s["name"])
    print(*[student["name"] for student in sorted_students], sep="\n")


def gryffindors4(students: list) -> None:
    print(
        *[
            student["name"]
            for student in sorted(
                filter(lambda s: s["house"] == "Gryffindor", students),
                key=lambda s: s["name"],
            )
        ],
        sep="\n",
        end=""
    )


if __name__ == "__main__":
    main()
