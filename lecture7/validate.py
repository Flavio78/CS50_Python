def main():
    email = input("What's your email? ").strip()
    if validate1(email):
        print("Valid")
    else:
        print("Invalid")


def validate1(email: str) -> bool:
    """
    Validate string as email
    """
    username, domain = email.split("@")
    return username and domain.endswith(".edu")


if __name__ == "__main__":
    main()
