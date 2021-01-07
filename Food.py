import random

from Movement import MovementDirection


def getRandDirection() -> MovementDirection:
    return MovementDirection(random.randint(1, 4))


def getRandSteps() -> int:
    return random.randint(1, 3)


class Food:
    def __init__(self, board, position):
        self.oldPosition = []
        self.position = [position]
        self.board = board
        self.updateBoard()

    def move(self):
        direction = getRandDirection()
        steps = getRandSteps()
        self.board.Movement.move_food(self.board, self, direction, steps)
        self.updateBoard()

    def updateBoard(self):
        self.board.foodUpdate(self.position, self.oldPosition)
