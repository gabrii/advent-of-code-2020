import pytest
from .day_1 import solve


@pytest.fixture()
def example_input():
    return {
        1721,
        979,
        366,
        299,
        675,
        1456,
    }


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_1.txt", "r") as f:
        return {int(i) for i in f.read().split()}


def test_example_part_1(example_input):
    assert solve(example_input, 2, 2020) == 514579


def test_input_part_1(puzzle_input):
    assert solve(puzzle_input, 2, 2020) == 319531


def test_example_part_2(example_input):
    assert solve(example_input, 3, 2020) == 241861950


def test_input_part_2(puzzle_input):
    assert solve(puzzle_input, 3, 2020) == 244300320
