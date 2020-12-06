import pytest
from .day_5 import parse_boarding_pass, get_higher_boarding_pass_id, get_missing_boarding_pass_id


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_5.txt", "r") as f:
        return f.read()


def test_parse_boarding_pass():
    assert parse_boarding_pass("FBFBBFFRLR") == (44, 5, 357)


def test_get_higher_boarding_pass_id(puzzle_input):
    assert get_higher_boarding_pass_id(puzzle_input) == 951


def test_get_missing_boarding_pass_id(puzzle_input):
    assert get_missing_boarding_pass_id(puzzle_input) == 653
