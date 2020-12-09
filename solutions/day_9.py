from typing import Iterator, Tuple, List


def parse_input(intput_text: str) -> List[int]:
    return [int(i) for i in intput_text.split()]


def composable(number, components):
    return set(components) & {-(component - number) for component in components}


def window(elements, window_size) -> Iterator[Tuple[int, List[int]]]:
    for i in range(window_size, len(elements) - window_size):
        yield elements[i], elements[i - window_size:i]


def get_non_composable(input_numbers: List[int], window_size: int) -> int:
    for number, preamble in window(input_numbers, window_size):
        if not composable(number, preamble):
            return number


def get_key(input_numbers: List[int], window_size: int) -> int:
    target = get_non_composable(input_numbers, window_size)
    lower = 0
    upper = 1
    while (current := sum(input_numbers[lower:upper + 1])) != target:
        if current < target:
            upper += 1
        else:
            lower += 1
    components = input_numbers[lower:upper + 1]
    return min(components) + max(components)
