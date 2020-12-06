import re
from typing import Tuple, List


def parse_boarding_pass(boarding_pass: str) -> Tuple[int, int, int]:  # Row, Column, ID
    binary = re.sub(r"[BR]", "1", re.sub(r"[FL]", "0", boarding_pass))
    row = int(binary[:-3], 2)
    column = int(binary[-3:], 2)
    return (row, column, row * 8 + column)


def get_sorted_boarding_passess_ids(boarding_passes: str) -> List[int]:
    return sorted(parse_boarding_pass(boarding_pass)[2] for boarding_pass in boarding_passes.split())


def get_higher_boarding_pass_id(boarding_passess: str):
    return get_sorted_boarding_passess_ids(boarding_passess)[-1]


def get_missing_boarding_pass_id(boarding_passess: str):
    sorted_boarding_passess_ids = get_sorted_boarding_passess_ids(boarding_passess)
    for i in range(len(sorted_boarding_passess_ids) - 1):
        a, b = sorted_boarding_passess_ids[i:i + 2]
        if b - a > 1:
            return a + 1
