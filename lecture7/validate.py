import re
import sys


def main():
    # ival = intArray()
    # for v in ival:
    #     print(v)

    email = input("What's your email? ").strip() if len(sys.argv) != 2 else sys.argv[1]

    if validate1(email):
        print("Valid")
    else:
        print("Invalid")


def validate1(email: str) -> bool:
    """
    Validate string as email
    """
    # username, domain = email.split("@")
    # return username and domain.endswith(".edu")
    # r for raw string, that is without escaping \
    regex1 = "^[^@]+@[^@]+\.edu$"
    regex2 = "^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
    regex3 = "^\w+@\w+\.(com|edu|gov|net|org)$"
    regex4 = "^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net|org)$"
    return True if re.search(rf"{regex4}", email, re.IGNORECASE) else False


def intArray() -> list[int]:
    x: list[int] = []
    x.append(1)
    return x


if __name__ == "__main__":
    main()
