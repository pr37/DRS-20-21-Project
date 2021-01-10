from Game.GameObjects.GameObject import GameObject
from Game.GameObjects.GridElement import GridElementType


class PowerUp(GameObject):
    def __init__(self, board, position, turnsAlive):
        super(PowerUp, self).__init__(board, position, GridElementType.PowerUp)
        self.type = GridElementType.PowerUp


