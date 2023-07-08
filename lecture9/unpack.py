"""Unpack example"""


def main() -> None:
    # function1()
    # print(total(100, 50, 25), "Knuts")
    coins = [100, 50, 25]
    # print(total(coins[0], coins[1], coins[2]), "Knuts")
    # with *coins I pass the individual elements of the list
    print(total(*coins), "Knuts")


def function1() -> None:
    """Function for get strings from input"""
    first, last = input("What's your name? ").split()
    print(f"hello, {first}")


def total(galleons: int, sickles: int, knuts: int) -> int:
    """Evaluate knuts"""
    return (galleons * 17 + sickles) * 29 + knuts


if __name__ == "__main__":
    main()
