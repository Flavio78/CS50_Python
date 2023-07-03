def main():
    # readNames()
    # writeFile()
    readFile4()


def readNames():
    names = []
    for _ in range(3):
        name = input("What's your name? ")
        names.append(name)
    for name in sorted(names):
        print(f"hello, {name}")


def writeFile():
    name = input("What's your name? ")
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


def readFile1():
    with open("names.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.rstrip()
        print("hello, ", line)


def readFile2():
    with open("names.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            print("hello, ", line)


def readFile3():
    names = []
    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"hello, {name}")


def readFile4():
    with open("names.txt") as file:
        for line in sorted(file, reverse=True):
            print(f"hello, {line.rstrip()}")


if __name__ == "__main__":
    main()
