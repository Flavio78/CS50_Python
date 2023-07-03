def main():
    num2()


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


main()
