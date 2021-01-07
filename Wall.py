from GameObject import GameObject
from GridElement import GridElementType


class Wall(GameObject):
    def __init__(self, board, position):
        super(Wall, self).__init__(board, position, GridElementType.Wall)
