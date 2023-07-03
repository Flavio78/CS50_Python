def main():
    mario1()

def mario1():
    print_column2(3)
    print_row1(4)
    print_square2(5)

def print_column1(height: int = 0):
    for _ in range(height):
        print("#")

def print_column2(height: int = 0):
    print("#\n" * height, end="")

def print_row1(width: int = 0, char: str = '?'):
    print(char * width)

def print_square1(size: int = 0):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("*", end="")
        # add carriage return at the end of each line
        print()


def print_square2(size: int = 0):
    for i in range(size):
        print_row1(size, "*")
main()