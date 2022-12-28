import cProfile
from datetime import datetime

data = "2022-06-21T10:30:57+0300"


def method_strptime():
    i = 300_000
    for _ in range(i):
        datetime.strptime(data, "%Y-%m-%dT%H:%M:%S%z").strftime("%d.%m.%Y")


def method_two():
    i = 300_000
    for _ in range(i):
        ".".join(reversed(data[:10].split("-")))


def method_three():
    i = 300_000
    for _ in range(i):
        a = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S%z")
        f"{a.day}.{a.month:02}.{a.year}"


def main():
    method_strptime()
    method_two()
    method_three()


if __name__ == "__main__":
    cProfile.run("main()", sort="cumtime")