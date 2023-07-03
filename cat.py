def main():
    meow(get_number())


def meow():
    """
    Write meow 3 times
    """
    print("meow")
    i = 0
    while i < 3:
        print(f"meow {i}")
        i += 1

def meow2():
    """
    Write meow 3 times with list implementation
    """
    print("meows2")
    for i in [0,1,2]:
        print(f"meow {i}")

def meow3():
    """
    Write meow 3 times with list range
    """
    print("meows3")
    for _ in range(3):
        print(f"meow {_}")

def meow4():
    """
    Write meow 4 times with times in print
    """
    print("meows4")
    print(f"meow\n" * 3, end="")

def meow5():
    """
    Purpose: user enters a positive value
    """
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    for _ in range(n):
        print(f"meow {_ + 1}")

def meow(n: int):
    """
    Purpose:
    """
    for _ in range(n):
        print(f"meow {_ + 1}")

def get_number():
    """
    Purpose: get number
    """
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

main()