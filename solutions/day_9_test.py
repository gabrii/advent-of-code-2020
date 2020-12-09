import pytest
from .day_9 import parse_input, get_non_composable, get_key


@pytest.fixture()
def example_input():
    return parse_input(
        """35
        20
        15
        25
        47
        40
        62
        55
        65
        95
        102
        117
        150
        182
        127
        219
        299
        277
        309
        576"""
    )


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_9.txt", "r") as f:
        return parse_input(f.read())


def test_example_part_1(example_input):
    assert get_non_composable(example_input, 5) == 127


def test_input_part_1(puzzle_input):
    assert get_non_composable(puzzle_input, 25) == 1930745883


def test_example_part_2(example_input):
    assert get_key(example_input, 5) == 62


def test_input_part_2(puzzle_input):
    assert get_key(puzzle_input, 25) == -1
