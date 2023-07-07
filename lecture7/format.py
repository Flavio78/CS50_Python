import re
import sys


def main():
    function2()


def function1():
    name = input("What's your name? ").strip() if len(sys.argv) != 2 else sys.argv[1]
    matches = re.search(r"^(.+), *(.+)$", name)
    if matches:
        name = matches.group(2) + " " + matches.group(1)
    print(f"Hello, {name}")


def function2():
    name = input("What's your name? ").strip() if len(sys.argv) != 2 else sys.argv[1]
    if matches := re.search(r"^(.+), *(.+)$", name):
        name = matches.group(2) + " " + matches.group(1)
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()
