import re
from typing import Tuple, List, Dict
from dataclasses import dataclass, field


@dataclass
class Bag:
    color: str
    contents: List[Tuple[int, "Bag"]] = field(default_factory=list)
    containers: Dict[str, "Bag"] = field(default_factory=dict)

    def total_containers(self):
        return set(self.containers.keys()) | set(
            nested_container
            for container in self.containers.values()
            for nested_container in container.total_containers()
        )

    def total_contents(self):
        return sum(
            amount + amount * content.total_contents()
            for amount, content in self.contents
        )


@dataclass()
class Rules:
    bags: Dict[str, Bag] = field(default_factory=dict)

    def get_bag(self, color):
        if color not in self.bags:
            self.bags[color] = Bag(color)
        return self.bags[color]

    def contains(self, container, content, amount):
        container.contents.append((amount, content))
        content.containers[container.color] = container


def parse_input(input_text: str) -> Bag:
    rules = Rules()
    for color, contents in re.findall(r"(.+?) bags contain(.*)\n", input_text):
        container_bag = rules.get_bag(color)
        for amount, content_color in re.findall(r" (\d+) (.+?) bags?[,.]", contents):
            content_bag = rules.get_bag(content_color)
            rules.contains(container_bag, content_bag, int(amount))
    return rules.get_bag('shiny gold')


def solve_part_1(input_text: str) -> int:
    bag = parse_input(input_text)
    return len(bag.total_containers())


def solve_part_2(input_text: str) -> int:
    bag = parse_input(input_text)
    return bag.total_contents()
