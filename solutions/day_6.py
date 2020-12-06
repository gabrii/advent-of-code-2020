import re
from typing import Tuple, List, Callable


def aggregate(flat_answers: str, operation: Callable) -> int:
    group_answers = flat_answers.split('\n\n')
    return sum(
        len(operation(group_answer))
        for group_answer in group_answers
    )


def solve_part_1(flat_answers: str) -> int:
    return aggregate(
        flat_answers,
        lambda group_answer: set(group_answer.replace('\n', ''))
    )


def solve_part_2(flat_answers: str) -> int:
    return aggregate(
        flat_answers,
        lambda group_answer: set.intersection(*(set(person_answer) for person_answer in group_answer.split()))
    )
