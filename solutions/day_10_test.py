import pytest
from .day_10 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input():
    return [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_10.txt", "r") as f:
        return [int(i) for i in f.read().split()]


def test_example_part_1(example_input):
    assert solve_part_1(example_input) == 220


def test_input_part_1(puzzle_input):
    assert solve_part_1(puzzle_input) == 2346


def test_example_part_2(example_input):
    assert solve_part_2(example_input) == 19208


def test_input_part_2(puzzle_input):
    assert solve_part_2(puzzle_input) == 6044831973376
