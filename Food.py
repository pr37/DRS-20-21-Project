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
        # TODO move food to a valid slot moving  1-3 tiles in a random direction

    def updateBoard(self):
        self.board.foodUpdate(self.position, self.oldPosition)
