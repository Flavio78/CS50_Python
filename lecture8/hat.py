import random


class Hat:
    houses: list[str]

    def __init__(self):
        self.houses = ["Gryffondor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    """
    new class with methodclass
    """

    def sort(self, name: str) -> None:
        print(name, "is in", random.choice(self.houses))


def main():
    hat = Hat()
    hat.sort("Harry")


if __name__ == "__main__":
    main()
