"""
Cleaner version of student.py
Typed all functions and variables
"""


class Student:
    """
    Custom Class with attributes
    """

    _house: str
    _name: str

    def __init__(self, name: str, house: str) -> None:
        """
        implement of the initialization in Python
        """
        self.name = name
        self.house = house

    def __str__(self) -> str:
        """
        To customize the print this object as string
        """
        return f"{self.name} from {self.house}"

    # Getter: get attribute from a class
    # _house is my instance variable name
    @property
    def house(self) -> str:
        return self._house

    # Setter: set value for an attribut from a class
    @house.setter
    def house(self, house: str) -> None:
        if house not in ["Gryffindor", "Hufflepuff", "Revenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house  # self.house would be in conflict with the property house

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main() -> None:
    student = get_student()
    # Unlucky instance variables are visible
    # Programme must not change them
    # student._house = "Number Four, Privet Drive"
    print(student)


def get_student() -> Student:
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
