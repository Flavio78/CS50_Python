students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


def main():
    houses = houses2()
    for house in sorted(houses):
        print(house)


def houses1() -> []:
    houses = []
    for student in students:
        if student["house"] not in houses:
            houses.append(student["house"])
    return houses


def houses2() -> []:
    houses = set()
    for student in students:
        houses.add(student["house"])
    return houses


if __name__ == "__main__":
    main()
