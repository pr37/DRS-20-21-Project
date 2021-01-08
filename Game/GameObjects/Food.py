import random

from Game.GameObjects.GameObject import GameObject
from Game.GameObjects.GridElement import GridElementType
from Game.Movement import MovementDirection


def getRandDirection() -> MovementDirection:
    return MovementDirection(random.randint(1, 4))


def getRandSteps() -> int:
    return random.randint(1, 3)


class Food(GameObject):
    def __init__(self, board, position):
        super(Food, self).__init__(board, position, GridElementType.Food)
        self.type = GridElementType.Food

    def move(self):
        direction = getRandDirection()
        steps = getRandSteps()
        self.oldPosition = self.position
        # self.oldPosition = [self.oldPosition[0][0], self.oldPosition[0][1]] #hack fix LAZEM
        self.position = self.board.Movement.move_food(self.board, self, direction, steps)
        super(Food, self).updateBoard()

