"""Meow file v.3"""
import argparse
import sys


def main() -> None:
    """Main function"""
    args2()


def args1() -> None:
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        n = int(sys.argv[2])
        for _ in range(n):
            print("meow")
    else:
        print("usage: meows.py")


def args2() -> None:
    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="Number of time times to meow", type=int)
    args = parser.parse_args()

    # no need to convert the args.n to int because done from parse with type=int
    for _ in range(args.n):
        print("meow")


if __name__ == "__main__":
    main()
