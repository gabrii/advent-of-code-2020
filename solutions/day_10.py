from typing import List, Tuple
from functools import lru_cache


def solve_part_1(adapters: List[int]) -> int:
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    last = 0
    counts = [0, 0, 0, 0]
    for adapter in adapters:
        steps = adapter - last
        if steps > 3:
            break
        last = adapter
        counts[steps] = counts[steps] + 1
    return counts[1] * counts[3]


@lru_cache
def f(adapters: Tuple[int]) -> int:
    return len(adapters) == 1 or sum(
        f(adapters[i + 1:]) for i, adapter in enumerate(adapters[1:]) if adapter - adapters[0] <= 3
    )


def solve_part_2(adapters: List[int]) -> int:
    adapters.sort()
    return f((0, *adapters, adapters[-1] + 3))
