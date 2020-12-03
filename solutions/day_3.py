from dataclasses import dataclass
from typing import Tuple, List
from math import prod


@dataclass
class Terrain:
    terrain: Tuple[Tuple[bool]] = None  # y, x

    @property
    def height(self):
        return len(self.terrain)

    @property
    def __width(self):
        """Private since it has now width, it's infinitely repeating (used only for the modulus)."""
        return len(self.terrain[0])

    @staticmethod
    def __parse_input(input_text: str):
        return tuple(
            tuple(col == "#" for col in row)
            for row
            in input_text.split()
        )

    @classmethod
    def from_input(cls: "Terrain", input_text: str) -> "Terrain":
        return Terrain(cls.__parse_input(input_text))

    def get(self, x, y):
        return self.terrain[y][x % self.__width]

    def trees_in_slope(self, x, y):
        return sum(
            self.get(int(y_ * (x / y)), y_)
            for y_ in range(0, self.height, y)
        )


def solve(input_text: str, slopes: List[Tuple[int, int]]) -> int:
    terrain = Terrain.from_input(input_text)
    return prod(
        terrain.trees_in_slope(*slope)
        for slope in slopes
    )
