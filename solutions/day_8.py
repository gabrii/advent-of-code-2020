from typing import Tuple, List, Dict, Union, Type
from dataclasses import dataclass, field


class LoopDetected(Exception):
    ...


class Overflow(Exception):
    ...


@dataclass
class Instruction:
    interpreter: "Interpreter"
    amount: int
    executed: bool = False

    def exec(self):
        if self.executed:
            raise LoopDetected()
        self.executed = True

    def jump(self, amount=1):
        self.interpreter.jump(amount)


class Acc(Instruction):
    def exec(self):
        super().exec()
        self.jump()
        self.interpreter.acc += self.amount


class Jmp(Instruction):
    def exec(self):
        super().exec()
        self.jump(self.amount)


class Nop(Instruction):
    def exec(self):
        super().exec()
        self.jump()


@dataclass
class Interpreter:
    stop_on: Union[Type[LoopDetected], Type[StopIteration]]
    cursor: int = 0
    acc: int = 0
    instructions: List[Union[Acc, Jmp, Nop, None]] = field(default_factory=list)

    def load_instructions(self, instructions_text: str):
        for line in instructions_text.splitlines():
            self.instructions.append(
                globals()[line[:3].title()](self, int(line[4:]))
            )

    def jump(self, amount):
        self.cursor += amount
        if self.cursor == len(self.instructions):
            raise StopIteration
        elif self.cursor > len(self.instructions):
            raise Overflow

    def cycle(self):
        instruction = self.instructions[self.cursor]
        instruction.exec()
        return True

    def reset(self):
        self.cursor = 0
        self.acc = 0
        for instruction in self.instructions:
            instruction.executed = False

    def run(self):
        self.reset()
        try:
            while self.cycle():
                pass
        except self.stop_on:
            print("Found", self.stop_on)
            return self.acc

    def flip(self, index):
        if isinstance((instruction := self.instructions[index]), Jmp):
            self.instructions[index] = Nop(self, instruction.amount)
        else:
            self.instructions[index] = Jmp(self, instruction.amount)

    def run_fixing(self):
        for index, instruction in enumerate(self.instructions):
            if not isinstance(instruction, (Jmp, Nop)):
                continue
            self.flip(index)
            try:
                return self.run()
            except (LoopDetected, Overflow):
                pass
            self.flip(index)


def solve_part_1(input_text: str) -> int:
    interpreter = Interpreter(stop_on=LoopDetected)
    interpreter.load_instructions(input_text)
    return interpreter.run()


def solve_part_2(input_text: str) -> int:
    interpreter = Interpreter(stop_on=StopIteration)
    interpreter.load_instructions(input_text)
    return interpreter.run_fixing()
