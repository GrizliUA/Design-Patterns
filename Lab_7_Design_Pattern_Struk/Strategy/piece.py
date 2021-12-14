from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from move_rules import MoveRule

@dataclass
class Piece(metaclass=ABCMeta):
    position:list
    color:str
    move_rule:MoveRule
    number_of_moves = 0

    @abstractmethod
    def move(self, new_position: list) -> dict:
        pass

    @abstractmethod
    def print_info(self) -> None:
        pass

    @staticmethod
    def check_position_range(position: list):
        x, y = position[0]
        if 0 <= x <= 8 and 0 <= y < 8: return True
        else: return False

@dataclass
class Knight(Piece):
    def __init__(self, position: list, color: str, move_rule):
        super().__init__(position, color, move_rule)

    def move(self, new_position) -> dict:
        if str(new_position)[1:-1] in str(self.move_rule.get_all_moves())[1:-1] \
                and self.check_position_range(self.position):
            self.number_of_moves += 1
            return {self.color + "Knight": f"{str(self.position)[1:-1]} -> {str(new_position)[1:-1]}"}

    def print_info(self) -> None:
        print(f'Knight\n\tPosition: {str(self.position)[1:-1]}\n\tColor: {self.color}')

@dataclass
class Bishop(Piece):
    def __init__(self, position: list, color: str, move_rule):
        super().__init__(position, color, move_rule)

    def move(self, new_position: list) -> dict:
        if str(new_position)[1:-1] in str(self.move_rule.get_all_moves())[1:-1] \
                and self.check_position_range(self.position):
            self.number_of_moves += 1
            return {self.color + "Bishop": f"{str(self.position)[1:-1]} -> {str(new_position)[1:-1]}"}

    def print_info(self) -> None:
        print(f'Bishop\n\tPosition: {str(self.position)[1:-1]}\n\tColor: {self.color}')