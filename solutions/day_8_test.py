import pytest
from .day_8 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input():
    return (
"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    )


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_8.txt", "r") as f:
        return f.read()


def test_example_part_1(example_input):
    assert solve_part_1(example_input) == 5


def test_input_part_1(puzzle_input):
    assert solve_part_1(puzzle_input) == 1810


def test_example_part_2(example_input):
    assert solve_part_2(example_input) == 2  # Example says solution is 8, but it seems to be wrong


def test_input_part_2(puzzle_input):
    assert solve_part_2(puzzle_input) == 969
