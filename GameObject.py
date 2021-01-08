

class GameObject:
    def __init__(self, board, position, type):
        self.oldPosition = []
        self.position = [position]
        self.board = board
        self.type = type
        self.updateBoard()

    def updateBoard(self):
        self.board.gameObjectUpdate(self.position, self.oldPosition, self.type)
