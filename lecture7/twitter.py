import sys
import re


def main():
    url = input("URL: ").strip() if len(sys.argv) < 2 else sys.argv[1]
    print(url)
    function7(url)


def function1(url: str):
    username = url.replace("https://twitter.com/", "")
    print(f"Username: {username}")


def function2(url: str):
    url = input("URL: ").strip() if len(sys.argv) < 2 else sys.argv[1]
    print(url)
    username = url.removeprefix("https://twitter.com/")
    print(f"Username: {username}")


def function3(url: str):
    # find and replace using regular expression
    username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    print(f"Username: {username}")


def function4(url: str):
    # find and replace using regular expression
    # group 2 becauase group 1 is (www\.)
    if matches := re.search(
        r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE
    ):
        print(f"Username:", matches.group(2))


def function5(url: str):
    # find and replace using regular expression
    ## ?: for not-capturing in group
    if matches := re.search(
        r"^https?://?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE
    ):
        print(f"Username:", matches.group(1))


def function6(url: str):
    # find and replace using regular expression
    ## ?: for not-capturing in group
    if matches := re.search(
        r"^https?://?(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE
    ):
        if matches.group(1) == ".com":
            print(f"Username:", matches.group(1))


def function7(url: str):
    # find and replace using regular expression
    # ?: for not-capturing in group
    # set rules from Twitter documentation for username
    if matches := re.search(
        r"^https?://?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE
    ):
        print(f"Username:", matches.group(1))


if __name__ == "__main__":
    main()
