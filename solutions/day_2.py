import re
from typing import Callable, Iterator, Tuple


def parse_input(intput_text: str) -> Iterator[Tuple[int, int, str, str]]:
    return (
        (int(a), int(b), char, string)
        for a, b, char, string
        in re.findall(r"(\d+)-(\d+) (\w): (\w+)", intput_text)
    )


def part_1_validator(a: int, b: int, char: str, string: str) -> bool:
    return a <= string.count(char) <= b


def part_2_validator(a: int, b: int, char: str, string: str) -> bool:
    def matches(pos: int) -> bool:
        try:
            return string[pos - 1] == char
        except IndexError:
            return False

    return sum((matches(a), matches(b))) == 1


def solve(input_text: str, validator: Callable) -> int:
    parsed_input = parse_input(input_text)
    return sum([validator(*password) for password in parsed_input])
