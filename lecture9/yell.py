def main() -> None:
    yell5("This", "is", "CS50")


def yell1(phrase: str) -> None:
    print(phrase.upper())


def yell2(words: list[str]) -> None:
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


def yell3(*words: str) -> None:
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


def yell4(*words: str) -> None:
    # map to get a brand new list
    uppercased = map(str.upper, words)
    print(*uppercased)


def yell5(*words: str) -> None:
    # list comprehensions
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
