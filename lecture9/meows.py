class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


MEOWS = 3


def main():
    cat = Cat()
    cat.meow()


def print_meow():
    for _ in range(MEOWS):
        print("meow")


if __name__ == "__main__":
    main()
