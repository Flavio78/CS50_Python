from random import choice, randint, shuffle


def main():
    """
    program for coin choice
    """
    coin = choice(["heads", "tails"])
    print(coin)
    random1()
    shuffle1()


def random1():
    number = randint(1, 10)
    print(number)


def shuffle1():
    cards = ["jack", "queen", "king"]
    shuffle(cards)
    for card in cards:
        print(card)


if __name__ == "__main__":
    main()
