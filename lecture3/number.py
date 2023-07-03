def main():
    # num4()
    x = get_int4("What's x? ")
    print(f"x is {x}")


def num1():
    try:
        x = (int)(input("What's x? "))
        print(f"x is {x}")
    except ValueError:
        print("x is not an integer")


def num2():
    x: int
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")


def num3():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    print(f"x is {x}")


def num4():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("x is not an integer")
    print(f"x is {x}")


def get_int1():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


def get_int2() -> int:
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


def get_int3() -> int:
    """
    Get value from input until an integer is entered
    """
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


def get_int4(prompt: str = "promt") -> int:
    """
    Get value from input until an integer is entered
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
