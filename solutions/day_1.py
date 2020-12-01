"""Generalized solution with recursivity."""
from typing import Set


def solve(report: Set[int], parts: int, target: int) -> int:
    for r_i in report:
        if parts == 1 and r_i == target:
            return r_i
        if r_i > target:
            continue
        if parts > 1:
            answer = r_i * solve(
                report - {r_i},
                parts - 1,
                target - r_i
            )
            if answer:
                return answer
    return 0
