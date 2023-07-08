"""New version for mypy"""


def meow1(n: int) -> None:
    """
    Meow n times. v.1
    :param n: Number of times to meow
    :type n: int
    """
    for _ in range(n):
        print("meow")


def meow2(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n  # multiplication concatenates strings


def main() -> None:
    """Main function."""
    number: int = int(input("Number: "))
    meows: str = meow2(number)
    print(meows, end="")


if __name__ == "__main__":
    main()
