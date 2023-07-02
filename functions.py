def main():
    hello()
    name = input("What's your name? ")
    hello(name)
    x = int(input("Enter value x:\t"))
    print(f"x squared is:\t{square(x)}")
# end main

def hello(to: str = "world"):
    """
    Purpose: print hello
    """
    print(f"Hello, {to}!")

def square(n: int):
    """
    Purpose: square of value
    """
    return pow(n,2)


main()
