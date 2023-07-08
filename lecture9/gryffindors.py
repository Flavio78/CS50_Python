students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

print(*sorted(gryffindors), sep="\n")


def is_gryffindor(s) -> bool:
    return s["house"] == "Gryffindor"


griffyndors2 = filter(is_gryffindor, students)
for gryffindor in sorted(griffyndors2, key=lambda s: s["name"]):
    print(gryffindor["name"])
