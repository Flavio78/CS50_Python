from sys import argv, exit


def main():
    # print(argv[0])
    args4()


def args1() -> None:
    try:
        print(f"Hello, my name is", argv[1])
    except IndexError:
        print("Too few arguments")


def args2() -> None:
    if len(argv) < 2:
        print("Too few arguments")
    elif len(argv) > 2:
        print("Too many arguments")
    else:
        print(f"Hello, my name is", argv[1])


def args3() -> None:
    if len(argv) < 2:
        exit("Too few arguments")
    elif len(argv) > 2:
        exit("Too many arguments")
    print(f"Hello, my name is", argv[1])


def args4() -> None:
    if len(argv) < 2:
        exit("Too few arguments")
    # slice of the list from 1st to last-1 element
    arg in argv[1:-1]:
        print("Hello, my name is", arg)


if __name__ == "__main__":
    main()
