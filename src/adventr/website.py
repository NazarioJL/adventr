from urllib import request


def download_puzzle_input(url: str, token: str) -> str:
    req = request.Request(url, headers={"Cookie": token})
    return request.urlopen(req).read().decode()


def get_puzzle_input_url(year: int, day: int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}/input"
