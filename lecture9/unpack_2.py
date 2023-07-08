def main():
    f1(100, 50, 25, 5)
    f1(100)
    f2(galleons=100, sickles=50, knuts=25)


def f1(*args, **kwargs):
    """take a variable numbre of arguments"""
    """some number of key arguments"""
    print("Positional:", args)


def f2(*args, **kwargs):
    """take a variable numbre of arguments"""
    """some number of key arguments"""
    print("Named:", kwargs)


if __name__ == "__main__":
    main()
