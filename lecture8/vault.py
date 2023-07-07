class Vault:
    """Vault class"""

    def __init__(self, galleons=0, sickles=0, knuts=0) -> None:
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        """
        Overload of built-in add method\n
        other could be of any type
        """
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


def main():
    """Main function"""
    potter = Vault(100, 50, 25)
    print(potter)
    weasley = Vault(25, 50, 100)
    print(weasley)
    total = sumVaults2(potter, weasley)
    print(total)


def sumVaults1(potter: Vault, weasley: Vault) -> Vault:
    galleons = potter.galleons + weasley.galleons
    sickles = potter.sickles + weasley.sickles
    knuts = potter.knuts + weasley.knuts
    total = Vault(galleons, sickles, knuts)
    return total


def sumVaults2(potter, weasley) -> Vault:
    total = potter + weasley
    return total


if __name__ == "__main__":
    main()
