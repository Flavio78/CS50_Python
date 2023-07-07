class Wizard:
    """Wizard class (super class for Student and Professor classes)"""

    name: str

    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self) -> str:
        return self.name

    ...


class Student(Wizard):
    """Student class"""

    house: str

    def __init__(self, name: str, house: str) -> None:
        super().__init__(name)
        # it refer to the super that is the parent class: Wizard class
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} {self.house}"

    ...


class Professor(Wizard):
    """Professor class"""

    subject: str

    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def __str__(self) -> str:
        return f"{self.name} {self.subject}"

    ...


def main():
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")
    print(professor)
    print(student)
    print(wizard)


if __name__ == "__main__":
    main()
