"""Generalized solution with recursivity."""
from typing import Set


def solve(report: Set[int], parts: int, target: int) -> int:
    for r in report:
        if parts == 1 and r == target:
            return r
        if r > target:
            continue
        if answer := r * solve(
                report - {r},
                parts - 1,
                target - r
        ):
            return answer
    return 0
