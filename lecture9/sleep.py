"""Count sheep to sleep"""


def main() -> None:
    """Main function"""
    n = int(input("What's n? "))
    # print_sheep(n)
    for s in sheep3(n):
        print(s)

def print_sheep(n):
    for i in range(n):
        print(sheep1(i))

def sheep1(n: int) -> str:
    return "🐑" * n

def sheep2(n: int) -> list[str]:
    flock = []
    for i in range(n):
        flock.append("🐑"*i)
    return flock

def sheep3(n: int) -> list[str]:
    """Using generator for generating a huge amount of data"""
    # with yield a return only 1 value at the time
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()
