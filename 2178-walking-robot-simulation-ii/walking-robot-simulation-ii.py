from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height - 2)
        self.pos = 0
        self.started = False

    def step(self, num: int) -> None:
        self.started = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        if not self.started:
            return [0, 0]

        p = self.pos

        if p < self.w:
            return [p, 0]
        p -= (self.w - 1)

        if p < self.h:
            return [self.w - 1, p]
        p -= (self.h - 1)

        if p < self.w:
            return [self.w - 1 - p, self.h - 1]
        p -= (self.w - 1)

        return [0, self.h - 1 - p]

    def getDir(self) -> str:
        if not self.started:
            return "East"

        p = self.pos

        if p == 0:
            return "South"  # critical edge case

        if p < self.w:
            return "East"
        p -= (self.w - 1)

        if p < self.h:
            return "North"
        p -= (self.h - 1)

        if p < self.w:
            return "West"

        return "South"