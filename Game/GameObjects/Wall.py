from Game.GameObjects.GameObject import GameObject
from Game.GameObjects.GridElement import GridElementType


class Wall(GameObject):
    def __init__(self, board, position):
        super(Wall, self).__init__(board, position, GridElementType.Wall)
