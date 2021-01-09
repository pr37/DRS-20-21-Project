import enum


class GridElementType(enum.Enum):
    Empty = 0
    Food = 1
    Wall = 2
    SnakePart = 3


#class GridElement:
#    def __init__(self, type, position):
#        self.type = type
#        self.position = position
