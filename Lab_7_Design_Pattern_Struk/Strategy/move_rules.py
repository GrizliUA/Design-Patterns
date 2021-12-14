from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from itertools import product

class MoveRule(metaclass=ABCMeta):
    def __init__(self, position: list):
        self.position = position

    @abstractmethod
    def get_all_moves(self) -> list:
        pass



@dataclass
class KnightMove(MoveRule):
    def __init__(self, position: list):
        super().__init__(position)

    def get_all_moves(self) -> list:
        x, y = self.position[0]
        moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
        moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
        return moves

@dataclass
class BishopMove(MoveRule):
    def __init__(self, position: list):
        super().__init__(position)

    def get_all_moves(self) -> list:
        x, y = self.position[0]
        moves = []
        directions = [
            zip(range(x+1, 8), range(y-1, -1, -1)),
            zip(range(x+1, 8), range(y+1, 8)),
            zip(range(x-1, -1, -1), range(y-1, -1, -1)),
            zip(range(x-1, -1, -1), range(y+1, 8))
        ]
        for direction in directions:
            for new_x, new_y in direction:
                moves.append((new_x, new_y))
        return moves