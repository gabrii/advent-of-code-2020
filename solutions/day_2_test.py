import pytest
from .day_2 import solve, part_1_validator, part_2_validator


@pytest.fixture()
def example_input():
    return (
        "1-3 a: abcde"
        "1-3 b: cdefg"
        "2-9 c: ccccccccc"
    )


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_2.txt", "r") as f:
        return f.read()


def test_example_part_1(example_input):
    assert solve(example_input, part_1_validator) == 2


def test_input_part_1(puzzle_input):
    assert solve(puzzle_input, part_1_validator) == 439


def test_example_part_2(example_input):
    assert solve(example_input, part_2_validator) == 1


def test_input_part_2(puzzle_input):
    assert solve(puzzle_input, part_2_validator) == 584
