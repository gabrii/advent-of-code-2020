import pytest
from .day_6 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input():
    return (
        """abc

a
b
c

ab
ac

a
a
a
a

b"""
    )


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_6.txt", "r") as f:
        return f.read()


def test_example_part_1(example_input):
    assert solve_part_1(example_input) == 11


def test_input_part_1(puzzle_input):
    assert solve_part_1(puzzle_input) == 6437


def test_example_part_2(example_input):
    assert solve_part_2(example_input) == 6


def test_input_part_2(puzzle_input):
    assert solve_part_2(puzzle_input) == 3229
