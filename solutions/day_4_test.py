import pytest
from .day_4 import solve_part_1, solve_part_2


@pytest.fixture()
def example_input():
    return (
        """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    )


@pytest.fixture()
def puzzle_input():
    with open("../inputs/day_4.txt", "r") as f:
        return f.read()


def test_example_part_1(example_input):
    assert solve_part_1(example_input) == 2


def test_input_part_1(puzzle_input):
    assert solve_part_1(puzzle_input) == 202


def test_input_part_2(puzzle_input):
    assert solve_part_2(puzzle_input) == 137
