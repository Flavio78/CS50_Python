class Account:
    _balance = 0

    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        """Only getter is needed here"""
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

    ...


balance = 0
"""Global variable scoped to the module"""


def main():
    balance2()


def balance2():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


def balance1():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n: int) -> None:
    global balance
    balance += n


def withdraw(n: int) -> None:
    global balance
    balance -= n


if __name__ == "__main__":
    main()
