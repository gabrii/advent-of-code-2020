import pytest
from .day_7 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input():
    return (
"""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
    )


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_7.txt", "r") as f:
        return f.read()


def test_example_part_1(example_input):
    assert solve_part_1(example_input) == 4


def test_input_part_1(puzzle_input):
    assert solve_part_1(puzzle_input) == 335


def test_example_part_2(example_input):
    assert solve_part_2(example_input) == 32


def test_input_part_2(puzzle_input):
    assert solve_part_2(puzzle_input) == 2431
