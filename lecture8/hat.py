import random


class Hat:
    """
    shared the same variable in all the instances of the class.\n
    I can use it in any instance of my class.\n
    This is class variable vs instance variable
    """

    houses = ["Gryffondor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name: str) -> None:
        """
        new class with methodclass.\n
        I refer to the class and its variables with cls\n
        class method vs instance method\n
        class method is related to class not to a specific instance
        """
        print(name, "is in", random.choice(cls.houses))


def main():
    """
    Main function\n
    no need to instatiate an object of class for a method related to the class not the instance
    """
    Hat.sort("Harry")


if __name__ == "__main__":
    main()
