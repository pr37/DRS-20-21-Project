import enum
import random

from Game.GameObjects.GameObject import GameObject
from Game.GameObjects.GridElement import GridElementType


class PowerEffects(enum.IntEnum):
    Grow = 1
    Death = 2


class PowerUp(GameObject):
    def __init__(self, board, position, turnsAlive, rng):
        super(PowerUp, self).__init__(board, position, GridElementType.PowerUp)
        self.type = GridElementType.PowerUp
        self.turnsAlive = turnsAlive
        self.turnsPassed = 0
        self.rng = rng

    def determineEffect(self):
        if random.randint(0, 100) > self.rng:
            return PowerEffects.Grow
        else:
            return PowerEffects.Death

    def update(self):
        self.turnsPassed += self.turnsPassed + 1
        if self.turnsPassed == self.turnsAlive:
            return True
        return False
