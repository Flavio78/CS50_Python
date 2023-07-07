class Student:
    """
    Custom Class with attributes.\n
    Everything related to a student, is in this class\n
    Classes are defined on top of the file or mainly on separated file
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

    @property
    def house(self) -> str:
        return self._house

    @house.setter
    def house(self, house: str) -> None:
        """
        Setter: set value for an attribut from a class
        """
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

    @classmethod
    def get(cls):
        """
        I could use this method without instanciate a new object of this class.\n
        Furthermore it would be strange to instanciate an object to get a new object.
        (chicken/egg problem- circular problem)
        """
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main() -> None:
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
