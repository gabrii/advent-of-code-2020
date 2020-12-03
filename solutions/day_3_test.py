import pytest
from .day_3 import solve, Terrain


@pytest.fixture()
def example_input():
    return (
        """..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#"""
    )


@pytest.fixture()
def part_1_slopes():
    return ((3, 1),)


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_3.txt", "r") as f:
        return f.read()


@pytest.fixture()
def part_2_slopes():
    return (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )


def test_example_part_1(example_input, part_1_slopes):
    assert solve(example_input, part_1_slopes) == 7


def test_input_part_1(puzzle_input, part_1_slopes):
    assert solve(puzzle_input, part_1_slopes) == 189


def test_example_part_2(example_input, part_2_slopes):
    assert solve(example_input, part_2_slopes) == 336


def test_input_part_2(puzzle_input, part_2_slopes):
    assert solve(puzzle_input, part_2_slopes) == 1718180100
