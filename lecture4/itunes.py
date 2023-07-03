import json
from sys import argv, exit
from requests import get


def main():
    request1(50)


def request1(limit: int = 3):
    """
    Request of itunes songs according limit and band
    """
    if len(argv) != 2:
        exit()
    response = get(
        f"https://itunes.apple.com/search?entity=song&limit={limit}&term={argv[1]}"
    )
    # print(json.dumps(response.json(), indent=2))
    o = response.json()
    for result in o["results"]:
        print(result["trackName"])


if __name__ == "__main__":
    main()
