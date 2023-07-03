from cowsay import cow, trex
from sys import argv

from sayings import hello


def main():
    if len(argv) == 2:
        hello(argv[1])
        # say2()


def say1() -> None:
    """
    Say something from cow
    """
    if len(argv) == 2:
        cow(f"hello, {argv[1]}")


def say2() -> None:
    """
    Say something from trex
    """
    if len(argv) == 2:
        trex(f"hello, {argv[1]}")


if __name__ == "__main__":
    main()
